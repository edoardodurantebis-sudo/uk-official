# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T05:11:32.873657Z`  
Memory snapshots: **1725**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-6777 d1=0.0 d12=-250.0 z=-39.09446358653846
- **CHANGE_POINT** `ind_generation` value=1.318e+04 d1=0.0 d12=-14.0 z=-39.09446358653846
- **ROBUST_OUTLIER** `imbalance` value=-6777 d1=0.0 d12=-250.0 z=-39.09446358653846
- **ROBUST_OUTLIER** `ind_generation` value=1.318e+04 d1=0.0 d12=-14.0 z=-39.09446358653846
- **CHANGE_POINT** `margin` value=3.752e+04 d1=0.0 d12=3.0 z=13.198123756756758
- **ROBUST_OUTLIER** `margin` value=3.752e+04 d1=0.0 d12=3.0 z=13.198123756756758
- **CHANGE_POINT** `ind_demand` value=-1.218e+04 d1=0.0 d12=138.0 z=0.1143202966101695
- **CHANGE_POINT** `ps_gen` value=-696 d1=-3.0 d12=4.0 z=-0.015995804347826086
- **PERSISTENT_DOWN** `thermal_base` value=6707 d1=-26.0 d12=-777.0 z=-0.950559973255814
- **PERSISTENT_DOWN** `ccgt_gen` value=3371 d1=-28.0 d12=-783.0 z=-0.9381071179389314
- **PERSISTENT_UP** `interconnector_net` value=-1.193e+04 d1=184.0 d12=397.0 z=-0.8688158333064776
- **ACCELERATION** `interconnector_net` value=-1.193e+04 d1=184.0 d12=397.0 z=-0.8688158333064776
- **ACCELERATION** `nuclear_gen` value=3336 d1=2.0 d12=6.0 z=0.6744897499999999
- **PERSISTENT_DOWN** `biomass_gen` value=1219 d1=-4.0 d12=-14.0 z=0.5395918
- **ACCELERATION** `biomass_gen` value=1219 d1=-4.0 d12=-14.0 z=0.5395918

## Nearest historical live analogues

- `2026-09-20T03:34:04.391029Z` distance=0.124 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:38:17.578686Z` distance=0.124 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:42:30.347706Z` distance=0.124 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:46:44.690279Z` distance=0.124 → {'next30m_imbalance_delta': -2712.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T03:50:56.701349Z` distance=0.131 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
