# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T18:32:46.898081Z`  
Memory snapshots: **945**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.65e+04 d1=0.0 d12=18.0 z=-111.4594311875
- **PERSISTENT_UP** `ind_generation` value=2.65e+04 d1=0.0 d12=18.0 z=-111.4594311875
- **ROBUST_OUTLIER** `ind_generation` value=2.65e+04 d1=0.0 d12=18.0 z=-111.4594311875
- **CHANGE_POINT** `ind_demand` value=-1.125e+04 d1=0.0 d12=29.0 z=5.8455778333333335
- **CHANGE_POINT** `imbalance` value=9682 d1=0.0 d12=18.0 z=-5.175411735576923
- **PERSISTENT_UP** `ind_demand` value=-1.125e+04 d1=0.0 d12=29.0 z=5.8455778333333335
- **ROBUST_OUTLIER** `ind_demand` value=-1.125e+04 d1=0.0 d12=29.0 z=5.8455778333333335
- **PERSISTENT_UP** `imbalance` value=9682 d1=0.0 d12=18.0 z=-5.175411735576923
- **ACCELERATION** `imbalance` value=9682 d1=0.0 d12=18.0 z=-5.175411735576923
- **ROBUST_OUTLIER** `imbalance` value=9682 d1=0.0 d12=18.0 z=-5.175411735576923
- **CHANGE_POINT** `ps_gen` value=279 d1=0.0 d12=-77.0 z=2.069406259551495
- **CHANGE_POINT** `interconnector_net` value=-345 d1=-445.0 d12=-1206.0 z=-1.5176019375
- **CHANGE_POINT** `wind_gen` value=1.501e+04 d1=13.0 d12=386.0 z=1.0746376659482757
- **PERSISTENT_UP** `thermal_base` value=1.039e+04 d1=147.0 d12=564.0 z=2.50082404125
- **PERSISTENT_UP** `ccgt_gen` value=7069 d1=144.0 d12=560.0 z=2.4769949371040725

## Nearest historical live analogues

- `2026-09-17T16:51:11.529831Z` distance=0.040 → {'next30m_imbalance_delta': -25.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T17:21:14.586656Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:55:22.028914Z` distance=0.043 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:59:33.030689Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T17:04:23.689660Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
