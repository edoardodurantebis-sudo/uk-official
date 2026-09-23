# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T07:45:09.516370Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **ROBUST_OUTLIER** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **PERSISTENT_DOWN** `ps_gen` value=-18 d1=0.0 d12=-268.0 z=-36.4224465
- **ROBUST_OUTLIER** `ps_gen` value=-18 d1=0.0 d12=-268.0 z=-36.4224465
- **CHANGE_POINT** `ind_generation` value=1.396e+04 d1=0.0 d12=260.0 z=13.52483342857143
- **ROBUST_OUTLIER** `ind_generation` value=1.396e+04 d1=0.0 d12=260.0 z=13.52483342857143
- **CHANGE_POINT** `imbalance` value=-7454 d1=0.0 d12=14.0 z=9.215106714285714
- **ROBUST_OUTLIER** `imbalance` value=-7454 d1=0.0 d12=14.0 z=9.215106714285714
- **PERSISTENT_DOWN** `biomass_gen` value=2554 d1=0.0 d12=-8.0 z=-6.947244424999999
- **ROBUST_OUTLIER** `biomass_gen` value=2554 d1=0.0 d12=-8.0 z=-6.947244424999999
- **CHANGE_POINT** `ccgt_gen` value=8067 d1=0.0 d12=-2150.0 z=-3.0455984088184933
- **CHANGE_POINT** `interconnector_net` value=3798 d1=0.0 d12=7388.0 z=2.68075823046663
- **CHANGE_POINT** `thermal_base` value=1.188e+04 d1=0.0 d12=-2147.0 z=-2.5547596376923076
- **PERSISTENT_DOWN** `ccgt_gen` value=8067 d1=0.0 d12=-2150.0 z=-3.0455984088184933
- **ROBUST_OUTLIER** `ccgt_gen` value=8067 d1=0.0 d12=-2150.0 z=-3.0455984088184933

## Nearest historical live analogues

- `2026-09-23T06:50:14.011711Z` distance=0.258 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:20:46.707492Z` distance=0.262 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:24:57.207675Z` distance=0.262 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:29:10.567050Z` distance=0.262 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:33:22.680489Z` distance=0.262 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
