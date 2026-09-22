# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T03:46:49.421565Z`  
Memory snapshots: **2385**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.779e+04 d1=0.0 d12=-43.0 z=26.688143811728395
- **ROBUST_OUTLIER** `margin` value=3.779e+04 d1=0.0 d12=-43.0 z=26.688143811728395
- **CHANGE_POINT** `interconnector_net` value=-1451 d1=-4.0 d12=-4142.0 z=-4.468654982878884
- **CHANGE_POINT** `ps_gen` value=-709 d1=3.0 d12=-544.0 z=-3.178054324235808
- **ROBUST_OUTLIER** `interconnector_net` value=-1451 d1=-4.0 d12=-4142.0 z=-4.468654982878884
- **CHANGE_POINT** `ind_demand` value=-1.25e+04 d1=0.0 d12=0.0 z=-2.2739940142857145
- **REVERSAL** `ps_gen` value=-709 d1=3.0 d12=-544.0 z=-3.178054324235808
- **ACCELERATION** `ps_gen` value=-709 d1=3.0 d12=-544.0 z=-3.178054324235808
- **ROBUST_OUTLIER** `ps_gen` value=-709 d1=3.0 d12=-544.0 z=-3.178054324235808
- **CHANGE_POINT** `imbalance` value=-2644 d1=0.0 d12=15.0 z=-0.2459077213541667
- **CHANGE_POINT** `ind_generation` value=1.882e+04 d1=0.0 d12=15.0 z=-0.2459077213541667
- **CHANGE_POINT** `thermal_base` value=1.498e+04 d1=-35.0 d12=606.0 z=0.21609865776699028
- **CHANGE_POINT** `ccgt_gen` value=1.132e+04 d1=-34.0 d12=603.0 z=0.20107028824921136
- **PERSISTENT_UP** `biomass_gen` value=3047 d1=1.0 d12=6.0 z=0.67448975
- **REVERSAL** `nuclear_gen` value=3657 d1=-1.0 d12=3.0 z=0.67448975

## Nearest historical live analogues

- `2026-09-22T02:20:47.392507Z` distance=0.196 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:24:59.358718Z` distance=0.196 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:29:12.426907Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:33:26.071895Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:37:48.213453Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
