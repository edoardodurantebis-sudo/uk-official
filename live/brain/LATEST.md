# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T10:04:36.575001Z`  
Memory snapshots: **520**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1204.0 z=-27.39086423780488
- **ROBUST_OUTLIER** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1204.0 z=-27.39086423780488
- **CHANGE_POINT** `margin` value=3.416e+04 d1=0.0 d12=-1586.0 z=-23.344445242105266
- **ROBUST_OUTLIER** `margin` value=3.416e+04 d1=0.0 d12=-1586.0 z=-23.344445242105266
- **CHANGE_POINT** `imbalance` value=5367 d1=0.0 d12=-1338.0 z=-10.968337990654206
- **ROBUST_OUTLIER** `imbalance` value=5367 d1=0.0 d12=-1338.0 z=-10.968337990654206
- **REVERSAL** `biomass_gen` value=3217 d1=5.0 d12=-23.0 z=-4.0469385
- **ROBUST_OUTLIER** `biomass_gen` value=3217 d1=5.0 d12=-23.0 z=-4.0469385
- **PERSISTENT_DOWN** `wind_gen` value=5505 d1=-86.0 d12=-760.0 z=-1.3000112121616079
- **REVERSAL** `thermal_base` value=9638 d1=6.0 d12=-909.0 z=-1.0180678620892019
- **REVERSAL** `ccgt_gen` value=6309 d1=4.0 d12=-906.0 z=-1.0162893120963006
- **PERSISTENT_UP** `interconnector_net` value=1.032e+04 d1=9.0 d12=39.0 z=0.9436826131094709
- **REVERSAL** `ps_gen` value=229 d1=5.0 d12=-1.0 z=0.8093876999999999
- **ACCELERATION** `ps_gen` value=229 d1=5.0 d12=-1.0 z=0.8093876999999999
- **REVERSAL** `nuclear_gen` value=3329 d1=2.0 d12=-3.0 z=0.0

## Nearest historical live analogues

- `2026-09-16T08:52:24.970739Z` distance=3.006 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=3.006 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=3.006 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:05:03.473837Z` distance=3.006 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:09:50.095639Z` distance=3.006 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
