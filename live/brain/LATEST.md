# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T09:26:41.423464Z`  
Memory snapshots: **511**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **PERSISTENT_DOWN** `margin` value=3.451e+04 d1=0.0 d12=-2052.0 z=-78.16298525961538
- **ACCELERATION** `margin` value=3.451e+04 d1=0.0 d12=-2052.0 z=-78.16298525961538
- **ROBUST_OUTLIER** `margin` value=3.451e+04 d1=0.0 d12=-2052.0 z=-78.16298525961538
- **PERSISTENT_DOWN** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1219.0 z=-53.47740160714286
- **ACCELERATION** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1219.0 z=-53.47740160714286
- **ROBUST_OUTLIER** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1219.0 z=-53.47740160714286
- **PERSISTENT_DOWN** `biomass_gen` value=3163 d1=-46.0 d12=-73.0 z=-18.75081505
- **ROBUST_OUTLIER** `biomass_gen` value=3163 d1=-46.0 d12=-73.0 z=-18.75081505
- **PERSISTENT_DOWN** `imbalance` value=5364 d1=0.0 d12=-1743.0 z=-10.9872489182243
- **ACCELERATION** `imbalance` value=5364 d1=0.0 d12=-1743.0 z=-10.9872489182243
- **ROBUST_OUTLIER** `imbalance` value=5364 d1=0.0 d12=-1743.0 z=-10.9872489182243
- **ROBUST_OUTLIER** `residual_proxy` value=-813 d1=0.0 d12=0.0 z=-4.3519625270700635
- **CHANGE_POINT** `interconnector_net` value=1.028e+04 d1=0.0 d12=36.0 z=1.4506689143254519
- **CHANGE_POINT** `thermal_base` value=9957 d1=-230.0 d12=-1452.0 z=-0.765530033157277
- **CHANGE_POINT** `ccgt_gen` value=6628 d1=-228.0 d12=-1451.0 z=-0.7636031931884909

## Nearest historical live analogues

- `2026-09-16T08:31:21.232151Z` distance=3.118 → {'next30m_imbalance_delta': -402.0, 'next30m_margin_delta': -815.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:17:56.653795Z` distance=3.129 → {'next30m_imbalance_delta': 235.0, 'next30m_margin_delta': 235.0, 'next30m_residual_proxy_delta': -321.0}
- `2026-09-16T07:23:21.620957Z` distance=3.131 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:27:32.881343Z` distance=3.131 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:31:44.991160Z` distance=3.131 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
