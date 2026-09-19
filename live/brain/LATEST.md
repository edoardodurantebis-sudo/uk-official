# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T18:17:13.067441Z`  
Memory snapshots: **1570**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.681e+04 d1=0.0 d12=-3.0 z=2.5480723888888885
- **REVERSAL** `ccgt_gen` value=6738 d1=-117.0 d12=181.0 z=4.3787657866465866
- **ROBUST_OUTLIER** `ccgt_gen` value=6738 d1=-117.0 d12=181.0 z=4.3787657866465866
- **REVERSAL** `thermal_base` value=1.007e+04 d1=-118.0 d12=180.0 z=4.30979602868447
- **ROBUST_OUTLIER** `thermal_base` value=1.007e+04 d1=-118.0 d12=180.0 z=4.30979602868447
- **CHANGE_POINT** `margin` value=3.63e+04 d1=0.0 d12=50.0 z=-2.2436152100694446
- **ROBUST_OUTLIER** `ps_gen` value=824 d1=0.0 d12=60.0 z=3.229615626470588
- **CHANGE_POINT** `biomass_gen` value=781 d1=22.0 d12=173.0 z=1.209108353686636
- **CHANGE_POINT** `imbalance` value=-3139 d1=0.0 d12=-3.0 z=0.9314382261904761
- **PERSISTENT_UP** `biomass_gen` value=781 d1=22.0 d12=173.0 z=1.209108353686636
- **ACCELERATION** `nuclear_gen` value=3329 d1=-1.0 d12=-1.0 z=-0.67448975
- **REVERSAL** `wind_gen` value=1.437e+04 d1=22.0 d12=-223.0 z=-0.4669544423076923
- **REVERSAL** `interconnector_net` value=-2105 d1=36.0 d12=-793.0 z=0.42569901898532225

## Nearest historical live analogues

- `2026-09-19T16:52:42.433757Z` distance=0.014 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T16:56:53.146650Z` distance=0.014 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:01:39.109374Z` distance=0.014 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:05:49.699644Z` distance=0.014 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:10:02.143135Z` distance=0.014 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
