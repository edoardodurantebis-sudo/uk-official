# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T10:35:44.157165Z`  
Memory snapshots: **832**  
Current physical regime: **TIGHT**

Regime read: margin low, wind falling.

## Active patterns

- **PERSISTENT_DOWN** `wind_forecast` value=1.903e+04 d1=0.0 d12=-223.0 z=-15.041121425
- **ACCELERATION** `wind_forecast` value=1.903e+04 d1=0.0 d12=-223.0 z=-15.041121425
- **ROBUST_OUTLIER** `wind_forecast` value=1.903e+04 d1=0.0 d12=-223.0 z=-15.041121425
- **CHANGE_POINT** `margin` value=3.444e+04 d1=0.0 d12=-33.0 z=-12.34133947972973
- **ROBUST_OUTLIER** `margin` value=3.444e+04 d1=0.0 d12=-33.0 z=-12.34133947972973
- **CHANGE_POINT** `imbalance` value=6691 d1=0.0 d12=54.0 z=-4.222892347826087
- **ROBUST_OUTLIER** `imbalance` value=6691 d1=0.0 d12=54.0 z=-4.222892347826087
- **PERSISTENT_UP** `wind_gen` value=1.592e+04 d1=0.0 d12=220.0 z=3.9850288128019327
- **ACCELERATION** `wind_gen` value=1.592e+04 d1=0.0 d12=220.0 z=3.9850288128019327
- **ROBUST_OUTLIER** `wind_gen` value=1.592e+04 d1=0.0 d12=220.0 z=3.9850288128019327
- **CHANGE_POINT** `ind_demand` value=-1.304e+04 d1=0.0 d12=-53.0 z=-0.9857092970257235
- **PERSISTENT_DOWN** `ccgt_gen` value=1811 d1=0.0 d12=-5.0 z=-1.575239177662957
- **PERSISTENT_DOWN** `thermal_base` value=5121 d1=0.0 d12=-7.0 z=-1.5716732654394299
- **ACCELERATION** `thermal_base` value=5121 d1=0.0 d12=-7.0 z=-1.5716732654394299
- **PERSISTENT_DOWN** `ps_gen` value=-960 d1=0.0 d12=-12.0 z=-0.884155185483871

## Nearest historical live analogues

- `2026-09-17T09:19:56.543683Z` distance=0.167 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:24:08.362874Z` distance=0.167 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:28:21.130076Z` distance=0.167 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:32:33.001998Z` distance=0.167 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:36:45.320295Z` distance=0.167 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
