# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T11:23:04.537077Z`  
Memory snapshots: **1813**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=41.6497420625
- **ROBUST_OUTLIER** `ind_demand` value=-1.181e+04 d1=0.0 d12=653.0 z=41.6497420625
- **CHANGE_POINT** `ind_generation` value=1.536e+04 d1=0.0 d12=-668.0 z=13.74194070093458
- **ROBUST_OUTLIER** `ind_generation` value=1.536e+04 d1=0.0 d12=-668.0 z=13.74194070093458
- **CHANGE_POINT** `margin` value=3.578e+04 d1=-13.0 d12=-3998.0 z=-7.289516552795031
- **PERSISTENT_DOWN** `margin` value=3.578e+04 d1=-13.0 d12=-3998.0 z=-7.289516552795031
- **ROBUST_OUTLIER** `margin` value=3.578e+04 d1=-13.0 d12=-3998.0 z=-7.289516552795031
- **CHANGE_POINT** `imbalance` value=-5746 d1=0.0 d12=-1606.0 z=2.1600481713395636
- **PERSISTENT_DOWN** `wind_gen` value=1.329e+04 d1=-89.0 d12=-697.0 z=-3.544394888633377
- **ROBUST_OUTLIER** `wind_gen` value=1.329e+04 d1=-89.0 d12=-697.0 z=-3.544394888633377
- **CHANGE_POINT** `ps_gen` value=-662 d1=3.0 d12=248.0 z=0.9653247798165138
- **REVERSAL** `thermal_base` value=5725 d1=2.0 d12=-121.0 z=-1.199025433168317
- **REVERSAL** `ccgt_gen` value=2394 d1=2.0 d12=-114.0 z=-1.1838229392314568
- **PERSISTENT_UP** `ps_gen` value=-662 d1=3.0 d12=248.0 z=0.9653247798165138
- **PERSISTENT_DOWN** `biomass_gen` value=585 d1=-9.0 d12=-15.0 z=-0.6952788176369863

## Nearest historical live analogues

- `2026-09-20T04:50:36.902238Z` distance=0.758 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:54:47.005275Z` distance=0.758 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:58:57.948602Z` distance=0.758 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:03:10.294370Z` distance=0.758 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:07:21.689505Z` distance=0.758 → {'next30m_imbalance_delta': -34.0, 'next30m_margin_delta': 4.0, 'next30m_residual_proxy_delta': 161.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
