# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T12:52:53.633160Z`  
Memory snapshots: **1206**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=-813.0 z=-8.175909537162163
- **ROBUST_OUTLIER** `residual_proxy` value=9368 d1=0.0 d12=813.0 z=7.833716667857142
- **CHANGE_POINT** `wind_gen` value=1.496e+04 d1=-59.0 d12=1386.0 z=4.1222416773709485
- **CHANGE_POINT** `ind_generation` value=2.559e+04 d1=0.0 d12=-33.0 z=-2.4974770236175114
- **REVERSAL** `wind_gen` value=1.496e+04 d1=-59.0 d12=1386.0 z=4.1222416773709485
- **ROBUST_OUTLIER** `wind_gen` value=1.496e+04 d1=-59.0 d12=1386.0 z=4.1222416773709485
- **CHANGE_POINT** `biomass_gen` value=1037 d1=1.0 d12=-4.0 z=-1.0495423464125562
- **CHANGE_POINT** `ccgt_gen` value=2431 d1=1.0 d12=-2.0 z=-0.6838576631944444
- **CHANGE_POINT** `thermal_base` value=5774 d1=2.0 d12=3.0 z=-0.6779179062897077
- **CHANGE_POINT** `margin` value=3.81e+04 d1=0.0 d12=0.0 z=0.67448975
- **CHANGE_POINT** `ps_gen` value=-716 d1=1.0 d12=6.0 z=-0.6598514081803005
- **CHANGE_POINT** `imbalance` value=8916 d1=0.0 d12=-33.0 z=-0.0522060867176302
- **PERSISTENT_UP** `nuclear_gen` value=3343 d1=1.0 d12=5.0 z=1.7986393333333333
- **ACCELERATION** `nuclear_gen` value=3343 d1=1.0 d12=5.0 z=1.7986393333333333
- **REVERSAL** `biomass_gen` value=1037 d1=1.0 d12=-4.0 z=-1.0495423464125562

## Nearest historical live analogues

- `2026-09-18T11:53:30.754266Z` distance=0.545 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:57:41.506573Z` distance=0.545 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:24:04.514292Z` distance=0.546 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:28:15.080322Z` distance=0.546 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:32:27.606520Z` distance=0.546 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
