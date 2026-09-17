# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T02:31:05.012181Z`  
Memory snapshots: **717**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2034 d1=0.0 d12=-505.0 z=-315.93099889999996
- **ROBUST_OUTLIER** `biomass_gen` value=2034 d1=0.0 d12=-505.0 z=-315.93099889999996
- **CHANGE_POINT** `ind_demand` value=-1.153e+04 d1=0.0 d12=120.0 z=31.835916200000003
- **ROBUST_OUTLIER** `ind_demand` value=-1.153e+04 d1=0.0 d12=120.0 z=31.835916200000003
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `margin` value=3.585e+04 d1=0.0 d12=1359.0 z=6.4198958382838285
- **PERSISTENT_UP** `margin` value=3.585e+04 d1=0.0 d12=1359.0 z=6.4198958382838285
- **ROBUST_OUTLIER** `margin` value=3.585e+04 d1=0.0 d12=1359.0 z=6.4198958382838285
- **CHANGE_POINT** `ps_gen` value=-540 d1=-2.0 d12=-232.0 z=-0.5655778073654391
- **REVERSAL** `wind_gen` value=1.341e+04 d1=-24.0 d12=405.0 z=1.098715456318365
- **PERSISTENT_DOWN** `thermal_base` value=7083 d1=-19.0 d12=-290.0 z=-0.6828885687260536
- **PERSISTENT_DOWN** `ccgt_gen` value=3773 d1=-17.0 d12=-288.0 z=-0.6817510032894737
- **PERSISTENT_DOWN** `ps_gen` value=-540 d1=-2.0 d12=-232.0 z=-0.5655778073654391
- **PERSISTENT_UP** `interconnector_net` value=-6467 d1=112.0 d12=196.0 z=-0.5377550654311649

## Nearest historical live analogues

- `2026-09-16T12:23:49.836209Z` distance=0.593 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T12:28:01.597273Z` distance=0.593 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T11:54:04.473281Z` distance=0.600 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T11:58:14.719154Z` distance=0.600 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T12:02:46.560952Z` distance=0.600 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
