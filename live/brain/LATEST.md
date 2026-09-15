# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T16:17:45.330338Z`  
Memory snapshots: **267**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=8877 d1=701.0 d12=4276.0 z=18.592004553949902
- **CHANGE_POINT** `thermal_base` value=1.22e+04 d1=706.0 d12=4274.0 z=18.43949224760994
- **PERSISTENT_UP** `ccgt_gen` value=8877 d1=701.0 d12=4276.0 z=18.592004553949902
- **ROBUST_OUTLIER** `ccgt_gen` value=8877 d1=701.0 d12=4276.0 z=18.592004553949902
- **PERSISTENT_UP** `thermal_base` value=1.22e+04 d1=706.0 d12=4274.0 z=18.43949224760994
- **ROBUST_OUTLIER** `thermal_base` value=1.22e+04 d1=706.0 d12=4274.0 z=18.43949224760994
- **CHANGE_POINT** `interconnector_net` value=2666 d1=68.0 d12=-3853.0 z=-14.890248717763157
- **REVERSAL** `interconnector_net` value=2666 d1=68.0 d12=-3853.0 z=-14.890248717763157
- **ROBUST_OUTLIER** `interconnector_net` value=2666 d1=68.0 d12=-3853.0 z=-14.890248717763157
- **CHANGE_POINT** `ps_gen` value=123 d1=-6.0 d12=259.0 z=2.986237850204499
- **CHANGE_POINT** `biomass_gen` value=1803 d1=52.0 d12=55.0 z=2.2817844734042554
- **CHANGE_POINT** `imbalance` value=5825 d1=0.0 d12=8.0 z=1.146218777607362
- **CHANGE_POINT** `ind_generation` value=2.495e+04 d1=0.0 d12=8.0 z=1.0628323333333334
- **REVERSAL** `ps_gen` value=123 d1=-6.0 d12=259.0 z=2.986237850204499
- **CHANGE_POINT** `margin` value=3.497e+04 d1=0.0 d12=320.0 z=-0.47336917

## Nearest historical live analogues

- `2026-09-15T13:25:09.783150Z` distance=0.184 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:29:22.306019Z` distance=0.184 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:33:32.333732Z` distance=0.184 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:37:45.498739Z` distance=0.184 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:41:57.247780Z` distance=0.184 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
