# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T17:26:48.291042Z`  
Memory snapshots: **1558**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=608 d1=2.0 d12=1.0 z=29.452719083333335
- **PERSISTENT_UP** `biomass_gen` value=608 d1=2.0 d12=1.0 z=29.452719083333335
- **ACCELERATION** `biomass_gen` value=608 d1=2.0 d12=1.0 z=29.452719083333335
- **ROBUST_OUTLIER** `biomass_gen` value=608 d1=2.0 d12=1.0 z=29.452719083333335
- **CHANGE_POINT** `thermal_base` value=9887 d1=44.0 d12=2198.0 z=5.8173661408450705
- **CHANGE_POINT** `ccgt_gen` value=6557 d1=44.0 d12=2198.0 z=5.79768676690051
- **PERSISTENT_UP** `thermal_base` value=9887 d1=44.0 d12=2198.0 z=5.8173661408450705
- **ROBUST_OUTLIER** `thermal_base` value=9887 d1=44.0 d12=2198.0 z=5.8173661408450705
- **PERSISTENT_UP** `ccgt_gen` value=6557 d1=44.0 d12=2198.0 z=5.79768676690051
- **ROBUST_OUTLIER** `ccgt_gen` value=6557 d1=44.0 d12=2198.0 z=5.79768676690051
- **CHANGE_POINT** `ind_generation` value=1.682e+04 d1=14.0 d12=15.0 z=3.2038263125
- **CHANGE_POINT** `margin` value=3.625e+04 d1=0.0 d12=-673.0 z=-2.4778130399305556
- **REVERSAL** `ps_gen` value=764 d1=81.0 d12=-99.0 z=3.8990637897091722
- **ACCELERATION** `ps_gen` value=764 d1=81.0 d12=-99.0 z=3.8990637897091722
- **ROBUST_OUTLIER** `ps_gen` value=764 d1=81.0 d12=-99.0 z=3.8990637897091722

## Nearest historical live analogues

- `2026-09-19T11:50:05.858742Z` distance=0.174 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.178 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.178 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.178 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:37:21.494450Z` distance=0.178 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
