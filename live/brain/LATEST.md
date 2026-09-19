# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T17:22:38.318939Z`  
Memory snapshots: **1557**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=606 d1=1.0 d12=-1.0 z=29.003059250000003
- **REVERSAL** `biomass_gen` value=606 d1=1.0 d12=-1.0 z=29.003059250000003
- **ACCELERATION** `biomass_gen` value=606 d1=1.0 d12=-1.0 z=29.003059250000003
- **ROBUST_OUTLIER** `biomass_gen` value=606 d1=1.0 d12=-1.0 z=29.003059250000003
- **CHANGE_POINT** `ccgt_gen` value=6513 d1=132.0 d12=2229.0 z=5.990261437917223
- **CHANGE_POINT** `thermal_base` value=9843 d1=126.0 d12=2230.0 z=5.939083255629139
- **PERSISTENT_UP** `ccgt_gen` value=6513 d1=132.0 d12=2229.0 z=5.990261437917223
- **ROBUST_OUTLIER** `ccgt_gen` value=6513 d1=132.0 d12=2229.0 z=5.990261437917223
- **PERSISTENT_UP** `thermal_base` value=9843 d1=126.0 d12=2230.0 z=5.939083255629139
- **ROBUST_OUTLIER** `thermal_base` value=9843 d1=126.0 d12=2230.0 z=5.939083255629139
- **CHANGE_POINT** `margin` value=3.625e+04 d1=-8.0 d12=-673.0 z=-2.4778130399305556
- **CHANGE_POINT** `ind_generation` value=1.68e+04 d1=0.0 d12=1.0 z=2.0234692499999998
- **REVERSAL** `ps_gen` value=683 d1=-112.0 d12=10.0 z=3.8787128211764705
- **ACCELERATION** `ps_gen` value=683 d1=-112.0 d12=10.0 z=3.8787128211764705
- **ROBUST_OUTLIER** `ps_gen` value=683 d1=-112.0 d12=10.0 z=3.8787128211764705

## Nearest historical live analogues

- `2026-09-19T11:50:05.858742Z` distance=0.174 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.178 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.178 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.178 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.178 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
