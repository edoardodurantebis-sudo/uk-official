import unittest

import GB_ALIEN_SCANNER_V1 as scanner


class ScannerPriorAuctionGateTests(unittest.TestCase):
    def test_pida1_is_only_available_after_ida1_for_ida2(self):
        self.assertFalse(scanner.gate_allows_master("pida1", "DA"))
        self.assertFalse(scanner.gate_allows_master("pida1", "IDA1"))
        self.assertTrue(scanner.gate_allows_master("pida1", "IDA2"))

    def test_pida2_never_leaks_into_ida2_features(self):
        for gate in ("DA", "IDA1", "IDA2"):
            self.assertFalse(scanner.gate_allows_master("pida2", gate))

    def test_da_price_is_prior_auction_only(self):
        self.assertFalse(scanner.gate_allows_master("pda_gbp", "DA"))
        self.assertTrue(scanner.gate_allows_master("pda_gbp", "IDA1"))
        self.assertTrue(scanner.gate_allows_master("pda_gbp", "IDA2"))

    def test_post_outcome_fields_remain_blocked(self):
        for field in ("niv", "psbil", "actual_residual_load", "actual_net_demand", "boa_acceptance"):
            for gate in ("DA", "IDA1", "IDA2"):
                self.assertFalse(scanner.gate_allows_master(field, gate))


if __name__ == "__main__":
    unittest.main()
