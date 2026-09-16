# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T09:51:49.097467Z`  
Memory snapshots: **517**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1204.0 z=-27.39086423780488
- **ROBUST_OUTLIER** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1204.0 z=-27.39086423780488
- **CHANGE_POINT** `margin` value=3.416e+04 d1=-349.0 d12=-1586.0 z=-23.344445242105266
- **PERSISTENT_DOWN** `margin` value=3.416e+04 d1=-349.0 d12=-1586.0 z=-23.344445242105266
- **ROBUST_OUTLIER** `margin` value=3.416e+04 d1=-349.0 d12=-1586.0 z=-23.344445242105266
- **CHANGE_POINT** `imbalance` value=5367 d1=3.0 d12=-1338.0 z=-10.968337990654206
- **CHANGE_POINT** `biomass_gen` value=3201 d1=-23.0 d12=-41.0 z=-10.454591125
- **REVERSAL** `imbalance` value=5367 d1=3.0 d12=-1338.0 z=-10.968337990654206
- **ROBUST_OUTLIER** `imbalance` value=5367 d1=3.0 d12=-1338.0 z=-10.968337990654206
- **ACCELERATION** `biomass_gen` value=3201 d1=-23.0 d12=-41.0 z=-10.454591125
- **ROBUST_OUTLIER** `biomass_gen` value=3201 d1=-23.0 d12=-41.0 z=-10.454591125
- **CHANGE_POINT** `interconnector_net` value=1.03e+04 d1=-1.0 d12=51.0 z=1.360551198336366
- **CHANGE_POINT** `thermal_base` value=9693 d1=24.0 d12=-1200.0 z=-0.9745268571009389
- **CHANGE_POINT** `ccgt_gen` value=6367 d1=22.0 d12=-1192.0 z=-0.9703463813857898
- **REVERSAL** `ind_generation` value=2.6e+04 d1=3.0 d12=-158.0 z=-1.6380465357142857

## Nearest historical live analogues

- `2026-09-16T08:52:24.970739Z` distance=3.006 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:56:37.275315Z` distance=3.006 → {'next30m_imbalance_delta': -1341.0, 'next30m_margin_delta': -1237.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:17:56.653795Z` distance=3.138 → {'next30m_imbalance_delta': 235.0, 'next30m_margin_delta': 235.0, 'next30m_residual_proxy_delta': -321.0}
- `2026-09-16T07:23:21.620957Z` distance=3.140 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:27:32.881343Z` distance=3.140 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
