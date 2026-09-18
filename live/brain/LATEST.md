# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T09:17:23.453524Z`  
Memory snapshots: **1155**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1731 d1=-13.0 d12=-416.0 z=-18.21122325
- **PERSISTENT_DOWN** `biomass_gen` value=1731 d1=-13.0 d12=-416.0 z=-18.21122325
- **ROBUST_OUTLIER** `biomass_gen` value=1731 d1=-13.0 d12=-416.0 z=-18.21122325
- **CHANGE_POINT** `wind_gen` value=1.167e+04 d1=-87.0 d12=-594.0 z=-3.9515561111111115
- **CHANGE_POINT** `ps_gen` value=-244 d1=-178.0 d12=-841.0 z=-2.983401370689655
- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=1.0 z=-4.228531894230769
- **PERSISTENT_DOWN** `wind_gen` value=1.167e+04 d1=-87.0 d12=-594.0 z=-3.9515561111111115
- **ROBUST_OUTLIER** `wind_gen` value=1.167e+04 d1=-87.0 d12=-594.0 z=-3.9515561111111115
- **ROBUST_OUTLIER** `imbalance` value=9602 d1=0.0 d12=-23.0 z=-3.24766814625
- **PERSISTENT_DOWN** `ps_gen` value=-244 d1=-178.0 d12=-841.0 z=-2.983401370689655
- **CHANGE_POINT** `ccgt_gen` value=3464 d1=-9.0 d12=-554.0 z=-0.6883189899813607
- **CHANGE_POINT** `thermal_base` value=6799 d1=-8.0 d12=-556.0 z=-0.6832169741219963
- **REVERSAL** `interconnector_net` value=3850 d1=-40.0 d12=694.0 z=2.6171654767833106
- **ACCELERATION** `interconnector_net` value=3850 d1=-40.0 d12=694.0 z=2.6171654767833106
- **CHANGE_POINT** `ts_demand_forecast` value=1.909e+04 d1=1449.0 d12=1449.0 z=None

## Nearest historical live analogues

- `2026-09-18T08:22:03.400207Z` distance=0.051 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 74.0}
- `2026-09-18T08:17:51.592822Z` distance=0.062 → {'next30m_imbalance_delta': -593.0, 'next30m_margin_delta': -112.0, 'next30m_residual_proxy_delta': 74.0}
- `2026-09-18T07:23:09.699179Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:27:20.707745Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:31:32.031758Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
