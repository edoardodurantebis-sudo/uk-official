# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T17:55:35.667246Z`  
Memory snapshots: **2246**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=6619 d1=-1.0 d12=-2755.0 z=-13.64624120021882
- **PERSISTENT_DOWN** `interconnector_net` value=6619 d1=-1.0 d12=-2755.0 z=-13.64624120021882
- **ROBUST_OUTLIER** `interconnector_net` value=6619 d1=-1.0 d12=-2755.0 z=-13.64624120021882
- **CHANGE_POINT** `margin` value=3.617e+04 d1=0.0 d12=-106.0 z=-4.0469385
- **CHANGE_POINT** `thermal_base` value=1.74e+04 d1=-74.0 d12=427.0 z=2.102511017578125
- **CHANGE_POINT** `ccgt_gen` value=1.388e+04 d1=-74.0 d12=420.0 z=2.0856242122287703
- **ROBUST_OUTLIER** `margin` value=3.617e+04 d1=0.0 d12=-106.0 z=-4.0469385
- **CHANGE_POINT** `ind_generation` value=1.842e+04 d1=-24.0 d12=-16.0 z=0.5412572067901235
- **CHANGE_POINT** `imbalance` value=-3042 d1=-24.0 d12=-16.0 z=0.47141756720430106
- **CHANGE_POINT** `wind_gen` value=3523 d1=-62.0 d12=176.0 z=0.3037176067251462
- **REVERSAL** `thermal_base` value=1.74e+04 d1=-74.0 d12=427.0 z=2.102511017578125
- **REVERSAL** `ccgt_gen` value=1.388e+04 d1=-74.0 d12=420.0 z=2.0856242122287703
- **PERSISTENT_UP** `ps_gen` value=448 d1=12.0 d12=100.0 z=1.9773199513157895
- **PERSISTENT_UP** `nuclear_gen` value=3511 d1=0.0 d12=7.0 z=0.5620747916666667
- **ACCELERATION** `nuclear_gen` value=3511 d1=0.0 d12=7.0 z=0.5620747916666667

## Nearest historical live analogues

- `2026-09-21T15:52:07.020346Z` distance=0.019 → {'next30m_imbalance_delta': 28.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T15:56:21.179145Z` distance=0.020 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:00:35.791303Z` distance=0.020 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:04:50.781494Z` distance=0.020 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:09:03.909955Z` distance=0.020 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': -4.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
