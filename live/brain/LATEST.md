# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T03:49:19.033601Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.857e+04 d1=0.0 d12=-111.0 z=90.51652444999999
- **ROBUST_OUTLIER** `margin` value=3.857e+04 d1=0.0 d12=-111.0 z=90.51652444999999
- **CHANGE_POINT** `interconnector_net` value=-3743 d1=27.0 d12=-3295.0 z=-2.992011541919515
- **CHANGE_POINT** `ind_demand` value=-1.242e+04 d1=0.0 d12=4.0 z=2.61364778125
- **CHANGE_POINT** `wind_gen` value=6966 d1=271.0 d12=1520.0 z=1.5997725765765767
- **REVERSAL** `biomass_gen` value=2876 d1=-8.0 d12=8.0 z=-3.476216403846154
- **ACCELERATION** `biomass_gen` value=2876 d1=-8.0 d12=8.0 z=-3.476216403846154
- **ROBUST_OUTLIER** `biomass_gen` value=2876 d1=-8.0 d12=8.0 z=-3.476216403846154
- **CHANGE_POINT** `ps_gen` value=144 d1=0.0 d12=4.0 z=-1.1241495833333335
- **REVERSAL** `interconnector_net` value=-3743 d1=27.0 d12=-3295.0 z=-2.992011541919515
- **REVERSAL** `nuclear_gen` value=3721 d1=4.0 d12=-4.0 z=-1.6187753999999999
- **ACCELERATION** `nuclear_gen` value=3721 d1=4.0 d12=-4.0 z=-1.6187753999999999
- **PERSISTENT_UP** `wind_gen` value=6966 d1=271.0 d12=1520.0 z=1.5997725765765767
- **REVERSAL** `ccgt_gen` value=9140 d1=4.0 d12=-254.0 z=-1.2249549363979848
- **REVERSAL** `thermal_base` value=1.286e+04 d1=8.0 d12=-258.0 z=-1.2247533284919654

## Nearest historical live analogues

- `2026-09-21T07:19:16.764355Z` distance=0.390 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:53:56.422040Z` distance=0.419 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:06:37.268181Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
