# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T03:47:21.677814Z`  
Memory snapshots: **735**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2459 d1=151.0 d12=424.0 z=-59.07736692647059
- **PERSISTENT_UP** `biomass_gen` value=2459 d1=151.0 d12=424.0 z=-59.07736692647059
- **ROBUST_OUTLIER** `biomass_gen` value=2459 d1=151.0 d12=424.0 z=-59.07736692647059
- **ROBUST_OUTLIER** `ind_demand` value=-1.152e+04 d1=0.0 d12=0.0 z=33.31979365
- **CHANGE_POINT** `interconnector_net` value=-9820 d1=0.0 d12=-3304.0 z=-10.748372460023866
- **CHANGE_POINT** `margin` value=3.585e+04 d1=0.0 d12=-10.0 z=9.156709333333334
- **ROBUST_OUTLIER** `interconnector_net` value=-9820 d1=0.0 d12=-3304.0 z=-10.748372460023866
- **ROBUST_OUTLIER** `margin` value=3.585e+04 d1=0.0 d12=-10.0 z=9.156709333333334
- **CHANGE_POINT** `ind_generation` value=2.565e+04 d1=0.0 d12=14.0 z=0.3709693625
- **CHANGE_POINT** `ps_gen` value=-300 d1=131.0 d12=245.0 z=-0.11709891493055556
- **CHANGE_POINT** `imbalance` value=6527 d1=0.0 d12=14.0 z=0.04087816666666667
- **PERSISTENT_DOWN** `ccgt_gen` value=3404 d1=-114.0 d12=-45.0 z=-0.9135269283833596
- **PERSISTENT_DOWN** `thermal_base` value=6719 d1=-114.0 d12=-42.0 z=-0.9107556928421604
- **PERSISTENT_UP** `wind_gen` value=1.386e+04 d1=124.0 d12=479.0 z=0.891173128113879
- **PERSISTENT_UP** `nuclear_gen` value=3315 d1=0.0 d12=3.0 z=0.8093876999999999

## Nearest historical live analogues

- `2026-09-17T02:52:02.690108Z` distance=0.591 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:22:41.615797Z` distance=0.591 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:26:53.112988Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:31:05.012181Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:35:17.375315Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
