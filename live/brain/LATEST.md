# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T05:07:21.689505Z`  
Memory snapshots: **1724**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-6777 d1=0.0 d12=-250.0 z=-39.09446358653846
- **CHANGE_POINT** `ind_generation` value=1.318e+04 d1=0.0 d12=-250.0 z=-39.09446358653846
- **ROBUST_OUTLIER** `imbalance` value=-6777 d1=0.0 d12=-250.0 z=-39.09446358653846
- **ROBUST_OUTLIER** `ind_generation` value=1.318e+04 d1=0.0 d12=-250.0 z=-39.09446358653846
- **CHANGE_POINT** `margin` value=3.752e+04 d1=0.0 d12=-28.0 z=13.198123756756758
- **ROBUST_OUTLIER** `margin` value=3.752e+04 d1=0.0 d12=-28.0 z=13.198123756756758
- **CHANGE_POINT** `ind_demand` value=-1.218e+04 d1=0.0 d12=116.0 z=0.1143202966101695
- **CHANGE_POINT** `ps_gen` value=-693 d1=2.0 d12=-164.0 z=0.0
- **PERSISTENT_DOWN** `thermal_base` value=6733 d1=-210.0 d12=-602.0 z=-0.958599580385852
- **PERSISTENT_DOWN** `ccgt_gen` value=3399 d1=-204.0 d12=-605.0 z=-0.955885155254777
- **PERSISTENT_UP** `interconnector_net` value=-1.211e+04 d1=348.0 d12=211.0 z=-0.9493301897163121
- **ACCELERATION** `interconnector_net` value=-1.211e+04 d1=348.0 d12=211.0 z=-0.9493301897163121
- **PERSISTENT_DOWN** `biomass_gen` value=1223 d1=-10.0 d12=-6.0 z=0.597534543624161
- **ACCELERATION** `biomass_gen` value=1223 d1=-10.0 d12=-6.0 z=0.597534543624161
- **REVERSAL** `nuclear_gen` value=3334 d1=-6.0 d12=3.0 z=0.22482991666666666

## Nearest historical live analogues

- `2026-09-20T03:34:04.391029Z` distance=0.124 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:38:17.578686Z` distance=0.124 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:42:30.347706Z` distance=0.124 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:46:44.690279Z` distance=0.124 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:50:56.701349Z` distance=0.131 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
