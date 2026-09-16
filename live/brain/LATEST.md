# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T07:06:38.418412Z`  
Memory snapshots: **478**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `imbalance` value=7314 d1=0.0 d12=100.0 z=11.502298536666666
- **CHANGE_POINT** `ind_generation` value=2.644e+04 d1=0.0 d12=100.0 z=11.502298536666666
- **ROBUST_OUTLIER** `imbalance` value=7314 d1=0.0 d12=100.0 z=11.502298536666666
- **ROBUST_OUTLIER** `ind_generation` value=2.644e+04 d1=0.0 d12=100.0 z=11.502298536666666
- **ROBUST_OUTLIER** `ind_demand` value=-1.247e+04 d1=0.0 d12=-249.0 z=-10.553780794117648
- **CHANGE_POINT** `margin` value=3.74e+04 d1=0.0 d12=-124.0 z=-5.2272955625
- **PERSISTENT_DOWN** `ccgt_gen` value=8320 d1=-37.0 d12=-96.0 z=6.151613164645103
- **ACCELERATION** `ccgt_gen` value=8320 d1=-37.0 d12=-96.0 z=6.151613164645103
- **ROBUST_OUTLIER** `ccgt_gen` value=8320 d1=-37.0 d12=-96.0 z=6.151613164645103
- **PERSISTENT_DOWN** `thermal_base` value=1.165e+04 d1=-39.0 d12=-105.0 z=6.146159069631626
- **ACCELERATION** `thermal_base` value=1.165e+04 d1=-39.0 d12=-105.0 z=6.146159069631626
- **ROBUST_OUTLIER** `thermal_base` value=1.165e+04 d1=-39.0 d12=-105.0 z=6.146159069631626
- **ROBUST_OUTLIER** `margin` value=3.74e+04 d1=0.0 d12=-124.0 z=-5.2272955625
- **CHANGE_POINT** `interconnector_net` value=6101 d1=1521.0 d12=5151.0 z=1.4660669627139367
- **CHANGE_POINT** `ps_gen` value=222 d1=0.0 d12=4.0 z=0.4496598333333333

## Nearest historical live analogues

- `2026-09-16T05:51:19.396641Z` distance=0.699 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:55:30.704372Z` distance=0.699 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -79.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:59:40.455597Z` distance=0.699 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -79.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:03:52.494424Z` distance=0.699 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -79.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:08:05.860458Z` distance=0.699 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -79.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
