import unittest
import pandas as pd

import GB_ALIEN_SCANNER_V1 as scanner
import GB_NIGHTLY_DISCOVERY_V1 as nightly
import gb_power_runner as runner


class NivLineageContractTests(unittest.TestCase):
    def test_scanner_master_raw_is_flipped(self):
        d = pd.DataFrame({"niv": [-3.0, 3.0, 0.0], "psbil": [1.0, 2.0, 3.0]})
        x = scanner.add_targets(d, scanner.NIV_SOURCE_MASTER_INTERNAL_INVERTED)
        self.assertEqual(x["niv_master_raw"].tolist(), [-3.0, 3.0, 0.0])
        self.assertEqual(x["niv_elexon_sign"].tolist(), [3.0, -3.0, -0.0])
        self.assertEqual(x["short_flag"].tolist()[:2], [1.0, 0.0])
        self.assertEqual(x["long_flag"].tolist()[:2], [0.0, 1.0])

    def test_scanner_elexon_raw_is_not_flipped(self):
        d = pd.DataFrame({"niv": [3.0, -3.0, 0.0], "psbil": [1.0, 2.0, 3.0]})
        x = scanner.add_targets(d, scanner.NIV_SOURCE_ELEXON_OFFICIAL)
        self.assertEqual(x["niv"].tolist(), [3.0, -3.0, 0.0])
        self.assertEqual(x["short_flag"].tolist()[:2], [1.0, 0.0])
        self.assertNotIn("niv_master_raw", x.columns)

    def test_nightly_master_raw_is_flipped(self):
        d = pd.DataFrame({"niv": [-4.0, 4.0, 0.0], "psbil": [10.0, 20.0, 30.0]})
        x = nightly.add_targets(
            d, "niv", "psbil", nightly.NIV_SOURCE_MASTER_INTERNAL_INVERTED
        )
        self.assertEqual(x["niv"].tolist(), [4.0, -4.0, -0.0])
        self.assertEqual(x["short_flag"].tolist()[:2], [1.0, 0.0])
        self.assertEqual(x["long_flag"].tolist()[:2], [0.0, 1.0])

    def test_nightly_elexon_raw_is_not_flipped(self):
        d = pd.DataFrame({"niv": [4.0, -4.0, 0.0], "psbil": [10.0, 20.0, 30.0]})
        x = nightly.add_targets(
            d, "niv", "psbil", nightly.NIV_SOURCE_ELEXON_OFFICIAL
        )
        self.assertEqual(x["niv"].tolist(), [4.0, -4.0, 0.0])
        self.assertEqual(x["short_flag"].tolist()[:2], [1.0, 0.0])

    def test_unknown_lineage_fails_closed(self):
        d = pd.DataFrame({"niv": [1.0], "psbil": [2.0]})
        with self.assertRaisesRegex(RuntimeError, "NIV_LINEAGE_UNRESOLVED"):
            scanner.add_targets(d, "UNKNOWN")
        with self.assertRaisesRegex(RuntimeError, "NIV_LINEAGE_UNRESOLVED"):
            nightly.add_targets(d, "niv", "psbil", "UNKNOWN")

    def test_all_niv_outcome_columns_are_blocked(self):
        for field in ("niv", "niv_raw_source", "niv_master_raw", "niv_elexon_sign"):
            for gate in ("DA", "IDA1", "IDA2"):
                self.assertFalse(scanner.gate_allows_master(field, gate))

    def test_runner_defaults_to_historical_master_lineage(self):
        a = runner.parse_args([])
        self.assertEqual(a.niv_source, "MASTER_INTERNAL_INVERTED")
        b = runner.parse_args(["--niv-source", "ELEXON_OFFICIAL"])
        self.assertEqual(b.niv_source, "ELEXON_OFFICIAL")


if __name__ == "__main__":
    unittest.main()
