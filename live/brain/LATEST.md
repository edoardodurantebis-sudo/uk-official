# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T12:44:28.244075Z`  
Memory snapshots: **1204**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=9368 d1=0.0 d12=813.0 z=39.16858333928571
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=-813.0 z=-8.175909537162163
- **CHANGE_POINT** `wind_gen` value=1.479e+04 d1=190.0 d12=1730.0 z=3.8534174312725087
- **CHANGE_POINT** `ind_generation` value=2.559e+04 d1=0.0 d12=-81.0 z=-2.8035089227099235
- **PERSISTENT_UP** `wind_gen` value=1.479e+04 d1=190.0 d12=1730.0 z=3.8534174312725087
- **ROBUST_OUTLIER** `wind_gen` value=1.479e+04 d1=190.0 d12=1730.0 z=3.8534174312725087
- **CHANGE_POINT** `biomass_gen` value=1038 d1=-1.0 d12=-2.0 z=-1.0519008685393259
- **CHANGE_POINT** `margin` value=3.81e+04 d1=0.0 d12=0.0 z=0.7898170129533679
- **CHANGE_POINT** `ccgt_gen` value=2433 d1=-5.0 d12=1.0 z=-0.7517272383786847
- **CHANGE_POINT** `thermal_base` value=5772 d1=0.0 d12=3.0 z=-0.7507530796874999
- **CHANGE_POINT** `ps_gen` value=-715 d1=-235.0 d12=7.0 z=-0.6606894482097186
- **CHANGE_POINT** `imbalance` value=8916 d1=0.0 d12=-81.0 z=-0.28161874700598805
- **PERSISTENT_DOWN** `biomass_gen` value=1038 d1=-1.0 d12=-2.0 z=-1.0519008685393259
- **ACCELERATION** `biomass_gen` value=1038 d1=-1.0 d12=-2.0 z=-1.0519008685393259
- **PERSISTENT_UP** `interconnector_net` value=5612 d1=49.0 d12=536.0 z=0.919686299527373

## Nearest historical live analogues

- `2026-09-18T11:24:04.514292Z` distance=0.546 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:28:15.080322Z` distance=0.546 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:32:27.606520Z` distance=0.546 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:36:39.120027Z` distance=0.546 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:40:49.072894Z` distance=0.546 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
