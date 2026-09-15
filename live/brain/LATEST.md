# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T07:21:37.326101Z`  
Memory snapshots: **140**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3240 d1=9.0 d12=36.0 z=3.192584816666667
- **CHANGE_POINT** `interconnector_net` value=3060 d1=-23.0 d12=3666.0 z=1.7433642057168248
- **PERSISTENT_UP** `biomass_gen` value=3240 d1=9.0 d12=36.0 z=3.192584816666667
- **ROBUST_OUTLIER** `biomass_gen` value=3240 d1=9.0 d12=36.0 z=3.192584816666667
- **PERSISTENT_UP** `ind_demand` value=-1.228e+04 d1=144.0 d12=155.0 z=3.1074706339285716
- **ACCELERATION** `ind_demand` value=-1.228e+04 d1=144.0 d12=155.0 z=3.1074706339285716
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=144.0 d12=155.0 z=3.1074706339285716
- **CHANGE_POINT** `thermal_base` value=6788 d1=45.0 d12=-445.0 z=-0.6231326624365483
- **CHANGE_POINT** `ccgt_gen` value=3468 d1=45.0 d12=-442.0 z=-0.6092719115776082
- **CHANGE_POINT** `ind_generation` value=2.003e+04 d1=249.0 d12=136.0 z=-0.24274695372750643
- **CHANGE_POINT** `imbalance` value=-454 d1=249.0 d12=136.0 z=-0.24163421456185566
- **REVERSAL** `interconnector_net` value=3060 d1=-23.0 d12=3666.0 z=1.7433642057168248
- **ACCELERATION** `nuclear_gen` value=3320 d1=0.0 d12=-3.0 z=-1.3489795
- **PERSISTENT_DOWN** `wind_gen` value=1.28e+04 d1=-318.0 d12=-642.0 z=-1.3014193253205129
- **PERSISTENT_UP** `margin` value=3.413e+04 d1=158.0 d12=231.0 z=0.9323828897058823

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=1.004 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=1.004 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=1.004 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=1.004 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=1.004 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
