# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T03:23:44.436802Z`  
Memory snapshots: **1358**  
Current physical regime: **BALANCED**

Regime read: margin high, frequency stress.

## Active patterns

- **CHANGE_POINT** `margin` value=3.831e+04 d1=0.0 d12=2.0 z=6.354831138554217
- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=2.0 z=6.354831138554217
- **CHANGE_POINT** `biomass_gen` value=803 d1=-9.0 d12=-242.0 z=-3.4865931692307695
- **CHANGE_POINT** `imbalance` value=9422 d1=26.0 d12=166.0 z=2.2514657852112676
- **CHANGE_POINT** `ind_generation` value=2.662e+04 d1=26.0 d12=166.0 z=2.2295633402777777
- **PERSISTENT_DOWN** `biomass_gen` value=803 d1=-9.0 d12=-242.0 z=-3.4865931692307695
- **ROBUST_OUTLIER** `biomass_gen` value=803 d1=-9.0 d12=-242.0 z=-3.4865931692307695
- **CHANGE_POINT** `interconnector_net` value=-1.116e+04 d1=1.0 d12=23.0 z=-1.0327844379150066
- **REVERSAL** `ccgt_gen` value=3058 d1=1.0 d12=-36.0 z=-2.263845916223404
- **PERSISTENT_UP** `imbalance` value=9422 d1=26.0 d12=166.0 z=2.2514657852112676
- **PERSISTENT_UP** `ind_generation` value=2.662e+04 d1=26.0 d12=166.0 z=2.2295633402777777
- **REVERSAL** `thermal_base` value=6402 d1=4.0 d12=-40.0 z=-2.2187162828947367
- **PERSISTENT_UP** `ind_demand` value=-1.088e+04 d1=1.0 d12=5.0 z=2.0234692499999998
- **REVERSAL** `nuclear_gen` value=3344 d1=3.0 d12=-4.0 z=2.0234692499999998
- **PERSISTENT_UP** `wind_gen` value=1.616e+04 d1=12.0 d12=9.0 z=-0.11857759310018903

## Nearest historical live analogues

- `2026-09-19T02:20:35.608449Z` distance=0.005 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:24:50.521130Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:29:01.647315Z` distance=0.005 → {'next30m_imbalance_delta': 140.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:22:06.996302Z` distance=0.274 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:26:19.516071Z` distance=0.274 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
