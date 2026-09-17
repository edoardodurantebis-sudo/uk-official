# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T09:15:44.928080Z`  
Memory snapshots: **813**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.213e+04 d1=0.0 d12=14.0 z=-6.646987697580645
- **PERSISTENT_UP** `wind_gen` value=1.569e+04 d1=0.0 d12=60.0 z=6.486465286005435
- **ACCELERATION** `wind_gen` value=1.569e+04 d1=0.0 d12=60.0 z=6.486465286005435
- **ROBUST_OUTLIER** `wind_gen` value=1.569e+04 d1=0.0 d12=60.0 z=6.486465286005435
- **CHANGE_POINT** `thermal_base` value=5416 d1=0.0 d12=-921.0 z=-3.675338117983368
- **CHANGE_POINT** `ccgt_gen` value=2101 d1=0.0 d12=-924.0 z=-3.661714457216495
- **CHANGE_POINT** `biomass_gen` value=1674 d1=0.0 d12=-357.0 z=-2.073630506308101
- **PERSISTENT_DOWN** `thermal_base` value=5416 d1=0.0 d12=-921.0 z=-3.675338117983368
- **ROBUST_OUTLIER** `thermal_base` value=5416 d1=0.0 d12=-921.0 z=-3.675338117983368
- **PERSISTENT_DOWN** `ccgt_gen` value=2101 d1=0.0 d12=-924.0 z=-3.661714457216495
- **ROBUST_OUTLIER** `ccgt_gen` value=2101 d1=0.0 d12=-924.0 z=-3.661714457216495
- **CHANGE_POINT** `ps_gen` value=-557 d1=0.0 d12=-142.0 z=-0.667009272181146
- **PERSISTENT_DOWN** `interconnector_net` value=3935 d1=0.0 d12=-963.0 z=2.3768526315984215
- **PERSISTENT_DOWN** `biomass_gen` value=1674 d1=0.0 d12=-357.0 z=-2.073630506308101
- **ACCELERATION** `ps_gen` value=-557 d1=0.0 d12=-142.0 z=-0.667009272181146

## Nearest historical live analogues

- `2026-09-17T08:21:01.012290Z` distance=0.028 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 10.0}
- `2026-09-17T06:52:29.952634Z` distance=0.228 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:56:43.028097Z` distance=0.228 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:00:51.548981Z` distance=0.228 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T07:05:06.905847Z` distance=0.228 → {'next30m_imbalance_delta': -181.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
