# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T23:28:05.319553Z`  
Memory snapshots: **1644**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **REVERSAL** `ps_gen` value=-255 d1=2.0 d12=-118.0 z=-90.929649421875
- **ROBUST_OUTLIER** `ps_gen` value=-255 d1=2.0 d12=-118.0 z=-90.929649421875
- **ROBUST_OUTLIER** `ind_demand` value=-1.189e+04 d1=0.0 d12=-14.0 z=-10.11734625
- **CHANGE_POINT** `wind_gen` value=1.609e+04 d1=30.0 d12=930.0 z=4.089892236230638
- **PERSISTENT_UP** `wind_gen` value=1.609e+04 d1=30.0 d12=930.0 z=4.089892236230638
- **ROBUST_OUTLIER** `wind_gen` value=1.609e+04 d1=30.0 d12=930.0 z=4.089892236230638
- **PERSISTENT_DOWN** `thermal_base` value=6678 d1=-140.0 d12=-802.0 z=-3.6312807219650205
- **ROBUST_OUTLIER** `thermal_base` value=6678 d1=-140.0 d12=-802.0 z=-3.6312807219650205
- **PERSISTENT_DOWN** `ccgt_gen` value=3344 d1=-138.0 d12=-795.0 z=-3.6110719130879345
- **ROBUST_OUTLIER** `ccgt_gen` value=3344 d1=-138.0 d12=-795.0 z=-3.6110719130879345
- **CHANGE_POINT** `imbalance` value=-3940 d1=0.0 d12=-25.0 z=-0.9822666262135922
- **CHANGE_POINT** `ind_generation` value=1.601e+04 d1=0.0 d12=-25.0 z=-0.9822666262135922
- **CHANGE_POINT** `biomass_gen` value=909 d1=-2.0 d12=-16.0 z=0.07615206854838709
- **PERSISTENT_UP** `margin` value=3.607e+04 d1=0.0 d12=2.0 z=-1.78065294
- **ACCELERATION** `margin` value=3.607e+04 d1=0.0 d12=2.0 z=-1.78065294

## Nearest historical live analogues

- `2026-09-19T22:20:55.351132Z` distance=0.013 → {'next30m_imbalance_delta': -22.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T22:25:06.371138Z` distance=0.013 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T22:29:16.794263Z` distance=0.013 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T22:33:29.926961Z` distance=0.013 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:51:35.987527Z` distance=0.013 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
