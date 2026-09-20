# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T05:41:17.937410Z`  
Memory snapshots: **1732**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-6811 d1=0.0 d12=-34.0 z=-39.53547611538462
- **CHANGE_POINT** `ind_generation` value=1.314e+04 d1=0.0 d12=-34.0 z=-39.53547611538462
- **ROBUST_OUTLIER** `imbalance` value=-6811 d1=0.0 d12=-34.0 z=-39.53547611538462
- **ROBUST_OUTLIER** `ind_generation` value=1.314e+04 d1=0.0 d12=-34.0 z=-39.53547611538462
- **ROBUST_OUTLIER** `margin` value=3.752e+04 d1=0.0 d12=4.0 z=11.50600161764706
- **CHANGE_POINT** `biomass_gen` value=1111 d1=-52.0 d12=-120.0 z=-2.2810017
- **CHANGE_POINT** `ps_gen` value=-807 d1=-61.0 d12=-106.0 z=-0.8835421286549707
- **PERSISTENT_DOWN** `biomass_gen` value=1111 d1=-52.0 d12=-120.0 z=-2.2810017
- **ACCELERATION** `nuclear_gen` value=3338 d1=1.0 d12=4.0 z=1.1241495833333335
- **PERSISTENT_DOWN** `ps_gen` value=-807 d1=-61.0 d12=-106.0 z=-0.8835421286549707
- **REVERSAL** `interconnector_net` value=-1.125e+04 d1=-2.0 d12=1406.0 z=-0.3578161890018484
- **REVERSAL** `ccgt_gen` value=3559 d1=114.0 d12=-514.0 z=-0.26248615886699506
- **REVERSAL** `thermal_base` value=6897 d1=115.0 d12=-510.0 z=-0.24914596422628954
- **ACCELERATION** `wind_gen` value=1.546e+04 d1=18.0 d12=112.0 z=0.06891071749226006
- **PERSISTENT_UP** `residual_proxy` value=1.68e+04 d1=0.0 d12=161.0 z=None

## Nearest historical live analogues

- `2026-09-20T04:20:43.261806Z` distance=0.043 → {'next30m_imbalance_delta': -236.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:24:55.304349Z` distance=0.043 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:29:05.930316Z` distance=0.043 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:33:18.594038Z` distance=0.043 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:38:07.201517Z` distance=0.043 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 3.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
