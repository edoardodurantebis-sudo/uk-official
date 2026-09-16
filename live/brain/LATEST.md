# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T10:29:49.153739Z`  
Memory snapshots: **526**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ps_gen` value=-5 d1=0.0 d12=-235.0 z=-30.7567326
- **ROBUST_OUTLIER** `margin` value=3.422e+04 d1=0.0 d12=-284.0 z=-14.78295465862069
- **PERSISTENT_UP** `imbalance` value=5373 d1=0.0 d12=9.0 z=-10.93051613551402
- **ROBUST_OUTLIER** `imbalance` value=5373 d1=0.0 d12=9.0 z=-10.93051613551402
- **CHANGE_POINT** `ind_demand` value=-1.511e+04 d1=0.0 d12=-1226.0 z=-7.156634214859437
- **PERSISTENT_DOWN** `ind_demand` value=-1.511e+04 d1=0.0 d12=-1226.0 z=-7.156634214859437
- **ROBUST_OUTLIER** `ind_demand` value=-1.511e+04 d1=0.0 d12=-1226.0 z=-7.156634214859437
- **PERSISTENT_UP** `ind_generation` value=2.601e+04 d1=0.0 d12=9.0 z=-1.6059279761904761
- **PERSISTENT_DOWN** `wind_gen` value=5190 d1=-58.0 d12=-462.0 z=-1.4774401745143582
- **PERSISTENT_UP** `nuclear_gen` value=3326 d1=1.0 d12=4.0 z=-1.0117346249999999
- **PERSISTENT_DOWN** `thermal_base` value=9651 d1=-23.0 d12=-8.0 z=-1.0077763518192489
- **ACCELERATION** `thermal_base` value=9651 d1=-23.0 d12=-8.0 z=-1.0077763518192489
- **PERSISTENT_DOWN** `ccgt_gen` value=6325 d1=-24.0 d12=-12.0 z=-1.0036154001761597
- **ACCELERATION** `ccgt_gen` value=6325 d1=-24.0 d12=-12.0 z=-1.0036154001761597
- **PERSISTENT_UP** `biomass_gen` value=3228 d1=1.0 d12=50.0 z=-0.8993196666666666

## Nearest historical live analogues

- `2026-09-16T09:22:28.850484Z` distance=3.163 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:26:41.423464Z` distance=3.163 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:30:50.292124Z` distance=3.163 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:35:00.318078Z` distance=3.163 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:52:24.970739Z` distance=6.309 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
