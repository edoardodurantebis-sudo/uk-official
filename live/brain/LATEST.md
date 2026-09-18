# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T18:41:58.721095Z`  
Memory snapshots: **1260**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=4904 d1=101.0 d12=-223.0 z=27.574055542372882
- **CHANGE_POINT** `thermal_base` value=8240 d1=96.0 d12=-227.0 z=27.30266492226891
- **REVERSAL** `ccgt_gen` value=4904 d1=101.0 d12=-223.0 z=27.574055542372882
- **ROBUST_OUTLIER** `ccgt_gen` value=4904 d1=101.0 d12=-223.0 z=27.574055542372882
- **REVERSAL** `thermal_base` value=8240 d1=96.0 d12=-227.0 z=27.30266492226891
- **ROBUST_OUTLIER** `thermal_base` value=8240 d1=96.0 d12=-227.0 z=27.30266492226891
- **CHANGE_POINT** `ind_generation` value=2.623e+04 d1=0.0 d12=655.0 z=18.09392068478261
- **ROBUST_OUTLIER** `ind_generation` value=2.623e+04 d1=0.0 d12=655.0 z=18.09392068478261
- **CHANGE_POINT** `interconnector_net` value=-306 d1=0.0 d12=1236.0 z=-9.820009416124838
- **PERSISTENT_UP** `interconnector_net` value=-306 d1=0.0 d12=1236.0 z=-9.820009416124838
- **ROBUST_OUTLIER** `interconnector_net` value=-306 d1=0.0 d12=1236.0 z=-9.820009416124838
- **PERSISTENT_DOWN** `ps_gen` value=295 d1=-108.0 d12=-383.0 z=6.328503317602041
- **ROBUST_OUTLIER** `ps_gen` value=295 d1=-108.0 d12=-383.0 z=6.328503317602041
- **ROBUST_OUTLIER** `ind_demand` value=-1.074e+04 d1=0.0 d12=31.0 z=6.07040775
- **CHANGE_POINT** `imbalance` value=9176 d1=0.0 d12=655.0 z=2.424253014492754

## Nearest historical live analogues

- `2026-09-18T15:24:41.804681Z` distance=0.108 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T15:29:30.162883Z` distance=0.108 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T15:33:43.267823Z` distance=0.108 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T15:37:58.638986Z` distance=0.108 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:42:43.021012Z` distance=0.108 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
