# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T11:32:27.606520Z`  
Memory snapshots: **1187**  
Current physical regime: **BALANCED**

## Active patterns

- **PERSISTENT_DOWN** `biomass_gen` value=1085 d1=0.0 d12=-3.0 z=-45.44374690625
- **ROBUST_OUTLIER** `biomass_gen` value=1085 d1=0.0 d12=-3.0 z=-45.44374690625
- **CHANGE_POINT** `ind_generation` value=2.567e+04 d1=0.0 d12=-1092.0 z=-6.208206731182797
- **ROBUST_OUTLIER** `ind_generation` value=2.567e+04 d1=0.0 d12=-1092.0 z=-6.208206731182797
- **CHANGE_POINT** `thermal_base` value=5774 d1=-26.0 d12=-528.0 z=-1.5232912803302225
- **CHANGE_POINT** `ccgt_gen` value=2439 d1=-27.0 d12=-531.0 z=-1.5195345728868195
- **CHANGE_POINT** `ind_demand` value=-1.074e+04 d1=0.0 d12=3052.0 z=1.1809529015017668
- **CHANGE_POINT** `margin` value=3.812e+04 d1=0.0 d12=1771.0 z=1.0089242510416667
- **REVERSAL** `ps_gen` value=-718 d1=-121.0 d12=5.0 z=-2.3992230553633216
- **ACCELERATION** `ps_gen` value=-718 d1=-121.0 d12=5.0 z=-2.3992230553633216
- **CHANGE_POINT** `ts_demand_forecast` value=1.667e+04 d1=0.0 d12=-3011.0 z=-0.21875343243243245
- **PERSISTENT_DOWN** `thermal_base` value=5774 d1=-26.0 d12=-528.0 z=-1.5232912803302225
- **PERSISTENT_DOWN** `ccgt_gen` value=2439 d1=-27.0 d12=-531.0 z=-1.5195345728868195
- **PERSISTENT_UP** `imbalance` value=8997 d1=0.0 d12=1919.0 z=-1.5055794968007312
- **PERSISTENT_DOWN** `interconnector_net` value=5073 d1=-436.0 d12=-595.0 z=0.6113460287234043

## Nearest historical live analogues

- `2026-09-18T05:50:47.091039Z` distance=0.518 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T05:54:59.248868Z` distance=0.518 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T05:59:09.222653Z` distance=0.518 → {'next30m_imbalance_delta': -67.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T06:03:20.906831Z` distance=0.518 → {'next30m_imbalance_delta': -67.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T06:07:33.046654Z` distance=0.518 → {'next30m_imbalance_delta': -67.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
