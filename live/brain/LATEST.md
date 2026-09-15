# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T17:16:36.649879Z`  
Memory snapshots: **281**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2991 d1=13.0 d12=989.0 z=37.96627859444445
- **PERSISTENT_UP** `biomass_gen` value=2991 d1=13.0 d12=989.0 z=37.96627859444445
- **ROBUST_OUTLIER** `biomass_gen` value=2991 d1=13.0 d12=989.0 z=37.96627859444445
- **REVERSAL** `ccgt_gen` value=1.039e+04 d1=-3.0 d12=938.0 z=22.015548676082865
- **ROBUST_OUTLIER** `ccgt_gen` value=1.039e+04 d1=-3.0 d12=938.0 z=22.015548676082865
- **REVERSAL** `thermal_base` value=1.371e+04 d1=-6.0 d12=931.0 z=21.93866660526316
- **ROBUST_OUTLIER** `thermal_base` value=1.371e+04 d1=-6.0 d12=931.0 z=21.93866660526316
- **REVERSAL** `interconnector_net` value=-766 d1=29.0 d12=-3457.0 z=-7.422746262699203
- **ROBUST_OUTLIER** `interconnector_net` value=-766 d1=29.0 d12=-3457.0 z=-7.422746262699203
- **CHANGE_POINT** `ps_gen` value=501 d1=-2.0 d12=377.0 z=3.509550114791289
- **REVERSAL** `ps_gen` value=501 d1=-2.0 d12=377.0 z=3.509550114791289
- **ROBUST_OUTLIER** `ps_gen` value=501 d1=-2.0 d12=377.0 z=3.509550114791289
- **CHANGE_POINT** `imbalance` value=5835 d1=0.0 d12=8.0 z=1.38059620703125
- **CHANGE_POINT** `ind_generation` value=2.496e+04 d1=0.0 d12=8.0 z=1.2271966284722222
- **PERSISTENT_DOWN** `nuclear_gen` value=3317 d1=-3.0 d12=-7.0 z=-2.4731290833333333

## Nearest historical live analogues

- `2026-09-15T16:21:57.402275Z` distance=0.088 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 53.0}
- `2026-09-15T15:52:27.365496Z` distance=0.134 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:56:36.878520Z` distance=0.134 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T16:00:48.162751Z` distance=0.134 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T16:05:00.775012Z` distance=0.134 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -54.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
