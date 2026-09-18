# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T18:16:31.101722Z`  
Memory snapshots: **1254**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=4919 d1=-53.0 d12=2349.0 z=27.745535987288136
- **CHANGE_POINT** `thermal_base` value=8253 d1=-55.0 d12=2353.0 z=27.45003243067227
- **REVERSAL** `ccgt_gen` value=4919 d1=-53.0 d12=2349.0 z=27.745535987288136
- **ROBUST_OUTLIER** `ccgt_gen` value=4919 d1=-53.0 d12=2349.0 z=27.745535987288136
- **REVERSAL** `thermal_base` value=8253 d1=-55.0 d12=2353.0 z=27.45003243067227
- **ROBUST_OUTLIER** `thermal_base` value=8253 d1=-55.0 d12=2353.0 z=27.45003243067227
- **CHANGE_POINT** `ind_generation` value=2.616e+04 d1=0.0 d12=590.0 z=16.187753999999998
- **ROBUST_OUTLIER** `ind_generation` value=2.616e+04 d1=0.0 d12=590.0 z=16.187753999999998
- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=1.0 z=-14.16428475
- **CHANGE_POINT** `interconnector_net` value=-872 d1=65.0 d12=-5956.0 z=-10.812886395318596
- **REVERSAL** `interconnector_net` value=-872 d1=65.0 d12=-5956.0 z=-10.812886395318596
- **ROBUST_OUTLIER** `interconnector_net` value=-872 d1=65.0 d12=-5956.0 z=-10.812886395318596
- **CHANGE_POINT** `ps_gen` value=513 d1=-35.0 d12=562.0 z=7.828898883928571
- **REVERSAL** `ps_gen` value=513 d1=-35.0 d12=562.0 z=7.828898883928571
- **ROBUST_OUTLIER** `ps_gen` value=513 d1=-35.0 d12=562.0 z=7.828898883928571

## Nearest historical live analogues

- `2026-09-18T14:21:00.093276Z` distance=0.224 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:57:04.108111Z` distance=0.232 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:01:14.855580Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:05:25.405882Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:09:36.028376Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
