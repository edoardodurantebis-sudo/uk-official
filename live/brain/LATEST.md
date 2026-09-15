# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T09:19:04.462321Z`  
Memory snapshots: **168**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2040 d1=1.0 d12=-565.0 z=-71.618548
- **REVERSAL** `biomass_gen` value=2040 d1=1.0 d12=-565.0 z=-71.618548
- **ROBUST_OUTLIER** `biomass_gen` value=2040 d1=1.0 d12=-565.0 z=-71.618548
- **CHANGE_POINT** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=-50.0 z=56.657139
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=-50.0 z=56.657139
- **PERSISTENT_UP** `margin` value=3.45e+04 d1=420.0 d12=453.0 z=7.217040325000001
- **ACCELERATION** `margin` value=3.45e+04 d1=420.0 d12=453.0 z=7.217040325000001
- **ROBUST_OUTLIER** `margin` value=3.45e+04 d1=420.0 d12=453.0 z=7.217040325000001
- **CHANGE_POINT** `ps_gen` value=-1160 d1=-174.0 d12=-853.0 z=-4.133095949817519
- **CHANGE_POINT** `wind_gen` value=1.204e+04 d1=41.0 d12=-601.0 z=-2.9379216995192308
- **CHANGE_POINT** `interconnector_net` value=1.059e+04 d1=48.0 d12=2317.0 z=2.507095979064691
- **PERSISTENT_DOWN** `ps_gen` value=-1160 d1=-174.0 d12=-853.0 z=-4.133095949817519
- **ROBUST_OUTLIER** `ps_gen` value=-1160 d1=-174.0 d12=-853.0 z=-4.133095949817519
- **CHANGE_POINT** `ccgt_gen` value=2510 d1=10.0 d12=-543.0 z=-1.6817752341688654
- **CHANGE_POINT** `thermal_base` value=5827 d1=13.0 d12=-540.0 z=-1.6569935772962485

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=1.468 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=1.468 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=1.468 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=1.468 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=1.468 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
