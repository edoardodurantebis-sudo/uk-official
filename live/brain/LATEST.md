# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T16:40:27.159371Z`  
Memory snapshots: **1888**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high, wind falling.

## Active patterns

- **REVERSAL** `biomass_gen` value=2018 d1=-6.0 d12=699.0 z=386.0779329
- **ROBUST_OUTLIER** `biomass_gen` value=2018 d1=-6.0 d12=699.0 z=386.0779329
- **CHANGE_POINT** `thermal_base` value=9008 d1=296.0 d12=2011.0 z=84.76520223557692
- **CHANGE_POINT** `ccgt_gen` value=5674 d1=298.0 d12=2017.0 z=83.10222768867924
- **PERSISTENT_UP** `thermal_base` value=9008 d1=296.0 d12=2011.0 z=84.76520223557692
- **ROBUST_OUTLIER** `thermal_base` value=9008 d1=296.0 d12=2011.0 z=84.76520223557692
- **PERSISTENT_UP** `ccgt_gen` value=5674 d1=298.0 d12=2017.0 z=83.10222768867924
- **ROBUST_OUTLIER** `ccgt_gen` value=5674 d1=298.0 d12=2017.0 z=83.10222768867924
- **CHANGE_POINT** `imbalance` value=-5182 d1=0.0 d12=-22.0 z=13.956749442307693
- **ROBUST_OUTLIER** `imbalance` value=-5182 d1=0.0 d12=-22.0 z=13.956749442307693
- **PERSISTENT_UP** `ps_gen` value=632 d1=469.0 d12=642.0 z=8.112612826388888
- **ACCELERATION** `ps_gen` value=632 d1=469.0 d12=642.0 z=8.112612826388888
- **ROBUST_OUTLIER** `ps_gen` value=632 d1=469.0 d12=642.0 z=8.112612826388888
- **REVERSAL** `interconnector_net` value=1.196e+04 d1=-1.0 d12=4012.0 z=4.649295318402777
- **ROBUST_OUTLIER** `interconnector_net` value=1.196e+04 d1=-1.0 d12=4012.0 z=4.649295318402777

## Nearest historical live analogues

- `2026-09-20T14:54:10.136499Z` distance=0.032 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:58:25.329493Z` distance=0.032 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:02:37.176302Z` distance=0.032 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:06:50.185709Z` distance=0.032 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:11:00.797261Z` distance=0.032 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
