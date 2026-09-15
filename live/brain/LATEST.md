# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T12:05:17.663793Z`  
Memory snapshots: **207**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=5650 d1=0.0 d12=-25.0 z=32.59678329347826
- **PERSISTENT_DOWN** `imbalance` value=5650 d1=0.0 d12=-25.0 z=32.59678329347826
- **ROBUST_OUTLIER** `imbalance` value=5650 d1=0.0 d12=-25.0 z=32.59678329347826
- **CHANGE_POINT** `ind_generation` value=2.475e+04 d1=0.0 d12=-26.0 z=18.30813269683908
- **PERSISTENT_DOWN** `ind_generation` value=2.475e+04 d1=0.0 d12=-26.0 z=18.30813269683908
- **ROBUST_OUTLIER** `ind_generation` value=2.475e+04 d1=0.0 d12=-26.0 z=18.30813269683908
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=0.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=0.0 z=-6.6449730925925925
- **CHANGE_POINT** `margin` value=3.518e+04 d1=0.0 d12=-28.0 z=3.4412074138349515
- **ROBUST_OUTLIER** `margin` value=3.518e+04 d1=0.0 d12=-28.0 z=3.4412074138349515
- **CHANGE_POINT** `wind_gen` value=1.056e+04 d1=0.0 d12=-1029.0 z=-1.40475884820457
- **ROBUST_OUTLIER** `ind_demand` value=-1.19e+04 d1=0.0 d12=0.0 z=3.0166739368131865
- **PERSISTENT_DOWN** `wind_gen` value=1.056e+04 d1=0.0 d12=-1029.0 z=-1.40475884820457
- **ACCELERATION** `wind_gen` value=1.056e+04 d1=0.0 d12=-1029.0 z=-1.40475884820457
- **ACCELERATION** `nuclear_gen` value=3330 d1=0.0 d12=3.0 z=1.3489795

## Nearest historical live analogues

- `2026-09-15T11:05:46.278538Z` distance=0.048 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:09:57.090238Z` distance=0.048 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T10:57:20.493386Z` distance=3.000 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:01:34.132769Z` distance=3.000 → {'next30m_imbalance_delta': 6483.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T10:53:07.965768Z` distance=3.232 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
