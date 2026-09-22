# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T21:16:16.302467Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-8041 d1=0.0 d12=-3.0 z=-3.62538240625
- **CHANGE_POINT** `ind_generation` value=1.313e+04 d1=0.0 d12=-3.0 z=-2.63215512195122
- **CHANGE_POINT** `thermal_base` value=1.779e+04 d1=-303.0 d12=-980.0 z=-1.9304699375907113
- **CHANGE_POINT** `ccgt_gen` value=1.406e+04 d1=-302.0 d12=-976.0 z=-1.9146178782420749
- **CHANGE_POINT** `margin` value=3.721e+04 d1=0.0 d12=78.0 z=1.6862243749999999
- **ROBUST_OUTLIER** `imbalance` value=-8041 d1=0.0 d12=-3.0 z=-3.62538240625
- **CHANGE_POINT** `biomass_gen` value=2918 d1=-2.0 d12=74.0 z=0.4562724779411765
- **REVERSAL** `ps_gen` value=144 d1=1.0 d12=-233.0 z=-2.4487407533898304
- **PERSISTENT_DOWN** `thermal_base` value=1.779e+04 d1=-303.0 d12=-980.0 z=-1.9304699375907113
- **PERSISTENT_DOWN** `ccgt_gen` value=1.406e+04 d1=-302.0 d12=-976.0 z=-1.9146178782420749
- **PERSISTENT_UP** `wind_gen` value=2308 d1=0.0 d12=250.0 z=1.6996629753320684
- **PERSISTENT_DOWN** `interconnector_net` value=5681 d1=-3.0 d12=-1049.0 z=-1.2337223151700085
- **REVERSAL** `biomass_gen` value=2918 d1=-2.0 d12=74.0 z=0.4562724779411765
- **PERSISTENT_DOWN** `nuclear_gen` value=3731 d1=-1.0 d12=-4.0 z=0.337244875
- **ACCELERATION** `nuclear_gen` value=3731 d1=-1.0 d12=-4.0 z=0.337244875

## Nearest historical live analogues

- `2026-09-22T17:22:55.061007Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:27:09.876357Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:31:30.036637Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:35:44.591045Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:39:59.899041Z` distance=0.021 → {'next30m_imbalance_delta': -2.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
