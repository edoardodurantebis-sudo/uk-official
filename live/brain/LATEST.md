# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T03:51:00.662974Z`  
Memory snapshots: **2386**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.78e+04 d1=5.0 d12=-38.0 z=23.24057073369565
- **REVERSAL** `margin` value=3.78e+04 d1=5.0 d12=-38.0 z=23.24057073369565
- **ROBUST_OUTLIER** `margin` value=3.78e+04 d1=5.0 d12=-38.0 z=23.24057073369565
- **CHANGE_POINT** `interconnector_net` value=-1450 d1=1.0 d12=-4135.0 z=-4.467799574191503
- **CHANGE_POINT** `ps_gen` value=-711 d1=-2.0 d12=-546.0 z=-3.2008680241228067
- **REVERSAL** `interconnector_net` value=-1450 d1=1.0 d12=-4135.0 z=-4.467799574191503
- **ROBUST_OUTLIER** `interconnector_net` value=-1450 d1=1.0 d12=-4135.0 z=-4.467799574191503
- **CHANGE_POINT** `ind_demand` value=-1.25e+04 d1=0.0 d12=0.0 z=-2.2739940142857145
- **PERSISTENT_DOWN** `ps_gen` value=-711 d1=-2.0 d12=-546.0 z=-3.2008680241228067
- **ROBUST_OUTLIER** `ps_gen` value=-711 d1=-2.0 d12=-546.0 z=-3.2008680241228067
- **CHANGE_POINT** `imbalance` value=-2644 d1=0.0 d12=15.0 z=-0.2459077213541667
- **CHANGE_POINT** `ind_generation` value=1.882e+04 d1=0.0 d12=15.0 z=-0.2459077213541667
- **CHANGE_POINT** `thermal_base` value=1.495e+04 d1=-26.0 d12=572.0 z=0.16776065332197615
- **CHANGE_POINT** `ccgt_gen` value=1.13e+04 d1=-23.0 d12=574.0 z=0.16075339041666667
- **REVERSAL** `biomass_gen` value=3045 d1=-2.0 d12=2.0 z=0.46695444230769234

## Nearest historical live analogues

- `2026-09-22T02:20:47.392507Z` distance=0.196 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:24:59.358718Z` distance=0.196 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:29:12.426907Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:33:26.071895Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:37:48.213453Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
