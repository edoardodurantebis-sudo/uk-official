import json
import unittest
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


if __name__ == "__main__":
    unittest.main()
