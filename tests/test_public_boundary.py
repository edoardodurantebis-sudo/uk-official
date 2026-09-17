"""Regression tripwires for accidental private access in public execution.

Static checks cover current local sources/workflows, not arbitrary obfuscated
code or transitive third-party dependency behavior.
"""
import ast
from pathlib import Path
import re
import tempfile
import unittest
from urllib.parse import urlsplit

PUBLIC_DATA_HOSTS = {"data.elexon.co.uk", "api.neso.energy"}
OFFICIAL_ACTIONS = {"actions/checkout", "actions/setup-python", "actions/upload-artifact", "actions/download-artifact", "actions/cache"}


def violations(root):
    found = []
    for path in (root / ".github/workflows").glob("*.yml"):
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("#"):
                continue
            category = None
            if re.search(r"secrets\.(?!GITHUB_TOKEN\b)\w+", line, re.I):
                category = "EXTERNAL_CREDENTIAL_IN_PUBLIC_WORKFLOW"
            match = re.match(r"\s*repository:\s*(.+)", line)
            if match and match[1].strip().strip("'\"") != "${{ github.repository }}":
                category = "CROSS_REPOSITORY_CHECKOUT"
            match = re.match(r"\s*(?:-\s*)?uses:\s*([^\s@]+)", line)
            if match and match[1] not in OFFICIAL_ACTIONS:
                category = "UNREVIEWED_ACTION"
            if re.search(r"\b(?:git\s+clone|gh\s+repo\s+clone|git\s+remote\s+add)\b", line):
                category = "CROSS_REPOSITORY_FETCH"
            normalized = re.sub(r"\$\{\{\s*github\.repository\s*\}\}", "${GITHUB_REPOSITORY}", line)
            for url in re.findall(r"https?://[^\s'\"\\]+", normalized):
                allowed = (url.startswith("https://api.github.com/repos/${GITHUB_REPOSITORY}/") or
                           url.startswith("https://github.com/gitleaks/gitleaks/releases/download/v8.30.1/"))
                if not allowed:
                    category = "UNREVIEWED_WORKFLOW_URL"
            if category:
                found.append((path.name, number, category))
    for path in root.rglob("*.py"):
        if any(part in {"tests", ".git", ".venv", "venv", "__pycache__"} for part in path.relative_to(root).parts):
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                for url in re.findall(r"https?://[^\s'\"]+", node.value):
                    if urlsplit(url).hostname not in PUBLIC_DATA_HOSTS:
                        found.append((path.name, node.lineno, "UNREVIEWED_DATA_HOST"))
    return found


class PublicBoundaryTests(unittest.TestCase):
    def test_current_public_execution_boundary(self):
        self.assertEqual(violations(Path(__file__).resolve().parents[1]), [])

    def test_cross_repo_and_external_credentials_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workflows = root / ".github/workflows"
            workflows.mkdir(parents=True)
            path = workflows / "probe.yml"
            path.write_text("repository: some-owner/other-repository\ntoken: ${{ secrets.OTHER_TOKEN }}\n")
            self.assertEqual({x[2] for x in violations(root)}, {"CROSS_REPOSITORY_CHECKOUT", "EXTERNAL_CREDENTIAL_IN_PUBLIC_WORKFLOW"})

    def test_unreviewed_fetch_and_host_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workflows = root / ".github/workflows"
            workflows.mkdir(parents=True)
            (workflows / "probe.yml").write_text("run: git clone https://example.invalid/repo\nuses: unreviewed/action@v1\n")
            (root / "probe.py").write_text("URL = 'https://example.invalid/data'\n")
            self.assertGreaterEqual(len(violations(root)), 3)

    def test_dynamic_other_repository_is_not_self(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workflows = root / ".github/workflows"
            workflows.mkdir(parents=True)
            (workflows / "probe.yml").write_text('run: curl "https://api.github.com/repos/${OTHER_REPO}/contents"\n')
            self.assertEqual(violations(root)[0][2], "UNREVIEWED_WORKFLOW_URL")


if __name__ == "__main__":
    unittest.main()

