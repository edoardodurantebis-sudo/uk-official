# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T20:33:05.115461Z`  
Memory snapshots: **2283**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `nuclear_gen` value=3549 d1=2.0 d12=34.0 z=5.6657139
- **CHANGE_POINT** `imbalance` value=-2707 d1=0.0 d12=87.0 z=4.734154471698114
- **CHANGE_POINT** `ind_generation` value=1.875e+04 d1=0.0 d12=87.0 z=4.734154471698114
- **PERSISTENT_UP** `nuclear_gen` value=3549 d1=2.0 d12=34.0 z=5.6657139
- **ROBUST_OUTLIER** `nuclear_gen` value=3549 d1=2.0 d12=34.0 z=5.6657139
- **PERSISTENT_UP** `ind_demand` value=-1.226e+04 d1=0.0 d12=4.0 z=4.9462581666666665
- **ROBUST_OUTLIER** `ind_demand` value=-1.226e+04 d1=0.0 d12=4.0 z=4.9462581666666665
- **PERSISTENT_UP** `imbalance` value=-2707 d1=0.0 d12=87.0 z=4.734154471698114
- **ROBUST_OUTLIER** `imbalance` value=-2707 d1=0.0 d12=87.0 z=4.734154471698114
- **PERSISTENT_UP** `ind_generation` value=1.875e+04 d1=0.0 d12=87.0 z=4.734154471698114
- **ROBUST_OUTLIER** `ind_generation` value=1.875e+04 d1=0.0 d12=87.0 z=4.734154471698114
- **ACCELERATION** `biomass_gen` value=3014 d1=0.0 d12=-2.0 z=2.346051304347826
- **CHANGE_POINT** `ps_gen` value=253 d1=-67.0 d12=-273.0 z=-0.3163024737687366
- **PERSISTENT_DOWN** `interconnector_net` value=8086 d1=-705.0 d12=-1419.0 z=-0.6051855550110654
- **ACCELERATION** `interconnector_net` value=8086 d1=-705.0 d12=-1419.0 z=-0.6051855550110654

## Nearest historical live analogues

- `2026-09-21T19:33:55.455548Z` distance=0.005 → {'next30m_imbalance_delta': 15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -48.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:38:10.834672Z` distance=0.005 → {'next30m_imbalance_delta': 15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -48.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:25:28.829877Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1.0}
- `2026-09-21T19:29:43.204818Z` distance=0.005 → {'next30m_imbalance_delta': 15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -48.0, 'next30m_residual_proxy_delta': -1.0}
- `2026-09-21T19:21:16.242485Z` distance=0.027 → {'next30m_imbalance_delta': 290.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
