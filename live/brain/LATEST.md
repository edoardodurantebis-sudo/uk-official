# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T11:10:29.817646Z`  
Memory snapshots: **1810**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=39.35846070588235
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=39.35846070588235
- **CHANGE_POINT** `ind_generation` value=1.536e+04 d1=0.0 d12=-668.0 z=18.3798456875
- **CHANGE_POINT** `margin` value=3.579e+04 d1=0.0 d12=-3985.0 z=-17.385728332089553
- **ROBUST_OUTLIER** `ind_generation` value=1.536e+04 d1=0.0 d12=-668.0 z=18.3798456875
- **ROBUST_OUTLIER** `margin` value=3.579e+04 d1=0.0 d12=-3985.0 z=-17.385728332089553
- **ROBUST_OUTLIER** `demand_forecast` value=2.06e+04 d1=0.0 d12=938.0 z=6.587306436915887
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.11e+04 d1=0.0 d12=938.0 z=6.587306436915887
- **CHANGE_POINT** `imbalance` value=-5746 d1=0.0 d12=-1606.0 z=2.530567383211679
- **ROBUST_OUTLIER** `residual_proxy` value=1.824e+04 d1=0.0 d12=1031.0 z=3.3699319972014927
- **PERSISTENT_DOWN** `wind_gen` value=1.352e+04 d1=-185.0 d12=-438.0 z=-3.2243255107843134
- **ROBUST_OUTLIER** `wind_gen` value=1.352e+04 d1=-185.0 d12=-438.0 z=-3.2243255107843134
- **CHANGE_POINT** `ps_gen` value=-674 d1=44.0 d12=-89.0 z=0.8910690275229358
- **CHANGE_POINT** `biomass_gen` value=589 d1=4.0 d12=-5.0 z=-0.686039232020548
- **PERSISTENT_DOWN** `nuclear_gen` value=3331 d1=-7.0 d12=-6.0 z=-1.686224375

## Nearest historical live analogues

- `2026-09-20T04:50:36.902238Z` distance=0.754 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:54:47.005275Z` distance=0.754 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:58:57.948602Z` distance=0.754 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:03:10.294370Z` distance=0.754 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:07:21.689505Z` distance=0.754 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 161.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
