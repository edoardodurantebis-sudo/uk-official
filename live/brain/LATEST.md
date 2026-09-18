# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T08:47:16.640835Z`  
Memory snapshots: **1148**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `wind_gen` value=1.225e+04 d1=-18.0 d12=-199.0 z=-3.8042715235239855
- **CHANGE_POINT** `interconnector_net` value=2927 d1=-2.0 d12=-446.0 z=3.345290809344952
- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=3.0 z=-5.265202932170543
- **ROBUST_OUTLIER** `wind_gen` value=1.225e+04 d1=-18.0 d12=-199.0 z=-3.8042715235239855
- **PERSISTENT_DOWN** `interconnector_net` value=2927 d1=-2.0 d12=-446.0 z=3.345290809344952
- **ROBUST_OUTLIER** `interconnector_net` value=2927 d1=-2.0 d12=-446.0 z=3.345290809344952
- **ROBUST_OUTLIER** `imbalance` value=9625 d1=0.0 d12=-593.0 z=-3.1701018249999997
- **CHANGE_POINT** `ps_gen` value=224 d1=2.0 d12=-374.0 z=-1.0643941237541528
- **CHANGE_POINT** `biomass_gen` value=2144 d1=-38.0 d12=-25.0 z=-0.800956578125
- **CHANGE_POINT** `thermal_base` value=7266 d1=-69.0 d12=-400.0 z=-0.09339088846153847
- **CHANGE_POINT** `ccgt_gen` value=3934 d1=-66.0 d12=-391.0 z=-0.08989330288048152
- **REVERSAL** `ps_gen` value=224 d1=2.0 d12=-374.0 z=-1.0643941237541528
- **PERSISTENT_DOWN** `biomass_gen` value=2144 d1=-38.0 d12=-25.0 z=-0.800956578125
- **ACCELERATION** `biomass_gen` value=2144 d1=-38.0 d12=-25.0 z=-0.800956578125
- **ACCELERATION** `nuclear_gen` value=3332 d1=-3.0 d12=-9.0 z=-0.6744897499999999

## Nearest historical live analogues

- `2026-09-18T07:23:09.699179Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:27:20.707745Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:31:32.031758Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:35:44.221296Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:39:57.955920Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
