# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T08:43:00.251145Z`  
Memory snapshots: **1147**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low, wind falling.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=3.0 z=-6.480144514018691
- **CHANGE_POINT** `wind_gen` value=1.226e+04 d1=1.0 d12=-140.0 z=-3.952432258637236
- **REVERSAL** `wind_gen` value=1.226e+04 d1=1.0 d12=-140.0 z=-3.952432258637236
- **ROBUST_OUTLIER** `wind_gen` value=1.226e+04 d1=1.0 d12=-140.0 z=-3.952432258637236
- **PERSISTENT_DOWN** `interconnector_net` value=2929 d1=0.0 d12=-504.0 z=3.3765328538449895
- **ROBUST_OUTLIER** `interconnector_net` value=2929 d1=0.0 d12=-504.0 z=3.3765328538449895
- **ROBUST_OUTLIER** `imbalance` value=9625 d1=0.0 d12=-593.0 z=-3.1701018249999997
- **CHANGE_POINT** `ps_gen` value=222 d1=2.0 d12=-376.0 z=-1.1179259178200691
- **CHANGE_POINT** `biomass_gen` value=2182 d1=18.0 d12=19.0 z=0.8164875921052632
- **PERSISTENT_UP** `residual_proxy` value=8755 d1=0.0 d12=658.0 z=2.679223173611111
- **CHANGE_POINT** `thermal_base` value=7335 d1=-4.0 d12=-322.0 z=-0.013835687179487178
- **CHANGE_POINT** `ccgt_gen` value=4000 d1=-5.0 d12=-323.0 z=-0.013339006233877902
- **PERSISTENT_DOWN** `wind_forecast` value=7699 d1=0.0 d12=-74.0 z=-1.3677153263888888
- **REVERSAL** `ps_gen` value=222 d1=2.0 d12=-376.0 z=-1.1179259178200691
- **ACCELERATION** `ps_gen` value=222 d1=2.0 d12=-376.0 z=-1.1179259178200691

## Nearest historical live analogues

- `2026-09-18T07:23:09.699179Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:27:20.707745Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:31:32.031758Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:35:44.221296Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:39:57.955920Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
