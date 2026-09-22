# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T07:44:14.922697Z`  
Memory snapshots: **2441**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.269e+04 d1=0.0 d12=-238.0 z=-7.531802208333334
- **ROBUST_OUTLIER** `ind_demand` value=-1.269e+04 d1=0.0 d12=-238.0 z=-7.531802208333334
- **CHANGE_POINT** `imbalance` value=-3831 d1=0.0 d12=-691.0 z=-1.7957194642857142
- **CHANGE_POINT** `interconnector_net` value=7065 d1=-26.0 d12=6451.0 z=1.379944954765687
- **CHANGE_POINT** `ind_generation` value=1.788e+04 d1=0.0 d12=-445.0 z=-1.2526238214285714
- **CHANGE_POINT** `thermal_base` value=1.754e+04 d1=-144.0 d12=-309.0 z=0.6161081070862396
- **CHANGE_POINT** `ccgt_gen` value=1.389e+04 d1=-150.0 d12=-310.0 z=0.6152828821439849
- **CHANGE_POINT** `ps_gen` value=-172 d1=1.0 d12=-118.0 z=0.07099892105263157
- **REVERSAL** `interconnector_net` value=7065 d1=-26.0 d12=6451.0 z=1.379944954765687
- **PERSISTENT_UP** `nuclear_gen` value=3649 d1=6.0 d12=1.0 z=-0.8993196666666666
- **ACCELERATION** `nuclear_gen` value=3649 d1=6.0 d12=1.0 z=-0.8993196666666666
- **PERSISTENT_DOWN** `thermal_base` value=1.754e+04 d1=-144.0 d12=-309.0 z=0.6161081070862396
- **PERSISTENT_DOWN** `ccgt_gen` value=1.389e+04 d1=-150.0 d12=-310.0 z=0.6152828821439849
- **PERSISTENT_UP** `biomass_gen` value=3029 d1=1.0 d12=2.0 z=-0.3113029615384615
- **ACCELERATION** `biomass_gen` value=3029 d1=1.0 d12=2.0 z=-0.3113029615384615

## Nearest historical live analogues

- `2026-09-22T04:54:50.378428Z` distance=0.201 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T04:59:01.331890Z` distance=0.201 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:03:14.010868Z` distance=0.201 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:07:26.495356Z` distance=0.201 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': -696.0}
- `2026-09-22T05:11:39.965439Z` distance=0.201 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -18.0, 'next30m_residual_proxy_delta': -696.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
