# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T05:29:41.115456Z`  
Memory snapshots: **2070**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `nuclear_gen` value=3449 d1=1.0 d12=66.0 z=21.10189360714286
- **ROBUST_OUTLIER** `nuclear_gen` value=3449 d1=1.0 d12=66.0 z=21.10189360714286
- **ROBUST_OUTLIER** `margin` value=3.753e+04 d1=0.0 d12=5.0 z=16.178254144366196
- **CHANGE_POINT** `imbalance` value=-4015 d1=0.0 d12=-33.0 z=7.547454924050633
- **CHANGE_POINT** `ind_generation` value=1.66e+04 d1=0.0 d12=-33.0 z=7.547454924050633
- **ROBUST_OUTLIER** `imbalance` value=-4015 d1=0.0 d12=-33.0 z=7.547454924050633
- **ROBUST_OUTLIER** `ind_generation` value=1.66e+04 d1=0.0 d12=-33.0 z=7.547454924050633
- **REVERSAL** `thermal_base` value=1.176e+04 d1=-70.0 d12=632.0 z=5.37307077724595
- **ROBUST_OUTLIER** `thermal_base` value=1.176e+04 d1=-70.0 d12=632.0 z=5.37307077724595
- **REVERSAL** `ccgt_gen` value=8310 d1=-71.0 d12=566.0 z=5.150919517279412
- **ROBUST_OUTLIER** `ccgt_gen` value=8310 d1=-71.0 d12=566.0 z=5.150919517279412
- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=4.0 z=4.777635729166667
- **PERSISTENT_UP** `interconnector_net` value=6131 d1=37.0 d12=1289.0 z=-1.921781366442001
- **PERSISTENT_DOWN** `wind_gen` value=3911 d1=-14.0 d12=-268.0 z=-0.47363389466840056
- **PERSISTENT_DOWN** `biomass_gen` value=3016 d1=-2.0 d12=-10.0 z=-0.22482991666666666

## Nearest historical live analogues

- `2026-09-21T04:21:09.590737Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T04:25:21.513242Z` distance=0.005 → {'next30m_imbalance_delta': -54.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T04:29:31.590182Z` distance=0.005 → {'next30m_imbalance_delta': -54.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T04:33:44.939265Z` distance=0.005 → {'next30m_imbalance_delta': -54.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T03:51:43.129687Z` distance=0.022 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
