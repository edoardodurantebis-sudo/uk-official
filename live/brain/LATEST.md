# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T08:35:02.510891Z`  
Memory snapshots: **2453**  
Current physical regime: **LOOSE**

Regime read: margin high, wind rising.

## Active patterns

- **CHANGE_POINT** `margin` value=3.9e+04 d1=0.0 d12=1221.0 z=74.1938725
- **ROBUST_OUTLIER** `margin` value=3.9e+04 d1=0.0 d12=1221.0 z=74.1938725
- **ROBUST_OUTLIER** `ind_demand` value=-1.28e+04 d1=0.0 d12=-110.0 z=-8.739041108695652
- **CHANGE_POINT** `imbalance` value=-1355 d1=0.0 d12=2476.0 z=6.315676750000001
- **CHANGE_POINT** `ind_generation` value=1.971e+04 d1=0.0 d12=1837.0 z=4.983729819444444
- **ROBUST_OUTLIER** `imbalance` value=-1355 d1=0.0 d12=2476.0 z=6.315676750000001
- **CHANGE_POINT** `biomass_gen` value=3047 d1=-1.0 d12=18.0 z=3.5972786666666665
- **ROBUST_OUTLIER** `ind_generation` value=1.971e+04 d1=0.0 d12=1837.0 z=4.983729819444444
- **REVERSAL** `biomass_gen` value=3047 d1=-1.0 d12=18.0 z=3.5972786666666665
- **ROBUST_OUTLIER** `biomass_gen` value=3047 d1=-1.0 d12=18.0 z=3.5972786666666665
- **CHANGE_POINT** `wind_gen` value=3761 d1=50.0 d12=289.0 z=1.3695074489130434
- **CHANGE_POINT** `ccgt_gen` value=1.24e+04 d1=10.0 d12=-1494.0 z=-0.5511662921348315
- **CHANGE_POINT** `thermal_base` value=1.605e+04 d1=10.0 d12=-1489.0 z=-0.5510401945296524
- **CHANGE_POINT** `ps_gen` value=-170 d1=-1.0 d12=2.0 z=0.2697959
- **PERSISTENT_UP** `interconnector_net` value=9411 d1=1095.0 d12=2346.0 z=1.8826782203733123

## Nearest historical live analogues

- `2026-09-21T09:47:25.921035Z` distance=0.527 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T09:22:16.225384Z` distance=0.529 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:26:26.475864Z` distance=0.529 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:30:39.158321Z` distance=0.529 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:34:50.037660Z` distance=0.529 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
