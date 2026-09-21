# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T10:42:10.019375Z`  
Memory snapshots: **2144**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.473e+04 d1=0.0 d12=2999.0 z=32.28261420209581
- **ROBUST_OUTLIER** `ind_generation` value=2.473e+04 d1=0.0 d12=2999.0 z=32.28261420209581
- **CHANGE_POINT** `imbalance` value=3568 d1=0.0 d12=2999.0 z=10.213505684826883
- **ROBUST_OUTLIER** `imbalance` value=3568 d1=0.0 d12=2999.0 z=10.213505684826883
- **CHANGE_POINT** `margin` value=4.101e+04 d1=0.0 d12=1193.0 z=2.990202596546311
- **PERSISTENT_DOWN** `ccgt_gen` value=6958 d1=0.0 d12=-500.0 z=-3.1409217719858153
- **ROBUST_OUTLIER** `ccgt_gen` value=6958 d1=0.0 d12=-500.0 z=-3.1409217719858153
- **PERSISTENT_DOWN** `thermal_base` value=1.045e+04 d1=0.0 d12=-499.0 z=-2.9267226837146705
- **CHANGE_POINT** `interconnector_net` value=1.099e+04 d1=0.0 d12=354.0 z=0.8603491477777777
- **PERSISTENT_UP** `biomass_gen` value=3002 d1=0.0 d12=54.0 z=-1.0315725588235294
- **PERSISTENT_UP** `wind_gen` value=3410 d1=0.0 d12=109.0 z=-0.9353585797794118
- **PERSISTENT_UP** `interconnector_net` value=1.099e+04 d1=0.0 d12=354.0 z=0.8603491477777777
- **PERSISTENT_UP** `residual_proxy` value=1.108e+04 d1=0.0 d12=354.0 z=-0.33375372722567287
- **PERSISTENT_DOWN** `wind_forecast` value=8923 d1=0.0 d12=-354.0 z=0.18014322515527953
- **PERSISTENT_UP** `nuclear_gen` value=3495 d1=0.0 d12=1.0 z=0.16862243749999997

## Nearest historical live analogues

- `2026-09-21T09:22:16.225384Z` distance=0.603 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:26:26.475864Z` distance=0.603 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:30:39.158321Z` distance=0.603 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:34:50.037660Z` distance=0.603 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:39:02.425016Z` distance=0.603 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
