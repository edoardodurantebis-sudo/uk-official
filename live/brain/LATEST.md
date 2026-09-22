# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T04:50:17.653029Z`  
Memory snapshots: **2400**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.779e+04 d1=0.0 d12=-5.0 z=16.4617654609375
- **ROBUST_OUTLIER** `margin` value=3.779e+04 d1=0.0 d12=-5.0 z=16.4617654609375
- **PERSISTENT_DOWN** `interconnector_net` value=-4622 d1=0.0 d12=-3186.0 z=-7.672019579521087
- **ROBUST_OUTLIER** `interconnector_net` value=-4622 d1=0.0 d12=-3186.0 z=-7.672019579521087
- **CHANGE_POINT** `ccgt_gen` value=1.32e+04 d1=0.0 d12=1928.0 z=5.303209249501991
- **CHANGE_POINT** `thermal_base` value=1.685e+04 d1=0.0 d12=1931.0 z=5.180711153696499
- **PERSISTENT_UP** `ccgt_gen` value=1.32e+04 d1=0.0 d12=1928.0 z=5.303209249501991
- **ROBUST_OUTLIER** `ccgt_gen` value=1.32e+04 d1=0.0 d12=1928.0 z=5.303209249501991
- **PERSISTENT_UP** `thermal_base` value=1.685e+04 d1=0.0 d12=1931.0 z=5.180711153696499
- **ROBUST_OUTLIER** `thermal_base` value=1.685e+04 d1=0.0 d12=1931.0 z=5.180711153696499
- **CHANGE_POINT** `imbalance` value=-3324 d1=0.0 d12=-88.0 z=-3.028413709731544
- **CHANGE_POINT** `ind_generation` value=1.814e+04 d1=0.0 d12=-88.0 z=-3.028413709731544
- **ROBUST_OUTLIER** `ind_demand` value=-1.252e+04 d1=0.0 d12=-15.0 z=-4.237179198717949
- **CHANGE_POINT** `biomass_gen` value=3029 d1=0.0 d12=-15.0 z=-1.7536733500000001
- **ROBUST_OUTLIER** `imbalance` value=-3324 d1=0.0 d12=-88.0 z=-3.028413709731544

## Nearest historical live analogues

- `2026-09-22T03:55:16.196094Z` distance=0.018 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:33:35.816390Z` distance=0.023 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:37:48.990972Z` distance=0.023 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:42:37.215255Z` distance=0.023 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:46:49.421565Z` distance=0.023 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
