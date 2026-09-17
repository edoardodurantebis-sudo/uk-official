# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T02:52:02.690108Z`  
Memory snapshots: **722**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **PERSISTENT_DOWN** `biomass_gen` value=2034 d1=-1.0 d12=-23.0 z=-315.93099889999996
- **ROBUST_OUTLIER** `biomass_gen` value=2034 d1=-1.0 d12=-23.0 z=-315.93099889999996
- **PERSISTENT_UP** `ind_demand` value=-1.152e+04 d1=11.0 d12=11.0 z=33.31979365
- **ACCELERATION** `ind_demand` value=-1.152e+04 d1=11.0 d12=11.0 z=33.31979365
- **ROBUST_OUTLIER** `ind_demand` value=-1.152e+04 d1=11.0 d12=11.0 z=33.31979365
- **CHANGE_POINT** `margin` value=3.586e+04 d1=11.0 d12=1301.0 z=12.22068928618421
- **PERSISTENT_UP** `margin` value=3.586e+04 d1=11.0 d12=1301.0 z=12.22068928618421
- **ROBUST_OUTLIER** `margin` value=3.586e+04 d1=11.0 d12=1301.0 z=12.22068928618421
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `ps_gen` value=-548 d1=3.0 d12=49.0 z=-0.6711506918316832
- **CHANGE_POINT** `interconnector_net` value=-6473 d1=-1.0 d12=224.0 z=-0.528106331803005
- **PERSISTENT_UP** `nuclear_gen` value=3317 d1=0.0 d12=4.0 z=1.1241495833333335
- **ACCELERATION** `nuclear_gen` value=3317 d1=0.0 d12=4.0 z=1.1241495833333335
- **ACCELERATION** `wind_gen` value=1.344e+04 d1=42.0 d12=109.0 z=0.9481814776108518

## Nearest historical live analogues

- `2026-09-16T12:23:49.836209Z` distance=0.566 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T12:28:01.597273Z` distance=0.566 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T11:54:04.473281Z` distance=0.573 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T11:58:14.719154Z` distance=0.573 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T12:02:46.560952Z` distance=0.573 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
