# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T16:42:30.303350Z`  
Memory snapshots: **614**  
Current physical regime: **BALANCED**

Regime read: wind falling.

## Active patterns

- **CHANGE_POINT** `ps_gen` value=1209 d1=54.0 d12=986.0 z=408.7407885
- **PERSISTENT_UP** `ps_gen` value=1209 d1=54.0 d12=986.0 z=408.7407885
- **ROBUST_OUTLIER** `ps_gen` value=1209 d1=54.0 d12=986.0 z=408.7407885
- **CHANGE_POINT** `interconnector_net` value=8029 d1=-19.0 d12=-2878.0 z=-3.442781889722431
- **CHANGE_POINT** `thermal_base` value=1.298e+04 d1=-16.0 d12=1680.0 z=3.3482518082959642
- **CHANGE_POINT** `ccgt_gen` value=9672 d1=-17.0 d12=1677.0 z=3.149145691850594
- **PERSISTENT_DOWN** `interconnector_net` value=8029 d1=-19.0 d12=-2878.0 z=-3.442781889722431
- **ROBUST_OUTLIER** `interconnector_net` value=8029 d1=-19.0 d12=-2878.0 z=-3.442781889722431
- **REVERSAL** `thermal_base` value=1.298e+04 d1=-16.0 d12=1680.0 z=3.3482518082959642
- **ROBUST_OUTLIER** `thermal_base` value=1.298e+04 d1=-16.0 d12=1680.0 z=3.3482518082959642
- **CHANGE_POINT** `wind_gen` value=5937 d1=162.0 d12=493.0 z=1.2210177921099292
- **REVERSAL** `ccgt_gen` value=9672 d1=-17.0 d12=1677.0 z=3.149145691850594
- **ROBUST_OUTLIER** `ccgt_gen` value=9672 d1=-17.0 d12=1677.0 z=3.149145691850594
- **CHANGE_POINT** `biomass_gen` value=3219 d1=-1.0 d12=-17.0 z=-1.04239325
- **CHANGE_POINT** `margin` value=3.417e+04 d1=0.0 d12=-147.0 z=-0.659797894059406

## Nearest historical live analogues

- `2026-09-16T15:24:31.150364Z` distance=0.098 → {'next30m_imbalance_delta': -339.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T15:28:42.332391Z` distance=0.098 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -80.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T15:32:56.539709Z` distance=0.098 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -80.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T15:37:09.894991Z` distance=0.098 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -80.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T15:41:23.424005Z` distance=0.098 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -80.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
