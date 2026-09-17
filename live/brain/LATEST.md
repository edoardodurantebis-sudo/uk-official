# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T21:54:26.142796Z`  
Memory snapshots: **993**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1854 d1=-285.0 d12=-1354.0 z=-5.1976808691756275
- **CHANGE_POINT** `ps_gen` value=-140 d1=-192.0 d12=-495.0 z=-3.3399866764705886
- **PERSISTENT_DOWN** `biomass_gen` value=1854 d1=-285.0 d12=-1354.0 z=-5.1976808691756275
- **ROBUST_OUTLIER** `biomass_gen` value=1854 d1=-285.0 d12=-1354.0 z=-5.1976808691756275
- **ROBUST_OUTLIER** `interconnector_net` value=-5438 d1=0.0 d12=-2023.0 z=-3.8761355999461204
- **PERSISTENT_DOWN** `ps_gen` value=-140 d1=-192.0 d12=-495.0 z=-3.3399866764705886
- **ACCELERATION** `ps_gen` value=-140 d1=-192.0 d12=-495.0 z=-3.3399866764705886
- **ROBUST_OUTLIER** `ps_gen` value=-140 d1=-192.0 d12=-495.0 z=-3.3399866764705886
- **CHANGE_POINT** `thermal_base` value=7773 d1=-84.0 d12=-540.0 z=-0.369437070237599
- **CHANGE_POINT** `ccgt_gen` value=4457 d1=-84.0 d12=-531.0 z=-0.36872482775219756
- **PERSISTENT_DOWN** `ind_demand` value=-1.116e+04 d1=-1.0 d12=-1.0 z=2.186277120689655
- **ACCELERATION** `ind_demand` value=-1.116e+04 d1=-1.0 d12=-1.0 z=2.186277120689655
- **PERSISTENT_DOWN** `margin` value=3.644e+04 d1=-1.0 d12=-17.0 z=-1.0458380393258426
- **PERSISTENT_DOWN** `nuclear_gen` value=3316 d1=0.0 d12=-9.0 z=-0.67448975
- **PERSISTENT_UP** `imbalance` value=9718 d1=16.0 d12=16.0 z=0.5395918

## Nearest historical live analogues

- `2026-09-17T20:22:00.773279Z` distance=0.003 → {'next30m_imbalance_delta': -22.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T20:26:16.510508Z` distance=0.003 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T20:30:29.039368Z` distance=0.003 → {'next30m_imbalance_delta': 16.0, 'next30m_margin_delta': 10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T20:34:40.503953Z` distance=0.003 → {'next30m_imbalance_delta': 16.0, 'next30m_margin_delta': 10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T20:38:54.540186Z` distance=0.003 → {'next30m_imbalance_delta': 16.0, 'next30m_margin_delta': 10.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
