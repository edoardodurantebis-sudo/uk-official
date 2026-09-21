# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T00:58:12.338936Z`  
Memory snapshots: **2006**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `imbalance` value=-4908 d1=0.0 d12=321.0 z=2.638941146875
- **CHANGE_POINT** `ind_generation` value=1.57e+04 d1=0.0 d12=321.0 z=2.638941146875
- **CHANGE_POINT** `ccgt_gen` value=5405 d1=36.0 d12=-532.0 z=-0.7952938843283582
- **CHANGE_POINT** `thermal_base` value=8741 d1=32.0 d12=-532.0 z=-0.7928286212027279
- **CHANGE_POINT** `interconnector_net` value=1.108e+04 d1=10.0 d12=1005.0 z=0.7217093983691328
- **PERSISTENT_DOWN** `wind_gen` value=4917 d1=-58.0 d12=-229.0 z=-2.2745643438473517
- **REVERSAL** `ccgt_gen` value=5405 d1=36.0 d12=-532.0 z=-0.7952938843283582
- **REVERSAL** `thermal_base` value=8741 d1=32.0 d12=-532.0 z=-0.7928286212027279
- **PERSISTENT_UP** `interconnector_net` value=1.108e+04 d1=10.0 d12=1005.0 z=0.7217093983691328
- **PERSISTENT_UP** `ind_demand` value=-1.184e+04 d1=0.0 d12=1.0 z=None
- **ACCELERATION** `ind_demand` value=-1.184e+04 d1=0.0 d12=1.0 z=None
- **PERSISTENT_DOWN** `nuclear_gen` value=3336 d1=-4.0 d12=0.0 z=0.0
- **ACCELERATION** `nuclear_gen` value=3336 d1=-4.0 d12=0.0 z=0.0

## Nearest historical live analogues

- `2026-09-21T00:03:26.283660Z` distance=0.006 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T23:53:21.201980Z` distance=1.155 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T23:57:34.023150Z` distance=1.155 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T23:32:17.355228Z` distance=1.158 → {'next30m_imbalance_delta': 232.0, 'next30m_margin_delta': -76.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T23:36:30.492110Z` distance=1.158 → {'next30m_imbalance_delta': 232.0, 'next30m_margin_delta': -76.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
