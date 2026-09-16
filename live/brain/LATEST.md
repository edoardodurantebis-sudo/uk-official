# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T23:21:21.856031Z`  
Memory snapshots: **672**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=-5756 d1=27.0 d12=-11359.0 z=-4.646570471754637
- **REVERSAL** `interconnector_net` value=-5756 d1=27.0 d12=-11359.0 z=-4.646570471754637
- **ROBUST_OUTLIER** `interconnector_net` value=-5756 d1=27.0 d12=-11359.0 z=-4.646570471754637
- **CHANGE_POINT** `ccgt_gen` value=5756 d1=-57.0 d12=-2942.0 z=-2.6086430057077625
- **CHANGE_POINT** `thermal_base` value=9069 d1=-61.0 d12=-2941.0 z=-2.596555074031891
- **CHANGE_POINT** `ps_gen` value=-249 d1=2.0 d12=-477.0 z=-1.748983646216769
- **CHANGE_POINT** `margin` value=3.448e+04 d1=227.0 d12=76.0 z=1.5138547722222222
- **PERSISTENT_DOWN** `ccgt_gen` value=5756 d1=-57.0 d12=-2942.0 z=-2.6086430057077625
- **PERSISTENT_DOWN** `thermal_base` value=9069 d1=-61.0 d12=-2941.0 z=-2.596555074031891
- **REVERSAL** `ps_gen` value=-249 d1=2.0 d12=-477.0 z=-1.748983646216769
- **PERSISTENT_UP** `wind_gen` value=1.1e+04 d1=19.0 d12=985.0 z=1.7315645950704226
- **PERSISTENT_UP** `margin` value=3.448e+04 d1=227.0 d12=76.0 z=1.5138547722222222
- **ACCELERATION** `margin` value=3.448e+04 d1=227.0 d12=76.0 z=1.5138547722222222
- **PERSISTENT_DOWN** `ind_generation` value=2.572e+04 d1=-16.0 d12=-37.0 z=1.2069816578947368
- **ACCELERATION** `ind_generation` value=2.572e+04 d1=-16.0 d12=-37.0 z=1.2069816578947368

## Nearest historical live analogues

- `2026-09-16T19:51:38.678882Z` distance=0.051 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T15:24:31.150364Z` distance=0.130 → {'next30m_imbalance_delta': -339.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T15:28:42.332391Z` distance=0.130 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -80.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T15:32:56.539709Z` distance=0.130 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -80.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T15:37:09.894991Z` distance=0.130 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -80.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
