# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T17:21:51.078919Z`  
Memory snapshots: **2238**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=8083 d1=0.0 d12=-2120.0 z=-10.425731539119804
- **PERSISTENT_DOWN** `interconnector_net` value=8083 d1=0.0 d12=-2120.0 z=-10.425731539119804
- **ROBUST_OUTLIER** `interconnector_net` value=8083 d1=0.0 d12=-2120.0 z=-10.425731539119804
- **CHANGE_POINT** `ps_gen` value=855 d1=-125.0 d12=770.0 z=4.417012522123894
- **REVERSAL** `ps_gen` value=855 d1=-125.0 d12=770.0 z=4.417012522123894
- **ROBUST_OUTLIER** `ps_gen` value=855 d1=-125.0 d12=770.0 z=4.417012522123894
- **PERSISTENT_UP** `thermal_base` value=1.717e+04 d1=230.0 d12=834.0 z=4.166155125655074
- **ROBUST_OUTLIER** `thermal_base` value=1.717e+04 d1=230.0 d12=834.0 z=4.166155125655074
- **PERSISTENT_UP** `ccgt_gen` value=1.366e+04 d1=226.0 d12=830.0 z=4.124678461738309
- **ROBUST_OUTLIER** `ccgt_gen` value=1.366e+04 d1=226.0 d12=830.0 z=4.124678461738309
- **PERSISTENT_DOWN** `margin` value=3.617e+04 d1=-106.0 d12=-108.0 z=-3.859580236111111
- **ACCELERATION** `margin` value=3.617e+04 d1=-106.0 d12=-108.0 z=-3.859580236111111
- **ROBUST_OUTLIER** `margin` value=3.617e+04 d1=-106.0 d12=-108.0 z=-3.859580236111111
- **CHANGE_POINT** `ind_generation` value=1.843e+04 d1=0.0 d12=45.0 z=1.1104404420731708
- **CHANGE_POINT** `imbalance` value=-3026 d1=0.0 d12=45.0 z=0.9559697244094487

## Nearest historical live analogues

- `2026-09-21T15:52:07.020346Z` distance=0.019 → {'next30m_imbalance_delta': 28.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T15:56:21.179145Z` distance=0.019 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:00:35.791303Z` distance=0.019 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:04:50.781494Z` distance=0.019 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:09:03.909955Z` distance=0.019 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': -4.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
