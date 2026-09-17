# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T15:14:24.580940Z`  
Memory snapshots: **898**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2657 d1=-7.0 d12=400.0 z=15.416908571428573
- **REVERSAL** `biomass_gen` value=2657 d1=-7.0 d12=400.0 z=15.416908571428573
- **ROBUST_OUTLIER** `biomass_gen` value=2657 d1=-7.0 d12=400.0 z=15.416908571428573
- **CHANGE_POINT** `thermal_base` value=6366 d1=2.0 d12=402.0 z=9.5164372
- **CHANGE_POINT** `ccgt_gen` value=3060 d1=0.0 d12=403.0 z=8.859822987288135
- **PERSISTENT_UP** `thermal_base` value=6366 d1=2.0 d12=402.0 z=9.5164372
- **ROBUST_OUTLIER** `thermal_base` value=6366 d1=2.0 d12=402.0 z=9.5164372
- **PERSISTENT_UP** `ccgt_gen` value=3060 d1=0.0 d12=403.0 z=8.859822987288135
- **ROBUST_OUTLIER** `ccgt_gen` value=3060 d1=0.0 d12=403.0 z=8.859822987288135
- **CHANGE_POINT** `imbalance` value=1.168e+04 d1=0.0 d12=-260.0 z=-6.7448974999999995
- **ROBUST_OUTLIER** `ps_gen` value=-651 d1=0.0 d12=284.0 z=7.9790702340425534
- **ROBUST_OUTLIER** `imbalance` value=1.168e+04 d1=0.0 d12=-260.0 z=-6.7448974999999995
- **ROBUST_OUTLIER** `residual_proxy` value=-2671 d1=0.0 d12=271.0 z=3.8890791968085106
- **CHANGE_POINT** `margin` value=3.565e+04 d1=0.0 d12=-271.0 z=-0.6829208718750001
- **CHANGE_POINT** `interconnector_net` value=1173 d1=108.0 d12=524.0 z=0.5131987228260869

## Nearest historical live analogues

- `2026-09-17T13:54:16.255911Z` distance=0.175 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T13:58:30.621005Z` distance=0.178 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:02:42.198136Z` distance=0.178 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:06:57.483529Z` distance=0.178 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:11:12.490811Z` distance=0.178 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
