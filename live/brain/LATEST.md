# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T02:45:51.156094Z`  
Memory snapshots: **1349**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.831e+04 d1=0.0 d12=1195.0 z=6.338578373493975
- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=1195.0 z=6.338578373493975
- **CHANGE_POINT** `biomass_gen` value=899 d1=-44.0 d12=-242.0 z=-2.903238489130435
- **CHANGE_POINT** `ccgt_gen` value=3058 d1=2.0 d12=-460.0 z=-2.0799381593023254
- **CHANGE_POINT** `thermal_base` value=6401 d1=4.0 d12=-456.0 z=-2.045226983870968
- **CHANGE_POINT** `ind_generation` value=2.645e+04 d1=0.0 d12=16.0 z=1.7109008292682928
- **PERSISTENT_DOWN** `biomass_gen` value=899 d1=-44.0 d12=-242.0 z=-2.903238489130435
- **CHANGE_POINT** `imbalance` value=9256 d1=0.0 d12=15.0 z=0.8130835342465753
- **CHANGE_POINT** `ps_gen` value=-543 d1=68.0 d12=282.0 z=-0.18449783237913486
- **REVERSAL** `ccgt_gen` value=3058 d1=2.0 d12=-460.0 z=-2.0799381593023254
- **REVERSAL** `thermal_base` value=6401 d1=4.0 d12=-456.0 z=-2.045226983870968
- **ACCELERATION** `nuclear_gen` value=3343 d1=2.0 d12=4.0 z=1.686224375
- **PERSISTENT_DOWN** `interconnector_net` value=-1.118e+04 d1=-1.0 d12=-47.0 z=-1.0827217600431607
- **ACCELERATION** `wind_gen` value=1.62e+04 d1=-88.0 d12=-243.0 z=-0.31854053739495797
- **PERSISTENT_UP** `ps_gen` value=-543 d1=68.0 d12=282.0 z=-0.18449783237913486

## Nearest historical live analogues

- `2026-09-19T00:22:06.996302Z` distance=0.276 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:26:19.516071Z` distance=0.276 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:30:34.705011Z` distance=0.276 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:34:45.510432Z` distance=0.276 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:38:55.391009Z` distance=0.276 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
