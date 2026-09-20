# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T08:08:43.628031Z`  
Memory snapshots: **1767**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=894 d1=5.0 d12=8.0 z=-7.603339
- **ROBUST_OUTLIER** `biomass_gen` value=894 d1=5.0 d12=8.0 z=-7.603339
- **ROBUST_OUTLIER** `margin` value=3.803e+04 d1=0.0 d12=348.0 z=6.24209605
- **ROBUST_OUTLIER** `residual_proxy` value=1.796e+04 d1=0.0 d12=1162.0 z=5.542546206521739
- **CHANGE_POINT** `wind_gen` value=1.491e+04 d1=-365.0 d12=-819.0 z=-2.0234692499999998
- **PERSISTENT_UP** `interconnector_net` value=-5092 d1=1197.0 d12=2867.0 z=3.844914297368421
- **ROBUST_OUTLIER** `interconnector_net` value=-5092 d1=1197.0 d12=2867.0 z=3.844914297368421
- **CHANGE_POINT** `ps_gen` value=-924 d1=0.0 d12=-117.0 z=-1.5750053204787235
- **CHANGE_POINT** `imbalance` value=-6364 d1=0.0 d12=438.0 z=0.38711911707746477
- **CHANGE_POINT** `ind_generation` value=1.359e+04 d1=0.0 d12=438.0 z=0.38711911707746477
- **PERSISTENT_UP** `nuclear_gen` value=3339 d1=3.0 d12=6.0 z=2.0234692499999998
- **ACCELERATION** `nuclear_gen` value=3339 d1=3.0 d12=6.0 z=2.0234692499999998
- **PERSISTENT_DOWN** `wind_gen` value=1.491e+04 d1=-365.0 d12=-819.0 z=-2.0234692499999998
- **PERSISTENT_DOWN** `ccgt_gen` value=3272 d1=-330.0 d12=-454.0 z=-1.9772713219178084
- **PERSISTENT_DOWN** `thermal_base` value=6611 d1=-327.0 d12=-448.0 z=-1.935252606948229

## Nearest historical live analogues

- `2026-09-20T06:53:07.699769Z` distance=0.181 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:57:19.576758Z` distance=0.181 → {'next30m_imbalance_delta': 438.0, 'next30m_margin_delta': 348.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T07:01:30.503093Z` distance=0.181 → {'next30m_imbalance_delta': 438.0, 'next30m_margin_delta': 348.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T07:05:43.852829Z` distance=0.181 → {'next30m_imbalance_delta': 438.0, 'next30m_margin_delta': 348.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T07:09:55.694993Z` distance=0.181 → {'next30m_imbalance_delta': 438.0, 'next30m_margin_delta': 348.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
