# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T08:18:00.136747Z`  
Memory snapshots: **2449**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.269e+04 d1=0.0 d12=0.0 z=-5.6807025611111115
- **ROBUST_OUTLIER** `ind_demand` value=-1.269e+04 d1=0.0 d12=0.0 z=-5.6807025611111115
- **CHANGE_POINT** `imbalance` value=-3831 d1=0.0 d12=0.0 z=-2.7082722989296637
- **CHANGE_POINT** `thermal_base` value=1.62e+04 d1=-325.0 d12=-1534.0 z=-0.4368701075349301
- **CHANGE_POINT** `ccgt_gen` value=1.255e+04 d1=-322.0 d12=-1536.0 z=-0.4339844407370518
- **CHANGE_POINT** `ps_gen` value=-169 d1=0.0 d12=5.0 z=0.28906703571428566
- **CHANGE_POINT** `ts_demand_forecast` value=2.107e+04 d1=-163.0 d12=-639.0 z=None
- **REVERSAL** `interconnector_net` value=8317 d1=-21.0 d12=4173.0 z=1.6482407981334393
- **PERSISTENT_DOWN** `residual_proxy` value=7980 d1=-411.0 d12=-639.0 z=-1.2937411153017242
- **ACCELERATION** `residual_proxy` value=7980 d1=-411.0 d12=-639.0 z=-1.2937411153017242
- **PERSISTENT_UP** `wind_gen` value=3662 d1=56.0 d12=141.0 z=0.9400919313471503
- **REVERSAL** `nuclear_gen` value=3650 d1=-3.0 d12=2.0 z=-0.5781340714285713
- **ACCELERATION** `nuclear_gen` value=3650 d1=-3.0 d12=2.0 z=-0.5781340714285713
- **PERSISTENT_UP** `biomass_gen` value=3033 d1=6.0 d12=4.0 z=0.4496598333333333
- **ACCELERATION** `biomass_gen` value=3033 d1=6.0 d12=4.0 z=0.4496598333333333

## Nearest historical live analogues

- `2026-09-22T07:23:01.738163Z` distance=0.038 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -228.0}
- `2026-09-22T04:54:50.378428Z` distance=0.212 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T04:59:01.331890Z` distance=0.212 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:03:14.010868Z` distance=0.212 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:07:26.495356Z` distance=0.212 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': -696.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
