# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T09:44:16.361628Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-5115 d1=0.0 d12=2250.0 z=15.88735100210084
- **CHANGE_POINT** `ind_demand` value=-1.268e+04 d1=0.0 d12=-22.0 z=-15.425287326086957
- **ROBUST_OUTLIER** `imbalance` value=-5115 d1=0.0 d12=2250.0 z=15.88735100210084
- **ROBUST_OUTLIER** `ind_demand` value=-1.268e+04 d1=0.0 d12=-22.0 z=-15.425287326086957
- **CHANGE_POINT** `ind_generation` value=1.591e+04 d1=0.0 d12=2250.0 z=12.810487466071429
- **ROBUST_OUTLIER** `ind_generation` value=1.591e+04 d1=0.0 d12=2250.0 z=12.810487466071429
- **CHANGE_POINT** `margin` value=4.072e+04 d1=0.0 d12=1065.0 z=8.541395596031746
- **ROBUST_OUTLIER** `margin` value=4.072e+04 d1=0.0 d12=1065.0 z=8.541395596031746
- **PERSISTENT_UP** `interconnector_net` value=1.135e+04 d1=34.0 d12=1425.0 z=5.443860570401519
- **ROBUST_OUTLIER** `interconnector_net` value=1.135e+04 d1=34.0 d12=1425.0 z=5.443860570401519
- **ROBUST_OUTLIER** `ccgt_gen` value=2767 d1=-82.0 d12=-1045.0 z=-4.849099524107142
- **CHANGE_POINT** `ps_gen` value=-461 d1=-236.0 d12=-444.0 z=-2.551330793478261
- **REVERSAL** `thermal_base` value=6566 d1=268.0 d12=-1046.0 z=-4.388596612186478
- **ROBUST_OUTLIER** `thermal_base` value=6566 d1=268.0 d12=-1046.0 z=-4.388596612186478
- **CHANGE_POINT** `wind_gen` value=1.02e+04 d1=-484.0 d12=-378.0 z=0.6468215287146764

## Nearest historical live analogues

- `2026-09-21T10:33:45.224867Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:37:58.343383Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:42:10.019375Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:46:20.592599Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:50:33.489846Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
