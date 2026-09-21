# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T03:00:57.173515Z`  
Memory snapshots: **2035**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.756e+04 d1=0.0 d12=1730.0 z=30.71522553846154
- **PERSISTENT_UP** `margin` value=3.756e+04 d1=0.0 d12=1730.0 z=30.71522553846154
- **ROBUST_OUTLIER** `margin` value=3.756e+04 d1=0.0 d12=1730.0 z=30.71522553846154
- **CHANGE_POINT** `ccgt_gen` value=4841 d1=48.0 d12=-530.0 z=-1.6325823824343015
- **CHANGE_POINT** `thermal_base` value=8185 d1=51.0 d12=-527.0 z=-1.6266553915159947
- **CHANGE_POINT** `ind_demand` value=-1.18e+04 d1=0.0 d12=26.0 z=1.4613944583333334
- **CHANGE_POINT** `imbalance` value=-4865 d1=0.0 d12=34.0 z=1.0516925485781992
- **CHANGE_POINT** `ind_generation` value=1.574e+04 d1=0.0 d12=34.0 z=1.0516925485781992
- **CHANGE_POINT** `interconnector_net` value=1.231e+04 d1=-209.0 d12=-33.0 z=0.9445135181587838
- **PERSISTENT_UP** `nuclear_gen` value=3344 d1=3.0 d12=3.0 z=1.7986393333333333
- **ACCELERATION** `nuclear_gen` value=3344 d1=3.0 d12=3.0 z=1.7986393333333333
- **REVERSAL** `wind_gen` value=3765 d1=37.0 d12=-107.0 z=-1.7883393228346458
- **ACCELERATION** `wind_gen` value=3765 d1=37.0 d12=-107.0 z=-1.7883393228346458
- **REVERSAL** `ccgt_gen` value=4841 d1=48.0 d12=-530.0 z=-1.6325823824343015
- **REVERSAL** `thermal_base` value=8185 d1=51.0 d12=-527.0 z=-1.6266553915159947

## Nearest historical live analogues

- `2026-09-21T01:53:20.720277Z` distance=0.825 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:57:30.190951Z` distance=0.825 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:01:42.969969Z` distance=0.825 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:05:53.234228Z` distance=0.825 → {'next30m_imbalance_delta': -5.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1716.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:23:21.503053Z` distance=0.828 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
