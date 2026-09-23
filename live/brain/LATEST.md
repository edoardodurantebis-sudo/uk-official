# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T07:40:56.431050Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **ROBUST_OUTLIER** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **PERSISTENT_DOWN** `ps_gen` value=-18 d1=0.0 d12=-280.0 z=-36.4224465
- **ROBUST_OUTLIER** `ps_gen` value=-18 d1=0.0 d12=-280.0 z=-36.4224465
- **CHANGE_POINT** `ind_generation` value=1.396e+04 d1=0.0 d12=260.0 z=15.314884911764707
- **ROBUST_OUTLIER** `ind_generation` value=1.396e+04 d1=0.0 d12=260.0 z=15.314884911764707
- **CHANGE_POINT** `imbalance` value=-7454 d1=0.0 d12=457.0 z=10.43475319117647
- **ROBUST_OUTLIER** `imbalance` value=-7454 d1=0.0 d12=457.0 z=10.43475319117647
- **PERSISTENT_DOWN** `biomass_gen` value=2554 d1=-1.0 d12=-10.0 z=-6.992210408333333
- **ACCELERATION** `biomass_gen` value=2554 d1=-1.0 d12=-10.0 z=-6.992210408333333
- **ROBUST_OUTLIER** `biomass_gen` value=2554 d1=-1.0 d12=-10.0 z=-6.992210408333333
- **CHANGE_POINT** `ccgt_gen` value=8067 d1=-459.0 d12=-2143.0 z=-3.1276077936300175
- **CHANGE_POINT** `thermal_base` value=1.188e+04 d1=-455.0 d12=-2141.0 z=-2.6860879804
- **CHANGE_POINT** `interconnector_net` value=3798 d1=-1.0 d12=7364.0 z=2.68075823046663
- **PERSISTENT_DOWN** `ccgt_gen` value=8067 d1=-459.0 d12=-2143.0 z=-3.1276077936300175

## Nearest historical live analogues

- `2026-09-23T06:20:46.707492Z` distance=0.262 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:24:57.207675Z` distance=0.262 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:29:10.567050Z` distance=0.262 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:33:22.680489Z` distance=0.262 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:37:35.207990Z` distance=0.262 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
