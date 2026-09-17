# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T15:18:39.103265Z`  
Memory snapshots: **899**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=6459 d1=93.0 d12=627.0 z=10.276771100000001
- **PERSISTENT_UP** `biomass_gen` value=2668 d1=11.0 d12=359.0 z=11.86737370945946
- **ROBUST_OUTLIER** `biomass_gen` value=2668 d1=11.0 d12=359.0 z=11.86737370945946
- **CHANGE_POINT** `ccgt_gen` value=3151 d1=91.0 d12=631.0 z=9.553366120056497
- **PERSISTENT_UP** `thermal_base` value=6459 d1=93.0 d12=627.0 z=10.276771100000001
- **ROBUST_OUTLIER** `thermal_base` value=6459 d1=93.0 d12=627.0 z=10.276771100000001
- **PERSISTENT_UP** `ccgt_gen` value=3151 d1=91.0 d12=631.0 z=9.553366120056497
- **ROBUST_OUTLIER** `ccgt_gen` value=3151 d1=91.0 d12=631.0 z=9.553366120056497
- **CHANGE_POINT** `imbalance` value=1.168e+04 d1=0.0 d12=-261.0 z=-6.7448974999999995
- **PERSISTENT_UP** `ps_gen` value=-645 d1=6.0 d12=298.0 z=8.151280382978724
- **ROBUST_OUTLIER** `ps_gen` value=-645 d1=6.0 d12=298.0 z=8.151280382978724
- **ROBUST_OUTLIER** `imbalance` value=1.168e+04 d1=0.0 d12=-261.0 z=-6.7448974999999995
- **ROBUST_OUTLIER** `residual_proxy` value=-2671 d1=0.0 d12=271.0 z=3.8890791968085106
- **CHANGE_POINT** `margin` value=3.565e+04 d1=0.0 d12=-271.0 z=-0.67448975
- **CHANGE_POINT** `interconnector_net` value=1229 d1=56.0 d12=529.0 z=0.5689603949733688

## Nearest historical live analogues

- `2026-09-17T13:54:16.255911Z` distance=0.175 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T13:58:30.621005Z` distance=0.178 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:02:42.198136Z` distance=0.178 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:06:57.483529Z` distance=0.178 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:11:12.490811Z` distance=0.178 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
