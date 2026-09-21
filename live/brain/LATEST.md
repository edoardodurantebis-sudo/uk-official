# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T04:37:57.283815Z`  
Memory snapshots: **2058**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.753e+04 d1=0.0 d12=-40.0 z=25.014772032608697
- **ROBUST_OUTLIER** `margin` value=3.753e+04 d1=0.0 d12=-40.0 z=25.014772032608697
- **CHANGE_POINT** `nuclear_gen` value=3383 d1=0.0 d12=49.0 z=10.117346249999999
- **PERSISTENT_UP** `nuclear_gen` value=3383 d1=0.0 d12=49.0 z=10.117346249999999
- **ROBUST_OUTLIER** `nuclear_gen` value=3383 d1=0.0 d12=49.0 z=10.117346249999999
- **CHANGE_POINT** `imbalance` value=-3982 d1=0.0 d12=838.0 z=7.246843360465116
- **CHANGE_POINT** `ind_generation` value=1.663e+04 d1=0.0 d12=838.0 z=7.246843360465116
- **CHANGE_POINT** `thermal_base` value=1.113e+04 d1=12.0 d12=2209.0 z=5.5151648066298335
- **CHANGE_POINT** `ccgt_gen` value=7744 d1=12.0 d12=2160.0 z=5.334489061020037
- **ROBUST_OUTLIER** `imbalance` value=-3982 d1=0.0 d12=838.0 z=7.246843360465116
- **ROBUST_OUTLIER** `ind_generation` value=1.663e+04 d1=0.0 d12=838.0 z=7.246843360465116
- **CHANGE_POINT** `ind_demand` value=-1.175e+04 d1=0.0 d12=51.0 z=4.5528058125
- **PERSISTENT_UP** `thermal_base` value=1.113e+04 d1=12.0 d12=2209.0 z=5.5151648066298335
- **ROBUST_OUTLIER** `thermal_base` value=1.113e+04 d1=12.0 d12=2209.0 z=5.5151648066298335
- **CHANGE_POINT** `interconnector_net` value=4842 d1=13.0 d12=-5158.0 z=-3.4897376435897436

## Nearest historical live analogues

- `2026-09-21T03:34:39.682087Z` distance=0.063 → {'next30m_imbalance_delta': 777.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -17.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T03:38:52.986660Z` distance=0.063 → {'next30m_imbalance_delta': 777.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -17.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T03:43:03.851853Z` distance=0.063 → {'next30m_imbalance_delta': 777.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -17.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T03:22:03.307428Z` distance=0.588 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -6418.0}
- `2026-09-21T03:26:15.582566Z` distance=0.588 → {'next30m_imbalance_delta': 777.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -17.0, 'next30m_residual_proxy_delta': -6418.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
