# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T03:32:33.216215Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.857e+04 d1=0.0 d12=-91.0 z=90.51652444999999
- **CHANGE_POINT** `ps_gen` value=-8 d1=1.0 d12=-148.0 z=-69.47244425
- **REVERSAL** `ps_gen` value=-8 d1=1.0 d12=-148.0 z=-69.47244425
- **ROBUST_OUTLIER** `ps_gen` value=-8 d1=1.0 d12=-148.0 z=-69.47244425
- **PERSISTENT_UP** `ind_demand` value=-1.242e+04 d1=0.0 d12=5.0 z=4.6464849444444445
- **ROBUST_OUTLIER** `ind_demand` value=-1.242e+04 d1=0.0 d12=5.0 z=4.6464849444444445
- **REVERSAL** `biomass_gen` value=2878 d1=3.0 d12=-1.0 z=-3.5972786666666665
- **ACCELERATION** `biomass_gen` value=2878 d1=3.0 d12=-1.0 z=-3.5972786666666665
- **ROBUST_OUTLIER** `biomass_gen` value=2878 d1=3.0 d12=-1.0 z=-3.5972786666666665
- **CHANGE_POINT** `wind_gen` value=6369 d1=55.0 d12=1033.0 z=1.5069841442095995
- **PERSISTENT_DOWN** `interconnector_net` value=-3799 d1=-1565.0 d12=-3314.0 z=-2.9770032228132384
- **ACCELERATION** `interconnector_net` value=-3799 d1=-1565.0 d12=-3314.0 z=-2.9770032228132384
- **PERSISTENT_UP** `wind_gen` value=6369 d1=55.0 d12=1033.0 z=1.5069841442095995
- **PERSISTENT_DOWN** `ccgt_gen` value=9208 d1=-73.0 d12=-189.0 z=-1.0921349673678533
- **ACCELERATION** `ccgt_gen` value=9208 d1=-73.0 d12=-189.0 z=-1.0921349673678533

## Nearest historical live analogues

- `2026-09-21T07:19:16.764355Z` distance=0.390 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:53:56.422040Z` distance=0.419 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:06:37.268181Z` distance=0.419 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
