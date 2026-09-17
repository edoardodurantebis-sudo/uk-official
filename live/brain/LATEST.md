# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T02:39:29.397540Z`  
Memory snapshots: **719**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2037 d1=3.0 d12=-352.0 z=-315.1216112
- **REVERSAL** `biomass_gen` value=2037 d1=3.0 d12=-352.0 z=-315.1216112
- **ROBUST_OUTLIER** `biomass_gen` value=2037 d1=3.0 d12=-352.0 z=-315.1216112
- **ROBUST_OUTLIER** `ind_demand` value=-1.153e+04 d1=0.0 d12=120.0 z=31.835916200000003
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `margin` value=3.585e+04 d1=0.0 d12=1290.0 z=6.4198958382838285
- **ROBUST_OUTLIER** `margin` value=3.585e+04 d1=0.0 d12=1290.0 z=6.4198958382838285
- **CHANGE_POINT** `ps_gen` value=-552 d1=-12.0 d12=-244.0 z=-0.6162748608630952
- **CHANGE_POINT** `interconnector_net` value=-6466 d1=1.0 d12=197.0 z=-0.5202086819862652
- **CHANGE_POINT** `imbalance` value=6512 d1=0.0 d12=7.0 z=-0.13248905803571429
- **CHANGE_POINT** `ind_generation` value=2.563e+04 d1=0.0 d12=7.0 z=-0.05506038775510204
- **PERSISTENT_UP** `wind_gen` value=1.344e+04 d1=25.0 d12=375.0 z=0.974437006023222
- **PERSISTENT_DOWN** `thermal_base` value=7048 d1=-35.0 d12=-329.0 z=-0.6946139244925409
- **PERSISTENT_DOWN** `ccgt_gen` value=3736 d1=-37.0 d12=-329.0 z=-0.6941527289931406

## Nearest historical live analogues

- `2026-09-16T12:23:49.836209Z` distance=0.567 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T12:28:01.597273Z` distance=0.567 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T11:54:04.473281Z` distance=0.574 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T11:58:14.719154Z` distance=0.574 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T12:02:46.560952Z` distance=0.574 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
