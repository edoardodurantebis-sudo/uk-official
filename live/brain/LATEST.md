# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T18:20:52.591456Z`  
Memory snapshots: **1255**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=4837 d1=-82.0 d12=2185.0 z=26.808109555084744
- **CHANGE_POINT** `thermal_base` value=8169 d1=-84.0 d12=2184.0 z=26.497811607142857
- **REVERSAL** `ccgt_gen` value=4837 d1=-82.0 d12=2185.0 z=26.808109555084744
- **ROBUST_OUTLIER** `ccgt_gen` value=4837 d1=-82.0 d12=2185.0 z=26.808109555084744
- **REVERSAL** `thermal_base` value=8169 d1=-84.0 d12=2184.0 z=26.497811607142857
- **ROBUST_OUTLIER** `thermal_base` value=8169 d1=-84.0 d12=2184.0 z=26.497811607142857
- **CHANGE_POINT** `ind_generation` value=2.616e+04 d1=0.0 d12=590.0 z=16.187753999999998
- **ROBUST_OUTLIER** `ind_generation` value=2.616e+04 d1=0.0 d12=590.0 z=16.187753999999998
- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=1.0 z=-14.16428475
- **CHANGE_POINT** `interconnector_net` value=-872 d1=0.0 d12=-5955.0 z=-10.812886395318596
- **ROBUST_OUTLIER** `interconnector_net` value=-872 d1=0.0 d12=-5955.0 z=-10.812886395318596
- **ROBUST_OUTLIER** `ps_gen` value=513 d1=0.0 d12=289.0 z=7.828898883928571
- **CHANGE_POINT** `biomass_gen` value=1529 d1=-1.0 d12=40.0 z=3.4904844562500004
- **ROBUST_OUTLIER** `margin` value=3.765e+04 d1=0.0 d12=-377.0 z=-3.853022696875
- **CHANGE_POINT** `imbalance` value=9111 d1=0.0 d12=590.0 z=1.69971417

## Nearest historical live analogues

- `2026-09-18T15:24:41.804681Z` distance=0.154 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:21:00.093276Z` distance=0.224 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:57:04.108111Z` distance=0.232 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:01:14.855580Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:05:25.405882Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
