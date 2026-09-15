# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T07:59:20.872877Z`  
Memory snapshots: **149**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=6440 d1=-26.0 d12=4413.0 z=2.643749417012243
- **CHANGE_POINT** `ccgt_gen` value=3000 d1=5.0 d12=-686.0 z=-2.1224940609418286
- **CHANGE_POINT** `thermal_base` value=6317 d1=7.0 d12=-684.0 z=-2.1107347702156334
- **CHANGE_POINT** `wind_gen` value=1.255e+04 d1=-62.0 d12=-1046.0 z=-1.8461995080128206
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=0.0 d12=144.0 z=3.1074706339285716
- **PERSISTENT_UP** `biomass_gen` value=3247 d1=7.0 d12=7.0 z=2.9227889166666667
- **ACCELERATION** `biomass_gen` value=3247 d1=7.0 d12=7.0 z=2.9227889166666667
- **CHANGE_POINT** `margin` value=3.413e+04 d1=0.0 d12=158.0 z=0.67448975
- **REVERSAL** `interconnector_net` value=6440 d1=-26.0 d12=4413.0 z=2.643749417012243
- **REVERSAL** `ccgt_gen` value=3000 d1=5.0 d12=-686.0 z=-2.1224940609418286
- **REVERSAL** `thermal_base` value=6317 d1=7.0 d12=-684.0 z=-2.1107347702156334
- **CHANGE_POINT** `ps_gen` value=-259 d1=2.0 d12=-5.0 z=0.0031226377314814814
- **CHANGE_POINT** `imbalance` value=-454 d1=0.0 d12=249.0 z=0.0
- **CHANGE_POINT** `ind_generation` value=2.003e+04 d1=0.0 d12=249.0 z=0.0
- **PERSISTENT_DOWN** `wind_gen` value=1.255e+04 d1=-62.0 d12=-1046.0 z=-1.8461995080128206

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=1.114 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=1.114 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=1.114 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=1.114 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=1.114 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
