# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T18:08:04.608022Z`  
Memory snapshots: **1252**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=5013 d1=-75.0 d12=2460.0 z=28.82014677542373
- **CHANGE_POINT** `thermal_base` value=8348 d1=-77.0 d12=2465.0 z=28.526948838235295
- **REVERSAL** `ccgt_gen` value=5013 d1=-75.0 d12=2460.0 z=28.82014677542373
- **ROBUST_OUTLIER** `ccgt_gen` value=5013 d1=-75.0 d12=2460.0 z=28.82014677542373
- **REVERSAL** `thermal_base` value=8348 d1=-77.0 d12=2465.0 z=28.526948838235295
- **ROBUST_OUTLIER** `thermal_base` value=8348 d1=-77.0 d12=2465.0 z=28.526948838235295
- **CHANGE_POINT** `ind_generation` value=2.616e+04 d1=0.0 d12=574.0 z=16.187753999999998
- **ROBUST_OUTLIER** `ind_generation` value=2.616e+04 d1=0.0 d12=574.0 z=16.187753999999998
- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=1.0 z=-14.16428475
- **CHANGE_POINT** `interconnector_net` value=-1103 d1=208.0 d12=-6186.0 z=-11.218106505201561
- **REVERSAL** `interconnector_net` value=-1103 d1=208.0 d12=-6186.0 z=-11.218106505201561
- **ROBUST_OUTLIER** `interconnector_net` value=-1103 d1=208.0 d12=-6186.0 z=-11.218106505201561
- **CHANGE_POINT** `ps_gen` value=579 d1=0.0 d12=752.0 z=8.283147082908163
- **ROBUST_OUTLIER** `ps_gen` value=579 d1=0.0 d12=752.0 z=8.283147082908163
- **CHANGE_POINT** `biomass_gen` value=1557 d1=-49.0 d12=69.0 z=3.72655586875

## Nearest historical live analogues

- `2026-09-18T14:21:00.093276Z` distance=0.224 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:57:04.108111Z` distance=0.232 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:01:14.855580Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:05:25.405882Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:09:36.028376Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
