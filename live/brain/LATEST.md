# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T08:29:24.431780Z`  
Memory snapshots: **802**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.214e+04 d1=0.0 d12=-3.0 z=-6.79929183467742
- **CHANGE_POINT** `wind_gen` value=1.565e+04 d1=20.0 d12=924.0 z=6.238147347513089
- **CHANGE_POINT** `margin` value=3.605e+04 d1=0.0 d12=471.0 z=6.011756467391304
- **PERSISTENT_DOWN** `ind_demand` value=-1.214e+04 d1=0.0 d12=-3.0 z=-6.79929183467742
- **ROBUST_OUTLIER** `ind_demand` value=-1.214e+04 d1=0.0 d12=-3.0 z=-6.79929183467742
- **PERSISTENT_UP** `wind_gen` value=1.565e+04 d1=20.0 d12=924.0 z=6.238147347513089
- **ROBUST_OUTLIER** `wind_gen` value=1.565e+04 d1=20.0 d12=924.0 z=6.238147347513089
- **PERSISTENT_UP** `margin` value=3.605e+04 d1=0.0 d12=471.0 z=6.011756467391304
- **ROBUST_OUTLIER** `margin` value=3.605e+04 d1=0.0 d12=471.0 z=6.011756467391304
- **CHANGE_POINT** `imbalance` value=7525 d1=0.0 d12=368.0 z=2.3524886402439025
- **CHANGE_POINT** `biomass_gen` value=2031 d1=0.0 d12=-439.0 z=-1.4359815023271278
- **REVERSAL** `interconnector_net` value=4890 d1=-8.0 d12=929.0 z=2.9200364079484324
- **CHANGE_POINT** `ps_gen` value=-425 d1=-10.0 d12=-648.0 z=-0.3556161911478599
- **PERSISTENT_UP** `imbalance` value=7525 d1=0.0 d12=368.0 z=2.3524886402439025
- **CHANGE_POINT** `ts_demand_forecast` value=1.901e+04 d1=0.0 d12=-365.0 z=None

## Nearest historical live analogues

- `2026-09-17T06:52:29.952634Z` distance=0.218 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:56:43.028097Z` distance=0.218 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:00:51.548981Z` distance=0.218 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:05:06.905847Z` distance=0.218 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:09:19.225959Z` distance=0.218 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
