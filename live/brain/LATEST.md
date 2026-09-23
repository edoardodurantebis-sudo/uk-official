# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T03:36:43.352003Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `margin` value=3.857e+04 d1=0.0 d12=-91.0 z=90.51652444999999
- **ROBUST_OUTLIER** `margin` value=3.857e+04 d1=0.0 d12=-91.0 z=90.51652444999999
- **CHANGE_POINT** `ps_gen` value=129 d1=137.0 d12=-11.0 z=-7.869047083333334
- **REVERSAL** `ps_gen` value=129 d1=137.0 d12=-11.0 z=-7.869047083333334
- **ACCELERATION** `ps_gen` value=129 d1=137.0 d12=-11.0 z=-7.869047083333334
- **ROBUST_OUTLIER** `ps_gen` value=129 d1=137.0 d12=-11.0 z=-7.869047083333334
- **ROBUST_OUTLIER** `ind_demand` value=-1.242e+04 d1=0.0 d12=5.0 z=4.6464849444444445
- **CHANGE_POINT** `wind_gen` value=6461 d1=92.0 d12=1105.0 z=1.4966694969827585
- **PERSISTENT_UP** `biomass_gen` value=2880 d1=2.0 d12=9.0 z=-3.37244875
- **ROBUST_OUTLIER** `biomass_gen` value=2880 d1=2.0 d12=9.0 z=-3.37244875
- **REVERSAL** `interconnector_net` value=-3791 d1=8.0 d12=-3324.0 z=-2.898914380612864
- **ACCELERATION** `interconnector_net` value=-3791 d1=8.0 d12=-3324.0 z=-2.898914380612864
- **CHANGE_POINT** `imbalance` value=-7992 d1=0.0 d12=-15.0 z=0.3747165277777778
- **CHANGE_POINT** `ind_generation` value=1.318e+04 d1=0.0 d12=-15.0 z=0.3747165277777778
- **PERSISTENT_DOWN** `nuclear_gen` value=3721 d1=-7.0 d12=-6.0 z=-2.0234692499999998

## Nearest historical live analogues

- `2026-09-21T07:19:16.764355Z` distance=0.390 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:53:56.422040Z` distance=0.419 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:06:37.268181Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
