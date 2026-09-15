# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T11:35:06.452199Z`  
Memory snapshots: **200**  
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
- **ROBUST_OUTLIER** `biomass_gen` value=1284 d1=0.0 d12=-60.0 z=-8.051721390625
- **CHANGE_POINT** `ind_demand` value=-1.19e+04 d1=0.0 d12=369.0 z=5.407159495833333
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=-1465.0 z=-6.6449730925925925
- **ROBUST_OUTLIER** `ind_demand` value=-1.19e+04 d1=0.0 d12=369.0 z=5.407159495833333
- **CHANGE_POINT** `ps_gen` value=-1205 d1=0.0 d12=-1.0 z=-1.4743369699835527
- **CHANGE_POINT** `ccgt_gen` value=1476 d1=0.0 d12=-369.0 z=-1.255664170509709
- **CHANGE_POINT** `thermal_base` value=4798 d1=0.0 d12=-372.0 z=-1.2222620439952439
- **CHANGE_POINT** `wind_gen` value=1.12e+04 d1=0.0 d12=-327.0 z=-1.0949255906990178

## Nearest historical live analogues

- `2026-09-15T10:32:07.729613Z` distance=4.716 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}
- `2026-09-15T10:36:19.373424Z` distance=4.716 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}
- `2026-09-15T10:40:31.143417Z` distance=4.716 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}
- `2026-09-15T09:23:16.973095Z` distance=4.791 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:27:29.987536Z` distance=4.791 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
