# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T14:59:25.790894Z`  
Memory snapshots: **1236**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=-22.0 z=-14.8387745
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-6.528097223214285
- **CHANGE_POINT** `imbalance` value=8537 d1=0.0 d12=-391.0 z=-4.32978904032258
- **CHANGE_POINT** `biomass_gen` value=1481 d1=-3.0 d12=271.0 z=3.08579060625
- **PERSISTENT_DOWN** `imbalance` value=8537 d1=0.0 d12=-391.0 z=-4.32978904032258
- **ROBUST_OUTLIER** `imbalance` value=8537 d1=0.0 d12=-391.0 z=-4.32978904032258
- **CHANGE_POINT** `margin` value=3.83e+04 d1=0.0 d12=104.0 z=1.4716139999999998
- **ROBUST_OUTLIER** `residual_proxy` value=9748 d1=0.0 d12=380.0 z=3.3488416087500004
- **CHANGE_POINT** `ps_gen` value=-446 d1=19.0 d12=66.0 z=1.2285349017857143
- **REVERSAL** `biomass_gen` value=1481 d1=-3.0 d12=271.0 z=3.08579060625
- **ROBUST_OUTLIER** `biomass_gen` value=1481 d1=-3.0 d12=271.0 z=3.08579060625
- **REVERSAL** `wind_gen` value=1.673e+04 d1=-149.0 d12=702.0 z=2.8618141015706806
- **CHANGE_POINT** `ccgt_gen` value=2526 d1=22.0 d12=42.0 z=0.3822108583333333
- **CHANGE_POINT** `interconnector_net` value=5084 d1=64.0 d12=-791.0 z=-0.32740692648774794
- **PERSISTENT_UP** `ps_gen` value=-446 d1=19.0 d12=66.0 z=1.2285349017857143

## Nearest historical live analogues

- `2026-09-18T13:55:43.928319Z` distance=0.144 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 380.0}
- `2026-09-18T13:59:56.236821Z` distance=0.144 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 380.0}
- `2026-09-18T14:04:09.224702Z` distance=0.144 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 380.0}
- `2026-09-18T13:22:08.039057Z` distance=0.147 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:26:20.440549Z` distance=0.147 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
