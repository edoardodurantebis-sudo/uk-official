# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T15:27:19.632279Z`  
Memory snapshots: **255**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=4601 d1=239.0 d12=2502.0 z=7.477869020231214
- **CHANGE_POINT** `thermal_base` value=7930 d1=243.0 d12=2502.0 z=7.415518283938814
- **REVERSAL** `interconnector_net` value=6519 d1=27.0 d12=-1450.0 z=-8.05127764736842
- **ROBUST_OUTLIER** `interconnector_net` value=6519 d1=27.0 d12=-1450.0 z=-8.05127764736842
- **PERSISTENT_UP** `ccgt_gen` value=4601 d1=239.0 d12=2502.0 z=7.477869020231214
- **ROBUST_OUTLIER** `ccgt_gen` value=4601 d1=239.0 d12=2502.0 z=7.477869020231214
- **PERSISTENT_UP** `thermal_base` value=7930 d1=243.0 d12=2502.0 z=7.415518283938814
- **ROBUST_OUTLIER** `thermal_base` value=7930 d1=243.0 d12=2502.0 z=7.415518283938814
- **CHANGE_POINT** `ps_gen` value=-136 d1=-38.0 d12=521.0 z=3.4877962724637683
- **REVERSAL** `ps_gen` value=-136 d1=-38.0 d12=521.0 z=3.4877962724637683
- **ROBUST_OUTLIER** `ps_gen` value=-136 d1=-38.0 d12=521.0 z=3.4877962724637683
- **CHANGE_POINT** `margin` value=3.465e+04 d1=0.0 d12=19.0 z=-0.9692247668067228
- **CHANGE_POINT** `imbalance` value=5817 d1=0.0 d12=49.0 z=0.9557663265957447
- **CHANGE_POINT** `ind_generation` value=2.494e+04 d1=0.0 d12=49.0 z=0.9202146403345725
- **PERSISTENT_UP** `margin` value=3.465e+04 d1=0.0 d12=19.0 z=-0.9692247668067228

## Nearest historical live analogues

- `2026-09-15T14:23:51.987860Z` distance=0.019 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T14:28:05.259603Z` distance=0.019 → {'next30m_imbalance_delta': 50.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T14:32:25.430629Z` distance=0.019 → {'next30m_imbalance_delta': 50.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:25:09.783150Z` distance=0.484 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:29:22.306019Z` distance=0.484 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
