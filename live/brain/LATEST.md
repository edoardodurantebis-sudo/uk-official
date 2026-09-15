# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T12:00:57.047099Z`  
Memory snapshots: **206**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=5650 d1=0.0 d12=-25.0 z=35.298296916666665
- **PERSISTENT_DOWN** `imbalance` value=5650 d1=0.0 d12=-25.0 z=35.298296916666665
- **ROBUST_OUTLIER** `imbalance` value=5650 d1=0.0 d12=-25.0 z=35.298296916666665
- **CHANGE_POINT** `ind_generation` value=2.475e+04 d1=0.0 d12=-26.0 z=18.30813269683908
- **PERSISTENT_DOWN** `ind_generation` value=2.475e+04 d1=0.0 d12=-26.0 z=18.30813269683908
- **ROBUST_OUTLIER** `ind_generation` value=2.475e+04 d1=0.0 d12=-26.0 z=18.30813269683908
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=0.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=0.0 z=-6.6449730925925925
- **CHANGE_POINT** `margin` value=3.518e+04 d1=0.0 d12=-28.0 z=3.4412074138349515
- **PERSISTENT_DOWN** `margin` value=3.518e+04 d1=0.0 d12=-28.0 z=3.4412074138349515
- **ROBUST_OUTLIER** `margin` value=3.518e+04 d1=0.0 d12=-28.0 z=3.4412074138349515
- **CHANGE_POINT** `wind_gen` value=1.056e+04 d1=-421.0 d12=-1033.0 z=-1.416575422657952
- **CHANGE_POINT** `ps_gen` value=-1118 d1=95.0 d12=91.0 z=-1.0499132900943395
- **ROBUST_OUTLIER** `ind_demand` value=-1.19e+04 d1=0.0 d12=0.0 z=3.0166739368131865
- **PERSISTENT_DOWN** `wind_gen` value=1.056e+04 d1=-421.0 d12=-1033.0 z=-1.416575422657952

## Nearest historical live analogues

- `2026-09-15T11:05:46.278538Z` distance=0.047 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T10:57:20.493386Z` distance=3.025 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:01:34.132769Z` distance=3.025 → {'next30m_imbalance_delta': 6483.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T10:53:07.965768Z` distance=3.240 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T10:32:07.729613Z` distance=3.263 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
