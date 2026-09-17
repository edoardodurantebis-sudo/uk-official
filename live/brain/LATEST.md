# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T08:58:54.569696Z`  
Memory snapshots: **809**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **PERSISTENT_UP** `margin` value=3.606e+04 d1=0.0 d12=481.0 z=7.869047083333332
- **ROBUST_OUTLIER** `margin` value=3.606e+04 d1=0.0 d12=481.0 z=7.869047083333332
- **PERSISTENT_UP** `ind_demand` value=-1.213e+04 d1=0.0 d12=11.0 z=-6.646987697580645
- **ROBUST_OUTLIER** `ind_demand` value=-1.213e+04 d1=0.0 d12=11.0 z=-6.646987697580645
- **REVERSAL** `wind_gen` value=1.553e+04 d1=-84.0 d12=64.0 z=6.125198233893558
- **ACCELERATION** `wind_gen` value=1.553e+04 d1=-84.0 d12=64.0 z=6.125198233893558
- **ROBUST_OUTLIER** `wind_gen` value=1.553e+04 d1=-84.0 d12=64.0 z=6.125198233893558
- **CHANGE_POINT** `thermal_base` value=5649 d1=-30.0 d12=-850.0 z=-2.835952122848948
- **CHANGE_POINT** `ccgt_gen` value=2333 d1=-30.0 d12=-851.0 z=-2.8297852699240984
- **CHANGE_POINT** `interconnector_net` value=5431 d1=-38.0 d12=578.0 z=2.765102263681383
- **CHANGE_POINT** `ps_gen` value=-723 d1=0.0 d12=-741.0 z=-1.1311075691489363
- **PERSISTENT_DOWN** `thermal_base` value=5649 d1=-30.0 d12=-850.0 z=-2.835952122848948
- **PERSISTENT_DOWN** `ccgt_gen` value=2333 d1=-30.0 d12=-851.0 z=-2.8297852699240984
- **REVERSAL** `interconnector_net` value=5431 d1=-38.0 d12=578.0 z=2.765102263681383
- **PERSISTENT_DOWN** `biomass_gen` value=1804 d1=-50.0 d12=-225.0 z=-1.8407389591633465

## Nearest historical live analogues

- `2026-09-17T06:52:29.952634Z` distance=0.229 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:56:43.028097Z` distance=0.229 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:00:51.548981Z` distance=0.229 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:05:06.905847Z` distance=0.229 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:09:19.225959Z` distance=0.229 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
