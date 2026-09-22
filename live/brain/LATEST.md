# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T07:48:27.653123Z`  
Memory snapshots: **2442**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.269e+04 d1=0.0 d12=-238.0 z=-5.855797375
- **ROBUST_OUTLIER** `ind_demand` value=-1.269e+04 d1=0.0 d12=-238.0 z=-5.855797375
- **CHANGE_POINT** `imbalance` value=-3831 d1=0.0 d12=-691.0 z=-2.050611694668008
- **CHANGE_POINT** `interconnector_net` value=7057 d1=-8.0 d12=6290.0 z=1.3782306043288326
- **CHANGE_POINT** `ind_generation` value=1.788e+04 d1=0.0 d12=-445.0 z=-1.3746614744488976
- **CHANGE_POINT** `ccgt_gen` value=1.374e+04 d1=-148.0 d12=-468.0 z=0.5125532474242898
- **CHANGE_POINT** `thermal_base` value=1.739e+04 d1=-148.0 d12=-468.0 z=0.5120028842534504
- **CHANGE_POINT** `ps_gen` value=-172 d1=0.0 d12=-117.0 z=0.07494330555555556
- **REVERSAL** `interconnector_net` value=7057 d1=-8.0 d12=6290.0 z=1.3782306043288326
- **ACCELERATION** `nuclear_gen` value=3649 d1=0.0 d12=0.0 z=-0.8993196666666666
- **PERSISTENT_DOWN** `residual_proxy` value=8391 d1=-228.0 d12=-228.0 z=-0.8954432887931034
- **ACCELERATION** `residual_proxy` value=8391 d1=-228.0 d12=-228.0 z=-0.8954432887931034
- **PERSISTENT_DOWN** `ccgt_gen` value=1.374e+04 d1=-148.0 d12=-468.0 z=0.5125532474242898
- **PERSISTENT_DOWN** `thermal_base` value=1.739e+04 d1=-148.0 d12=-468.0 z=0.5120028842534504
- **PERSISTENT_UP** `biomass_gen` value=3031 d1=2.0 d12=1.0 z=-0.07494330555555556

## Nearest historical live analogues

- `2026-09-22T04:54:50.378428Z` distance=0.205 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T04:59:01.331890Z` distance=0.205 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:03:14.010868Z` distance=0.205 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:07:26.495356Z` distance=0.205 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': -696.0}
- `2026-09-22T05:11:39.965439Z` distance=0.205 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': -696.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
