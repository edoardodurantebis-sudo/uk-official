# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T08:25:13.033747Z`  
Memory snapshots: **801**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.214e+04 d1=0.0 d12=-3.0 z=-6.79929183467742
- **CHANGE_POINT** `wind_gen` value=1.563e+04 d1=0.0 d12=1046.0 z=6.153178032637076
- **PERSISTENT_DOWN** `ind_demand` value=-1.214e+04 d1=0.0 d12=-3.0 z=-6.79929183467742
- **ACCELERATION** `ind_demand` value=-1.214e+04 d1=0.0 d12=-3.0 z=-6.79929183467742
- **ROBUST_OUTLIER** `ind_demand` value=-1.214e+04 d1=0.0 d12=-3.0 z=-6.79929183467742
- **PERSISTENT_UP** `wind_gen` value=1.563e+04 d1=0.0 d12=1046.0 z=6.153178032637076
- **ROBUST_OUTLIER** `wind_gen` value=1.563e+04 d1=0.0 d12=1046.0 z=6.153178032637076
- **PERSISTENT_UP** `margin` value=3.605e+04 d1=0.0 d12=471.0 z=6.011756467391304
- **ACCELERATION** `margin` value=3.605e+04 d1=0.0 d12=471.0 z=6.011756467391304
- **ROBUST_OUTLIER** `margin` value=3.605e+04 d1=0.0 d12=471.0 z=6.011756467391304
- **ROBUST_OUTLIER** `interconnector_net` value=4898 d1=0.0 d12=962.0 z=3.7205262426192727
- **CHANGE_POINT** `biomass_gen` value=2031 d1=0.0 d12=-538.0 z=-1.437893594873502
- **PERSISTENT_UP** `imbalance` value=7525 d1=0.0 d12=368.0 z=2.3524886402439025
- **ACCELERATION** `imbalance` value=7525 d1=0.0 d12=368.0 z=2.3524886402439025
- **CHANGE_POINT** `ps_gen` value=-415 d1=0.0 d12=-638.0 z=-0.32937145379377436

## Nearest historical live analogues

- `2026-09-17T06:52:29.952634Z` distance=0.218 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:56:43.028097Z` distance=0.218 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:00:51.548981Z` distance=0.218 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:05:06.905847Z` distance=0.218 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:09:19.225959Z` distance=0.218 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
