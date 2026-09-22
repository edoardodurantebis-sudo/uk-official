# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T22:15:16.656566Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.509e+04 d1=0.0 d12=-2495.0 z=-7.216746642960813
- **CHANGE_POINT** `ccgt_gen` value=1.136e+04 d1=0.0 d12=-2499.0 z=-7.1725278890489905
- **PERSISTENT_DOWN** `thermal_base` value=1.509e+04 d1=0.0 d12=-2495.0 z=-7.216746642960813
- **ROBUST_OUTLIER** `thermal_base` value=1.509e+04 d1=0.0 d12=-2495.0 z=-7.216746642960813
- **PERSISTENT_DOWN** `ccgt_gen` value=1.136e+04 d1=0.0 d12=-2499.0 z=-7.1725278890489905
- **ROBUST_OUTLIER** `ccgt_gen` value=1.136e+04 d1=0.0 d12=-2499.0 z=-7.1725278890489905
- **CHANGE_POINT** `ps_gen` value=144 d1=0.0 d12=1.0 z=-2.4487407533898304
- **CHANGE_POINT** `interconnector_net` value=5171 d1=0.0 d12=-510.0 z=-2.1608226803185437
- **CHANGE_POINT** `wind_gen` value=2518 d1=0.0 d12=217.0 z=1.5800093708272858
- **CHANGE_POINT** `imbalance` value=-8054 d1=0.0 d12=-35.0 z=-1.1562681428571429
- **CHANGE_POINT** `ind_generation` value=1.312e+04 d1=0.0 d12=-35.0 z=-0.94428565
- **PERSISTENT_UP** `ps_gen` value=144 d1=0.0 d12=1.0 z=-2.4487407533898304
- **ACCELERATION** `ps_gen` value=144 d1=0.0 d12=1.0 z=-2.4487407533898304
- **CHANGE_POINT** `biomass_gen` value=2911 d1=0.0 d12=-6.0 z=0.202346925
- **PERSISTENT_UP** `wind_gen` value=2518 d1=0.0 d12=217.0 z=1.5800093708272858

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.001 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:55:13.117327Z` distance=0.002 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:59:27.826421Z` distance=0.002 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:03:40.476515Z` distance=0.002 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:07:51.999414Z` distance=0.002 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
