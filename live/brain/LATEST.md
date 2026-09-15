# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T19:02:28.411957Z`  
Memory snapshots: **306**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **ROBUST_OUTLIER** `biomass_gen` value=3299 d1=0.0 d12=49.0 z=38.770670074074076
- **ROBUST_OUTLIER** `ind_demand` value=-1.191e+04 d1=0.0 d12=8.0 z=4.72142825
- **CHANGE_POINT** `thermal_base` value=1.413e+04 d1=-83.0 d12=202.0 z=1.0018631677754124
- **CHANGE_POINT** `ccgt_gen` value=1.081e+04 d1=-85.0 d12=198.0 z=0.999821326626826
- **CHANGE_POINT** `ps_gen` value=802 d1=-1.0 d12=-4.0 z=0.9885490398437501
- **CHANGE_POINT** `imbalance` value=5739 d1=0.0 d12=-36.0 z=-0.41996531603773585
- **CHANGE_POINT** `ind_generation` value=2.486e+04 d1=0.0 d12=-36.0 z=-0.41996531603773585
- **REVERSAL** `wind_gen` value=9956 d1=25.0 d12=-183.0 z=-1.0579560038071065
- **REVERSAL** `thermal_base` value=1.413e+04 d1=-83.0 d12=202.0 z=1.0018631677754124
- **ACCELERATION** `thermal_base` value=1.413e+04 d1=-83.0 d12=202.0 z=1.0018631677754124
- **REVERSAL** `ccgt_gen` value=1.081e+04 d1=-85.0 d12=198.0 z=0.999821326626826
- **ACCELERATION** `ccgt_gen` value=1.081e+04 d1=-85.0 d12=198.0 z=0.999821326626826
- **PERSISTENT_DOWN** `ps_gen` value=802 d1=-1.0 d12=-4.0 z=0.9885490398437501
- **PERSISTENT_UP** `interconnector_net` value=-1520 d1=181.0 d12=154.0 z=-0.8250398260501036
- **ACCELERATION** `interconnector_net` value=-1520 d1=181.0 d12=154.0 z=-0.8250398260501036

## Nearest historical live analogues

- `2026-09-15T17:50:55.506503Z` distance=0.062 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:55:09.760503Z` distance=0.062 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T17:59:22.215947Z` distance=0.062 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:03:35.364442Z` distance=0.062 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T18:07:47.333244Z` distance=0.062 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
