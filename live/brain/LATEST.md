# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T04:59:01.331890Z`  
Memory snapshots: **2402**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.779e+04 d1=0.0 d12=-5.0 z=16.4617654609375
- **CHANGE_POINT** `ccgt_gen` value=1.338e+04 d1=122.0 d12=1711.0 z=5.7788454477091635
- **CHANGE_POINT** `thermal_base` value=1.702e+04 d1=123.0 d12=1713.0 z=5.634745109922179
- **REVERSAL** `interconnector_net` value=-4550 d1=52.0 d12=-1757.0 z=-7.274119720740997
- **ROBUST_OUTLIER** `interconnector_net` value=-4550 d1=52.0 d12=-1757.0 z=-7.274119720740997
- **PERSISTENT_UP** `ccgt_gen` value=1.338e+04 d1=122.0 d12=1711.0 z=5.7788454477091635
- **ROBUST_OUTLIER** `ccgt_gen` value=1.338e+04 d1=122.0 d12=1711.0 z=5.7788454477091635
- **PERSISTENT_UP** `thermal_base` value=1.702e+04 d1=123.0 d12=1713.0 z=5.634745109922179
- **ROBUST_OUTLIER** `thermal_base` value=1.702e+04 d1=123.0 d12=1713.0 z=5.634745109922179
- **CHANGE_POINT** `imbalance` value=-3312 d1=0.0 d12=-76.0 z=-2.8406395240384614
- **CHANGE_POINT** `ind_generation` value=1.815e+04 d1=0.0 d12=-76.0 z=-2.8406395240384614
- **CHANGE_POINT** `biomass_gen` value=3028 d1=-2.0 d12=-16.0 z=-1.8885713
- **PERSISTENT_DOWN** `ind_demand` value=-1.252e+04 d1=0.0 d12=-18.0 z=-3.21057121
- **ROBUST_OUTLIER** `ind_demand` value=-1.252e+04 d1=0.0 d12=-18.0 z=-3.21057121
- **PERSISTENT_DOWN** `biomass_gen` value=3028 d1=-2.0 d12=-16.0 z=-1.8885713

## Nearest historical live analogues

- `2026-09-22T03:55:16.196094Z` distance=0.021 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:59:30.332417Z` distance=0.021 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T04:03:43.712214Z` distance=0.021 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:33:35.816390Z` distance=0.027 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:37:48.990972Z` distance=0.027 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
