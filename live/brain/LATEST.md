# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T14:04:09.224702Z`  
Memory snapshots: **1223**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `wind_gen` value=1.59e+04 d1=208.0 d12=955.0 z=4.759697171985816
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-6.528097223214285
- **PERSISTENT_UP** `wind_gen` value=1.59e+04 d1=208.0 d12=955.0 z=4.759697171985816
- **ROBUST_OUTLIER** `wind_gen` value=1.59e+04 d1=208.0 d12=955.0 z=4.759697171985816
- **CHANGE_POINT** `ps_gen` value=-718 d1=-4.0 d12=-15.0 z=-0.6699013843537415
- **CHANGE_POINT** `thermal_base` value=5817 d1=7.0 d12=9.0 z=-0.6377224515977443
- **CHANGE_POINT** `ccgt_gen` value=2480 d1=8.0 d12=12.0 z=-0.6368787973977694
- **CHANGE_POINT** `biomass_gen` value=1158 d1=56.0 d12=122.0 z=0.362538240625
- **REVERSAL** `interconnector_net` value=6507 d1=-24.0 d12=494.0 z=1.2452794472312705
- **PERSISTENT_UP** `margin` value=3.819e+04 d1=0.0 d12=88.0 z=0.8495785346607669
- **PERSISTENT_DOWN** `ind_generation` value=2.56e+04 d1=0.0 d12=-11.0 z=-0.8131698855140187
- **PERSISTENT_DOWN** `ps_gen` value=-718 d1=-4.0 d12=-15.0 z=-0.6699013843537415
- **ACCELERATION** `thermal_base` value=5817 d1=7.0 d12=9.0 z=-0.6377224515977443
- **ACCELERATION** `ccgt_gen` value=2480 d1=8.0 d12=12.0 z=-0.6368787973977694
- **PERSISTENT_DOWN** `nuclear_gen` value=3337 d1=-1.0 d12=-3.0 z=0.4496598333333333

## Nearest historical live analogues

- `2026-09-18T12:57:04.108111Z` distance=0.037 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:01:14.855580Z` distance=0.037 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:05:25.405882Z` distance=0.037 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:09:36.028376Z` distance=0.037 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:31:54.164710Z` distance=0.037 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
