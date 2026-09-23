# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T08:07:02.370765Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **ROBUST_OUTLIER** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **PERSISTENT_UP** `ps_gen` value=-18 d1=1.0 d12=254.0 z=-27.316834875
- **ROBUST_OUTLIER** `ps_gen` value=-18 d1=1.0 d12=254.0 z=-27.316834875
- **ROBUST_OUTLIER** `ind_generation` value=1.396e+04 d1=0.0 d12=260.0 z=12.10944388372093
- **CHANGE_POINT** `biomass_gen` value=2406 d1=-71.0 d12=-161.0 z=-9.5482455234375
- **PERSISTENT_DOWN** `biomass_gen` value=2406 d1=-71.0 d12=-161.0 z=-9.5482455234375
- **ROBUST_OUTLIER** `biomass_gen` value=2406 d1=-71.0 d12=-161.0 z=-9.5482455234375
- **ROBUST_OUTLIER** `imbalance` value=-7454 d1=0.0 d12=14.0 z=8.25073508139535
- **CHANGE_POINT** `ccgt_gen` value=6826 d1=-563.0 d12=-2579.0 z=-4.111580645018916
- **CHANGE_POINT** `thermal_base` value=1.063e+04 d1=-557.0 d12=-2585.0 z=-4.071792633100381
- **CHANGE_POINT** `interconnector_net` value=5728 d1=1174.0 d12=5415.0 z=3.387087702794357
- **PERSISTENT_DOWN** `ccgt_gen` value=6826 d1=-563.0 d12=-2579.0 z=-4.111580645018916
- **ROBUST_OUTLIER** `ccgt_gen` value=6826 d1=-563.0 d12=-2579.0 z=-4.111580645018916
- **PERSISTENT_DOWN** `thermal_base` value=1.063e+04 d1=-557.0 d12=-2585.0 z=-4.071792633100381

## Nearest historical live analogues

- `2026-09-23T05:21:50.517884Z` distance=0.289 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:26:03.675558Z` distance=0.289 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:30:15.575715Z` distance=0.289 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T06:50:14.011711Z` distance=0.290 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:54:26.763021Z` distance=0.290 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
