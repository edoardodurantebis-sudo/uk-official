# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T11:39:18.571623Z`  
Memory snapshots: **201**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=5651 d1=0.0 d12=6483.0 z=36.23311604385965
- **ROBUST_OUTLIER** `imbalance` value=5651 d1=0.0 d12=6483.0 z=36.23311604385965
- **CHANGE_POINT** `ind_generation` value=2.476e+04 d1=0.0 d12=5018.0 z=23.43355932904412
- **ROBUST_OUTLIER** `ind_generation` value=2.476e+04 d1=0.0 d12=5018.0 z=23.43355932904412
- **CHANGE_POINT** `margin` value=3.552e+04 d1=0.0 d12=1029.0 z=9.429759611650486
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=-1465.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `margin` value=3.552e+04 d1=0.0 d12=1029.0 z=9.429759611650486
- **CHANGE_POINT** `ind_demand` value=-1.19e+04 d1=0.0 d12=369.0 z=5.407159495833333
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=-1465.0 z=-6.6449730925925925
- **ROBUST_OUTLIER** `ind_demand` value=-1.19e+04 d1=0.0 d12=369.0 z=5.407159495833333
- **PERSISTENT_UP** `biomass_gen` value=1314 d1=30.0 d12=15.0 z=-4.072785734945255
- **ACCELERATION** `biomass_gen` value=1314 d1=30.0 d12=15.0 z=-4.072785734945255
- **ROBUST_OUTLIER** `biomass_gen` value=1314 d1=30.0 d12=15.0 z=-4.072785734945255
- **CHANGE_POINT** `ps_gen` value=-1212 d1=-7.0 d12=-11.0 z=-1.380853253429878
- **CHANGE_POINT** `ccgt_gen` value=1461 d1=-15.0 d12=-271.0 z=-1.254770215231788

## Nearest historical live analogues

- `2026-09-15T10:32:07.729613Z` distance=3.837 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}
- `2026-09-15T10:36:19.373424Z` distance=3.837 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}
- `2026-09-15T10:40:31.143417Z` distance=3.837 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}
- `2026-09-15T10:44:40.450787Z` distance=3.837 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}
- `2026-09-15T09:23:16.973095Z` distance=3.944 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
