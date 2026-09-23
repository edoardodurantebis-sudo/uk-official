# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T07:36:43.962318Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.265e+04 d1=0.0 d12=-242.0 z=-38.9517830625
- **ROBUST_OUTLIER** `ind_demand` value=-1.265e+04 d1=0.0 d12=-242.0 z=-38.9517830625
- **ROBUST_OUTLIER** `ps_gen` value=-18 d1=-1.0 d12=-280.0 z=-36.4224465
- **CHANGE_POINT** `ind_generation` value=1.396e+04 d1=0.0 d12=705.0 z=15.314884911764707
- **ROBUST_OUTLIER** `ind_generation` value=1.396e+04 d1=0.0 d12=705.0 z=15.314884911764707
- **CHANGE_POINT** `imbalance` value=-7454 d1=0.0 d12=457.0 z=10.43475319117647
- **ROBUST_OUTLIER** `imbalance` value=-7454 d1=0.0 d12=457.0 z=10.43475319117647
- **PERSISTENT_DOWN** `biomass_gen` value=2555 d1=-7.0 d12=-9.0 z=-6.969727416666667
- **ROBUST_OUTLIER** `biomass_gen` value=2555 d1=-7.0 d12=-9.0 z=-6.969727416666667
- **CHANGE_POINT** `interconnector_net` value=3799 d1=0.0 d12=7365.0 z=2.681124204286489
- **CHANGE_POINT** `ccgt_gen` value=8526 d1=-345.0 d12=-1684.0 z=-2.0758106062610233
- **CHANGE_POINT** `thermal_base` value=1.233e+04 d1=-345.0 d12=-1686.0 z=-1.736246342105263
- **PERSISTENT_DOWN** `nuclear_gen` value=3805 d1=0.0 d12=-2.0 z=2.797148669117647
- **ACCELERATION** `nuclear_gen` value=3805 d1=0.0 d12=-2.0 z=2.797148669117647
- **PERSISTENT_UP** `interconnector_net` value=3799 d1=0.0 d12=7365.0 z=2.681124204286489

## Nearest historical live analogues

- `2026-09-23T06:20:46.707492Z` distance=0.262 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:24:57.207675Z` distance=0.262 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:29:10.567050Z` distance=0.262 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:33:22.680489Z` distance=0.262 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:37:35.207990Z` distance=0.262 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
