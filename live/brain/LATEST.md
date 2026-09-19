# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T18:38:08.116705Z`  
Memory snapshots: **1575**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.62e+04 d1=0.0 d12=-614.0 z=-38.918058574999996
- **ROBUST_OUTLIER** `ind_generation` value=1.62e+04 d1=0.0 d12=-614.0 z=-38.918058574999996
- **CHANGE_POINT** `imbalance` value=-3750 d1=0.0 d12=-614.0 z=-10.223844631578947
- **ROBUST_OUTLIER** `imbalance` value=-3750 d1=0.0 d12=-614.0 z=-10.223844631578947
- **CHANGE_POINT** `margin` value=3.62e+04 d1=0.0 d12=-50.0 z=-2.712010869791667
- **PERSISTENT_UP** `ccgt_gen` value=7007 d1=7.0 d12=171.0 z=4.15914566728281
- **ACCELERATION** `ccgt_gen` value=7007 d1=7.0 d12=171.0 z=4.15914566728281
- **ROBUST_OUTLIER** `ccgt_gen` value=7007 d1=7.0 d12=171.0 z=4.15914566728281
- **PERSISTENT_UP** `thermal_base` value=1.034e+04 d1=6.0 d12=172.0 z=4.107248714872263
- **ACCELERATION** `thermal_base` value=1.034e+04 d1=6.0 d12=172.0 z=4.107248714872263
- **ROBUST_OUTLIER** `thermal_base` value=1.034e+04 d1=6.0 d12=172.0 z=4.107248714872263
- **CHANGE_POINT** `biomass_gen` value=920 d1=25.0 d12=302.0 z=2.0357327
- **PERSISTENT_UP** `biomass_gen` value=920 d1=25.0 d12=302.0 z=2.0357327
- **REVERSAL** `interconnector_net` value=-1196 d1=-1.0 d12=1786.0 z=1.3389623254950496
- **ACCELERATION** `interconnector_net` value=-1196 d1=-1.0 d12=1786.0 z=1.3389623254950496

## Nearest historical live analogues

- `2026-09-19T17:22:38.318939Z` distance=0.017 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:26:48.291042Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:31:01.384129Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:35:13.165368Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:39:26.231429Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
