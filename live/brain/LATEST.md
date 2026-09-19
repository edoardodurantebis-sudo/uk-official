# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T01:34:19.464108Z`  
Memory snapshots: **1332**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.712e+04 d1=0.0 d12=-398.0 z=-4.206686072368421
- **ROBUST_OUTLIER** `margin` value=3.712e+04 d1=0.0 d12=-398.0 z=-4.206686072368421
- **CHANGE_POINT** `interconnector_net` value=-1.11e+04 d1=-843.0 d12=-1791.0 z=-1.0495512051255231
- **CHANGE_POINT** `ps_gen` value=-830 d1=2.0 d12=-6.0 z=-0.676138869193154
- **CHANGE_POINT** `biomass_gen` value=1139 d1=1.0 d12=32.0 z=-0.16017567346938774
- **PERSISTENT_DOWN** `interconnector_net` value=-1.11e+04 d1=-843.0 d12=-1791.0 z=-1.0495512051255231
- **ACCELERATION** `interconnector_net` value=-1.11e+04 d1=-843.0 d12=-1791.0 z=-1.0495512051255231
- **REVERSAL** `ps_gen` value=-830 d1=2.0 d12=-6.0 z=-0.676138869193154
- **REVERSAL** `wind_gen` value=1.629e+04 d1=-64.0 d12=109.0 z=-0.29467069929078016
- **ACCELERATION** `wind_gen` value=1.629e+04 d1=-64.0 d12=109.0 z=-0.29467069929078016
- **PERSISTENT_UP** `biomass_gen` value=1139 d1=1.0 d12=32.0 z=-0.16017567346938774
- **REVERSAL** `thermal_base` value=7036 d1=-47.0 d12=43.0 z=-0.12369535207612457
- **ACCELERATION** `thermal_base` value=7036 d1=-47.0 d12=43.0 z=-0.12369535207612457
- **REVERSAL** `ccgt_gen` value=3698 d1=-48.0 d12=40.0 z=-0.12022990196078433
- **ACCELERATION** `ccgt_gen` value=3698 d1=-48.0 d12=40.0 z=-0.12022990196078433

## Nearest historical live analogues

- `2026-09-19T00:05:15.769782Z` distance=0.139 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:09:28.868640Z` distance=0.139 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:13:40.553498Z` distance=0.139 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:17:54.223700Z` distance=0.139 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:22:06.996302Z` distance=0.141 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
