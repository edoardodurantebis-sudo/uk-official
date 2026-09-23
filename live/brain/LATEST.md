# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T04:18:43.553086Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.855e+04 d1=0.0 d12=-23.0 z=80.8161355
- **CHANGE_POINT** `imbalance` value=-8081 d1=0.0 d12=-89.0 z=-3.110147180555556
- **CHANGE_POINT** `ind_generation` value=1.309e+04 d1=0.0 d12=-89.0 z=-3.110147180555556
- **CHANGE_POINT** `wind_gen` value=8258 d1=223.0 d12=1944.0 z=2.260436514353042
- **CHANGE_POINT** `ccgt_gen` value=8567 d1=-151.0 d12=-714.0 z=-2.2339483209219857
- **CHANGE_POINT** `thermal_base` value=1.231e+04 d1=-140.0 d12=-701.0 z=-2.142387553030303
- **CHANGE_POINT** `interconnector_net` value=-4632 d1=31.0 d12=-2398.0 z=-1.862643989947728
- **REVERSAL** `biomass_gen` value=2868 d1=1.0 d12=-7.0 z=-3.37244875
- **ROBUST_OUTLIER** `biomass_gen` value=2868 d1=1.0 d12=-7.0 z=-3.37244875
- **CHANGE_POINT** `ps_gen` value=144 d1=0.0 d12=153.0 z=-1.1241495833333335
- **ROBUST_OUTLIER** `imbalance` value=-8081 d1=0.0 d12=-89.0 z=-3.110147180555556
- **ROBUST_OUTLIER** `ind_generation` value=1.309e+04 d1=0.0 d12=-89.0 z=-3.110147180555556
- **CHANGE_POINT** `ind_demand` value=-1.24e+04 d1=0.0 d12=11.0 z=0.7219890281690141
- **PERSISTENT_UP** `wind_gen` value=8258 d1=223.0 d12=1944.0 z=2.260436514353042
- **PERSISTENT_DOWN** `ccgt_gen` value=8567 d1=-151.0 d12=-714.0 z=-2.2339483209219857

## Nearest historical live analogues

- `2026-09-21T07:19:16.764355Z` distance=0.391 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:53:56.422040Z` distance=0.416 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.416 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.416 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:06:37.268181Z` distance=0.416 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
