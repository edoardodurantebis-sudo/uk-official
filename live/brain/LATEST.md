# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T12:47:20.573574Z`  
Memory snapshots: **217**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=5650 d1=0.0 d12=0.0 z=14.496779697183097
- **ROBUST_OUTLIER** `imbalance` value=5650 d1=0.0 d12=0.0 z=14.496779697183097
- **CHANGE_POINT** `ind_generation` value=2.475e+04 d1=0.0 d12=1.0 z=9.982015240770465
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=0.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `ind_generation` value=2.475e+04 d1=0.0 d12=1.0 z=9.982015240770465
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=0.0 z=-6.6449730925925925
- **ROBUST_OUTLIER** `residual_proxy` value=756 d1=0.0 d12=-249.0 z=-3.155063532560707
- **CHANGE_POINT** `ccgt_gen` value=1459 d1=-12.0 d12=-4.0 z=-0.7877252554744525
- **CHANGE_POINT** `thermal_base` value=4787 d1=-14.0 d12=-8.0 z=-0.7813885767061477
- **CHANGE_POINT** `interconnector_net` value=1.128e+04 d1=-2.0 d12=6.0 z=0.5479475991661703
- **CHANGE_POINT** `ps_gen` value=-1086 d1=-11.0 d12=127.0 z=-0.33908105399274047
- **CHANGE_POINT** `biomass_gen` value=1724 d1=2.0 d12=195.0 z=-0.300562099122807
- **PERSISTENT_DOWN** `wind_gen` value=1.057e+04 d1=-42.0 d12=-410.0 z=-1.530427503202562
- **PERSISTENT_DOWN** `ccgt_gen` value=1459 d1=-12.0 d12=-4.0 z=-0.7877252554744525
- **ACCELERATION** `ccgt_gen` value=1459 d1=-12.0 d12=-4.0 z=-0.7877252554744525

## Nearest historical live analogues

- `2026-09-15T11:52:29.344058Z` distance=0.357 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:05:46.278538Z` distance=0.359 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:09:57.090238Z` distance=0.359 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:14:08.250499Z` distance=0.359 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:18:18.946730Z` distance=0.359 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
