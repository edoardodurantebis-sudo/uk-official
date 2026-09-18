# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T13:26:20.440549Z`  
Memory snapshots: **1214**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-8.175909537162163
- **PERSISTENT_UP** `wind_gen` value=1.508e+04 d1=126.0 d12=483.0 z=4.327908419867947
- **ROBUST_OUTLIER** `wind_gen` value=1.508e+04 d1=126.0 d12=483.0 z=4.327908419867947
- **ROBUST_OUTLIER** `residual_proxy` value=9368 d1=0.0 d12=0.0 z=3.6775750654761903
- **CHANGE_POINT** `biomass_gen` value=1037 d1=1.0 d12=-2.0 z=-0.7389630349264705
- **CHANGE_POINT** `thermal_base` value=5791 d1=-8.0 d12=19.0 z=-0.6563216759259259
- **CHANGE_POINT** `ccgt_gen` value=2465 d1=-7.0 d12=27.0 z=-0.6441123967889908
- **CHANGE_POINT** `ps_gen` value=-705 d1=-2.0 d12=-225.0 z=-0.6405226402877697
- **PERSISTENT_DOWN** `nuclear_gen` value=3326 d1=-1.0 d12=-8.0 z=-2.02346925
- **ACCELERATION** `nuclear_gen` value=3326 d1=-1.0 d12=-8.0 z=-2.02346925
- **REVERSAL** `ind_generation` value=2.56e+04 d1=-4.0 d12=19.0 z=-1.0500208789251209
- **PERSISTENT_UP** `interconnector_net` value=6075 d1=21.0 d12=512.0 z=0.846273858203125
- **PERSISTENT_UP** `margin` value=3.817e+04 d1=0.0 d12=70.0 z=0.8137649196165191
- **ACCELERATION** `margin` value=3.817e+04 d1=0.0 d12=70.0 z=0.8137649196165191
- **REVERSAL** `biomass_gen` value=1037 d1=1.0 d12=-2.0 z=-0.7389630349264705

## Nearest historical live analogues

- `2026-09-18T12:31:54.164710Z` distance=0.030 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T10:58:51.813919Z` distance=0.518 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:03:02.719756Z` distance=0.518 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:07:16.554570Z` distance=0.518 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:11:29.017632Z` distance=0.518 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -2.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
