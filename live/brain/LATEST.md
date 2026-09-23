# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T03:45:06.650607Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.857e+04 d1=0.0 d12=-111.0 z=90.51652444999999
- **ROBUST_OUTLIER** `margin` value=3.857e+04 d1=0.0 d12=-111.0 z=90.51652444999999
- **CHANGE_POINT** `ind_demand` value=-1.242e+04 d1=0.0 d12=4.0 z=3.34546916
- **CHANGE_POINT** `interconnector_net` value=-3770 d1=0.0 d12=-3304.0 z=-3.0038598128393486
- **CHANGE_POINT** `wind_gen` value=6695 d1=0.0 d12=1298.0 z=1.4396352651911468
- **ROBUST_OUTLIER** `ind_demand` value=-1.242e+04 d1=0.0 d12=4.0 z=3.34546916
- **CHANGE_POINT** `ps_gen` value=144 d1=0.0 d12=4.0 z=-1.1241495833333335
- **ROBUST_OUTLIER** `interconnector_net` value=-3770 d1=0.0 d12=-3304.0 z=-3.0038598128393486
- **PERSISTENT_UP** `biomass_gen` value=2884 d1=0.0 d12=11.0 z=-2.646075173076923
- **ACCELERATION** `biomass_gen` value=2884 d1=0.0 d12=11.0 z=-2.646075173076923
- **PERSISTENT_DOWN** `nuclear_gen` value=3717 d1=0.0 d12=-16.0 z=-2.1583672
- **PERSISTENT_UP** `wind_gen` value=6695 d1=0.0 d12=1298.0 z=1.4396352651911468
- **PERSISTENT_DOWN** `thermal_base` value=1.285e+04 d1=0.0 d12=-301.0 z=-1.2885774328358208
- **PERSISTENT_DOWN** `ccgt_gen` value=9136 d1=0.0 d12=-285.0 z=-1.2881297258576874
- **PERSISTENT_UP** `ps_gen` value=144 d1=0.0 d12=4.0 z=-1.1241495833333335

## Nearest historical live analogues

- `2026-09-21T07:19:16.764355Z` distance=0.390 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:53:56.422040Z` distance=0.419 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:06:37.268181Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
