# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T19:04:00.849934Z`  
Memory snapshots: **1922**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **PERSISTENT_DOWN** `thermal_base` value=1.206e+04 d1=-11.0 d12=-220.0 z=4.516789369538834
- **ROBUST_OUTLIER** `thermal_base` value=1.206e+04 d1=-11.0 d12=-220.0 z=4.516789369538834
- **PERSISTENT_DOWN** `ccgt_gen` value=8729 d1=-12.0 d12=-220.0 z=4.471181601924234
- **ROBUST_OUTLIER** `ccgt_gen` value=8729 d1=-12.0 d12=-220.0 z=4.471181601924234
- **CHANGE_POINT** `wind_gen` value=5428 d1=-128.0 d12=-1094.0 z=-1.5629722911870503
- **CHANGE_POINT** `ind_generation` value=1.547e+04 d1=0.0 d12=24.0 z=1.493513017857143
- **CHANGE_POINT** `biomass_gen` value=2346 d1=2.0 d12=67.0 z=1.2199934123505976
- **CHANGE_POINT** `imbalance` value=-5141 d1=0.0 d12=24.0 z=1.1522533229166667
- **CHANGE_POINT** `interconnector_net` value=9917 d1=43.0 d12=-16.0 z=0.3590906968623482
- **PERSISTENT_DOWN** `wind_gen` value=5428 d1=-128.0 d12=-1094.0 z=-1.5629722911870503
- **PERSISTENT_UP** `ind_generation` value=1.547e+04 d1=0.0 d12=24.0 z=1.493513017857143
- **PERSISTENT_UP** `biomass_gen` value=2346 d1=2.0 d12=67.0 z=1.2199934123505976
- **PERSISTENT_UP** `imbalance` value=-5141 d1=0.0 d12=24.0 z=1.1522533229166667
- **REVERSAL** `interconnector_net` value=9917 d1=43.0 d12=-16.0 z=0.3590906968623482
- **ACCELERATION** `interconnector_net` value=9917 d1=43.0 d12=-16.0 z=0.3590906968623482

## Nearest historical live analogues

- `2026-09-20T17:52:35.892709Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T17:56:46.494195Z` distance=0.026 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:00:58.540331Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:05:11.055248Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T18:09:24.806977Z` distance=0.026 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -30.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
