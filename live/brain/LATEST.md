# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T08:47:40.265673Z`  
Memory snapshots: **2456**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.9e+04 d1=0.0 d12=1221.0 z=74.1938725
- **ROBUST_OUTLIER** `ind_demand` value=-1.28e+04 d1=0.0 d12=-110.0 z=-8.739041108695652
- **ROBUST_OUTLIER** `imbalance` value=-1355 d1=0.0 d12=2476.0 z=6.315676750000001
- **CHANGE_POINT** `biomass_gen` value=3050 d1=-1.0 d12=19.0 z=4.271768416666666
- **ROBUST_OUTLIER** `ind_generation` value=1.971e+04 d1=0.0 d12=1837.0 z=4.983729819444444
- **REVERSAL** `biomass_gen` value=3050 d1=-1.0 d12=19.0 z=4.271768416666666
- **ROBUST_OUTLIER** `biomass_gen` value=3050 d1=-1.0 d12=19.0 z=4.271768416666666
- **CHANGE_POINT** `thermal_base` value=1.548e+04 d1=-189.0 d12=-1665.0 z=-0.9541052736189984
- **CHANGE_POINT** `ccgt_gen` value=1.183e+04 d1=-186.0 d12=-1673.0 z=-0.9487938077120823
- **CHANGE_POINT** `wind_gen` value=3660 d1=-55.0 d12=167.0 z=0.7178304568273092
- **CHANGE_POINT** `ps_gen` value=-169 d1=1.0 d12=1.0 z=0.6744897499999999
- **CHANGE_POINT** `nuclear_gen` value=3651 d1=-3.0 d12=8.0 z=-0.4496598333333333
- **REVERSAL** `interconnector_net` value=9444 d1=-1.0 d12=2393.0 z=1.8897499159253377
- **PERSISTENT_DOWN** `thermal_base` value=1.548e+04 d1=-189.0 d12=-1665.0 z=-0.9541052736189984
- **PERSISTENT_DOWN** `ccgt_gen` value=1.183e+04 d1=-186.0 d12=-1673.0 z=-0.9487938077120823

## Nearest historical live analogues

- `2026-09-21T09:47:25.921035Z` distance=0.527 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T09:22:16.225384Z` distance=0.529 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:26:26.475864Z` distance=0.529 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:30:39.158321Z` distance=0.529 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:34:50.037660Z` distance=0.529 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
