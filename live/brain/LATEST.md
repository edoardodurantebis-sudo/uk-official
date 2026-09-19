# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T11:20:28.286312Z`  
Memory snapshots: **1471**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.675e+04 d1=0.0 d12=-9313.0 z=-151.64028446111112
- **ROBUST_OUTLIER** `ind_generation` value=1.675e+04 d1=0.0 d12=-9313.0 z=-151.64028446111112
- **CHANGE_POINT** `imbalance` value=-3378 d1=0.0 d12=-10512.0 z=-10.64483182371795
- **ROBUST_OUTLIER** `imbalance` value=-3378 d1=0.0 d12=-10512.0 z=-10.64483182371795
- **ROBUST_OUTLIER** `residual_proxy` value=1.298e+04 d1=0.0 d12=4022.0 z=5.644143923223351
- **CHANGE_POINT** `margin` value=3.555e+04 d1=0.0 d12=-959.0 z=-2.0795069180513597
- **CHANGE_POINT** `ps_gen` value=-822 d1=0.0 d12=-129.0 z=-1.59270268697479
- **ROBUST_OUTLIER** `demand_forecast` value=1.963e+04 d1=0.0 d12=3691.0 z=3.40672609795082
- **CHANGE_POINT** `biomass_gen` value=474 d1=0.0 d12=-3.0 z=-0.9814834235880399
- **CHANGE_POINT** `ind_demand` value=-1.178e+04 d1=0.0 d12=1442.0 z=0.17677919569041337
- **PERSISTENT_DOWN** `ccgt_gen` value=2775 d1=0.0 d12=-172.0 z=-2.052124043300654
- **PERSISTENT_DOWN** `ps_gen` value=-822 d1=0.0 d12=-129.0 z=-1.59270268697479
- **PERSISTENT_UP** `nuclear_gen` value=3334 d1=0.0 d12=2.0 z=-0.22482991666666666
- **ACCELERATION** `nuclear_gen` value=3334 d1=0.0 d12=2.0 z=-0.22482991666666666
- **PERSISTENT_DOWN** `wind_gen` value=1.577e+04 d1=0.0 d12=-48.0 z=-0.09578552662721893

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.571 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.571 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.571 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.571 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.571 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
