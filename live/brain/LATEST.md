# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T18:46:10.287298Z`  
Memory snapshots: **1261**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=5031 d1=127.0 d12=-96.0 z=29.02592330932203
- **CHANGE_POINT** `thermal_base` value=8363 d1=123.0 d12=-104.0 z=28.696988271008404
- **REVERSAL** `ccgt_gen` value=5031 d1=127.0 d12=-96.0 z=29.02592330932203
- **ROBUST_OUTLIER** `ccgt_gen` value=5031 d1=127.0 d12=-96.0 z=29.02592330932203
- **REVERSAL** `thermal_base` value=8363 d1=123.0 d12=-104.0 z=28.696988271008404
- **ROBUST_OUTLIER** `thermal_base` value=8363 d1=123.0 d12=-104.0 z=28.696988271008404
- **CHANGE_POINT** `ind_generation` value=2.623e+04 d1=0.0 d12=65.0 z=18.09392068478261
- **ROBUST_OUTLIER** `ind_generation` value=2.623e+04 d1=0.0 d12=65.0 z=18.09392068478261
- **CHANGE_POINT** `interconnector_net` value=-307 d1=-1.0 d12=1235.0 z=-9.82176361573472
- **REVERSAL** `interconnector_net` value=-307 d1=-1.0 d12=1235.0 z=-9.82176361573472
- **ROBUST_OUTLIER** `interconnector_net` value=-307 d1=-1.0 d12=1235.0 z=-9.82176361573472
- **PERSISTENT_DOWN** `ps_gen` value=294 d1=-1.0 d12=-384.0 z=6.321620769132653
- **ROBUST_OUTLIER** `ps_gen` value=294 d1=-1.0 d12=-384.0 z=6.321620769132653
- **ROBUST_OUTLIER** `ind_demand` value=-1.074e+04 d1=0.0 d12=30.0 z=6.07040775
- **CHANGE_POINT** `imbalance` value=9176 d1=0.0 d12=65.0 z=2.424253014492754

## Nearest historical live analogues

- `2026-09-18T17:51:12.400587Z` distance=0.056 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T15:24:41.804681Z` distance=0.108 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T15:29:30.162883Z` distance=0.108 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T15:33:43.267823Z` distance=0.108 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T15:37:58.638986Z` distance=0.108 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
