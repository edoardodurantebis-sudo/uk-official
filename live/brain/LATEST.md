# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T20:16:03.760545Z`  
Memory snapshots: **2279**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-2779 d1=0.0 d12=15.0 z=3.5468857543103445
- **CHANGE_POINT** `ind_generation` value=1.868e+04 d1=0.0 d12=15.0 z=3.5468857543103445
- **PERSISTENT_UP** `nuclear_gen` value=3532 d1=10.0 d12=20.0 z=4.2155609375
- **ROBUST_OUTLIER** `nuclear_gen` value=3532 d1=10.0 d12=20.0 z=4.2155609375
- **ROBUST_OUTLIER** `ind_demand` value=-1.226e+04 d1=0.0 d12=0.0 z=4.0469385
- **ROBUST_OUTLIER** `imbalance` value=-2779 d1=0.0 d12=15.0 z=3.5468857543103445
- **ROBUST_OUTLIER** `ind_generation` value=1.868e+04 d1=0.0 d12=15.0 z=3.5468857543103445
- **PERSISTENT_DOWN** `biomass_gen` value=3010 d1=-9.0 d12=-10.0 z=2.4281631
- **ACCELERATION** `biomass_gen` value=3010 d1=-9.0 d12=-10.0 z=2.4281631
- **CHANGE_POINT** `interconnector_net` value=8792 d1=1.0 d12=402.0 z=-0.3866330644148284
- **ACCELERATION** `interconnector_net` value=8792 d1=1.0 d12=402.0 z=-0.3866330644148284
- **PERSISTENT_UP** `wind_gen` value=3716 d1=0.0 d12=24.0 z=0.38044253314606746
- **ACCELERATION** `wind_gen` value=3716 d1=0.0 d12=24.0 z=0.38044253314606746
- **PERSISTENT_DOWN** `ps_gen` value=397 d1=-171.0 d12=-129.0 z=0.2497556280487805
- **REVERSAL** `thermal_base` value=1.656e+04 d1=-79.0 d12=59.0 z=0.10261000253549697

## Nearest historical live analogues

- `2026-09-21T19:21:16.242485Z` distance=0.033 → {'next30m_imbalance_delta': 290.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1.0}
- `2026-09-21T18:51:48.360935Z` distance=0.054 → {'next30m_imbalance_delta': 40.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T18:56:00.829155Z` distance=0.054 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:00:12.997275Z` distance=0.054 → {'next30m_imbalance_delta': 290.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:04:23.644038Z` distance=0.054 → {'next30m_imbalance_delta': 290.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
