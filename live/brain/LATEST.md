# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T16:55:36.949343Z`  
Memory snapshots: **276**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2719 d1=105.0 d12=971.0 z=28.572533877659573
- **PERSISTENT_UP** `biomass_gen` value=2719 d1=105.0 d12=971.0 z=28.572533877659573
- **ROBUST_OUTLIER** `biomass_gen` value=2719 d1=105.0 d12=971.0 z=28.572533877659573
- **PERSISTENT_UP** `ccgt_gen` value=1.025e+04 d1=16.0 d12=3175.0 z=22.035916085249042
- **ROBUST_OUTLIER** `ccgt_gen` value=1.025e+04 d1=16.0 d12=3175.0 z=22.035916085249042
- **PERSISTENT_UP** `thermal_base` value=1.357e+04 d1=18.0 d12=3172.0 z=21.762513979166666
- **ROBUST_OUTLIER** `thermal_base` value=1.357e+04 d1=18.0 d12=3172.0 z=21.762513979166666
- **REVERSAL** `interconnector_net` value=516 d1=11.0 d12=-3830.0 z=-8.657467985709697
- **ROBUST_OUTLIER** `interconnector_net` value=516 d1=11.0 d12=-3830.0 z=-8.657467985709697
- **CHANGE_POINT** `ps_gen` value=429 d1=-3.0 d12=574.0 z=3.587295871138996
- **REVERSAL** `ps_gen` value=429 d1=-3.0 d12=574.0 z=3.587295871138996
- **ROBUST_OUTLIER** `ps_gen` value=429 d1=-3.0 d12=574.0 z=3.587295871138996
- **CHANGE_POINT** `imbalance` value=5835 d1=8.0 d12=10.0 z=1.3200727964285714
- **CHANGE_POINT** `ind_generation` value=2.496e+04 d1=8.0 d12=10.0 z=1.3200727964285714
- **CHANGE_POINT** `margin` value=3.483e+04 d1=0.0 d12=-139.0 z=-1.1602621606217618

## Nearest historical live analogues

- `2026-09-15T15:52:27.365496Z` distance=0.134 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:56:36.878520Z` distance=0.134 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T16:00:48.162751Z` distance=0.134 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:22:47.712669Z` distance=0.171 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:27:19.632279Z` distance=0.171 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 320.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
