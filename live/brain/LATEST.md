# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T10:16:36.334236Z`  
Memory snapshots: **2477**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=4.027e+04 d1=0.0 d12=-65.0 z=151.76019374999998
- **ROBUST_OUTLIER** `margin` value=4.027e+04 d1=0.0 d12=-65.0 z=151.76019374999998
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.107e+04 d1=0.0 d12=0.0 z=-131.862746125
- **ROBUST_OUTLIER** `imbalance` value=3833 d1=0.0 d12=1403.0 z=23.988670805555557
- **ROBUST_OUTLIER** `ind_generation` value=2.49e+04 d1=0.0 d12=1403.0 z=22.656723874999997
- **CHANGE_POINT** `ps_gen` value=-125 d1=43.0 d12=45.0 z=15.51326425
- **PERSISTENT_UP** `ps_gen` value=-125 d1=43.0 d12=45.0 z=15.51326425
- **ACCELERATION** `ps_gen` value=-125 d1=43.0 d12=45.0 z=15.51326425
- **ROBUST_OUTLIER** `ps_gen` value=-125 d1=43.0 d12=45.0 z=15.51326425
- **ROBUST_OUTLIER** `ind_demand` value=-1.31e+04 d1=0.0 d12=-294.0 z=-6.556269010593221
- **ROBUST_OUTLIER** `biomass_gen` value=3047 d1=-1.0 d12=-5.0 z=3.5972786666666665
- **PERSISTENT_DOWN** `thermal_base` value=1.346e+04 d1=-38.0 d12=-980.0 z=-2.3650667950438824
- **PERSISTENT_DOWN** `ccgt_gen` value=9805 d1=-32.0 d12=-981.0 z=-2.353951888431877
- **REVERSAL** `interconnector_net` value=1.093e+04 d1=-27.0 d12=759.0 z=1.716883
- **REVERSAL** `wind_gen` value=3633 d1=-143.0 d12=86.0 z=0.9946589351265823

## Nearest historical live analogues

- `2026-09-22T09:21:25.127373Z` distance=0.334 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T09:51:38.826991Z` distance=0.561 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T09:55:50.935902Z` distance=0.561 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:00:02.533283Z` distance=0.561 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:04:15.522994Z` distance=0.561 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
