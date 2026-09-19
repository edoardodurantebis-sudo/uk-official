# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T23:32:17.355228Z`  
Memory snapshots: **1645**  
Current physical regime: **TIGHT**

Regime read: margin low, wind falling.

## Active patterns

- **REVERSAL** `ps_gen` value=-254 d1=1.0 d12=-120.0 z=-85.4618189117647
- **ROBUST_OUTLIER** `ps_gen` value=-254 d1=1.0 d12=-120.0 z=-85.4618189117647
- **ROBUST_OUTLIER** `ind_demand` value=-1.189e+04 d1=0.0 d12=-14.0 z=-10.11734625
- **CHANGE_POINT** `wind_gen` value=1.607e+04 d1=-21.0 d12=853.0 z=3.9066536102329446
- **REVERSAL** `wind_gen` value=1.607e+04 d1=-21.0 d12=853.0 z=3.9066536102329446
- **ROBUST_OUTLIER** `wind_gen` value=1.607e+04 d1=-21.0 d12=853.0 z=3.9066536102329446
- **PERSISTENT_DOWN** `thermal_base` value=6542 d1=-136.0 d12=-783.0 z=-3.8200268248456792
- **ROBUST_OUTLIER** `thermal_base` value=6542 d1=-136.0 d12=-783.0 z=-3.8200268248456792
- **PERSISTENT_DOWN** `ccgt_gen` value=3208 d1=-136.0 d12=-777.0 z=-3.798660064417178
- **ROBUST_OUTLIER** `ccgt_gen` value=3208 d1=-136.0 d12=-777.0 z=-3.798660064417178
- **CHANGE_POINT** `imbalance` value=-3940 d1=0.0 d12=-25.0 z=-0.9822666262135922
- **CHANGE_POINT** `ind_generation` value=1.601e+04 d1=0.0 d12=-25.0 z=-0.9822666262135922
- **CHANGE_POINT** `biomass_gen` value=908 d1=-1.0 d12=-17.0 z=-0.01297095673076923
- **PERSISTENT_UP** `margin` value=3.607e+04 d1=0.0 d12=2.0 z=-1.78065294
- **PERSISTENT_DOWN** `interconnector_net` value=-8379 d1=-365.0 d12=-732.0 z=-1.3512174383410138

## Nearest historical live analogues

- `2026-09-19T19:24:22.442601Z` distance=0.106 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -119.0}
- `2026-09-19T19:28:35.593770Z` distance=0.106 → {'next30m_imbalance_delta': -36.0, 'next30m_margin_delta': 40.0, 'next30m_residual_proxy_delta': -119.0}
- `2026-09-19T18:21:25.144867Z` distance=0.110 → {'next30m_imbalance_delta': -611.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T18:25:36.560673Z` distance=0.110 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T18:29:47.180961Z` distance=0.110 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
