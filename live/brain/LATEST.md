# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T02:59:25.392262Z`  
Memory snapshots: **419**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.754e+04 d1=0.0 d12=1462.0 z=36.12487749264706
- **PERSISTENT_UP** `margin` value=3.754e+04 d1=0.0 d12=1462.0 z=36.12487749264706
- **ROBUST_OUTLIER** `margin` value=3.754e+04 d1=0.0 d12=1462.0 z=36.12487749264706
- **CHANGE_POINT** `ccgt_gen` value=2690 d1=4.0 d12=-517.0 z=-4.8900506875000005
- **CHANGE_POINT** `thermal_base` value=6023 d1=9.0 d12=-509.0 z=-4.773985892857143
- **REVERSAL** `ccgt_gen` value=2690 d1=4.0 d12=-517.0 z=-4.8900506875000005
- **ROBUST_OUTLIER** `ccgt_gen` value=2690 d1=4.0 d12=-517.0 z=-4.8900506875000005
- **REVERSAL** `thermal_base` value=6023 d1=9.0 d12=-509.0 z=-4.773985892857143
- **ROBUST_OUTLIER** `thermal_base` value=6023 d1=9.0 d12=-509.0 z=-4.773985892857143
- **CHANGE_POINT** `imbalance` value=6027 d1=0.0 d12=58.0 z=2.378463855263158
- **CHANGE_POINT** `ind_generation` value=2.515e+04 d1=0.0 d12=58.0 z=2.325826724137931
- **CHANGE_POINT** `wind_gen` value=9963 d1=66.0 d12=-195.0 z=-0.8825716141835966
- **CHANGE_POINT** `interconnector_net` value=3457 d1=13.0 d12=-636.0 z=-0.7393165186285098
- **PERSISTENT_UP** `imbalance` value=6027 d1=0.0 d12=58.0 z=2.378463855263158
- **PERSISTENT_UP** `ind_generation` value=2.515e+04 d1=0.0 d12=58.0 z=2.325826724137931

## Nearest historical live analogues

- `2026-09-16T01:51:47.907050Z` distance=0.980 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:56:00.416093Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:00:10.670180Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T02:04:21.558749Z` distance=0.980 → {'next30m_imbalance_delta': 38.0, 'next30m_margin_delta': 1461.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:22:27.619756Z` distance=1.013 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
