# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T05:15:52.483890Z`  
Memory snapshots: **2406**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.779e+04 d1=0.0 d12=0.0 z=16.07448091221374
- **CHANGE_POINT** `ccgt_gen` value=1.35e+04 d1=29.0 d12=967.0 z=5.7655536257062145
- **CHANGE_POINT** `thermal_base` value=1.716e+04 d1=30.0 d12=972.0 z=5.628159891941392
- **PERSISTENT_UP** `ccgt_gen` value=1.35e+04 d1=29.0 d12=967.0 z=5.7655536257062145
- **ROBUST_OUTLIER** `ccgt_gen` value=1.35e+04 d1=29.0 d12=967.0 z=5.7655536257062145
- **PERSISTENT_UP** `thermal_base` value=1.716e+04 d1=30.0 d12=972.0 z=5.628159891941392
- **ROBUST_OUTLIER** `thermal_base` value=1.716e+04 d1=30.0 d12=972.0 z=5.628159891941392
- **PERSISTENT_UP** `interconnector_net` value=-3049 d1=51.0 d12=86.0 z=-5.038499564501511
- **ACCELERATION** `interconnector_net` value=-3049 d1=51.0 d12=86.0 z=-5.038499564501511
- **ROBUST_OUTLIER** `interconnector_net` value=-3049 d1=51.0 d12=86.0 z=-5.038499564501511
- **CHANGE_POINT** `imbalance` value=-3312 d1=0.0 d12=12.0 z=-2.8406395240384614
- **CHANGE_POINT** `ind_generation` value=1.815e+04 d1=0.0 d12=12.0 z=-2.8406395240384614
- **CHANGE_POINT** `ind_demand` value=-1.252e+04 d1=0.0 d12=-3.0 z=-2.4088919642857145
- **CHANGE_POINT** `biomass_gen` value=3030 d1=1.0 d12=2.0 z=-0.92742340625
- **PERSISTENT_DOWN** `wind_gen` value=3439 d1=-17.0 d12=-37.0 z=-1.8775270233918129

## Nearest historical live analogues

- `2026-09-22T04:20:42.395983Z` distance=0.003 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:55:16.196094Z` distance=0.021 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:59:30.332417Z` distance=0.021 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T04:03:43.712214Z` distance=0.021 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T04:08:00.116133Z` distance=0.021 → {'next30m_imbalance_delta': -88.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
