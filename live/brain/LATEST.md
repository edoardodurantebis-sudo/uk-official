# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T09:38:17.610500Z`  
Memory snapshots: **2468**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=4.033e+04 d1=0.0 d12=1330.0 z=155.745815
- **ROBUST_OUTLIER** `margin` value=4.033e+04 d1=0.0 d12=1330.0 z=155.745815
- **CHANGE_POINT** `imbalance` value=2430 d1=0.0 d12=3785.0 z=19.209331819444444
- **ROBUST_OUTLIER** `imbalance` value=2430 d1=0.0 d12=3785.0 z=19.209331819444444
- **ROBUST_OUTLIER** `ind_generation` value=2.35e+04 d1=0.0 d12=3785.0 z=17.87738488888889
- **CHANGE_POINT** `ind_demand` value=-1.28e+04 d1=0.0 d12=-3.0 z=-6.8844471034482755
- **ROBUST_OUTLIER** `ind_demand` value=-1.28e+04 d1=0.0 d12=-3.0 z=-6.8844471034482755
- **PERSISTENT_DOWN** `biomass_gen` value=3048 d1=-1.0 d12=-2.0 z=3.8221085833333333
- **ACCELERATION** `biomass_gen` value=3048 d1=-1.0 d12=-2.0 z=3.8221085833333333
- **ROBUST_OUTLIER** `biomass_gen` value=3048 d1=-1.0 d12=-2.0 z=3.8221085833333333
- **CHANGE_POINT** `residual_proxy` value=7927 d1=0.0 d12=0.0 z=-0.67448975
- **PERSISTENT_UP** `interconnector_net` value=1.076e+04 d1=1.0 d12=1321.0 z=1.8647549611792773
- **ACCELERATION** `interconnector_net` value=1.076e+04 d1=1.0 d12=1321.0 z=1.8647549611792773
- **PERSISTENT_DOWN** `thermal_base` value=1.418e+04 d1=-203.0 d12=-1299.0 z=-1.8587642155394941
- **PERSISTENT_DOWN** `ccgt_gen` value=1.053e+04 d1=-199.0 d12=-1305.0 z=-1.8538931637532132

## Nearest historical live analogues

- `2026-09-21T09:51:38.826991Z` distance=0.472 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T09:55:50.935902Z` distance=0.472 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:00:02.533283Z` distance=0.472 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:04:15.522994Z` distance=0.472 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:08:28.408864Z` distance=0.472 → {'next30m_imbalance_delta': 2999.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1193.0, 'next30m_residual_proxy_delta': 354.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
