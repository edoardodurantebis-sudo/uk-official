# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T10:08:48.817161Z`  
Memory snapshots: **521**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1204.0 z=-27.39086423780488
- **ROBUST_OUTLIER** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1204.0 z=-27.39086423780488
- **PERSISTENT_DOWN** `ps_gen` value=27 d1=-202.0 d12=-203.0 z=-26.4399982
- **ACCELERATION** `ps_gen` value=27 d1=-202.0 d12=-203.0 z=-26.4399982
- **ROBUST_OUTLIER** `ps_gen` value=27 d1=-202.0 d12=-203.0 z=-26.4399982
- **ROBUST_OUTLIER** `margin` value=3.416e+04 d1=0.0 d12=-1586.0 z=-23.344445242105266
- **ROBUST_OUTLIER** `imbalance` value=5367 d1=0.0 d12=-1338.0 z=-10.968337990654206
- **REVERSAL** `biomass_gen` value=3221 d1=4.0 d12=-17.0 z=-2.4731290833333333
- **PERSISTENT_DOWN** `wind_gen` value=5410 d1=-95.0 d12=-514.0 z=-1.3584675643359536
- **REVERSAL** `thermal_base` value=9657 d1=19.0 d12=-732.0 z=-1.0030264240023474
- **REVERSAL** `ccgt_gen` value=6330 d1=21.0 d12=-725.0 z=-0.9996548027011157
- **PERSISTENT_DOWN** `interconnector_net` value=1.021e+04 d1=-104.0 d12=-66.0 z=0.922385095211064
- **ACCELERATION** `interconnector_net` value=1.021e+04 d1=-104.0 d12=-66.0 z=0.922385095211064
- **PERSISTENT_DOWN** `nuclear_gen` value=3327 d1=-2.0 d12=-7.0 z=-0.67448975
- **ACCELERATION** `nuclear_gen` value=3327 d1=-2.0 d12=-7.0 z=-0.67448975

## Nearest historical live analogues

- `2026-09-16T08:52:24.970739Z` distance=3.100 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=3.100 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=3.100 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:05:03.473837Z` distance=3.100 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:09:50.095639Z` distance=3.100 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
