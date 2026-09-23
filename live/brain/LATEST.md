# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T01:50:51.998161Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.244e+04 d1=0.0 d12=-6.0 z=12.1408155
- **ROBUST_OUTLIER** `ind_demand` value=-1.244e+04 d1=0.0 d12=-6.0 z=12.1408155
- **CHANGE_POINT** `biomass_gen` value=2859 d1=-1.0 d12=-57.0 z=-5.7331628750000005
- **PERSISTENT_DOWN** `biomass_gen` value=2859 d1=-1.0 d12=-57.0 z=-5.7331628750000005
- **ROBUST_OUTLIER** `biomass_gen` value=2859 d1=-1.0 d12=-57.0 z=-5.7331628750000005
- **PERSISTENT_UP** `wind_gen` value=4932 d1=42.0 d12=540.0 z=2.641704642201835
- **PERSISTENT_DOWN** `nuclear_gen` value=3725 d1=-5.0 d12=-1.0 z=-1.60191315625
- **ACCELERATION** `nuclear_gen` value=3725 d1=-5.0 d12=-1.0 z=-1.60191315625
- **REVERSAL** `thermal_base` value=1.322e+04 d1=32.0 d12=-203.0 z=-0.7577406972519795
- **REVERSAL** `ccgt_gen` value=9494 d1=37.0 d12=-202.0 z=-0.7567290484404536
- **ACCELERATION** `ccgt_gen` value=9494 d1=37.0 d12=-202.0 z=-0.7567290484404536
- **PERSISTENT_DOWN** `margin` value=3.722e+04 d1=-20.0 d12=-20.0 z=-0.2697959
- **ACCELERATION** `margin` value=3.722e+04 d1=-20.0 d12=-20.0 z=-0.2697959
- **PERSISTENT_DOWN** `ps_gen` value=147 d1=-1.0 d12=0.0 z=0.0
- **ACCELERATION** `ps_gen` value=147 d1=-1.0 d12=0.0 z=0.0

## Nearest historical live analogues

- `2026-09-23T00:50:49.821360Z` distance=0.013 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:55:39.096200Z` distance=0.013 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:21:31.120572Z` distance=0.049 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:25:43.305847Z` distance=0.049 → {'next30m_imbalance_delta': 9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:29:55.135999Z` distance=0.049 → {'next30m_imbalance_delta': 9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
