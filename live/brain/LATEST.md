# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T00:14:05.325096Z`  
Memory snapshots: **38**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=4546.0 z=9.154939979850747
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=4546.0 z=9.154939979850747
- **CHANGE_POINT** `biomass_gen` value=2808 d1=34.0 d12=127.0 z=6.510292369565218
- **PERSISTENT_UP** `biomass_gen` value=2808 d1=34.0 d12=127.0 z=6.510292369565218
- **ROBUST_OUTLIER** `biomass_gen` value=2808 d1=34.0 d12=127.0 z=6.510292369565218
- **CHANGE_POINT** `margin` value=3.272e+04 d1=0.0 d12=239.0 z=3.34546916
- **CHANGE_POINT** `imbalance` value=210 d1=0.0 d12=273.0 z=2.9309645499999997
- **CHANGE_POINT** `ind_generation` value=2.07e+04 d1=0.0 d12=274.0 z=2.8786258973214283
- **CHANGE_POINT** `interconnector_net` value=-303 d1=73.0 d12=2297.0 z=2.629108646115628
- **CHANGE_POINT** `ind_demand` value=-1.227e+04 d1=0.0 d12=-1.0 z=-1.6187753999999999
- **ROBUST_OUTLIER** `margin` value=3.272e+04 d1=0.0 d12=239.0 z=3.34546916
- **CHANGE_POINT** `wind_gen` value=1.202e+04 d1=-11.0 d12=-381.0 z=-0.8977529076655052
- **PERSISTENT_UP** `interconnector_net` value=-303 d1=73.0 d12=2297.0 z=2.629108646115628
- **PERSISTENT_DOWN** `ccgt_gen` value=3905 d1=-160.0 d12=-1154.0 z=-1.0721685274068868
- **PERSISTENT_DOWN** `thermal_base` value=7219 d1=-166.0 d12=-1157.0 z=-1.0691631496145761

## Nearest historical live analogues

- `2026-09-14T22:54:28.088906Z` distance=8.330 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': -8.0}
- `2026-09-14T23:11:14.299399Z` distance=8.339 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 4544.0}
- `2026-09-14T23:15:27.902002Z` distance=8.339 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 4544.0}
- `2026-09-14T23:02:51.731221Z` distance=8.344 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 158.0}
- `2026-09-14T23:07:03.439519Z` distance=8.375 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 4566.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
