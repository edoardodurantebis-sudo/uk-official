# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T10:44:45.089036Z`  
Memory snapshots: **834**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **ROBUST_OUTLIER** `wind_forecast` value=1.903e+04 d1=0.0 d12=-223.0 z=-15.041121425
- **CHANGE_POINT** `margin` value=3.444e+04 d1=0.0 d12=24.0 z=-6.23144509515571
- **ROBUST_OUTLIER** `margin` value=3.444e+04 d1=0.0 d12=24.0 z=-6.23144509515571
- **CHANGE_POINT** `imbalance` value=6691 d1=0.0 d12=28.0 z=-3.8198825445544555
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.986e+04 d1=0.0 d12=0.0 z=4.346060041304348
- **ROBUST_OUTLIER** `imbalance` value=6691 d1=0.0 d12=28.0 z=-3.8198825445544555
- **CHANGE_POINT** `ccgt_gen` value=1808 d1=-2.0 d12=-3.0 z=-1.2496760377629064
- **CHANGE_POINT** `thermal_base` value=5126 d1=0.0 d12=-1.0 z=-1.2425037151495861
- **REVERSAL** `wind_gen` value=1.568e+04 d1=-149.0 d12=11.0 z=2.934358745479833
- **ACCELERATION** `wind_gen` value=1.568e+04 d1=-149.0 d12=11.0 z=2.934358745479833
- **CHANGE_POINT** `ind_demand` value=-1.304e+04 d1=0.0 d12=-30.0 z=-0.9100099450222883
- **CHANGE_POINT** `ps_gen` value=-948 d1=8.0 d12=6.0 z=-0.866637073902439
- **CHANGE_POINT** `interconnector_net` value=-435 d1=0.0 d12=-2819.0 z=-6.329077132401239e-05
- **PERSISTENT_DOWN** `biomass_gen` value=1953 d1=-39.0 d12=-81.0 z=-1.5593138036184209
- **PERSISTENT_DOWN** `ccgt_gen` value=1808 d1=-2.0 d12=-3.0 z=-1.2496760377629064

## Nearest historical live analogues

- `2026-09-17T09:49:22.756114Z` distance=0.144 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:19:56.543683Z` distance=0.166 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:24:08.362874Z` distance=0.166 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:28:21.130076Z` distance=0.166 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T09:32:33.001998Z` distance=0.166 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -57.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
