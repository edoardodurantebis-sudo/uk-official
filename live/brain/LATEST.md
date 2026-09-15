# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T07:25:46.773269Z`  
Memory snapshots: **141**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3241 d1=1.0 d12=48.0 z=3.035203875
- **CHANGE_POINT** `wind_gen` value=1.249e+04 d1=-310.0 d12=-1069.0 z=-1.971585423076923
- **CHANGE_POINT** `interconnector_net` value=3059 d1=-1.0 d12=3693.0 z=1.7430978195596367
- **PERSISTENT_UP** `ind_demand` value=-1.228e+04 d1=0.0 d12=155.0 z=3.1074706339285716
- **ACCELERATION** `ind_demand` value=-1.228e+04 d1=0.0 d12=155.0 z=3.1074706339285716
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=0.0 d12=155.0 z=3.1074706339285716
- **PERSISTENT_UP** `biomass_gen` value=3241 d1=1.0 d12=48.0 z=3.035203875
- **ROBUST_OUTLIER** `biomass_gen` value=3241 d1=1.0 d12=48.0 z=3.035203875
- **CHANGE_POINT** `margin` value=3.413e+04 d1=0.0 d12=231.0 z=0.9323828897058823
- **CHANGE_POINT** `thermal_base` value=6769 d1=-19.0 d12=-460.0 z=-0.564056919395466
- **CHANGE_POINT** `ccgt_gen` value=3448 d1=-20.0 d12=-456.0 z=-0.5452964396766169
- **CHANGE_POINT** `ind_generation` value=2.003e+04 d1=0.0 d12=136.0 z=-0.24274695372750643
- **CHANGE_POINT** `imbalance` value=-454 d1=0.0 d12=136.0 z=-0.24163421456185566
- **PERSISTENT_DOWN** `wind_gen` value=1.249e+04 d1=-310.0 d12=-1069.0 z=-1.971585423076923
- **REVERSAL** `interconnector_net` value=3059 d1=-1.0 d12=3693.0 z=1.7430978195596367

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=0.873 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=0.873 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=0.873 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=0.873 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=0.873 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
