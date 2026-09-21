# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T17:30:18.299231Z`  
Memory snapshots: **2240**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=8083 d1=0.0 d12=-1645.0 z=-10.425731539119804
- **ROBUST_OUTLIER** `interconnector_net` value=8083 d1=0.0 d12=-1645.0 z=-10.425731539119804
- **CHANGE_POINT** `ps_gen` value=832 d1=0.0 d12=388.0 z=4.789558527777778
- **ROBUST_OUTLIER** `ps_gen` value=832 d1=0.0 d12=388.0 z=4.789558527777778
- **PERSISTENT_UP** `thermal_base` value=1.749e+04 d1=0.0 d12=890.0 z=3.918159031533477
- **ACCELERATION** `thermal_base` value=1.749e+04 d1=0.0 d12=890.0 z=3.918159031533477
- **ROBUST_OUTLIER** `thermal_base` value=1.749e+04 d1=0.0 d12=890.0 z=3.918159031533477
- **PERSISTENT_UP** `ccgt_gen` value=1.398e+04 d1=0.0 d12=882.0 z=3.8872822641509432
- **ACCELERATION** `ccgt_gen` value=1.398e+04 d1=0.0 d12=882.0 z=3.8872822641509432
- **ROBUST_OUTLIER** `ccgt_gen` value=1.398e+04 d1=0.0 d12=882.0 z=3.8872822641509432
- **PERSISTENT_DOWN** `margin` value=3.617e+04 d1=0.0 d12=-108.0 z=-3.859580236111111
- **ROBUST_OUTLIER** `margin` value=3.617e+04 d1=0.0 d12=-108.0 z=-3.859580236111111
- **CHANGE_POINT** `ind_generation` value=1.844e+04 d1=0.0 d12=53.0 z=1.1762443201219512
- **CHANGE_POINT** `imbalance` value=-3018 d1=0.0 d12=53.0 z=0.9984572677165354
- **CHANGE_POINT** `nuclear_gen` value=3512 d1=0.0 d12=8.0 z=0.6744897499999999

## Nearest historical live analogues

- `2026-09-21T15:52:07.020346Z` distance=0.019 → {'next30m_imbalance_delta': 28.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T15:56:21.179145Z` distance=0.020 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:00:35.791303Z` distance=0.020 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:04:50.781494Z` distance=0.020 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:09:03.909955Z` distance=0.020 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': -4.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
