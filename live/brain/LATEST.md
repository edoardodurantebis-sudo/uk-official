# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T15:43:57.484683Z`  
Memory snapshots: **905**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-275 d1=49.0 d12=471.0 z=18.770906234042553
- **PERSISTENT_UP** `ps_gen` value=-275 d1=49.0 d12=471.0 z=18.770906234042553
- **ROBUST_OUTLIER** `ps_gen` value=-275 d1=49.0 d12=471.0 z=18.770906234042553
- **PERSISTENT_UP** `biomass_gen` value=2751 d1=49.0 d12=117.0 z=10.755178948369565
- **ROBUST_OUTLIER** `biomass_gen` value=2751 d1=49.0 d12=117.0 z=10.755178948369565
- **PERSISTENT_UP** `thermal_base` value=6488 d1=84.0 d12=457.0 z=10.513864466666666
- **ROBUST_OUTLIER** `thermal_base` value=6488 d1=84.0 d12=457.0 z=10.513864466666666
- **PERSISTENT_UP** `ccgt_gen` value=3177 d1=83.0 d12=451.0 z=9.751521300847457
- **ROBUST_OUTLIER** `ccgt_gen` value=3177 d1=83.0 d12=451.0 z=9.751521300847457
- **CHANGE_POINT** `imbalance` value=1.166e+04 d1=0.0 d12=-282.0 z=-7.289677682692308
- **ROBUST_OUTLIER** `imbalance` value=1.166e+04 d1=0.0 d12=-282.0 z=-7.289677682692308
- **ROBUST_OUTLIER** `residual_proxy` value=-2671 d1=0.0 d12=0.0 z=3.8890791968085106
- **CHANGE_POINT** `interconnector_net` value=1544 d1=-25.0 d12=944.0 z=0.9577148620883233
- **CHANGE_POINT** `margin` value=3.564e+04 d1=0.0 d12=-14.0 z=-0.5138969523809523
- **CHANGE_POINT** `wind_gen` value=1.374e+04 d1=96.0 d12=776.0 z=-0.3110966640159046

## Nearest historical live analogues

- `2026-09-17T13:54:16.255911Z` distance=0.183 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T13:58:30.621005Z` distance=0.185 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:02:42.198136Z` distance=0.185 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:06:57.483529Z` distance=0.185 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T14:11:12.490811Z` distance=0.185 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 54.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
