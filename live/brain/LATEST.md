# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T12:17:37.622014Z`  
Memory snapshots: **1826**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=0.0 z=41.6497420625
- **CHANGE_POINT** `ind_generation` value=1.537e+04 d1=0.0 d12=0.0 z=2.327446255319149
- **CHANGE_POINT** `margin` value=3.578e+04 d1=0.0 d12=0.0 z=-2.134635153240741
- **CHANGE_POINT** `wind_gen` value=1.266e+04 d1=38.0 d12=-585.0 z=-2.0935282668024437
- **CHANGE_POINT** `imbalance` value=-5732 d1=0.0 d12=0.0 z=0.67448975
- **CHANGE_POINT** `thermal_base` value=5719 d1=5.0 d12=-2.0 z=-0.47847559016393443
- **CHANGE_POINT** `ccgt_gen` value=2385 d1=1.0 d12=-8.0 z=-0.4756401792592593
- **REVERSAL** `wind_gen` value=1.266e+04 d1=38.0 d12=-585.0 z=-2.0935282668024437
- **PERSISTENT_DOWN** `ps_gen` value=-676 d1=-1.0 d12=-12.0 z=0.8786930688073394
- **PERSISTENT_DOWN** `biomass_gen` value=584 d1=-1.0 d12=-4.0 z=-0.7494330555555556
- **PERSISTENT_UP** `interconnector_net` value=-4141 d1=44.0 d12=951.0 z=0.5221060437830151
- **REVERSAL** `thermal_base` value=5719 d1=5.0 d12=-2.0 z=-0.47847559016393443
- **ACCELERATION** `thermal_base` value=5719 d1=5.0 d12=-2.0 z=-0.47847559016393443
- **REVERSAL** `ccgt_gen` value=2385 d1=1.0 d12=-8.0 z=-0.4756401792592593
- **ACCELERATION** `nuclear_gen` value=3334 d1=4.0 d12=6.0 z=-0.2697959

## Nearest historical live analogues

- `2026-09-20T11:23:04.537077Z` distance=0.000 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T10:57:55.935414Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:02:06.579348Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:06:18.746524Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:10:29.817646Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
