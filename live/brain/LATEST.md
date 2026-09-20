# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T07:51:58.332403Z`  
Memory snapshots: **1763**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=886 d1=-3.0 d12=-2.0 z=-7.7995542
- **CHANGE_POINT** `margin` value=3.803e+04 d1=0.0 d12=348.0 z=6.24209605
- **PERSISTENT_DOWN** `biomass_gen` value=886 d1=-3.0 d12=-2.0 z=-7.7995542
- **ACCELERATION** `biomass_gen` value=886 d1=-3.0 d12=-2.0 z=-7.7995542
- **ROBUST_OUTLIER** `biomass_gen` value=886 d1=-3.0 d12=-2.0 z=-7.7995542
- **ROBUST_OUTLIER** `margin` value=3.803e+04 d1=0.0 d12=348.0 z=6.24209605
- **PERSISTENT_UP** `residual_proxy` value=1.796e+04 d1=0.0 d12=1162.0 z=5.542546206521739
- **ACCELERATION** `residual_proxy` value=1.796e+04 d1=0.0 d12=1162.0 z=5.542546206521739
- **ROBUST_OUTLIER** `residual_proxy` value=1.796e+04 d1=0.0 d12=1162.0 z=5.542546206521739
- **CHANGE_POINT** `interconnector_net` value=-6754 d1=-1.0 d12=2259.0 z=2.772185144736842
- **CHANGE_POINT** `ps_gen` value=-930 d1=-3.0 d12=-129.0 z=-2.2189735253623186
- **REVERSAL** `interconnector_net` value=-6754 d1=-1.0 d12=2259.0 z=2.772185144736842
- **CHANGE_POINT** `imbalance` value=-6364 d1=0.0 d12=438.0 z=0.38711911707746477
- **CHANGE_POINT** `ind_generation` value=1.359e+04 d1=0.0 d12=438.0 z=0.38711911707746477
- **PERSISTENT_DOWN** `ps_gen` value=-930 d1=-3.0 d12=-129.0 z=-2.2189735253623186

## Nearest historical live analogues

- `2026-09-20T06:53:07.699769Z` distance=0.191 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T06:57:19.576758Z` distance=0.191 → {'next30m_imbalance_delta': 438.0, 'next30m_margin_delta': 348.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:32:50.061317Z` distance=0.233 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': -55.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:37:06.199540Z` distance=0.233 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': -55.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T05:41:17.937410Z` distance=0.233 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': -55.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
