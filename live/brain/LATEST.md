# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T08:42:01.705604Z`  
Memory snapshots: **805**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.214e+04 d1=0.0 d12=-3.0 z=-6.79929183467742
- **ROBUST_OUTLIER** `margin` value=3.605e+04 d1=0.0 d12=471.0 z=6.011756467391304
- **REVERSAL** `wind_gen` value=1.545e+04 d1=33.0 d12=-62.0 z=5.560514968169762
- **ACCELERATION** `wind_gen` value=1.545e+04 d1=33.0 d12=-62.0 z=5.560514968169762
- **ROBUST_OUTLIER** `wind_gen` value=1.545e+04 d1=33.0 d12=-62.0 z=5.560514968169762
- **CHANGE_POINT** `ccgt_gen` value=2492 d1=-309.0 d12=-683.0 z=-2.3570484198369566
- **CHANGE_POINT** `thermal_base` value=5808 d1=-312.0 d12=-677.0 z=-2.353956941712204
- **CHANGE_POINT** `ps_gen` value=-711 d1=-148.0 d12=-937.0 z=-1.0997966329787234
- **PERSISTENT_UP** `interconnector_net` value=5461 d1=0.0 d12=1438.0 z=2.9902541777888443
- **PERSISTENT_DOWN** `ccgt_gen` value=2492 d1=-309.0 d12=-683.0 z=-2.3570484198369566
- **PERSISTENT_DOWN** `thermal_base` value=5808 d1=-312.0 d12=-677.0 z=-2.353956941712204
- **PERSISTENT_DOWN** `biomass_gen` value=1959 d1=-49.0 d12=-114.0 z=-1.5630605760292167
- **PERSISTENT_DOWN** `ps_gen` value=-711 d1=-148.0 d12=-937.0 z=-1.0997966329787234
- **REVERSAL** `nuclear_gen` value=3316 d1=-3.0 d12=6.0 z=0.94428565
- **ACCELERATION** `nuclear_gen` value=3316 d1=-3.0 d12=6.0 z=0.94428565

## Nearest historical live analogues

- `2026-09-17T06:52:29.952634Z` distance=0.213 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:56:43.028097Z` distance=0.213 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:00:51.548981Z` distance=0.213 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:05:06.905847Z` distance=0.213 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:09:19.225959Z` distance=0.213 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
