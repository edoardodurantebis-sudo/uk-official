# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T21:41:32.861170Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.703e+04 d1=-185.0 d12=-1392.0 z=-3.4282483374455732
- **CHANGE_POINT** `ccgt_gen` value=1.329e+04 d1=-189.0 d12=-1401.0 z=-3.4190993378962533
- **CHANGE_POINT** `interconnector_net` value=4760 d1=1.0 d12=-1890.0 z=-2.5545794423652692
- **CHANGE_POINT** `imbalance` value=-8019 d1=0.0 d12=19.0 z=-1.8628764523809522
- **CHANGE_POINT** `ind_generation` value=1.315e+04 d1=0.0 d12=19.0 z=-1.8628764523809522
- **CHANGE_POINT** `margin` value=3.721e+04 d1=0.0 d12=0.0 z=1.42991827
- **PERSISTENT_DOWN** `thermal_base` value=1.703e+04 d1=-185.0 d12=-1392.0 z=-3.4282483374455732
- **ROBUST_OUTLIER** `thermal_base` value=1.703e+04 d1=-185.0 d12=-1392.0 z=-3.4282483374455732
- **PERSISTENT_DOWN** `ccgt_gen` value=1.329e+04 d1=-189.0 d12=-1401.0 z=-3.4190993378962533
- **ROBUST_OUTLIER** `ccgt_gen` value=1.329e+04 d1=-189.0 d12=-1401.0 z=-3.4190993378962533
- **PERSISTENT_UP** `nuclear_gen` value=3740 d1=4.0 d12=9.0 z=3.37244875
- **ROBUST_OUTLIER** `nuclear_gen` value=3740 d1=4.0 d12=9.0 z=3.37244875
- **REVERSAL** `interconnector_net` value=4760 d1=1.0 d12=-1890.0 z=-2.5545794423652692
- **CHANGE_POINT** `biomass_gen` value=2913 d1=-1.0 d12=-1.0 z=0.28285054032258067
- **PERSISTENT_UP** `wind_gen` value=2456 d1=28.0 d12=134.0 z=2.006174641025641

## Nearest historical live analogues

- `2026-09-22T17:22:55.061007Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:27:09.876357Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:31:30.036637Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:35:44.591045Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:39:59.899041Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
