# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T02:47:52.502968Z`  
Memory snapshots: **721**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `biomass_gen` value=2035 d1=0.0 d12=-97.0 z=-315.661203
- **ROBUST_OUTLIER** `ind_demand` value=-1.153e+04 d1=0.0 d12=0.0 z=31.835916200000003
- **CHANGE_POINT** `margin` value=3.585e+04 d1=0.0 d12=1290.0 z=12.123065769736842
- **ROBUST_OUTLIER** `margin` value=3.585e+04 d1=0.0 d12=1290.0 z=12.123065769736842
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `ps_gen` value=-551 d1=-3.0 d12=46.0 z=-0.6767084662828947
- **CHANGE_POINT** `interconnector_net` value=-6472 d1=-3.0 d12=213.0 z=-0.529243464109589
- **CHANGE_POINT** `imbalance` value=6512 d1=0.0 d12=-4.0 z=-0.13613554587155963
- **PERSISTENT_UP** `nuclear_gen` value=3317 d1=2.0 d12=5.0 z=1.3489795
- **REVERSAL** `wind_gen` value=1.339e+04 d1=-18.0 d12=263.0 z=0.9427124960641399
- **PERSISTENT_DOWN** `ccgt_gen` value=3584 d1=-71.0 d12=-482.0 z=-0.7472541377199694
- **PERSISTENT_DOWN** `thermal_base` value=6901 d1=-69.0 d12=-477.0 z=-0.7460682540816327
- **REVERSAL** `ps_gen` value=-551 d1=-3.0 d12=46.0 z=-0.6767084662828947
- **REVERSAL** `interconnector_net` value=-6472 d1=-3.0 d12=213.0 z=-0.529243464109589

## Nearest historical live analogues

- `2026-09-16T12:23:49.836209Z` distance=0.544 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T12:28:01.597273Z` distance=0.544 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T11:54:04.473281Z` distance=0.552 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T11:58:14.719154Z` distance=0.552 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T12:02:46.560952Z` distance=0.552 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
