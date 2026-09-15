# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T09:10:39.885473Z`  
Memory snapshots: **166**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2039 d1=-2.0 d12=-862.0 z=-71.67986525
- **PERSISTENT_DOWN** `biomass_gen` value=2039 d1=-2.0 d12=-862.0 z=-71.67986525
- **ROBUST_OUTLIER** `biomass_gen` value=2039 d1=-2.0 d12=-862.0 z=-71.67986525
- **CHANGE_POINT** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=-50.0 z=56.657139
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=-50.0 z=56.657139
- **CHANGE_POINT** `ps_gen` value=-986 d1=-124.0 d12=-440.0 z=-3.283829658759124
- **CHANGE_POINT** `wind_gen` value=1.2e+04 d1=12.0 d12=-752.0 z=-3.026556570512821
- **CHANGE_POINT** `ccgt_gen` value=2500 d1=-28.0 d12=-505.0 z=-1.726910754021448
- **CHANGE_POINT** `thermal_base` value=5814 d1=-26.0 d12=-504.0 z=-1.7151819930647292
- **PERSISTENT_DOWN** `ps_gen` value=-986 d1=-124.0 d12=-440.0 z=-3.283829658759124
- **ROBUST_OUTLIER** `ps_gen` value=-986 d1=-124.0 d12=-440.0 z=-3.283829658759124
- **REVERSAL** `wind_gen` value=1.2e+04 d1=12.0 d12=-752.0 z=-3.026556570512821
- **ROBUST_OUTLIER** `wind_gen` value=1.2e+04 d1=12.0 d12=-752.0 z=-3.026556570512821
- **PERSISTENT_UP** `interconnector_net` value=1.054e+04 d1=178.0 d12=2242.0 z=2.5370474718720666
- **CHANGE_POINT** `demand_forecast` value=2.007e+04 d1=0.0 d12=0.0 z=None

## Nearest historical live analogues

- `2026-09-15T03:51:58.464857Z` distance=0.310 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:56:09.070441Z` distance=0.310 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:00:20.228720Z` distance=0.310 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:04:32.418140Z` distance=0.310 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:08:45.476934Z` distance=0.310 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
