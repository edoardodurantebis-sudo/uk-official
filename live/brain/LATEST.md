# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T19:15:03.341374Z`  
Memory snapshots: **309**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **ACCELERATION** `biomass_gen` value=3282 d1=0.0 d12=18.0 z=35.67818194827586
- **ROBUST_OUTLIER** `biomass_gen` value=3282 d1=0.0 d12=18.0 z=35.67818194827586
- **ROBUST_OUTLIER** `ind_demand` value=-1.191e+04 d1=0.0 d12=-1.0 z=4.72142825
- **CHANGE_POINT** `margin` value=3.559e+04 d1=0.0 d12=-65.0 z=1.906966475
- **CHANGE_POINT** `ps_gen` value=743 d1=0.0 d12=-62.0 z=0.9269612460845733
- **CHANGE_POINT** `thermal_base` value=1.392e+04 d1=0.0 d12=-105.0 z=0.7015818889451728
- **CHANGE_POINT** `ccgt_gen` value=1.06e+04 d1=0.0 d12=-108.0 z=0.7008978337498513
- **CHANGE_POINT** `interconnector_net` value=-368 d1=0.0 d12=1307.0 z=-0.6628129914836188
- **CHANGE_POINT** `imbalance` value=5739 d1=0.0 d12=2.0 z=-0.4496598333333333
- **CHANGE_POINT** `ind_generation` value=2.486e+04 d1=0.0 d12=2.0 z=-0.4496598333333333
- **PERSISTENT_DOWN** `ps_gen` value=743 d1=0.0 d12=-62.0 z=0.9269612460845733
- **ACCELERATION** `ps_gen` value=743 d1=0.0 d12=-62.0 z=0.9269612460845733
- **ACCELERATION** `nuclear_gen` value=3319 d1=0.0 d12=3.0 z=-0.8243763611111111
- **PERSISTENT_DOWN** `thermal_base` value=1.392e+04 d1=0.0 d12=-105.0 z=0.7015818889451728
- **ACCELERATION** `thermal_base` value=1.392e+04 d1=0.0 d12=-105.0 z=0.7015818889451728

## Nearest historical live analogues

- `2026-09-15T18:20:25.201646Z` distance=0.053 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:50:55.506503Z` distance=0.063 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.063 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:59:22.215947Z` distance=0.063 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:03:35.364442Z` distance=0.063 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
