# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T07:50:58.752993Z`  
Memory snapshots: **147**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=6466 d1=-18.0 d12=7127.0 z=2.650675457099131
- **CHANGE_POINT** `thermal_base` value=6310 d1=-30.0 d12=-1018.0 z=-2.010498293269231
- **CHANGE_POINT** `ccgt_gen` value=2995 d1=-27.0 d12=-1010.0 z=-1.9874528070388349
- **CHANGE_POINT** `wind_gen` value=1.261e+04 d1=55.0 d12=-880.0 z=-1.7121662884615385
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=0.0 d12=144.0 z=3.1074706339285716
- **CHANGE_POINT** `margin` value=3.413e+04 d1=0.0 d12=158.0 z=0.67448975
- **REVERSAL** `interconnector_net` value=6466 d1=-18.0 d12=7127.0 z=2.650675457099131
- **REVERSAL** `biomass_gen` value=3240 d1=-4.0 d12=4.0 z=2.3074649342105262
- **ACCELERATION** `biomass_gen` value=3240 d1=-4.0 d12=4.0 z=2.3074649342105262
- **ACCELERATION** `nuclear_gen` value=3315 d1=-3.0 d12=-8.0 z=-2.248299166666667
- **PERSISTENT_DOWN** `thermal_base` value=6310 d1=-30.0 d12=-1018.0 z=-2.010498293269231
- **CHANGE_POINT** `imbalance` value=-454 d1=0.0 d12=249.0 z=0.0
- **CHANGE_POINT** `ind_generation` value=2.003e+04 d1=0.0 d12=249.0 z=0.0
- **PERSISTENT_DOWN** `ccgt_gen` value=2995 d1=-27.0 d12=-1010.0 z=-1.9874528070388349
- **PERSISTENT_DOWN** `residual_proxy` value=1664 d1=0.0 d12=-1211.0 z=-1.8917879426229507

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=1.113 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=1.113 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=1.113 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=1.113 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=1.113 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
