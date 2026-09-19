# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T17:47:52.155729Z`  
Memory snapshots: **1563**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=618 d1=10.0 d12=13.0 z=18.885713000000003
- **PERSISTENT_UP** `biomass_gen` value=618 d1=10.0 d12=13.0 z=18.885713000000003
- **ACCELERATION** `biomass_gen` value=618 d1=10.0 d12=13.0 z=18.885713000000003
- **ROBUST_OUTLIER** `biomass_gen` value=618 d1=10.0 d12=13.0 z=18.885713000000003
- **CHANGE_POINT** `ccgt_gen` value=6836 d1=31.0 d12=2184.0 z=6.087103040841583
- **CHANGE_POINT** `thermal_base` value=1.016e+04 d1=28.0 d12=2178.0 z=6.0273728211656445
- **PERSISTENT_UP** `ccgt_gen` value=6836 d1=31.0 d12=2184.0 z=6.087103040841583
- **ROBUST_OUTLIER** `ccgt_gen` value=6836 d1=31.0 d12=2184.0 z=6.087103040841583
- **PERSISTENT_UP** `thermal_base` value=1.016e+04 d1=28.0 d12=2178.0 z=6.0273728211656445
- **ROBUST_OUTLIER** `thermal_base` value=1.016e+04 d1=28.0 d12=2178.0 z=6.0273728211656445
- **CHANGE_POINT** `ind_generation` value=1.682e+04 d1=0.0 d12=14.0 z=3.2038263125
- **CHANGE_POINT** `margin` value=3.625e+04 d1=0.0 d12=-8.0 z=-2.4778130399305556
- **PERSISTENT_DOWN** `ps_gen` value=796 d1=0.0 d12=-187.0 z=3.5582192319915253
- **ROBUST_OUTLIER** `ps_gen` value=796 d1=0.0 d12=-187.0 z=3.5582192319915253
- **ROBUST_OUTLIER** `ind_generation` value=1.682e+04 d1=0.0 d12=14.0 z=3.2038263125

## Nearest historical live analogues

- `2026-09-19T16:52:42.433757Z` distance=0.003 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:50:05.858742Z` distance=0.174 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.178 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.178 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:33:09.035060Z` distance=0.178 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
