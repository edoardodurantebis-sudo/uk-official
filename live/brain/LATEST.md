# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T04:08:18.703590Z`  
Memory snapshots: **740**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.15e+04 d1=0.0 d12=11.0 z=34.8036711
- **CHANGE_POINT** `ind_generation` value=2.639e+04 d1=0.0 d12=760.0 z=25.5294370375
- **ROBUST_OUTLIER** `ind_generation` value=2.639e+04 d1=0.0 d12=760.0 z=25.5294370375
- **CHANGE_POINT** `interconnector_net` value=-1.049e+04 d1=-526.0 d12=-2184.0 z=-18.51674125522648
- **PERSISTENT_DOWN** `interconnector_net` value=-1.049e+04 d1=-526.0 d12=-2184.0 z=-18.51674125522648
- **ROBUST_OUTLIER** `interconnector_net` value=-1.049e+04 d1=-526.0 d12=-2184.0 z=-18.51674125522648
- **CHANGE_POINT** `imbalance` value=7273 d1=0.0 d12=760.0 z=16.231269467741935
- **ROBUST_OUTLIER** `imbalance` value=7273 d1=0.0 d12=760.0 z=16.231269467741935
- **CHANGE_POINT** `biomass_gen` value=3041 d1=131.0 d12=1008.0 z=-9.133715364583333
- **CHANGE_POINT** `margin` value=3.584e+04 d1=0.0 d12=-19.0 z=9.095392083333333
- **PERSISTENT_UP** `biomass_gen` value=3041 d1=131.0 d12=1008.0 z=-9.133715364583333
- **ROBUST_OUTLIER** `biomass_gen` value=3041 d1=131.0 d12=1008.0 z=-9.133715364583333
- **ROBUST_OUTLIER** `margin` value=3.584e+04 d1=0.0 d12=-19.0 z=9.095392083333333
- **CHANGE_POINT** `wind_gen` value=1.368e+04 d1=-28.0 d12=268.0 z=0.8291648611597374
- **CHANGE_POINT** `nuclear_gen` value=3314 d1=-6.0 d12=7.0 z=0.5395918

## Nearest historical live analogues

- `2026-09-17T02:52:02.690108Z` distance=0.591 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:56:14.879410Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T03:00:26.007200Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T03:04:39.344891Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T03:08:48.749095Z` distance=0.591 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 1126.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
