# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T10:21:10.689748Z`  
Memory snapshots: **2139**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.173e+04 d1=0.0 d12=44.0 z=20.17007072754491
- **ROBUST_OUTLIER** `ind_generation` value=2.173e+04 d1=0.0 d12=44.0 z=20.17007072754491
- **CHANGE_POINT** `imbalance` value=569 d1=0.0 d12=154.0 z=6.093760755600815
- **REVERSAL** `biomass_gen` value=2950 d1=-1.0 d12=9.0 z=-6.359474785714285
- **ACCELERATION** `biomass_gen` value=2950 d1=-1.0 d12=9.0 z=-6.359474785714285
- **ROBUST_OUTLIER** `biomass_gen` value=2950 d1=-1.0 d12=9.0 z=-6.359474785714285
- **ROBUST_OUTLIER** `imbalance` value=569 d1=0.0 d12=154.0 z=6.093760755600815
- **CHANGE_POINT** `ccgt_gen` value=7048 d1=-70.0 d12=-814.0 z=-2.9687116230496455
- **CHANGE_POINT** `thermal_base` value=1.054e+04 d1=-72.0 d12=-819.0 z=-2.765135637281292
- **CHANGE_POINT** `margin` value=3.982e+04 d1=0.0 d12=140.0 z=1.8666111686046514
- **PERSISTENT_DOWN** `ccgt_gen` value=7048 d1=-70.0 d12=-814.0 z=-2.9687116230496455
- **PERSISTENT_DOWN** `thermal_base` value=1.054e+04 d1=-72.0 d12=-819.0 z=-2.765135637281292
- **CHANGE_POINT** `interconnector_net` value=1.081e+04 d1=25.0 d12=158.0 z=0.7517719014712438
- **CHANGE_POINT** `ind_demand` value=-1.281e+04 d1=0.0 d12=13.0 z=-0.6114079748201439
- **CHANGE_POINT** `ps_gen` value=-11 d1=0.0 d12=0.0 z=0.0

## Nearest historical live analogues

- `2026-09-21T09:22:16.225384Z` distance=0.065 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:26:26.475864Z` distance=0.065 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T08:31:05.309327Z` distance=0.708 → {'next30m_imbalance_delta': 271.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T08:35:54.594917Z` distance=0.708 → {'next30m_imbalance_delta': 271.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T08:40:08.617756Z` distance=0.708 → {'next30m_imbalance_delta': 271.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -29.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
