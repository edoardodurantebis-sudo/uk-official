import unittest

import GB_PHYSICAL_FANZINE as f

class PhysicalFanzineTests(unittest.TestCase):
    def test_build_is_observation_only(self):
        state={"last_heartbeat":"2026-09-20T12:00:00Z","events":[{"dataset":"MID","rows":3,"ts":"2026-09-20T11:59:00Z"}]}
        brain={"regime":"LOOSE","regime_reasons":["residual low"],"states":{"residual_proxy":{"value":17000,"d1":-10,"d12":-100,"accel":0,"tags":[]}},"active_patterns":[],"analogues":[]}
        out=f.build(state,brain)
        self.assertEqual(out["regime"],"LOOSE")
        self.assertEqual(out["health"]["mid"]["status"],"OK")
        self.assertFalse(out["certification"]["trading_signal"])
        self.assertFalse(out["certification"]["promotion_authority"])

    def test_mid_error_is_visible(self):
        state={"last_heartbeat":"x","events":[{"dataset":"MID","rows":0,"ts":"t","error":"HTTP 400"}]}
        out=f.build(state,{"states":{}})
        self.assertEqual(out["health"]["mid"]["status"],"DEGRADED")

if __name__=="__main__":
    unittest.main()