# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T16:34:16.300458Z`  
Memory snapshots: **917**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=4740 d1=242.0 d12=1563.0 z=15.471968959183673
- **CHANGE_POINT** `thermal_base` value=8052 d1=241.0 d12=1564.0 z=15.253220009036145
- **PERSISTENT_UP** `ccgt_gen` value=4740 d1=242.0 d12=1563.0 z=15.471968959183673
- **ROBUST_OUTLIER** `ccgt_gen` value=4740 d1=242.0 d12=1563.0 z=15.471968959183673
- **PERSISTENT_UP** `thermal_base` value=8052 d1=241.0 d12=1564.0 z=15.253220009036145
- **ROBUST_OUTLIER** `thermal_base` value=8052 d1=241.0 d12=1564.0 z=15.253220009036145
- **CHANGE_POINT** `biomass_gen` value=3069 d1=1.0 d12=318.0 z=11.730500902083332
- **ROBUST_OUTLIER** `biomass_gen` value=3069 d1=1.0 d12=318.0 z=11.730500902083332
- **CHANGE_POINT** `imbalance` value=1.162e+04 d1=0.0 d12=-34.0 z=-8.171702740384616
- **PERSISTENT_UP** `ps_gen` value=-254 d1=1.0 d12=21.0 z=9.840056019444445
- **ROBUST_OUTLIER** `ps_gen` value=-254 d1=1.0 d12=21.0 z=9.840056019444445
- **PERSISTENT_DOWN** `imbalance` value=1.162e+04 d1=0.0 d12=-34.0 z=-8.171702740384616
- **ROBUST_OUTLIER** `imbalance` value=1.162e+04 d1=0.0 d12=-34.0 z=-8.171702740384616
- **PERSISTENT_UP** `residual_proxy` value=-2590 d1=81.0 d12=81.0 z=5.0514977021276595
- **ACCELERATION** `residual_proxy` value=-2590 d1=81.0 d12=81.0 z=5.0514977021276595

## Nearest historical live analogues

- `2026-09-17T10:57:20.878127Z` distance=0.177 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:01:31.274983Z` distance=0.177 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:05:43.396655Z` distance=0.177 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:09:56.284661Z` distance=0.177 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:14:08.992825Z` distance=0.177 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
