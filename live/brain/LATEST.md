# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T03:27:55.750125Z`  
Memory snapshots: **1359**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.831e+04 d1=0.0 d12=2.0 z=6.354831138554217
- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=2.0 z=6.354831138554217
- **CHANGE_POINT** `biomass_gen` value=789 d1=-14.0 d12=-208.0 z=-3.6318678846153847
- **CHANGE_POINT** `imbalance` value=9422 d1=0.0 d12=166.0 z=2.2514657852112676
- **CHANGE_POINT** `ind_generation` value=2.662e+04 d1=0.0 d12=166.0 z=2.2295633402777777
- **PERSISTENT_DOWN** `biomass_gen` value=789 d1=-14.0 d12=-208.0 z=-3.6318678846153847
- **ROBUST_OUTLIER** `biomass_gen` value=789 d1=-14.0 d12=-208.0 z=-3.6318678846153847
- **CHANGE_POINT** `interconnector_net` value=-1.116e+04 d1=0.0 d12=23.0 z=-1.0260664125166004
- **PERSISTENT_UP** `imbalance` value=9422 d1=0.0 d12=166.0 z=2.2514657852112676
- **PERSISTENT_UP** `ind_generation` value=2.662e+04 d1=0.0 d12=166.0 z=2.2295633402777777
- **REVERSAL** `ccgt_gen` value=3059 d1=1.0 d12=-4.0 z=-2.2045164986842103
- **ACCELERATION** `thermal_base` value=6402 d1=0.0 d12=-2.0 z=-2.1636229642857145
- **PERSISTENT_UP** `ind_demand` value=-1.088e+04 d1=0.0 d12=5.0 z=2.0234692499999998
- **REVERSAL** `nuclear_gen` value=3343 d1=-1.0 d12=2.0 z=1.21408155
- **ACCELERATION** `nuclear_gen` value=3343 d1=-1.0 d12=2.0 z=1.21408155

## Nearest historical live analogues

- `2026-09-19T02:20:35.608449Z` distance=0.005 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:24:50.521130Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:29:01.647315Z` distance=0.005 → {'next30m_imbalance_delta': 140.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:33:15.620122Z` distance=0.005 → {'next30m_imbalance_delta': 140.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:22:06.996302Z` distance=0.271 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
