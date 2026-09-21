# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T18:04:07.054414Z`  
Memory snapshots: **2248**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=6590 d1=-29.0 d12=-1493.0 z=-13.457952136266094
- **PERSISTENT_DOWN** `interconnector_net` value=6590 d1=-29.0 d12=-1493.0 z=-13.457952136266094
- **ROBUST_OUTLIER** `interconnector_net` value=6590 d1=-29.0 d12=-1493.0 z=-13.457952136266094
- **CHANGE_POINT** `margin` value=3.617e+04 d1=0.0 d12=-106.0 z=-4.0469385
- **ROBUST_OUTLIER** `margin` value=3.617e+04 d1=0.0 d12=-106.0 z=-4.0469385
- **CHANGE_POINT** `wind_gen` value=3507 d1=-16.0 d12=203.0 z=-0.008286114864864866
- **REVERSAL** `thermal_base` value=1.728e+04 d1=-110.0 d12=356.0 z=1.7296353387367915
- **REVERSAL** `ccgt_gen` value=1.378e+04 d1=-107.0 d12=357.0 z=1.719350967896502
- **REVERSAL** `ps_gen` value=451 d1=3.0 d12=-439.0 z=1.209962528625954
- **PERSISTENT_DOWN** `ind_generation` value=1.842e+04 d1=0.0 d12=-16.0 z=0.5412572067901235
- **PERSISTENT_DOWN** `imbalance` value=-3042 d1=0.0 d12=-16.0 z=0.47141756720430106
- **PERSISTENT_DOWN** `nuclear_gen` value=3508 d1=-3.0 d12=-1.0 z=0.2697959
- **ACCELERATION** `nuclear_gen` value=3508 d1=-3.0 d12=-1.0 z=0.2697959
- **PERSISTENT_DOWN** `biomass_gen` value=2971 d1=-3.0 d12=-43.0 z=-0.1873582638888889
- **REVERSAL** `wind_gen` value=3507 d1=-16.0 d12=203.0 z=-0.008286114864864866

## Nearest historical live analogues

- `2026-09-21T15:52:07.020346Z` distance=0.019 → {'next30m_imbalance_delta': 28.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T15:56:21.179145Z` distance=0.020 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:00:35.791303Z` distance=0.020 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:04:50.781494Z` distance=0.020 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T16:09:03.909955Z` distance=0.020 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': -4.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
