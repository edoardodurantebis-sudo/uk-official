# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T18:53:45.990590Z`  
Memory snapshots: **950**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.65e+04 d1=0.0 d12=10.0 z=-95.10305475
- **ROBUST_OUTLIER** `ind_generation` value=2.65e+04 d1=0.0 d12=10.0 z=-95.10305475
- **CHANGE_POINT** `imbalance` value=9682 d1=0.0 d12=10.0 z=-4.738230485765125
- **ROBUST_OUTLIER** `ind_demand` value=-1.125e+04 d1=0.0 d12=29.0 z=5.8455778333333335
- **ROBUST_OUTLIER** `imbalance` value=9682 d1=0.0 d12=10.0 z=-4.738230485765125
- **CHANGE_POINT** `ccgt_gen` value=7083 d1=-4.0 d12=693.0 z=2.3193184021459228
- **CHANGE_POINT** `thermal_base` value=1.04e+04 d1=-2.0 d12=694.0 z=2.3188830669375533
- **CHANGE_POINT** `interconnector_net` value=-493 d1=-25.0 d12=-834.0 z=-1.6621891055122495
- **REVERSAL** `ccgt_gen` value=7083 d1=-4.0 d12=693.0 z=2.3193184021459228
- **REVERSAL** `thermal_base` value=1.04e+04 d1=-2.0 d12=694.0 z=2.3188830669375533
- **ACCELERATION** `nuclear_gen` value=3321 d1=2.0 d12=1.0 z=1.7236960277777778
- **PERSISTENT_DOWN** `interconnector_net` value=-493 d1=-25.0 d12=-834.0 z=-1.6621891055122495
- **PERSISTENT_UP** `wind_gen` value=1.513e+04 d1=62.0 d12=420.0 z=1.2036153297413792
- **PERSISTENT_DOWN** `ps_gen` value=278 d1=-2.0 d12=-74.0 z=0.8168190529878617
- **PERSISTENT_UP** `biomass_gen` value=2985 d1=54.0 d12=74.0 z=0.5524062394094993

## Nearest historical live analogues

- `2026-09-17T16:51:11.529831Z` distance=0.040 → {'next30m_imbalance_delta': -25.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T17:21:14.586656Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:55:22.028914Z` distance=0.043 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:59:33.030689Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T17:04:23.689660Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
