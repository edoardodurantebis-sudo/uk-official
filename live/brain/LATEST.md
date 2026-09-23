# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T09:02:01.425332Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **PERSISTENT_DOWN** `ind_demand` value=-1.266e+04 d1=0.0 d12=-10.0 z=-40.6380074375
- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-10.0 z=-40.6380074375
- **PERSISTENT_DOWN** `ccgt_gen` value=3088 d1=-312.0 d12=-3278.0 z=-7.317155171300448
- **ROBUST_OUTLIER** `ccgt_gen` value=3088 d1=-312.0 d12=-3278.0 z=-7.317155171300448
- **PERSISTENT_DOWN** `thermal_base` value=6887 d1=-312.0 d12=-3288.0 z=-6.568847973083197
- **ROBUST_OUTLIER** `thermal_base` value=6887 d1=-312.0 d12=-3288.0 z=-6.568847973083197
- **PERSISTENT_UP** `margin` value=3.966e+04 d1=0.0 d12=883.0 z=5.945060097345133
- **ROBUST_OUTLIER** `margin` value=3.966e+04 d1=0.0 d12=883.0 z=5.945060097345133
- **PERSISTENT_UP** `interconnector_net` value=1.058e+04 d1=604.0 d12=3864.0 z=5.160962807650569
- **ROBUST_OUTLIER** `interconnector_net` value=1.058e+04 d1=604.0 d12=3864.0 z=5.160962807650569
- **ROBUST_OUTLIER** `imbalance` value=-7365 d1=0.0 d12=89.0 z=5.010495285714286
- **PERSISTENT_DOWN** `ind_generation` value=1.366e+04 d1=0.0 d12=-302.0 z=3.74035225
- **ROBUST_OUTLIER** `ind_generation` value=1.366e+04 d1=0.0 d12=-302.0 z=3.74035225
- **CHANGE_POINT** `ps_gen` value=-17 d1=0.0 d12=83.0 z=-1.1831831368715084
- **CHANGE_POINT** `wind_gen` value=1.056e+04 d1=-14.0 d12=-67.0 z=0.8326061166277259

## Nearest historical live analogues

- `2026-09-21T09:22:16.225384Z` distance=0.443 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:26:26.475864Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:30:39.158321Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:34:50.037660Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:39:02.425016Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
