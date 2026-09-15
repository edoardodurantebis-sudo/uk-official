# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T21:51:27.029322Z`  
Memory snapshots: **346**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=7981 d1=-328.0 d12=-2766.0 z=-8.543029316591422
- **CHANGE_POINT** `ccgt_gen` value=4651 d1=-329.0 d12=-2773.0 z=-8.495395001401345
- **PERSISTENT_DOWN** `thermal_base` value=7981 d1=-328.0 d12=-2766.0 z=-8.543029316591422
- **ROBUST_OUTLIER** `thermal_base` value=7981 d1=-328.0 d12=-2766.0 z=-8.543029316591422
- **PERSISTENT_DOWN** `ccgt_gen` value=4651 d1=-329.0 d12=-2773.0 z=-8.495395001401345
- **ROBUST_OUTLIER** `ccgt_gen` value=4651 d1=-329.0 d12=-2773.0 z=-8.495395001401345
- **PERSISTENT_DOWN** `wind_gen` value=1.208e+04 d1=-68.0 d12=-246.0 z=4.598028877858628
- **ROBUST_OUTLIER** `wind_gen` value=1.208e+04 d1=-68.0 d12=-246.0 z=4.598028877858628
- **PERSISTENT_UP** `nuclear_gen` value=3330 d1=1.0 d12=7.0 z=2.697959
- **ACCELERATION** `nuclear_gen` value=3330 d1=1.0 d12=7.0 z=2.697959
- **CHANGE_POINT** `ps_gen` value=-259 d1=-3.0 d12=2.0 z=-0.6815896421052631
- **CHANGE_POINT** `interconnector_net` value=1317 d1=4.0 d12=1010.0 z=0.6067876831613509
- **REVERSAL** `ps_gen` value=-259 d1=-3.0 d12=2.0 z=-0.6815896421052631
- **ACCELERATION** `ps_gen` value=-259 d1=-3.0 d12=2.0 z=-0.6815896421052631
- **PERSISTENT_UP** `interconnector_net` value=1317 d1=4.0 d12=1010.0 z=0.6067876831613509

## Nearest historical live analogues

- `2026-09-15T20:52:49.933053Z` distance=0.003 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:57:02.699458Z` distance=0.003 → {'next30m_imbalance_delta': 47.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:22:50.211969Z` distance=0.014 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:27:39.367678Z` distance=0.014 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:31:49.811988Z` distance=0.014 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
