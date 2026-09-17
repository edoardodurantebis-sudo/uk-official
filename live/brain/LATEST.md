# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T00:58:51.888099Z`  
Memory snapshots: **695**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6680 d1=-64.0 d12=-173.0 z=-5.035562954669497
- **PERSISTENT_DOWN** `interconnector_net` value=-6680 d1=-64.0 d12=-173.0 z=-5.035562954669497
- **ROBUST_OUTLIER** `interconnector_net` value=-6680 d1=-64.0 d12=-173.0 z=-5.035562954669497
- **REVERSAL** `ccgt_gen` value=4522 d1=121.0 d12=-122.0 z=-3.5587803932648403
- **ACCELERATION** `ccgt_gen` value=4522 d1=121.0 d12=-122.0 z=-3.5587803932648403
- **ROBUST_OUTLIER** `ccgt_gen` value=4522 d1=121.0 d12=-122.0 z=-3.5587803932648403
- **REVERSAL** `thermal_base` value=7832 d1=120.0 d12=-128.0 z=-3.5468327742027337
- **ACCELERATION** `thermal_base` value=7832 d1=120.0 d12=-128.0 z=-3.5468327742027337
- **ROBUST_OUTLIER** `thermal_base` value=7832 d1=120.0 d12=-128.0 z=-3.5468327742027337
- **CHANGE_POINT** `wind_gen` value=1.226e+04 d1=33.0 d12=520.0 z=1.139596774197593
- **PERSISTENT_UP** `ind_demand` value=-1.175e+04 d1=0.0 d12=16.0 z=2.83285695
- **ACCELERATION** `ind_demand` value=-1.175e+04 d1=0.0 d12=16.0 z=2.83285695
- **CHANGE_POINT** `ps_gen` value=-306 d1=-18.0 d12=-59.0 z=-0.740973636327504

## Nearest historical live analogues

- `2026-09-17T00:03:44.260171Z` distance=0.035 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:51:11.579176Z` distance=0.054 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:55:23.288978Z` distance=0.054 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:59:33.595851Z` distance=0.054 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:33:53.959539Z` distance=0.056 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 23.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
