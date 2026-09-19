# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T12:53:10.001618Z`  
Memory snapshots: **1493**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.676e+04 d1=0.0 d12=10.0 z=-36.728362616120215
- **ROBUST_OUTLIER** `ind_generation` value=1.676e+04 d1=0.0 d12=10.0 z=-36.728362616120215
- **CHANGE_POINT** `imbalance` value=-3250 d1=0.0 d12=10.0 z=-6.181236771161826
- **ROBUST_OUTLIER** `imbalance` value=-3250 d1=0.0 d12=10.0 z=-6.181236771161826
- **CHANGE_POINT** `wind_gen` value=1.523e+04 d1=-63.0 d12=-596.0 z=-2.686670468619247
- **ROBUST_OUTLIER** `demand_forecast` value=1.951e+04 d1=0.0 d12=0.0 z=3.2718281479508198
- **PERSISTENT_DOWN** `wind_gen` value=1.523e+04 d1=-63.0 d12=-596.0 z=-2.686670468619247
- **CHANGE_POINT** `ccgt_gen` value=3062 d1=24.0 d12=261.0 z=-0.43411308377659574
- **CHANGE_POINT** `thermal_base` value=6390 d1=27.0 d12=255.0 z=-0.43397402519379846
- **CHANGE_POINT** `interconnector_net` value=-1813 d1=1.0 d12=-353.0 z=-0.23635481155462187
- **CHANGE_POINT** `margin` value=3.676e+04 d1=0.0 d12=-24.0 z=-0.0534249306930693
- **REVERSAL** `nuclear_gen` value=3328 d1=3.0 d12=-6.0 z=-1.48387745
- **ACCELERATION** `nuclear_gen` value=3328 d1=3.0 d12=-6.0 z=-1.48387745
- **PERSISTENT_DOWN** `biomass_gen` value=475 d1=0.0 d12=-2.0 z=-0.5058673124999999
- **ACCELERATION** `biomass_gen` value=475 d1=0.0 d12=-2.0 z=-0.5058673124999999

## Nearest historical live analogues

- `2026-09-19T11:54:18.195696Z` distance=0.008 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:58:27.853052Z` distance=0.008 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:50:05.858742Z` distance=0.031 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.035 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.035 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
