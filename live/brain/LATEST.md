# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T08:16:09.812367Z`  
Memory snapshots: **153**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2901 d1=-135.0 d12=-340.0 z=-23.007594805555556
- **PERSISTENT_DOWN** `biomass_gen` value=2901 d1=-135.0 d12=-340.0 z=-23.007594805555556
- **ROBUST_OUTLIER** `biomass_gen` value=2901 d1=-135.0 d12=-340.0 z=-23.007594805555556
- **CHANGE_POINT** `ind_demand` value=-1.228e+04 d1=0.0 d12=0.0 z=3.1074706339285716
- **CHANGE_POINT** `thermal_base` value=6318 d1=8.0 d12=-451.0 z=-1.6346457470588236
- **CHANGE_POINT** `ccgt_gen` value=3005 d1=6.0 d12=-443.0 z=-1.5981439488235294
- **CHANGE_POINT** `wind_gen` value=1.275e+04 d1=33.0 d12=264.0 z=-1.400863326923077
- **REVERSAL** `interconnector_net` value=8298 d1=-26.0 d12=5239.0 z=3.1386948970675355
- **ROBUST_OUTLIER** `interconnector_net` value=8298 d1=-26.0 d12=5239.0 z=3.1386948970675355
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=0.0 d12=0.0 z=3.1074706339285716
- **CHANGE_POINT** `ps_gen` value=-546 d1=-6.0 d12=-288.0 z=-1.0390788040540542
- **REVERSAL** `nuclear_gen` value=3313 d1=2.0 d12=-8.0 z=-2.6979589999999996
- **ACCELERATION** `nuclear_gen` value=3313 d1=2.0 d12=-8.0 z=-2.6979589999999996
- **REVERSAL** `thermal_base` value=6318 d1=8.0 d12=-451.0 z=-1.6346457470588236
- **REVERSAL** `ccgt_gen` value=3005 d1=6.0 d12=-443.0 z=-1.5981439488235294

## Nearest historical live analogues

- `2026-09-15T07:21:37.326101Z` distance=0.140 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}
- `2026-09-15T03:31:03.539054Z` distance=1.277 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=1.277 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=1.277 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=1.277 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
