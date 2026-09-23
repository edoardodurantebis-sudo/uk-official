# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T01:38:16.622812Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.244e+04 d1=0.0 d12=42.0 z=24.281631
- **ROBUST_OUTLIER** `ind_demand` value=-1.244e+04 d1=0.0 d12=42.0 z=24.281631
- **CHANGE_POINT** `wind_gen` value=4844 d1=-15.0 d12=579.0 z=2.5761299811165848
- **PERSISTENT_DOWN** `biomass_gen` value=2872 d1=-30.0 d12=-45.0 z=-4.271768416666666
- **ACCELERATION** `biomass_gen` value=2872 d1=-30.0 d12=-45.0 z=-4.271768416666666
- **ROBUST_OUTLIER** `biomass_gen` value=2872 d1=-30.0 d12=-45.0 z=-4.271768416666666
- **REVERSAL** `wind_gen` value=4844 d1=-15.0 d12=579.0 z=2.5761299811165848
- **REVERSAL** `interconnector_net` value=1631 d1=24.0 d12=-640.0 z=-2.340249833127775
- **ACCELERATION** `interconnector_net` value=1631 d1=24.0 d12=-640.0 z=-2.340249833127775
- **REVERSAL** `nuclear_gen` value=3725 d1=1.0 d12=-8.0 z=-1.60191315625
- **ACCELERATION** `nuclear_gen` value=3725 d1=1.0 d12=-8.0 z=-1.60191315625
- **PERSISTENT_DOWN** `ccgt_gen` value=9522 d1=-58.0 d12=-233.0 z=-0.7451042003610108
- **PERSISTENT_DOWN** `thermal_base` value=1.325e+04 d1=-57.0 d12=-241.0 z=-0.7450852680921052
- **PERSISTENT_UP** `ps_gen` value=148 d1=1.0 d12=1.0 z=0.22482991666666666
- **ACCELERATION** `ps_gen` value=148 d1=1.0 d12=1.0 z=0.22482991666666666

## Nearest historical live analogues

- `2026-09-23T00:21:31.120572Z` distance=0.048 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:25:43.305847Z` distance=0.048 → {'next30m_imbalance_delta': 9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:29:55.135999Z` distance=0.048 → {'next30m_imbalance_delta': 9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:34:05.411449Z` distance=0.048 → {'next30m_imbalance_delta': 9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:38:16.702070Z` distance=0.048 → {'next30m_imbalance_delta': 9.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
