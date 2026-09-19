# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T17:52:03.867019Z`  
Memory snapshots: **1564**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=682 d1=64.0 d12=77.0 z=27.519181800000002
- **ACCELERATION** `biomass_gen` value=682 d1=64.0 d12=77.0 z=27.519181800000002
- **ROBUST_OUTLIER** `biomass_gen` value=682 d1=64.0 d12=77.0 z=27.519181800000002
- **CHANGE_POINT** `ccgt_gen` value=6914 d1=78.0 d12=1687.0 z=6.217326309405941
- **CHANGE_POINT** `thermal_base` value=1.024e+04 d1=78.0 d12=1680.0 z=6.131425160146699
- **PERSISTENT_UP** `ccgt_gen` value=6914 d1=78.0 d12=1687.0 z=6.217326309405941
- **ROBUST_OUTLIER** `ccgt_gen` value=6914 d1=78.0 d12=1687.0 z=6.217326309405941
- **PERSISTENT_UP** `thermal_base` value=1.024e+04 d1=78.0 d12=1680.0 z=6.131425160146699
- **ROBUST_OUTLIER** `thermal_base` value=1.024e+04 d1=78.0 d12=1680.0 z=6.131425160146699
- **CHANGE_POINT** `ind_generation` value=1.682e+04 d1=0.0 d12=14.0 z=3.2038263125
- **CHANGE_POINT** `margin` value=3.63e+04 d1=50.0 d12=42.0 z=-2.2436152100694446
- **REVERSAL** `ps_gen` value=797 d1=1.0 d12=-186.0 z=3.475456598849372
- **ROBUST_OUTLIER** `ps_gen` value=797 d1=1.0 d12=-186.0 z=3.475456598849372
- **CHANGE_POINT** `imbalance` value=-3136 d1=0.0 d12=14.0 z=1.2316769347826086
- **ROBUST_OUTLIER** `ind_generation` value=1.682e+04 d1=0.0 d12=14.0 z=3.2038263125

## Nearest historical live analogues

- `2026-09-19T16:52:42.433757Z` distance=0.014 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T16:56:53.146650Z` distance=0.014 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:50:05.858742Z` distance=0.161 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.166 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}
- `2026-09-19T11:28:55.218479Z` distance=0.166 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
