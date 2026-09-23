# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T00:00:29.286244Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.374e+04 d1=6.0 d12=-141.0 z=-6.836873375
- **CHANGE_POINT** `ccgt_gen` value=1e+04 d1=1.0 d12=-138.0 z=-6.680173736111111
- **REVERSAL** `thermal_base` value=1.374e+04 d1=6.0 d12=-141.0 z=-6.836873375
- **ROBUST_OUTLIER** `thermal_base` value=1.374e+04 d1=6.0 d12=-141.0 z=-6.836873375
- **REVERSAL** `ccgt_gen` value=1e+04 d1=1.0 d12=-138.0 z=-6.680173736111111
- **ROBUST_OUTLIER** `ccgt_gen` value=1e+04 d1=1.0 d12=-138.0 z=-6.680173736111111
- **ROBUST_OUTLIER** `ind_demand` value=-1.249e+04 d1=0.0 d12=7.0 z=-5.395918
- **CHANGE_POINT** `interconnector_net` value=3957 d1=-243.0 d12=-766.0 z=-1.560677502406932
- **CHANGE_POINT** `imbalance` value=-7998 d1=0.0 d12=58.0 z=1.5076829705882353
- **CHANGE_POINT** `ind_generation` value=1.318e+04 d1=0.0 d12=58.0 z=1.5076829705882353
- **PERSISTENT_UP** `wind_gen` value=3800 d1=69.0 d12=755.0 z=2.5734016594076654
- **PERSISTENT_DOWN** `interconnector_net` value=3957 d1=-243.0 d12=-766.0 z=-1.560677502406932
- **PERSISTENT_UP** `imbalance` value=-7998 d1=0.0 d12=58.0 z=1.5076829705882353
- **PERSISTENT_UP** `ind_generation` value=1.318e+04 d1=0.0 d12=58.0 z=1.5076829705882353
- **PERSISTENT_DOWN** `margin` value=3.722e+04 d1=0.0 d12=-10.0 z=0.8530311544117647

## Nearest historical live analogues

- `2026-09-22T22:53:13.778957Z` distance=0.184 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:57:26.907882Z` distance=0.184 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:01:39.891099Z` distance=0.184 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:05:56.234014Z` distance=0.184 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -158.0}
- `2026-09-22T20:50:58.019212Z` distance=0.184 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
