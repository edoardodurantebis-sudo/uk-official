# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T11:52:29.344058Z`  
Memory snapshots: **204**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=5651 d1=0.0 d12=6483.0 z=35.30406178632479
- **ROBUST_OUTLIER** `imbalance` value=5651 d1=0.0 d12=6483.0 z=35.30406178632479
- **CHANGE_POINT** `ind_generation` value=2.476e+04 d1=0.0 d12=5018.0 z=18.31588545258621
- **ROBUST_OUTLIER** `ind_generation` value=2.476e+04 d1=0.0 d12=5018.0 z=18.31588545258621
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.91e+04 d1=0.0 d12=0.0 z=-10.950539470588234
- **ROBUST_OUTLIER** `demand_forecast` value=1.86e+04 d1=0.0 d12=0.0 z=-6.6449730925925925
- **CHANGE_POINT** `margin` value=3.518e+04 d1=-334.0 d12=-28.0 z=3.4412074138349515
- **PERSISTENT_DOWN** `margin` value=3.518e+04 d1=-334.0 d12=-28.0 z=3.4412074138349515
- **ACCELERATION** `margin` value=3.518e+04 d1=-334.0 d12=-28.0 z=3.4412074138349515
- **ROBUST_OUTLIER** `margin` value=3.518e+04 d1=-334.0 d12=-28.0 z=3.4412074138349515
- **CHANGE_POINT** `ps_gen` value=-1224 d1=1.0 d12=-24.0 z=-1.353931700807636
- **ROBUST_OUTLIER** `ind_demand` value=-1.19e+04 d1=0.0 d12=369.0 z=3.0166739368131865
- **CHANGE_POINT** `wind_gen` value=1.133e+04 d1=19.0 d12=-164.0 z=-0.8673054446399566
- **REVERSAL** `nuclear_gen` value=3331 d1=-1.0 d12=3.0 z=1.5176019375
- **PERSISTENT_UP** `biomass_gen` value=1484 d1=49.0 d12=216.0 z=-1.4737264709882139

## Nearest historical live analogues

- `2026-09-15T10:57:20.493386Z` distance=3.025 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 306.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T10:53:07.965768Z` distance=3.240 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T10:32:07.729613Z` distance=3.263 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}
- `2026-09-15T10:36:19.373424Z` distance=3.263 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}
- `2026-09-15T10:40:31.143417Z` distance=3.263 → {'next30m_imbalance_delta': 6507.0, 'next30m_margin_delta': 723.0, 'next30m_residual_proxy_delta': -1465.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
