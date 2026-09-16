# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T07:56:53.147187Z`  
Memory snapshots: **490**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.632e+04 d1=0.0 d12=-1077.0 z=-50.628886859375
- **ROBUST_OUTLIER** `margin` value=3.632e+04 d1=0.0 d12=-1077.0 z=-50.628886859375
- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-195.0 z=-22.065450392857144
- **PERSISTENT_UP** `residual_proxy` value=864 d1=0.0 d12=1249.0 z=4.691355458598727
- **ROBUST_OUTLIER** `residual_proxy` value=864 d1=0.0 d12=1249.0 z=4.691355458598727
- **PERSISTENT_UP** `thermal_base` value=1.172e+04 d1=43.0 d12=78.0 z=2.5618947853025937
- **ACCELERATION** `thermal_base` value=1.172e+04 d1=43.0 d12=78.0 z=2.5618947853025937
- **PERSISTENT_UP** `ccgt_gen` value=8394 d1=39.0 d12=74.0 z=2.547580957377049
- **ACCELERATION** `ccgt_gen` value=8394 d1=39.0 d12=74.0 z=2.547580957377049
- **CHANGE_POINT** `imbalance` value=6872 d1=0.0 d12=-442.0 z=-0.5207200660621761
- **PERSISTENT_UP** `ps_gen` value=230 d1=1.0 d12=8.0 z=2.1583672
- **REVERSAL** `biomass_gen` value=3226 d1=1.0 d12=-1.0 z=-2.0234692499999998
- **ACCELERATION** `biomass_gen` value=3226 d1=1.0 d12=-1.0 z=-2.0234692499999998
- **PERSISTENT_DOWN** `wind_gen` value=7369 d1=-80.0 d12=-689.0 z=-1.8872040910472971
- **PERSISTENT_UP** `nuclear_gen` value=3330 d1=4.0 d12=4.0 z=0.337244875

## Nearest historical live analogues

- `2026-09-16T06:54:08.413156Z` distance=1.127 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:58:18.248300Z` distance=1.127 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T07:02:28.186045Z` distance=1.127 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:22:04.416358Z` distance=1.499 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -157.0}
- `2026-09-16T05:26:14.079375Z` distance=1.499 → {'next30m_imbalance_delta': 41.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -157.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
