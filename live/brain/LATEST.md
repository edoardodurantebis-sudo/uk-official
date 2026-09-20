# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T05:37:06.199540Z`  
Memory snapshots: **1731**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-6811 d1=0.0 d12=-48.0 z=-39.53547611538462
- **CHANGE_POINT** `ind_generation` value=1.314e+04 d1=0.0 d12=-48.0 z=-39.53547611538462
- **ROBUST_OUTLIER** `imbalance` value=-6811 d1=0.0 d12=-48.0 z=-39.53547611538462
- **ROBUST_OUTLIER** `ind_generation` value=1.314e+04 d1=0.0 d12=-48.0 z=-39.53547611538462
- **ROBUST_OUTLIER** `margin` value=3.752e+04 d1=0.0 d12=7.0 z=11.50600161764706
- **CHANGE_POINT** `biomass_gen` value=1163 d1=-38.0 d12=-64.0 z=-1.0056029
- **CHANGE_POINT** `ps_gen` value=-746 d1=-53.0 d12=-45.0 z=-0.28665814375000004
- **PERSISTENT_DOWN** `biomass_gen` value=1163 d1=-38.0 d12=-64.0 z=-1.0056029
- **ACCELERATION** `biomass_gen` value=1163 d1=-38.0 d12=-64.0 z=-1.0056029
- **ACCELERATION** `nuclear_gen` value=3337 d1=3.0 d12=4.0 z=0.8993196666666666
- **REVERSAL** `ccgt_gen` value=3445 d1=18.0 d12=-697.0 z=-0.5213912829365079
- **REVERSAL** `thermal_base` value=6782 d1=21.0 d12=-693.0 z=-0.513433703926282
- **PERSISTENT_UP** `interconnector_net` value=-1.125e+04 d1=1.0 d12=1410.0 z=-0.3752641302192067
- **ACCELERATION** `interconnector_net` value=-1.125e+04 d1=1.0 d12=1410.0 z=-0.3752641302192067
- **PERSISTENT_DOWN** `ps_gen` value=-746 d1=-53.0 d12=-45.0 z=-0.28665814375000004

## Nearest historical live analogues

- `2026-09-20T04:20:43.261806Z` distance=0.043 → {'next30m_imbalance_delta': -236.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:24:55.304349Z` distance=0.043 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:29:05.930316Z` distance=0.043 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:33:18.594038Z` distance=0.043 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:38:07.201517Z` distance=0.043 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 3.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
