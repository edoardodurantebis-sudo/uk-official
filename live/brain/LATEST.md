# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T05:05:14.612812Z`  
Memory snapshots: **449**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=5570 d1=0.0 d12=1854.0 z=25.0738888015873
- **CHANGE_POINT** `thermal_base` value=8897 d1=0.0 d12=1850.0 z=24.292007765384614
- **PERSISTENT_UP** `ccgt_gen` value=5570 d1=0.0 d12=1854.0 z=25.0738888015873
- **ACCELERATION** `ccgt_gen` value=5570 d1=0.0 d12=1854.0 z=25.0738888015873
- **ROBUST_OUTLIER** `ccgt_gen` value=5570 d1=0.0 d12=1854.0 z=25.0738888015873
- **PERSISTENT_UP** `thermal_base` value=8897 d1=0.0 d12=1850.0 z=24.292007765384614
- **ACCELERATION** `thermal_base` value=8897 d1=0.0 d12=1850.0 z=24.292007765384614
- **ROBUST_OUTLIER** `thermal_base` value=8897 d1=0.0 d12=1850.0 z=24.292007765384614
- **ROBUST_OUTLIER** `imbalance` value=7203 d1=0.0 d12=182.0 z=20.822709205128206
- **ROBUST_OUTLIER** `ind_generation` value=2.632e+04 d1=0.0 d12=182.0 z=20.822709205128206
- **PERSISTENT_DOWN** `interconnector_net` value=-1088 d1=0.0 d12=-1334.0 z=-7.360387606641468
- **ROBUST_OUTLIER** `interconnector_net` value=-1088 d1=0.0 d12=-1334.0 z=-7.360387606641468
- **CHANGE_POINT** `wind_gen` value=9184 d1=0.0 d12=-357.0 z=-1.6617109810022026
- **CHANGE_POINT** `ps_gen` value=39 d1=0.0 d12=-181.0 z=-0.4012051099137931
- **CHANGE_POINT** `ind_demand` value=-1.218e+04 d1=0.0 d12=23.0 z=-0.287016914893617

## Nearest historical live analogues

- `2026-09-16T03:53:53.579562Z` distance=0.056 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:58:05.004513Z` distance=0.056 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T04:02:15.050270Z` distance=0.056 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T04:06:27.964921Z` distance=0.056 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T04:10:40.377612Z` distance=0.056 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
