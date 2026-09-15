# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T12:13:43.291335Z`  
Memory snapshots: **209**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=5650 d1=0.0 d12=-25.0 z=30.27268701470588
- **ROBUST_OUTLIER** `imbalance` value=5650 d1=0.0 d12=-25.0 z=30.27268701470588
- **CHANGE_POINT** `ind_generation` value=2.475e+04 d1=0.0 d12=-26.0 z=18.30813269683908
- **ROBUST_OUTLIER** `ind_generation` value=2.475e+04 d1=0.0 d12=-26.0 z=18.30813269683908
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=0.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=0.0 z=-6.6449730925925925
- **ROBUST_OUTLIER** `margin` value=3.518e+04 d1=0.0 d12=-334.0 z=3.3999459340527576
- **CHANGE_POINT** `wind_gen` value=1.091e+04 d1=270.0 d12=-387.0 z=-1.2378870705882352
- **ROBUST_OUTLIER** `ind_demand` value=-1.19e+04 d1=0.0 d12=0.0 z=3.0166739368131865
- **CHANGE_POINT** `ps_gen` value=-925 d1=-34.0 d12=275.0 z=-0.6071991059272301
- **REVERSAL** `wind_gen` value=1.091e+04 d1=270.0 d12=-387.0 z=-1.2378870705882352
- **ACCELERATION** `wind_gen` value=1.091e+04 d1=270.0 d12=-387.0 z=-1.2378870705882352
- **PERSISTENT_DOWN** `ccgt_gen` value=1458 d1=-25.0 d12=-22.0 z=-1.1168261332790443
- **ACCELERATION** `ccgt_gen` value=1458 d1=-25.0 d12=-22.0 z=-1.1168261332790443
- **PERSISTENT_DOWN** `thermal_base` value=4781 d1=-27.0 d12=-29.0 z=-1.101763396797632

## Nearest historical live analogues

- `2026-09-15T11:05:46.278538Z` distance=0.050 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:09:57.090238Z` distance=0.050 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:14:08.250499Z` distance=0.050 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:18:18.946730Z` distance=0.050 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T10:57:20.493386Z` distance=2.976 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
