# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T19:19:15.605715Z`  
Memory snapshots: **310**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **ROBUST_OUTLIER** `biomass_gen` value=3283 d1=1.0 d12=20.0 z=35.701440215517245
- **ROBUST_OUTLIER** `ind_demand` value=-1.191e+04 d1=0.0 d12=-1.0 z=4.72142825
- **CHANGE_POINT** `margin` value=3.559e+04 d1=0.0 d12=-65.0 z=1.8240548891304347
- **CHANGE_POINT** `interconnector_net` value=-435 d1=-67.0 d12=1241.0 z=-0.6657366386725991
- **CHANGE_POINT** `imbalance` value=5739 d1=0.0 d12=2.0 z=-0.48387308152173913
- **CHANGE_POINT** `ind_generation` value=2.486e+04 d1=0.0 d12=2.0 z=-0.48387308152173913
- **PERSISTENT_DOWN** `ps_gen` value=552 d1=-191.0 d12=-253.0 z=0.7255380885668277
- **ACCELERATION** `ps_gen` value=552 d1=-191.0 d12=-253.0 z=0.7255380885668277
- **PERSISTENT_UP** `wind_gen` value=1.041e+04 d1=191.0 d12=500.0 z=0.6708634610215054
- **ACCELERATION** `wind_gen` value=1.041e+04 d1=191.0 d12=500.0 z=0.6708634610215054
- **PERSISTENT_DOWN** `thermal_base` value=1.387e+04 d1=-47.0 d12=-125.0 z=0.665779091363467
- **ACCELERATION** `thermal_base` value=1.387e+04 d1=-47.0 d12=-125.0 z=0.665779091363467
- **REVERSAL** `interconnector_net` value=-435 d1=-67.0 d12=1241.0 z=-0.6657366386725991
- **PERSISTENT_DOWN** `ccgt_gen` value=1.055e+04 d1=-48.0 d12=-127.0 z=0.6655322716271566
- **ACCELERATION** `ccgt_gen` value=1.055e+04 d1=-48.0 d12=-127.0 z=0.6655322716271566

## Nearest historical live analogues

- `2026-09-15T18:24:34.306197Z` distance=0.047 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:20:25.201646Z` distance=0.053 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:50:55.506503Z` distance=0.063 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.063 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:59:22.215947Z` distance=0.063 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
