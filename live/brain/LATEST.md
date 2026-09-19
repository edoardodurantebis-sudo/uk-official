# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T19:07:32.438602Z`  
Memory snapshots: **1582**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.621e+04 d1=0.0 d12=-603.0 z=-38.378466775
- **ROBUST_OUTLIER** `ind_generation` value=1.621e+04 d1=0.0 d12=-603.0 z=-38.378466775
- **CHANGE_POINT** `imbalance` value=-3742 d1=0.0 d12=-603.0 z=-10.081846789473685
- **ROBUST_OUTLIER** `imbalance` value=-3742 d1=0.0 d12=-603.0 z=-10.081846789473685
- **PERSISTENT_DOWN** `ccgt_gen` value=6319 d1=-226.0 d12=-419.0 z=2.8888949593802344
- **PERSISTENT_DOWN** `thermal_base` value=9647 d1=-234.0 d12=-420.0 z=2.8846885448825503
- **PERSISTENT_UP** `interconnector_net` value=137 d1=863.0 d12=2242.0 z=2.610666479314003
- **REVERSAL** `biomass_gen` value=959 d1=-54.0 d12=178.0 z=2.1036949030837007
- **PERSISTENT_DOWN** `wind_gen` value=1.406e+04 d1=-145.0 d12=-303.0 z=-0.9879668909523809
- **ACCELERATION** `wind_gen` value=1.406e+04 d1=-145.0 d12=-303.0 z=-0.9879668909523809
- **PERSISTENT_DOWN** `nuclear_gen` value=3328 d1=-8.0 d12=-1.0 z=-0.8093876999999999
- **ACCELERATION** `nuclear_gen` value=3328 d1=-8.0 d12=-1.0 z=-0.8093876999999999

## Nearest historical live analogues

- `2026-09-19T17:22:38.318939Z` distance=0.017 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:26:48.291042Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:31:01.384129Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:35:13.165368Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:39:26.231429Z` distance=0.017 → {'next30m_imbalance_delta': -3.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
