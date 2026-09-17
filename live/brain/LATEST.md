# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T10:01:57.598308Z`  
Memory snapshots: **824**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.441e+04 d1=0.0 d12=-1644.0 z=-13.769226467857143
- **ROBUST_OUTLIER** `margin` value=3.441e+04 d1=0.0 d12=-1644.0 z=-13.769226467857143
- **CHANGE_POINT** `imbalance` value=6663 d1=0.0 d12=-778.0 z=-4.428171836956522
- **CHANGE_POINT** `ind_demand` value=-1.301e+04 d1=0.0 d12=-879.0 z=-2.504043196875
- **ROBUST_OUTLIER** `imbalance` value=6663 d1=0.0 d12=-778.0 z=-4.428171836956522
- **PERSISTENT_DOWN** `wind_gen` value=1.554e+04 d1=-62.0 d12=-149.0 z=4.113985194831014
- **ROBUST_OUTLIER** `wind_gen` value=1.554e+04 d1=-62.0 d12=-149.0 z=4.113985194831014
- **CHANGE_POINT** `interconnector_net` value=1836 d1=-532.0 d12=-2099.0 z=0.9470333289039767
- **REVERSAL** `ccgt_gen` value=1811 d1=1.0 d12=-290.0 z=-2.722646206535948
- **REVERSAL** `biomass_gen` value=2005 d1=-6.0 d12=331.0 z=-1.480652797808765
- **PERSISTENT_DOWN** `interconnector_net` value=1836 d1=-532.0 d12=-2099.0 z=0.9470333289039767
- **ACCELERATION** `nuclear_gen` value=3315 d1=-1.0 d12=0.0 z=0.4496598333333333

## Nearest historical live analogues

- `2026-09-16T08:52:24.970739Z` distance=1.071 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=1.071 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=1.071 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:05:03.473837Z` distance=1.071 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:09:50.095639Z` distance=1.071 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
