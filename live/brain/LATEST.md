# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T01:50:42.136685Z`  
Memory snapshots: **1049**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=1.013e+04 d1=0.0 d12=-2.0 z=9.9487238125
- **CHANGE_POINT** `ind_generation` value=2.694e+04 d1=0.0 d12=-2.0 z=9.9487238125
- **ROBUST_OUTLIER** `ind_demand` value=-1.119e+04 d1=0.0 d12=31.0 z=-10.454591125
- **ROBUST_OUTLIER** `imbalance` value=1.013e+04 d1=0.0 d12=-2.0 z=9.9487238125
- **ROBUST_OUTLIER** `ind_generation` value=2.694e+04 d1=0.0 d12=-2.0 z=9.9487238125
- **CHANGE_POINT** `margin` value=3.67e+04 d1=1.0 d12=101.0 z=2.557970561320755
- **PERSISTENT_UP** `margin` value=3.67e+04 d1=1.0 d12=101.0 z=2.557970561320755
- **CHANGE_POINT** `biomass_gen` value=1941 d1=-7.0 d12=-18.0 z=-0.06375773756218905
- **REVERSAL** `nuclear_gen` value=3333 d1=-4.0 d12=4.0 z=2.0234692499999998
- **ACCELERATION** `nuclear_gen` value=3333 d1=-4.0 d12=4.0 z=2.0234692499999998
- **PERSISTENT_UP** `wind_gen` value=1.443e+04 d1=221.0 d12=333.0 z=-1.0019650747392816
- **ACCELERATION** `wind_gen` value=1.443e+04 d1=221.0 d12=333.0 z=-1.0019650747392816
- **REVERSAL** `ccgt_gen` value=3749 d1=5.0 d12=-47.0 z=-0.792895474137931
- **ACCELERATION** `ccgt_gen` value=3749 d1=5.0 d12=-47.0 z=-0.792895474137931
- **REVERSAL** `thermal_base` value=7082 d1=1.0 d12=-43.0 z=-0.7810442128751975

## Nearest historical live analogues

- `2026-09-18T00:50:53.445195Z` distance=0.046 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:55:05.130155Z` distance=0.061 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:25:46.059957Z` distance=0.074 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:29:58.615763Z` distance=0.074 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:34:09.969710Z` distance=0.074 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 62.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
