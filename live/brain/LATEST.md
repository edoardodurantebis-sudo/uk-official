# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T10:32:40.818301Z`  
Memory snapshots: **1801**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high, wind falling.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.978e+04 d1=0.0 d12=889.0 z=27.6908701
- **ROBUST_OUTLIER** `ind_generation` value=1.603e+04 d1=0.0 d12=47.0 z=24.0118351
- **ROBUST_OUTLIER** `ind_demand` value=-1.247e+04 d1=0.0 d12=-90.0 z=-13.40548378125
- **ROBUST_OUTLIER** `imbalance` value=-4140 d1=0.0 d12=47.0 z=7.1927368481781375
- **CHANGE_POINT** `wind_gen` value=1.399e+04 d1=-45.0 d12=-873.0 z=-2.8129641647465435
- **CHANGE_POINT** `biomass_gen` value=600 d1=5.0 d12=14.0 z=-0.6584577355687606
- **CHANGE_POINT** `ps_gen` value=-910 d1=-208.0 d12=19.0 z=-0.6202896808035714
- **REVERSAL** `ccgt_gen` value=2508 d1=-4.0 d12=234.0 z=-2.431426760080645
- **REVERSAL** `thermal_base` value=5846 d1=-3.0 d12=235.0 z=-2.389805535942492
- **PERSISTENT_UP** `residual_proxy` value=1.731e+04 d1=93.0 d12=93.0 z=2.1282036832298137
- **ACCELERATION** `residual_proxy` value=1.731e+04 d1=93.0 d12=93.0 z=2.1282036832298137
- **PERSISTENT_DOWN** `wind_forecast` value=2360 d1=-93.0 d12=-93.0 z=-1.2316769347826086
- **ACCELERATION** `wind_forecast` value=2360 d1=-93.0 d12=-93.0 z=-1.2316769347826086
- **PERSISTENT_UP** `nuclear_gen` value=3338 d1=1.0 d12=1.0 z=0.67448975
- **ACCELERATION** `nuclear_gen` value=3338 d1=1.0 d12=1.0 z=0.67448975

## Nearest historical live analogues

- `2026-09-20T09:20:07.153673Z` distance=0.336 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:24:18.809197Z` distance=0.336 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:28:32.169507Z` distance=0.336 → {'next30m_imbalance_delta': 33.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:32:44.320157Z` distance=0.336 → {'next30m_imbalance_delta': 33.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T09:36:54.599847Z` distance=0.336 → {'next30m_imbalance_delta': 33.0, 'next30m_margin_delta': 399.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
