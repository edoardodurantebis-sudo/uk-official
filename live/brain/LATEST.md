# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T02:26:53.112988Z`  
Memory snapshots: **716**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2034 d1=1.0 d12=-654.0 z=-315.93099889999996
- **REVERSAL** `biomass_gen` value=2034 d1=1.0 d12=-654.0 z=-315.93099889999996
- **ROBUST_OUTLIER** `biomass_gen` value=2034 d1=1.0 d12=-654.0 z=-315.93099889999996
- **CHANGE_POINT** `ind_demand` value=-1.153e+04 d1=0.0 d12=120.0 z=31.835916200000003
- **ROBUST_OUTLIER** `ind_demand` value=-1.153e+04 d1=0.0 d12=120.0 z=31.835916200000003
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `margin` value=3.585e+04 d1=0.0 d12=1359.0 z=6.4198958382838285
- **PERSISTENT_UP** `margin` value=3.585e+04 d1=0.0 d12=1359.0 z=6.4198958382838285
- **ACCELERATION** `margin` value=3.585e+04 d1=0.0 d12=1359.0 z=6.4198958382838285
- **ROBUST_OUTLIER** `margin` value=3.585e+04 d1=0.0 d12=1359.0 z=6.4198958382838285
- **CHANGE_POINT** `ps_gen` value=-538 d1=0.0 d12=-229.0 z=-1.1603417162601626
- **PERSISTENT_DOWN** `ps_gen` value=-538 d1=0.0 d12=-229.0 z=-1.1603417162601626
- **REVERSAL** `wind_gen` value=1.344e+04 d1=-77.0 d12=480.0 z=1.1014340706709096
- **PERSISTENT_DOWN** `ccgt_gen` value=3790 d1=-11.0 d12=-259.0 z=-0.8512080884752438

## Nearest historical live analogues

- `2026-09-16T12:23:49.836209Z` distance=0.593 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T12:28:01.597273Z` distance=0.593 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T11:54:04.473281Z` distance=0.600 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T11:58:14.719154Z` distance=0.600 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T12:02:46.560952Z` distance=0.600 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
