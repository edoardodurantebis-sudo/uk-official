# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T02:43:41.119479Z`  
Memory snapshots: **720**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `biomass_gen` value=2035 d1=-2.0 d12=-209.0 z=-315.661203
- **ROBUST_OUTLIER** `ind_demand` value=-1.153e+04 d1=0.0 d12=0.0 z=31.835916200000003
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `margin` value=3.585e+04 d1=0.0 d12=1290.0 z=8.306873763157895
- **ROBUST_OUTLIER** `margin` value=3.585e+04 d1=0.0 d12=1290.0 z=8.306873763157895
- **CHANGE_POINT** `ps_gen` value=-548 d1=4.0 d12=-184.0 z=-0.6355566443057723
- **CHANGE_POINT** `interconnector_net` value=-6469 d1=-3.0 d12=194.0 z=-0.5247246029173419
- **CHANGE_POINT** `imbalance` value=6512 d1=0.0 d12=-4.0 z=-0.13248905803571429
- **REVERSAL** `wind_gen` value=1.341e+04 d1=-26.0 d12=296.0 z=0.9493761386792452
- **PERSISTENT_UP** `nuclear_gen` value=3315 d1=3.0 d12=4.0 z=0.8093876999999999
- **PERSISTENT_DOWN** `ccgt_gen` value=3655 d1=-81.0 d12=-402.0 z=-0.7221347021744595
- **PERSISTENT_DOWN** `thermal_base` value=6970 d1=-78.0 d12=-398.0 z=-0.7215905162647576
- **REVERSAL** `ps_gen` value=-548 d1=4.0 d12=-184.0 z=-0.6355566443057723
- **REVERSAL** `interconnector_net` value=-6469 d1=-3.0 d12=194.0 z=-0.5247246029173419

## Nearest historical live analogues

- `2026-09-16T12:23:49.836209Z` distance=0.544 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T12:28:01.597273Z` distance=0.544 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T11:54:04.473281Z` distance=0.552 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T11:58:14.719154Z` distance=0.552 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T12:02:46.560952Z` distance=0.552 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
