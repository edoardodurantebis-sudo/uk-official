# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T23:47:00.820172Z`  
Memory snapshots: **678**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=-657.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=657.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6445 d1=-9.0 d12=-10837.0 z=-4.8958553290184925
- **CHANGE_POINT** `ccgt_gen` value=5356 d1=-39.0 d12=-3053.0 z=-2.9166291929223744
- **CHANGE_POINT** `thermal_base` value=8670 d1=-40.0 d12=-3045.0 z=-2.903071486617312
- **PERSISTENT_DOWN** `interconnector_net` value=-6445 d1=-9.0 d12=-10837.0 z=-4.8958553290184925
- **ROBUST_OUTLIER** `interconnector_net` value=-6445 d1=-9.0 d12=-10837.0 z=-4.8958553290184925
- **CHANGE_POINT** `ind_generation` value=2.572e+04 d1=0.0 d12=-37.0 z=1.2069816578947368
- **CHANGE_POINT** `ps_gen` value=-250 d1=-3.0 d12=-476.0 z=-1.0395655127427184
- **PERSISTENT_DOWN** `ccgt_gen` value=5356 d1=-39.0 d12=-3053.0 z=-2.9166291929223744
- **PERSISTENT_DOWN** `thermal_base` value=8670 d1=-40.0 d12=-3045.0 z=-2.903071486617312
- **CHANGE_POINT** `imbalance` value=6603 d1=0.0 d12=-37.0 z=0.3118608521505376
- **PERSISTENT_UP** `wind_gen` value=1.154e+04 d1=47.0 d12=1405.0 z=1.551307828646264
- **REVERSAL** `nuclear_gen` value=3314 d1=-1.0 d12=8.0 z=1.1241495833333335
- **PERSISTENT_UP** `biomass_gen` value=3206 d1=1.0 d12=1.0 z=-0.67448975

## Nearest historical live analogues

- `2026-09-16T14:21:30.462993Z` distance=0.278 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.280 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:29:54.321922Z` distance=0.280 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:34:06.314775Z` distance=0.280 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:38:16.233128Z` distance=0.280 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
