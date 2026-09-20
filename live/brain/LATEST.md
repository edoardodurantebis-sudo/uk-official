# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T12:13:24.679696Z`  
Memory snapshots: **1825**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=0.0 z=41.6497420625
- **CHANGE_POINT** `ind_generation` value=1.537e+04 d1=0.0 d12=14.0 z=2.3898504746772593
- **CHANGE_POINT** `margin` value=3.578e+04 d1=0.0 d12=0.0 z=-2.217650283841754
- **CHANGE_POINT** `wind_gen` value=1.263e+04 d1=44.0 d12=-663.0 z=-2.19538877426676
- **CHANGE_POINT** `imbalance` value=-5732 d1=0.0 d12=14.0 z=0.6820440352
- **CHANGE_POINT** `thermal_base` value=5714 d1=-9.0 d12=-11.0 z=-0.49892535292164675
- **CHANGE_POINT** `ccgt_gen` value=2384 d1=2.0 d12=-10.0 z=-0.4876258350923483
- **REVERSAL** `wind_gen` value=1.263e+04 d1=44.0 d12=-663.0 z=-2.19538877426676
- **PERSISTENT_DOWN** `nuclear_gen` value=3330 d1=-11.0 d12=-1.0 z=-1.48387745
- **ACCELERATION** `nuclear_gen` value=3330 d1=-11.0 d12=-1.0 z=-1.48387745
- **PERSISTENT_DOWN** `ps_gen` value=-675 d1=0.0 d12=-13.0 z=0.8848810481651376
- **ACCELERATION** `ps_gen` value=-675 d1=0.0 d12=-13.0 z=0.8848810481651376
- **ACCELERATION** `biomass_gen` value=585 d1=0.0 d12=0.0 z=-0.67448975
- **PERSISTENT_DOWN** `thermal_base` value=5714 d1=-9.0 d12=-11.0 z=-0.49892535292164675
- **PERSISTENT_UP** `interconnector_net` value=-4185 d1=99.0 d12=907.0 z=0.49820265625000004

## Nearest historical live analogues

- `2026-09-20T10:57:55.935414Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:02:06.579348Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:06:18.746524Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:10:29.817646Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T11:14:40.539694Z` distance=0.005 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
