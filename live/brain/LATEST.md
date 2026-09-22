# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T08:39:15.667270Z`  
Memory snapshots: **2454**  
Current physical regime: **LOOSE**

Regime read: margin high, wind rising.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.9e+04 d1=0.0 d12=1221.0 z=74.1938725
- **ROBUST_OUTLIER** `ind_demand` value=-1.28e+04 d1=0.0 d12=-110.0 z=-8.739041108695652
- **ROBUST_OUTLIER** `imbalance` value=-1355 d1=0.0 d12=2476.0 z=6.315676750000001
- **CHANGE_POINT** `biomass_gen` value=3049 d1=2.0 d12=18.0 z=4.0469385
- **ROBUST_OUTLIER** `ind_generation` value=1.971e+04 d1=0.0 d12=1837.0 z=4.983729819444444
- **PERSISTENT_UP** `biomass_gen` value=3049 d1=2.0 d12=18.0 z=4.0469385
- **ROBUST_OUTLIER** `biomass_gen` value=3049 d1=2.0 d12=18.0 z=4.0469385
- **CHANGE_POINT** `wind_gen` value=3744 d1=-17.0 d12=253.0 z=1.2534509087982832
- **CHANGE_POINT** `thermal_base` value=1.593e+04 d1=-126.0 d12=-1467.0 z=-0.6392448962602459
- **CHANGE_POINT** `ccgt_gen` value=1.228e+04 d1=-124.0 d12=-1470.0 z=-0.6372479846625767
- **CHANGE_POINT** `ps_gen` value=-171 d1=-1.0 d12=1.0 z=0.14988661111111112
- **PERSISTENT_UP** `interconnector_net` value=9435 d1=24.0 d12=2378.0 z=1.887821271683876
- **ACCELERATION** `interconnector_net` value=9435 d1=24.0 d12=2378.0 z=1.887821271683876
- **PERSISTENT_DOWN** `residual_proxy` value=7927 d1=0.0 d12=-464.0 z=-1.345103122126437
- **REVERSAL** `wind_gen` value=3744 d1=-17.0 d12=253.0 z=1.2534509087982832

## Nearest historical live analogues

- `2026-09-21T09:47:25.921035Z` distance=0.527 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T09:22:16.225384Z` distance=0.529 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:26:26.475864Z` distance=0.529 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:30:39.158321Z` distance=0.529 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:34:50.037660Z` distance=0.529 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
