# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T13:37:45.498739Z`  
Memory snapshots: **229**  
Current physical regime: **BALANCED**

## Active patterns

- **ROBUST_OUTLIER** `imbalance` value=5698 d1=0.0 d12=48.0 z=6.926582238996479
- **ROBUST_OUTLIER** `ts_demand_forecast` value=1.912e+04 d1=0.0 d12=17.0 z=-6.8098483648148145
- **ROBUST_OUTLIER** `demand_forecast` value=1.862e+04 d1=0.0 d12=17.0 z=-6.560037346296297
- **CHANGE_POINT** `ind_generation` value=2.482e+04 d1=0.0 d12=65.0 z=4.529307126722817
- **ROBUST_OUTLIER** `ind_generation` value=2.482e+04 d1=0.0 d12=65.0 z=4.529307126722817
- **CHANGE_POINT** `ind_demand` value=-1.192e+04 d1=0.0 d12=-18.0 z=1.8509253604651164
- **CHANGE_POINT** `interconnector_net` value=1.028e+04 d1=0.0 d12=-1002.0 z=-1.3702791763157895
- **CHANGE_POINT** `margin` value=3.516e+04 d1=0.0 d12=-17.0 z=1.0208493513513515
- **CHANGE_POINT** `biomass_gen` value=1722 d1=-1.0 d12=-2.0 z=-0.43033851236979165
- **CHANGE_POINT** `ps_gen` value=-951 d1=4.0 d12=135.0 z=0.2917736558988764
- **REVERSAL** `wind_gen` value=1.01e+04 d1=44.0 d12=-467.0 z=-1.5150547707703927
- **PERSISTENT_DOWN** `interconnector_net` value=1.028e+04 d1=0.0 d12=-1002.0 z=-1.3702791763157895
- **ACCELERATION** `interconnector_net` value=1.028e+04 d1=0.0 d12=-1002.0 z=-1.3702791763157895
- **ACCELERATION** `nuclear_gen` value=3330 d1=2.0 d12=2.0 z=0.79712425
- **PERSISTENT_UP** `ccgt_gen` value=1473 d1=9.0 d12=14.0 z=-0.6488437519011406

## Nearest historical live analogues

- `2026-09-15T12:30:36.484168Z` distance=0.165 → {'next30m_imbalance_delta': 48.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T12:34:47.588906Z` distance=0.165 → {'next30m_imbalance_delta': 48.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T12:38:58.535756Z` distance=0.165 → {'next30m_imbalance_delta': 48.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T12:43:09.309119Z` distance=0.165 → {'next30m_imbalance_delta': 48.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T12:22:10.076168Z` distance=0.253 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
