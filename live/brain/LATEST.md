# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T04:45:59.012347Z`  
Memory snapshots: **2399**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.779e+04 d1=0.0 d12=-5.0 z=18.56621785526316
- **ROBUST_OUTLIER** `margin` value=3.779e+04 d1=0.0 d12=-5.0 z=18.56621785526316
- **PERSISTENT_DOWN** `interconnector_net` value=-4622 d1=-3.0 d12=-3172.0 z=-7.689664928392857
- **ROBUST_OUTLIER** `interconnector_net` value=-4622 d1=-3.0 d12=-3172.0 z=-7.689664928392857
- **CHANGE_POINT** `ccgt_gen` value=1.32e+04 d1=158.0 d12=1902.0 z=5.303209249501991
- **CHANGE_POINT** `thermal_base` value=1.685e+04 d1=164.0 d12=1901.0 z=5.180711153696499
- **CHANGE_POINT** `imbalance` value=-3324 d1=0.0 d12=-88.0 z=-3.3329182152014654
- **CHANGE_POINT** `ind_generation` value=1.814e+04 d1=0.0 d12=-88.0 z=-3.3329182152014654
- **PERSISTENT_UP** `ccgt_gen` value=1.32e+04 d1=158.0 d12=1902.0 z=5.303209249501991
- **ROBUST_OUTLIER** `ccgt_gen` value=1.32e+04 d1=158.0 d12=1902.0 z=5.303209249501991
- **PERSISTENT_UP** `thermal_base` value=1.685e+04 d1=164.0 d12=1901.0 z=5.180711153696499
- **ROBUST_OUTLIER** `thermal_base` value=1.685e+04 d1=164.0 d12=1901.0 z=5.180711153696499
- **CHANGE_POINT** `biomass_gen` value=3029 d1=0.0 d12=-16.0 z=-1.7536733500000001
- **ROBUST_OUTLIER** `ind_demand` value=-1.252e+04 d1=0.0 d12=-15.0 z=-3.346506836538462
- **ROBUST_OUTLIER** `imbalance` value=-3324 d1=0.0 d12=-88.0 z=-3.3329182152014654

## Nearest historical live analogues

- `2026-09-22T03:33:35.816390Z` distance=0.023 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:37:48.990972Z` distance=0.023 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:42:37.215255Z` distance=0.023 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:46:49.421565Z` distance=0.023 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:51:00.662974Z` distance=0.023 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
