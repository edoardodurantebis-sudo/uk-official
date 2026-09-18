# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T18:03:52.862865Z`  
Memory snapshots: **1251**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=5088 d1=-3.0 d12=2546.0 z=29.677549
- **CHANGE_POINT** `thermal_base` value=8425 d1=-5.0 d12=2551.0 z=29.39981792647059
- **REVERSAL** `ccgt_gen` value=5088 d1=-3.0 d12=2546.0 z=29.677549
- **ROBUST_OUTLIER** `ccgt_gen` value=5088 d1=-3.0 d12=2546.0 z=29.677549
- **REVERSAL** `thermal_base` value=8425 d1=-5.0 d12=2551.0 z=29.39981792647059
- **ROBUST_OUTLIER** `thermal_base` value=8425 d1=-5.0 d12=2551.0 z=29.39981792647059
- **CHANGE_POINT** `ind_generation` value=2.616e+04 d1=0.0 d12=574.0 z=16.187753999999998
- **PERSISTENT_UP** `ind_generation` value=2.616e+04 d1=0.0 d12=574.0 z=16.187753999999998
- **ROBUST_OUTLIER** `ind_generation` value=2.616e+04 d1=0.0 d12=574.0 z=16.187753999999998
- **PERSISTENT_UP** `ind_demand` value=-1.077e+04 d1=0.0 d12=1.0 z=-14.16428475
- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=1.0 z=-14.16428475
- **CHANGE_POINT** `interconnector_net` value=-1311 d1=170.0 d12=-6328.0 z=-11.582980024057216
- **REVERSAL** `interconnector_net` value=-1311 d1=170.0 d12=-6328.0 z=-11.582980024057216
- **ROBUST_OUTLIER** `interconnector_net` value=-1311 d1=170.0 d12=-6328.0 z=-11.582980024057216
- **CHANGE_POINT** `ps_gen` value=579 d1=-14.0 d12=754.0 z=8.283147082908163

## Nearest historical live analogues

- `2026-09-18T14:21:00.093276Z` distance=0.224 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:57:04.108111Z` distance=0.232 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:01:14.855580Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:05:25.405882Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:09:36.028376Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
