# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T12:27:42.936874Z`  
Memory snapshots: **1200**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `wind_gen` value=1.439e+04 d1=-70.0 d12=1694.0 z=3.205648163565426
- **CHANGE_POINT** `ind_generation` value=2.559e+04 d1=-33.0 d12=-81.0 z=-3.1808323437499997
- **CHANGE_POINT** `biomass_gen` value=1038 d1=0.0 d12=-47.0 z=-2.3707312995049508
- **REVERSAL** `wind_gen` value=1.439e+04 d1=-70.0 d12=1694.0 z=3.205648163565426
- **ROBUST_OUTLIER** `wind_gen` value=1.439e+04 d1=-70.0 d12=1694.0 z=3.205648163565426
- **PERSISTENT_DOWN** `ind_generation` value=2.559e+04 d1=-33.0 d12=-81.0 z=-3.1808323437499997
- **ACCELERATION** `ind_generation` value=2.559e+04 d1=-33.0 d12=-81.0 z=-3.1808323437499997
- **ROBUST_OUTLIER** `ind_generation` value=2.559e+04 d1=-33.0 d12=-81.0 z=-3.1808323437499997
- **CHANGE_POINT** `ps_gen` value=-708 d1=2.0 d12=13.0 z=-1.152899683072677
- **CHANGE_POINT** `margin` value=3.81e+04 d1=0.0 d12=-20.0 z=0.952716771875
- **CHANGE_POINT** `imbalance` value=8916 d1=-33.0 d12=-81.0 z=-0.7085757557427259
- **PERSISTENT_UP** `ps_gen` value=-708 d1=2.0 d12=13.0 z=-1.152899683072677
- **ACCELERATION** `ps_gen` value=-708 d1=2.0 d12=13.0 z=-1.152899683072677
- **ACCELERATION** `nuclear_gen` value=3340 d1=-1.0 d12=-3.0 z=1.1241495833333335
- **PERSISTENT_UP** `ccgt_gen` value=2461 d1=17.0 d12=28.0 z=-0.9653607332149775

## Nearest historical live analogues

- `2026-09-18T11:24:04.514292Z` distance=0.009 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:28:15.080322Z` distance=0.009 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:32:27.606520Z` distance=0.009 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': -20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T10:58:51.813919Z` distance=0.010 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:03:02.719756Z` distance=0.010 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -2.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
