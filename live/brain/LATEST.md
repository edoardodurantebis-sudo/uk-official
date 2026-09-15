# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T08:07:49.028399Z`  
Memory snapshots: **151**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.228e+04 d1=0.0 d12=144.0 z=3.1074706339285716
- **CHANGE_POINT** `interconnector_net` value=7933 d1=914.0 d12=4850.0 z=3.041463949693918
- **CHANGE_POINT** `thermal_base` value=6320 d1=-1.0 d12=-423.0 z=-2.0216060186464087
- **CHANGE_POINT** `ccgt_gen` value=3001 d1=-1.0 d12=-422.0 z=-2.006653716066482
- **CHANGE_POINT** `wind_gen` value=1.269e+04 d1=75.0 d12=-424.0 z=-1.5305728942307693
- **PERSISTENT_DOWN** `biomass_gen` value=3161 d1=-68.0 d12=-70.0 z=-3.5223353611111112
- **ACCELERATION** `biomass_gen` value=3161 d1=-68.0 d12=-70.0 z=-3.5223353611111112
- **ROBUST_OUTLIER** `biomass_gen` value=3161 d1=-68.0 d12=-70.0 z=-3.5223353611111112
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=0.0 d12=144.0 z=3.1074706339285716
- **PERSISTENT_UP** `interconnector_net` value=7933 d1=914.0 d12=4850.0 z=3.041463949693918
- **ROBUST_OUTLIER** `interconnector_net` value=7933 d1=914.0 d12=4850.0 z=3.041463949693918
- **CHANGE_POINT** `ps_gen` value=-288 d1=-24.0 d12=-28.0 z=-0.09635567857142857
- **REVERSAL** `wind_gen` value=1.269e+04 d1=75.0 d12=-424.0 z=-1.5305728942307693
- **ACCELERATION** `nuclear_gen` value=3319 d1=0.0 d12=-1.0 z=-1.3489794999999998
- **PERSISTENT_DOWN** `ps_gen` value=-288 d1=-24.0 d12=-28.0 z=-0.09635567857142857

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=1.147 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=1.147 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=1.147 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=1.147 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=1.147 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
