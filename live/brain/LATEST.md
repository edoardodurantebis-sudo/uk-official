# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T10:51:07.761758Z`  
Memory snapshots: **531**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **ROBUST_OUTLIER** `ps_gen` value=-5 d1=0.0 d12=-229.0 z=-30.7567326
- **CHANGE_POINT** `imbalance` value=5373 d1=0.0 d12=6.0 z=-5.650073557971015
- **ROBUST_OUTLIER** `imbalance` value=5373 d1=0.0 d12=6.0 z=-5.650073557971015
- **ROBUST_OUTLIER** `ind_demand` value=-1.511e+04 d1=0.0 d12=-1226.0 z=-3.717289230292793
- **CHANGE_POINT** `wind_gen` value=4816 d1=-65.0 d12=-775.0 z=-1.6413548851931332
- **CHANGE_POINT** `ind_generation` value=2.601e+04 d1=0.0 d12=6.0 z=-1.6059279761904761
- **ROBUST_OUTLIER** `wind_forecast` value=1.976e+04 d1=0.0 d12=433.0 z=3.2392692452229297
- **CHANGE_POINT** `thermal_base` value=9444 d1=21.0 d12=-188.0 z=-1.1716488615023475
- **CHANGE_POINT** `ccgt_gen` value=6121 d1=15.0 d12=-184.0 z=-1.1652077771579565
- **PERSISTENT_DOWN** `margin` value=3.34e+04 d1=-822.0 d12=-757.0 z=-2.216481405306972
- **ACCELERATION** `margin` value=3.34e+04 d1=-822.0 d12=-757.0 z=-2.216481405306972
- **PERSISTENT_UP** `residual_proxy` value=110 d1=1356.0 d12=923.0 z=2.126575963375796
- **ACCELERATION** `residual_proxy` value=110 d1=1356.0 d12=923.0 z=2.126575963375796
- **REVERSAL** `nuclear_gen` value=3323 d1=6.0 d12=-4.0 z=-2.0234692499999998
- **ACCELERATION** `nuclear_gen` value=3323 d1=6.0 d12=-4.0 z=-2.0234692499999998

## Nearest historical live analogues

- `2026-09-16T09:51:49.097467Z` distance=2.998 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:56:02.414820Z` distance=2.998 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:22:28.850484Z` distance=3.025 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:26:41.423464Z` distance=3.025 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:30:50.292124Z` distance=3.025 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': -349.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
