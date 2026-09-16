# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T10:17:15.732009Z`  
Memory snapshots: **523**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **PERSISTENT_DOWN** `ps_gen` value=-5 d1=0.0 d12=-235.0 z=-30.7567326
- **ROBUST_OUTLIER** `ps_gen` value=-5 d1=0.0 d12=-235.0 z=-30.7567326
- **ROBUST_OUTLIER** `margin` value=3.416e+04 d1=0.0 d12=-349.0 z=-15.08531213275862
- **ROBUST_OUTLIER** `imbalance` value=5367 d1=0.0 d12=3.0 z=-10.968337990654206
- **CHANGE_POINT** `ind_demand` value=-1.388e+04 d1=0.0 d12=0.0 z=-6.682002957395499
- **ROBUST_OUTLIER** `ind_demand` value=-1.388e+04 d1=0.0 d12=0.0 z=-6.682002957395499
- **PERSISTENT_UP** `biomass_gen` value=3224 d1=2.0 d12=61.0 z=-1.7986393333333333
- **PERSISTENT_DOWN** `wind_gen` value=5306 d1=-40.0 d12=-434.0 z=-1.423328265762004
- **PERSISTENT_DOWN** `nuclear_gen` value=3325 d1=-3.0 d12=-4.0 z=-1.3489795
- **ACCELERATION** `nuclear_gen` value=3325 d1=-3.0 d12=-4.0 z=-1.3489795
- **REVERSAL** `thermal_base` value=9655 d1=45.0 d12=-302.0 z=-1.0046097332746478
- **REVERSAL** `ccgt_gen` value=6330 d1=48.0 d12=-298.0 z=-0.9996548027011157
- **REVERSAL** `interconnector_net` value=1.023e+04 d1=21.0 d12=-47.0 z=0.9095651383588755
- **ACCELERATION** `interconnector_net` value=1.023e+04 d1=21.0 d12=-47.0 z=0.9095651383588755

## Nearest historical live analogues

- `2026-09-16T09:22:28.850484Z` distance=0.172 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:52:24.970739Z` distance=3.200 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=3.200 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:00:49.660272Z` distance=3.200 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T09:05:03.473837Z` distance=3.200 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
