# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T21:30:31.120147Z`  
Memory snapshots: **341**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=8937 d1=-290.0 d12=-3795.0 z=-7.087471300790067
- **CHANGE_POINT** `ccgt_gen` value=5615 d1=-289.0 d12=-3795.0 z=-7.037529263733184
- **PERSISTENT_DOWN** `thermal_base` value=8937 d1=-290.0 d12=-3795.0 z=-7.087471300790067
- **ROBUST_OUTLIER** `thermal_base` value=8937 d1=-290.0 d12=-3795.0 z=-7.087471300790067
- **PERSISTENT_DOWN** `ccgt_gen` value=5615 d1=-289.0 d12=-3795.0 z=-7.037529263733184
- **ROBUST_OUTLIER** `ccgt_gen` value=5615 d1=-289.0 d12=-3795.0 z=-7.037529263733184
- **REVERSAL** `wind_gen` value=1.238e+04 d1=-59.0 d12=455.0 z=6.001268709567198
- **ROBUST_OUTLIER** `wind_gen` value=1.238e+04 d1=-59.0 d12=455.0 z=6.001268709567198
- **CHANGE_POINT** `ps_gen` value=-258 d1=-1.0 d12=4.0 z=-0.6798146690789474
- **PERSISTENT_UP** `margin` value=3.572e+04 d1=0.0 d12=23.0 z=0.7016869173387097
- **REVERSAL** `ps_gen` value=-258 d1=-1.0 d12=4.0 z=-0.6798146690789474
- **ACCELERATION** `ps_gen` value=-258 d1=-1.0 d12=4.0 z=-0.6798146690789474
- **PERSISTENT_UP** `interconnector_net` value=1258 d1=519.0 d12=1181.0 z=0.405098948948949
- **ACCELERATION** `interconnector_net` value=1258 d1=519.0 d12=1181.0 z=0.405098948948949
- **PERSISTENT_DOWN** `biomass_gen` value=3251 d1=-8.0 d12=-26.0 z=0.2972327711864407

## Nearest historical live analogues

- `2026-09-15T20:22:50.211969Z` distance=0.018 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:27:39.367678Z` distance=0.018 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:31:49.811988Z` distance=0.018 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:36:00.984640Z` distance=0.018 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:31:50.302711Z` distance=0.061 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
