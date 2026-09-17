# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T10:06:11.088128Z`  
Memory snapshots: **825**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.441e+04 d1=0.0 d12=-1644.0 z=-13.769226467857143
- **ROBUST_OUTLIER** `margin` value=3.441e+04 d1=0.0 d12=-1644.0 z=-13.769226467857143
- **CHANGE_POINT** `imbalance` value=6663 d1=0.0 d12=-778.0 z=-4.428171836956522
- **CHANGE_POINT** `ind_demand` value=-1.301e+04 d1=0.0 d12=-879.0 z=-2.504043196875
- **ROBUST_OUTLIER** `imbalance` value=6663 d1=0.0 d12=-778.0 z=-4.428171836956522
- **PERSISTENT_DOWN** `wind_gen` value=1.553e+04 d1=-12.0 d12=-161.0 z=4.072365692956349
- **ROBUST_OUTLIER** `wind_gen` value=1.553e+04 d1=-12.0 d12=-161.0 z=4.072365692956349
- **CHANGE_POINT** `interconnector_net` value=1150 d1=-686.0 d12=-2785.0 z=0.8454026395877177
- **REVERSAL** `thermal_base` value=5170 d1=44.0 d12=-246.0 z=-2.5627186694162436
- **REVERSAL** `ccgt_gen` value=1860 d1=49.0 d12=-241.0 z=-2.5365571706549117
- **REVERSAL** `ps_gen` value=-931 d1=21.0 d12=-374.0 z=-0.8492348864082434
- **PERSISTENT_DOWN** `interconnector_net` value=1150 d1=-686.0 d12=-2785.0 z=0.8454026395877177
- **PERSISTENT_DOWN** `nuclear_gen` value=3310 d1=-5.0 d12=-5.0 z=-0.8093876999999999
- **ACCELERATION** `nuclear_gen` value=3310 d1=-5.0 d12=-5.0 z=-0.8093876999999999

## Nearest historical live analogues

- `2026-09-16T08:52:24.970739Z` distance=1.072 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=1.072 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=1.072 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:05:03.473837Z` distance=1.072 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:09:50.095639Z` distance=1.072 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
