# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T17:12:25.661677Z`  
Memory snapshots: **280**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2978 d1=82.0 d12=1107.0 z=36.00627197340425
- **PERSISTENT_UP** `biomass_gen` value=2978 d1=82.0 d12=1107.0 z=36.00627197340425
- **ROBUST_OUTLIER** `biomass_gen` value=2978 d1=82.0 d12=1107.0 z=36.00627197340425
- **PERSISTENT_UP** `ccgt_gen` value=1.039e+04 d1=17.0 d12=1040.0 z=22.10643343194707
- **ROBUST_OUTLIER** `ccgt_gen` value=1.039e+04 d1=17.0 d12=1040.0 z=22.10643343194707
- **PERSISTENT_UP** `thermal_base` value=1.371e+04 d1=15.0 d12=1032.0 z=21.953880659774438
- **ROBUST_OUTLIER** `thermal_base` value=1.371e+04 d1=15.0 d12=1032.0 z=21.953880659774438
- **PERSISTENT_DOWN** `interconnector_net` value=-795 d1=-284.0 d12=-3494.0 z=-7.442228536354581
- **ROBUST_OUTLIER** `interconnector_net` value=-795 d1=-284.0 d12=-3494.0 z=-7.442228536354581
- **CHANGE_POINT** `ps_gen` value=503 d1=1.0 d12=381.0 z=3.6559116092870547
- **PERSISTENT_UP** `ps_gen` value=503 d1=1.0 d12=381.0 z=3.6559116092870547
- **ROBUST_OUTLIER** `ps_gen` value=503 d1=1.0 d12=381.0 z=3.6559116092870547
- **CHANGE_POINT** `imbalance` value=5835 d1=0.0 d12=10.0 z=1.3200727964285714
- **CHANGE_POINT** `ind_generation` value=2.496e+04 d1=0.0 d12=10.0 z=1.3200727964285714
- **PERSISTENT_DOWN** `nuclear_gen` value=3320 d1=-2.0 d12=-8.0 z=-1.7986393333333333

## Nearest historical live analogues

- `2026-09-15T15:52:27.365496Z` distance=0.134 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:56:36.878520Z` distance=0.134 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T16:00:48.162751Z` distance=0.134 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T16:05:00.775012Z` distance=0.134 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T16:09:15.808095Z` distance=0.134 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -54.0, 'next30m_residual_proxy_delta': 53.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
