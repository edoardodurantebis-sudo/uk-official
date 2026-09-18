# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T18:12:17.834626Z`  
Memory snapshots: **1253**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=4972 d1=-41.0 d12=2419.0 z=28.351433559322036
- **CHANGE_POINT** `thermal_base` value=8308 d1=-40.0 d12=2425.0 z=28.073510350840337
- **REVERSAL** `ccgt_gen` value=4972 d1=-41.0 d12=2419.0 z=28.351433559322036
- **ROBUST_OUTLIER** `ccgt_gen` value=4972 d1=-41.0 d12=2419.0 z=28.351433559322036
- **REVERSAL** `thermal_base` value=8308 d1=-40.0 d12=2425.0 z=28.073510350840337
- **ROBUST_OUTLIER** `thermal_base` value=8308 d1=-40.0 d12=2425.0 z=28.073510350840337
- **CHANGE_POINT** `ind_generation` value=2.616e+04 d1=0.0 d12=574.0 z=16.187753999999998
- **ROBUST_OUTLIER** `ind_generation` value=2.616e+04 d1=0.0 d12=574.0 z=16.187753999999998
- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=1.0 z=-14.16428475
- **CHANGE_POINT** `interconnector_net` value=-937 d1=166.0 d12=-6020.0 z=-10.926909369960988
- **REVERSAL** `interconnector_net` value=-937 d1=166.0 d12=-6020.0 z=-10.926909369960988
- **ROBUST_OUTLIER** `interconnector_net` value=-937 d1=166.0 d12=-6020.0 z=-10.926909369960988
- **CHANGE_POINT** `ps_gen` value=548 d1=-31.0 d12=721.0 z=8.069788080357142
- **REVERSAL** `ps_gen` value=548 d1=-31.0 d12=721.0 z=8.069788080357142
- **ROBUST_OUTLIER** `ps_gen` value=548 d1=-31.0 d12=721.0 z=8.069788080357142

## Nearest historical live analogues

- `2026-09-18T14:21:00.093276Z` distance=0.224 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:57:04.108111Z` distance=0.232 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:01:14.855580Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:05:25.405882Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:09:36.028376Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
