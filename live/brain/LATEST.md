# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T12:21:49.762893Z`  
Memory snapshots: **1827**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=0.0 z=41.6497420625
- **CHANGE_POINT** `ind_generation` value=1.537e+04 d1=0.0 d12=0.0 z=2.327446255319149
- **CHANGE_POINT** `margin` value=3.578e+04 d1=0.0 d12=0.0 z=-2.134635153240741
- **CHANGE_POINT** `ps_gen` value=-676 d1=0.0 d12=-12.0 z=0.8786930688073394
- **CHANGE_POINT** `imbalance` value=-5732 d1=0.0 d12=0.0 z=0.67448975
- **CHANGE_POINT** `ccgt_gen` value=2386 d1=1.0 d12=-12.0 z=-0.43411308377659574
- **CHANGE_POINT** `thermal_base` value=5722 d1=3.0 d12=-7.0 z=-0.4336861269982238
- **REVERSAL** `wind_gen` value=1.267e+04 d1=4.0 d12=-443.0 z=-2.0477024146706584
- **PERSISTENT_DOWN** `ps_gen` value=-676 d1=0.0 d12=-12.0 z=0.8786930688073394
- **PERSISTENT_DOWN** `biomass_gen` value=584 d1=0.0 d12=-3.0 z=-0.7494330555555556
- **PERSISTENT_UP** `interconnector_net` value=-4141 d1=0.0 d12=486.0 z=0.5288044124072547
- **REVERSAL** `ccgt_gen` value=2386 d1=1.0 d12=-12.0 z=-0.43411308377659574
- **REVERSAL** `thermal_base` value=5722 d1=3.0 d12=-7.0 z=-0.4336861269982238
- **ACCELERATION** `nuclear_gen` value=3336 d1=2.0 d12=5.0 z=0.2697959

## Nearest historical live analogues

- `2026-09-20T11:23:04.537077Z` distance=0.000 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:27:16.047953Z` distance=0.000 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T10:57:55.935414Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:02:06.579348Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:06:18.746524Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
