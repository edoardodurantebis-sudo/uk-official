import json
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch
from datetime import datetime, timezone

import GB_ALIEN_CONTINUOUS as live


class PublicationRetryTests(unittest.TestCase):
    def test_failed_fetch_retried_after_state_round_trip(self):
        state = live.fresh_state()
        state["metadata"] = {"WINDFOR": "old"}
        metadata = {"data": [{"dataset": "WINDFOR", "latestPublishTime": "2026-09-17T00:00:00Z"}]}
        now = datetime(2026, 9, 17, tzinfo=timezone.utc)
        with patch.object(live, "http_json", return_value=metadata), patch.object(live, "fetch_dataset", side_effect=TimeoutError("transient")) as fetch:
            live.one_poll(state, ["WINDFOR"], now)
            self.assertEqual(fetch.call_count, 1)
            self.assertEqual(state["metadata"]["WINDFOR"], "old")
        restored = json.loads(json.dumps(state))
        with patch.object(live, "http_json", return_value=metadata), patch.object(live, "fetch_dataset", return_value=[{"forecast": 1000}]) as fetch:
            live.one_poll(restored, ["WINDFOR"], now)
            self.assertEqual(restored["metadata"]["WINDFOR"], "2026-09-17T00:00:00Z")
            live.one_poll(restored, ["WINDFOR"], now)
            self.assertEqual(fetch.call_count, 1)

    def test_first_observation_keeps_bootstrap_semantics(self):
        state = live.fresh_state()
        with patch.object(live, "http_json", return_value={"data": [{"dataset": "WINDFOR", "latestPublishTime": "new"}]}), patch.object(live, "fetch_dataset") as fetch:
            self.assertEqual(live.one_poll(state, ["WINDFOR"], datetime.now(timezone.utc)), (0, []))
            fetch.assert_not_called()
            self.assertEqual(state["metadata"], {"WINDFOR": "new"})

    def test_one_failed_dataset_does_not_replay_successful_one(self):
        state = live.fresh_state()
        state["metadata"] = {"WINDFOR": "old", "NDF": "old"}
        meta = {"data": [{"dataset": ds, "latestPublishTime": "new"} for ds in state["metadata"]]}
        def fetch(ds, *args):
            if ds == "WINDFOR":
                raise TimeoutError()
            return []
        with patch.object(live, "http_json", return_value=meta), patch.object(live, "fetch_dataset", side_effect=fetch):
            live.one_poll(state, ["WINDFOR", "NDF"], datetime.now(timezone.utc))
        self.assertEqual(state["metadata"], {"WINDFOR": "old", "NDF": "new"})

    def run_cycle(self, outcomes, times):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            args = ["observer", "--duration-seconds", "1", "--poll-seconds", "0", "--state", str(root / "state.json"), "--status", str(root / "status.md")]
            with patch.object(live.sys, "argv", args), patch.object(live.time, "monotonic", side_effect=times), patch.object(live, "one_poll", side_effect=outcomes):
                code = live.main()
            return code, json.loads((root / "state.json").read_text())

    def test_heartbeat_does_not_make_total_metadata_outage_healthy(self):
        code, state = self.run_cycle([TimeoutError("simulated")], [0, 0, 0, .1, 2])
        self.assertEqual(code, 1)
        self.assertIn("last_heartbeat", state)
        self.assertNotIn("last_successful_metadata_poll", state)

    def test_transient_metadata_failure_recovers_within_cycle(self):
        code, state = self.run_cycle([TimeoutError("simulated"), (0, [])], [0, 0, 0, .1, .2, .2, .3, 2])
        self.assertEqual(code, 0)
        self.assertIn("last_successful_metadata_poll", state)


if __name__ == "__main__":
    unittest.main()
