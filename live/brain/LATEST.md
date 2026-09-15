# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T12:09:30.579354Z`  
Memory snapshots: **208**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=5650 d1=0.0 d12=-25.0 z=30.27268701470588
- **ROBUST_OUTLIER** `imbalance` value=5650 d1=0.0 d12=-25.0 z=30.27268701470588
- **CHANGE_POINT** `ind_generation` value=2.475e+04 d1=0.0 d12=-26.0 z=18.30813269683908
- **ROBUST_OUTLIER** `ind_generation` value=2.475e+04 d1=0.0 d12=-26.0 z=18.30813269683908
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=0.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=0.0 z=-6.6449730925925925
- **ROBUST_OUTLIER** `margin` value=3.518e+04 d1=0.0 d12=-28.0 z=3.4412074138349515
- **CHANGE_POINT** `wind_gen` value=1.064e+04 d1=76.0 d12=-808.0 z=-1.3774682223173518
- **ROBUST_OUTLIER** `ind_demand` value=-1.19e+04 d1=0.0 d12=0.0 z=3.0166739368131865
- **CHANGE_POINT** `ps_gen` value=-891 d1=227.0 d12=312.0 z=-0.5536502514637002
- **REVERSAL** `wind_gen` value=1.064e+04 d1=76.0 d12=-808.0 z=-1.3774682223173518
- **PERSISTENT_UP** `ccgt_gen` value=1483 d1=9.0 d12=5.0 z=-1.1293781860465115
- **ACCELERATION** `ccgt_gen` value=1483 d1=9.0 d12=5.0 z=-1.1293781860465115
- **PERSISTENT_UP** `thermal_base` value=4808 d1=4.0 d12=4.0 z=-1.12439911709212
- **ACCELERATION** `thermal_base` value=4808 d1=4.0 d12=4.0 z=-1.12439911709212

## Nearest historical live analogues

- `2026-09-15T11:05:46.278538Z` distance=0.050 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:09:57.090238Z` distance=0.050 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:14:08.250499Z` distance=0.050 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T10:57:20.493386Z` distance=2.976 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:01:34.132769Z` distance=2.976 → {'next30m_imbalance_delta': 6483.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
