# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T10:48:57.536388Z`  
Memory snapshots: **835**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **ROBUST_OUTLIER** `wind_forecast` value=1.903e+04 d1=0.0 d12=-223.0 z=-15.041121425
- **CHANGE_POINT** `margin` value=3.444e+04 d1=0.0 d12=24.0 z=-4.594101103316326
- **CHANGE_POINT** `imbalance` value=6691 d1=0.0 d12=28.0 z=-3.639699405660377
- **ROBUST_OUTLIER** `margin` value=3.444e+04 d1=0.0 d12=24.0 z=-4.594101103316326
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.986e+04 d1=0.0 d12=0.0 z=4.346060041304348
- **ROBUST_OUTLIER** `imbalance` value=6691 d1=0.0 d12=28.0 z=-3.639699405660377
- **CHANGE_POINT** `ccgt_gen` value=1808 d1=0.0 d12=-2.0 z=-1.185491728684531
- **CHANGE_POINT** `thermal_base` value=5126 d1=0.0 d12=0.0 z=-1.1789193559683313
- **CHANGE_POINT** `ind_demand` value=-1.304e+04 d1=0.0 d12=-30.0 z=-0.9076590552670623
- **CHANGE_POINT** `ps_gen` value=-950 d1=-2.0 d12=-1.0 z=-0.8692692290243902
- **REVERSAL** `wind_gen` value=1.564e+04 d1=-35.0 d12=41.0 z=2.2653883764845606
- **ACCELERATION** `wind_gen` value=1.564e+04 d1=-35.0 d12=41.0 z=2.2653883764845606
- **PERSISTENT_DOWN** `biomass_gen` value=1916 d1=-37.0 d12=-95.0 z=-1.5357219213021491
- **PERSISTENT_DOWN** `ccgt_gen` value=1808 d1=0.0 d12=-2.0 z=-1.185491728684531
- **ACCELERATION** `ccgt_gen` value=1808 d1=0.0 d12=-2.0 z=-1.185491728684531

## Nearest historical live analogues

- `2026-09-17T09:49:22.756114Z` distance=0.144 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:53:34.920005Z` distance=0.144 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:19:56.543683Z` distance=0.166 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:24:08.362874Z` distance=0.166 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:28:21.130076Z` distance=0.166 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
