# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T03:08:52.962663Z`  
Memory snapshots: **1696**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.761e+04 d1=0.0 d12=1589.0 z=29.77390467857143
- **ROBUST_OUTLIER** `margin` value=3.761e+04 d1=0.0 d12=1589.0 z=29.77390467857143
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=0.0 d12=-81.0 z=-18.78935732142857
- **REVERSAL** `biomass_gen` value=1216 d1=9.0 d12=-13.0 z=6.244139958333333
- **ROBUST_OUTLIER** `biomass_gen` value=1216 d1=9.0 d12=-13.0 z=6.244139958333333
- **CHANGE_POINT** `interconnector_net` value=-1.139e+04 d1=-146.0 d12=-842.0 z=-1.4190471655299055
- **CHANGE_POINT** `imbalance` value=-3749 d1=0.0 d12=8.0 z=0.6560105787671233
- **CHANGE_POINT** `ind_generation` value=1.62e+04 d1=0.0 d12=8.0 z=0.6560105787671233
- **CHANGE_POINT** `thermal_base` value=6998 d1=31.0 d12=-636.0 z=-0.5033368257162346
- **CHANGE_POINT** `ccgt_gen` value=3669 d1=32.0 d12=-637.0 z=-0.4975219308474576
- **PERSISTENT_DOWN** `interconnector_net` value=-1.139e+04 d1=-146.0 d12=-842.0 z=-1.4190471655299055
- **REVERSAL** `nuclear_gen` value=3329 d1=-1.0 d12=1.0 z=-1.1241495833333335
- **ACCELERATION** `nuclear_gen` value=3329 d1=-1.0 d12=1.0 z=-1.1241495833333335
- **PERSISTENT_UP** `ps_gen` value=-693 d1=0.0 d12=5.0 z=-1.0249003408408408
- **REVERSAL** `thermal_base` value=6998 d1=31.0 d12=-636.0 z=-0.5033368257162346

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.375 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.375 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.375 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.375 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.375 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
