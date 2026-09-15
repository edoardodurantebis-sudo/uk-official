# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T11:48:17.686671Z`  
Memory snapshots: **203**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=5651 d1=0.0 d12=6483.0 z=35.7625560952381
- **ROBUST_OUTLIER** `imbalance` value=5651 d1=0.0 d12=6483.0 z=35.7625560952381
- **CHANGE_POINT** `ind_generation` value=2.476e+04 d1=0.0 d12=5018.0 z=20.561058508064516
- **ROBUST_OUTLIER** `ind_generation` value=2.476e+04 d1=0.0 d12=5018.0 z=20.561058508064516
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=0.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=0.0 z=-6.6449730925925925
- **CHANGE_POINT** `margin` value=3.552e+04 d1=0.0 d12=306.0 z=4.534797591019418
- **CHANGE_POINT** `ind_demand` value=-1.19e+04 d1=0.0 d12=369.0 z=3.0166739368131865
- **ROBUST_OUTLIER** `margin` value=3.552e+04 d1=0.0 d12=306.0 z=4.534797591019418
- **CHANGE_POINT** `ps_gen` value=-1225 d1=-3.0 d12=-253.0 z=-1.3761199221311475
- **CHANGE_POINT** `thermal_base` value=4789 d1=0.0 d12=-85.0 z=-1.2191013792085057
- **ROBUST_OUTLIER** `ind_demand` value=-1.19e+04 d1=0.0 d12=369.0 z=3.0166739368131865
- **CHANGE_POINT** `wind_gen` value=1.131e+04 d1=3.0 d12=-157.0 z=-0.9009046931941431
- **PERSISTENT_UP** `biomass_gen` value=1435 d1=55.0 d12=219.0 z=-2.3320212811344017
- **PERSISTENT_UP** `nuclear_gen` value=3332 d1=0.0 d12=4.0 z=1.686224375

## Nearest historical live analogues

- `2026-09-15T10:53:07.965768Z` distance=3.480 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T10:32:07.729613Z` distance=3.502 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}
- `2026-09-15T10:36:19.373424Z` distance=3.502 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}
- `2026-09-15T10:40:31.143417Z` distance=3.502 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}
- `2026-09-15T10:44:40.450787Z` distance=3.502 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
