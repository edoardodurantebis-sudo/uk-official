# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T05:09:27.239578Z`  
Memory snapshots: **450**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=6108 d1=538.0 d12=2418.0 z=27.16825846153846
- **CHANGE_POINT** `thermal_base` value=9437 d1=540.0 d12=2418.0 z=25.904902998333334
- **PERSISTENT_UP** `ccgt_gen` value=6108 d1=538.0 d12=2418.0 z=27.16825846153846
- **ROBUST_OUTLIER** `ccgt_gen` value=6108 d1=538.0 d12=2418.0 z=27.16825846153846
- **PERSISTENT_UP** `thermal_base` value=9437 d1=540.0 d12=2418.0 z=25.904902998333334
- **ROBUST_OUTLIER** `thermal_base` value=9437 d1=540.0 d12=2418.0 z=25.904902998333334
- **CHANGE_POINT** `imbalance` value=7203 d1=0.0 d12=182.0 z=20.822709205128206
- **CHANGE_POINT** `ind_generation` value=2.632e+04 d1=0.0 d12=182.0 z=20.822709205128206
- **ROBUST_OUTLIER** `imbalance` value=7203 d1=0.0 d12=182.0 z=20.822709205128206
- **ROBUST_OUTLIER** `ind_generation` value=2.632e+04 d1=0.0 d12=182.0 z=20.822709205128206
- **PERSISTENT_DOWN** `interconnector_net` value=-1197 d1=-109.0 d12=-1582.0 z=-7.5191767702483805
- **ROBUST_OUTLIER** `interconnector_net` value=-1197 d1=-109.0 d12=-1582.0 z=-7.5191767702483805
- **CHANGE_POINT** `wind_gen` value=9324 d1=140.0 d12=-162.0 z=-1.4150913807819383
- **CHANGE_POINT** `ps_gen` value=-37 d1=-76.0 d12=-260.0 z=-0.8431121874999999
- **CHANGE_POINT** `ind_demand` value=-1.218e+04 d1=0.0 d12=23.0 z=-0.287016914893617

## Nearest historical live analogues

- `2026-09-16T03:53:53.579562Z` distance=0.056 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:58:05.004513Z` distance=0.056 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T04:02:15.050270Z` distance=0.056 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T04:06:27.964921Z` distance=0.056 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T04:10:40.377612Z` distance=0.056 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
