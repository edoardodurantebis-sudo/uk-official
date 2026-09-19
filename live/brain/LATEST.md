# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T03:11:04.634985Z`  
Memory snapshots: **1355**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.831e+04 d1=0.0 d12=2.0 z=6.354831138554217
- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=2.0 z=6.354831138554217
- **CHANGE_POINT** `biomass_gen` value=813 d1=-2.0 d12=-328.0 z=-3.4142775717054263
- **CHANGE_POINT** `imbalance` value=9396 d1=0.0 d12=155.0 z=1.8548468125
- **CHANGE_POINT** `ind_generation` value=2.659e+04 d1=0.0 d12=156.0 z=1.7354848623595507
- **PERSISTENT_DOWN** `biomass_gen` value=813 d1=-2.0 d12=-328.0 z=-3.4142775717054263
- **ROBUST_OUTLIER** `biomass_gen` value=813 d1=-2.0 d12=-328.0 z=-3.4142775717054263
- **CHANGE_POINT** `interconnector_net` value=-1.116e+04 d1=6.0 d12=37.0 z=-1.0531624482901727
- **PERSISTENT_DOWN** `ccgt_gen` value=3057 d1=-1.0 d12=-127.0 z=-2.183172112720403
- **PERSISTENT_DOWN** `thermal_base` value=6395 d1=-3.0 d12=-128.0 z=-2.180168888888889
- **CHANGE_POINT** `ps_gen` value=-543 d1=0.0 d12=-164.0 z=-0.10330023198198199
- **PERSISTENT_UP** `interconnector_net` value=-1.116e+04 d1=6.0 d12=37.0 z=-1.0531624482901727
- **REVERSAL** `wind_gen` value=1.615e+04 d1=20.0 d12=-38.0 z=-0.37649033382642993
- **ACCELERATION** `wind_gen` value=1.615e+04 d1=20.0 d12=-38.0 z=-0.37649033382642993
- **PERSISTENT_DOWN** `ps_gen` value=-543 d1=0.0 d12=-164.0 z=-0.10330023198198199

## Nearest historical live analogues

- `2026-09-19T00:22:06.996302Z` distance=0.274 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:26:19.516071Z` distance=0.274 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:30:34.705011Z` distance=0.274 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:34:45.510432Z` distance=0.274 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:38:55.391009Z` distance=0.274 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
