# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T16:46:58.568264Z`  
Memory snapshots: **920**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3045 d1=1.0 d12=4.0 z=8.223120544910179
- **CHANGE_POINT** `imbalance` value=1.162e+04 d1=0.0 d12=-20.0 z=-8.171702740384616
- **CHANGE_POINT** `ps_gen` value=164 d1=100.0 d12=420.0 z=6.748220109605912
- **ACCELERATION** `biomass_gen` value=3045 d1=1.0 d12=4.0 z=8.223120544910179
- **ROBUST_OUTLIER** `biomass_gen` value=3045 d1=1.0 d12=4.0 z=8.223120544910179
- **ROBUST_OUTLIER** `imbalance` value=1.162e+04 d1=0.0 d12=-20.0 z=-8.171702740384616
- **PERSISTENT_UP** `ps_gen` value=164 d1=100.0 d12=420.0 z=6.748220109605912
- **ROBUST_OUTLIER** `ps_gen` value=164 d1=100.0 d12=420.0 z=6.748220109605912
- **CHANGE_POINT** `thermal_base` value=8233 d1=43.0 d12=1454.0 z=4.396009374244256
- **CHANGE_POINT** `ccgt_gen` value=4910 d1=40.0 d12=1444.0 z=4.290459739904988
- **CHANGE_POINT** `nuclear_gen` value=3323 d1=3.0 d12=10.0 z=3.37244875
- **ROBUST_OUTLIER** `residual_proxy` value=-2590 d1=0.0 d12=81.0 z=5.0514977021276595
- **PERSISTENT_UP** `thermal_base` value=8233 d1=43.0 d12=1454.0 z=4.396009374244256
- **ROBUST_OUTLIER** `thermal_base` value=8233 d1=43.0 d12=1454.0 z=4.396009374244256
- **PERSISTENT_UP** `ccgt_gen` value=4910 d1=40.0 d12=1444.0 z=4.290459739904988

## Nearest historical live analogues

- `2026-09-17T15:52:19.169744Z` distance=0.053 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T10:57:20.878127Z` distance=0.177 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:01:31.274983Z` distance=0.177 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:05:43.396655Z` distance=0.177 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:09:56.284661Z` distance=0.177 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
