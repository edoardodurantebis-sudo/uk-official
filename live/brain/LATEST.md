# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T10:12:56.190943Z`  
Memory snapshots: **1455**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.321e+04 d1=0.0 d12=2.0 z=-87.42136593055555
- **ROBUST_OUTLIER** `ind_demand` value=-1.321e+04 d1=0.0 d12=2.0 z=-87.42136593055555
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.893e+04 d1=0.0 d12=0.0 z=8.995972344650205
- **CHANGE_POINT** `margin` value=3.645e+04 d1=0.0 d12=-27.0 z=-6.180678553814714
- **ROBUST_OUTLIER** `margin` value=3.645e+04 d1=0.0 d12=-27.0 z=-6.180678553814714
- **CHANGE_POINT** `imbalance` value=7793 d1=0.0 d12=22.0 z=-3.973829471153846
- **CHANGE_POINT** `biomass_gen` value=478 d1=0.0 d12=1.0 z=-3.37244875
- **ROBUST_OUTLIER** `ind_generation` value=2.672e+04 d1=0.0 d12=22.0 z=-4.071919601851852
- **ROBUST_OUTLIER** `imbalance` value=7793 d1=0.0 d12=22.0 z=-3.973829471153846
- **PERSISTENT_UP** `biomass_gen` value=478 d1=0.0 d12=1.0 z=-3.37244875
- **ROBUST_OUTLIER** `biomass_gen` value=478 d1=0.0 d12=1.0 z=-3.37244875
- **CHANGE_POINT** `ps_gen` value=-688 d1=2.0 d12=-266.0 z=-1.3399259463087247
- **CHANGE_POINT** `thermal_base` value=6320 d1=-8.0 d12=-206.0 z=-1.150600161764706
- **CHANGE_POINT** `ccgt_gen` value=2991 d1=-8.0 d12=-203.0 z=-1.099903219771242
- **ROBUST_OUTLIER** `residual_proxy` value=8953 d1=0.0 d12=0.0 z=-3.094968789556962

## Nearest historical live analogues

- `2026-09-18T09:21:34.020078Z` distance=0.927 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:25:46.604177Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:30:05.383319Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:34:18.274964Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T09:39:05.140398Z` distance=0.927 → {'next30m_imbalance_delta': -299.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
