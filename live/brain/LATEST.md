# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T21:26:18.783967Z`  
Memory snapshots: **340**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=9227 d1=-288.0 d12=-3505.0 z=-6.645931735327314
- **CHANGE_POINT** `ccgt_gen` value=5904 d1=-288.0 d12=-3506.0 z=-6.600472004204036
- **PERSISTENT_DOWN** `thermal_base` value=9227 d1=-288.0 d12=-3505.0 z=-6.645931735327314
- **ROBUST_OUTLIER** `thermal_base` value=9227 d1=-288.0 d12=-3505.0 z=-6.645931735327314
- **PERSISTENT_DOWN** `ccgt_gen` value=5904 d1=-288.0 d12=-3506.0 z=-6.600472004204036
- **ROBUST_OUTLIER** `ccgt_gen` value=5904 d1=-288.0 d12=-3506.0 z=-6.600472004204036
- **REVERSAL** `wind_gen` value=1.244e+04 d1=-67.0 d12=514.0 z=6.245620029885058
- **ROBUST_OUTLIER** `wind_gen` value=1.244e+04 d1=-67.0 d12=514.0 z=6.245620029885058
- **CHANGE_POINT** `ps_gen` value=-257 d1=3.0 d12=5.0 z=-0.6780396960526316
- **CHANGE_POINT** `imbalance` value=5769 d1=0.0 d12=-19.0 z=-0.10649838157894735
- **CHANGE_POINT** `ind_generation` value=2.489e+04 d1=0.0 d12=-19.0 z=-0.10649838157894735
- **PERSISTENT_UP** `margin` value=3.572e+04 d1=0.0 d12=23.0 z=0.7016869173387097
- **PERSISTENT_UP** `ps_gen` value=-257 d1=3.0 d12=5.0 z=-0.6780396960526316
- **PERSISTENT_DOWN** `biomass_gen` value=3259 d1=-1.0 d12=-18.0 z=0.39505828214285715
- **PERSISTENT_UP** `interconnector_net` value=739 d1=11.0 d12=662.0 z=0.1380873695593767

## Nearest historical live analogues

- `2026-09-15T20:22:50.211969Z` distance=0.018 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:27:39.367678Z` distance=0.018 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:31:49.811988Z` distance=0.018 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:31:50.302711Z` distance=0.061 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:36:02.892054Z` distance=0.061 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
