# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T02:01:47.345807Z`  
Memory snapshots: **710**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2057 d1=-75.0 d12=-957.0 z=-387.494361375
- **PERSISTENT_DOWN** `biomass_gen` value=2057 d1=-75.0 d12=-957.0 z=-387.494361375
- **ROBUST_OUTLIER** `biomass_gen` value=2057 d1=-75.0 d12=-957.0 z=-387.494361375
- **PERSISTENT_UP** `ind_demand` value=-1.153e+04 d1=0.0 d12=220.0 z=31.835916200000003
- **ROBUST_OUTLIER** `ind_demand` value=-1.153e+04 d1=0.0 d12=220.0 z=31.835916200000003
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `thermal_base` value=7390 d1=12.0 d12=-718.0 z=-2.1148472660793707
- **CHANGE_POINT** `ccgt_gen` value=4077 d1=11.0 d12=-711.0 z=-2.1068899584327085
- **PERSISTENT_DOWN** `interconnector_net` value=-6697 d1=-12.0 d12=-70.0 z=-3.2775764043125264
- **ROBUST_OUTLIER** `interconnector_net` value=-6697 d1=-12.0 d12=-70.0 z=-3.2775764043125264
- **CHANGE_POINT** `ps_gen` value=-597 d1=0.0 d12=-285.0 z=-1.0548891824644548
- **CHANGE_POINT** `margin` value=3.456e+04 d1=0.0 d12=50.0 z=0.9003101068281939
- **REVERSAL** `thermal_base` value=7390 d1=12.0 d12=-718.0 z=-2.1148472660793707
- **REVERSAL** `ccgt_gen` value=4077 d1=11.0 d12=-711.0 z=-2.1068899584327085

## Nearest historical live analogues

- `2026-09-17T00:54:40.714610Z` distance=0.483 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:58:51.888099Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:03:09.320399Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:07:19.944210Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:50:29.902043Z` distance=0.518 → {'next30m_imbalance_delta': -43.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
