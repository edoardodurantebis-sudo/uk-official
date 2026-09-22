# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T04:12:15.818574Z`  
Memory snapshots: **2391**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.78e+04 d1=0.0 d12=5.0 z=23.24057073369565
- **ROBUST_OUTLIER** `margin` value=3.78e+04 d1=0.0 d12=5.0 z=23.24057073369565
- **CHANGE_POINT** `interconnector_net` value=-3173 d1=-380.0 d12=-3581.0 z=-5.935336631899872
- **CHANGE_POINT** `imbalance` value=-3236 d1=0.0 d12=-577.0 z=-4.4052611796875
- **CHANGE_POINT** `ind_generation` value=1.822e+04 d1=0.0 d12=-577.0 z=-4.4052611796875
- **PERSISTENT_DOWN** `interconnector_net` value=-3173 d1=-380.0 d12=-3581.0 z=-5.935336631899872
- **ROBUST_OUTLIER** `interconnector_net` value=-3173 d1=-380.0 d12=-3581.0 z=-5.935336631899872
- **ROBUST_OUTLIER** `imbalance` value=-3236 d1=0.0 d12=-577.0 z=-4.4052611796875
- **ROBUST_OUTLIER** `ind_generation` value=1.822e+04 d1=0.0 d12=-577.0 z=-4.4052611796875
- **CHANGE_POINT** `ps_gen` value=-448 d1=1.0 d12=-277.0 z=-2.015293616666667
- **CHANGE_POINT** `wind_gen` value=3592 d1=-12.0 d12=-350.0 z=-0.8663171100917432
- **PERSISTENT_UP** `ccgt_gen` value=1.207e+04 d1=405.0 d12=818.0 z=2.2693489795816735
- **PERSISTENT_UP** `thermal_base` value=1.572e+04 d1=404.0 d12=804.0 z=2.1993089902723737
- **REVERSAL** `ps_gen` value=-448 d1=1.0 d12=-277.0 z=-2.015293616666667
- **ACCELERATION** `ps_gen` value=-448 d1=1.0 d12=-277.0 z=-2.015293616666667

## Nearest historical live analogues

- `2026-09-22T02:20:47.392507Z` distance=0.196 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:24:59.358718Z` distance=0.196 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:29:12.426907Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:33:26.071895Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:37:48.213453Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
