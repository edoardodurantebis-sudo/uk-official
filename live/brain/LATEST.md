# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T09:06:16.198660Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-10.0 z=-40.6380074375
- **PERSISTENT_DOWN** `ccgt_gen` value=2972 d1=-116.0 d12=-3394.0 z=-7.205467623916811
- **ROBUST_OUTLIER** `ccgt_gen` value=2972 d1=-116.0 d12=-3394.0 z=-7.205467623916811
- **PERSISTENT_DOWN** `thermal_base` value=6771 d1=-116.0 d12=-3404.0 z=-6.626222144471347
- **ROBUST_OUTLIER** `thermal_base` value=6771 d1=-116.0 d12=-3404.0 z=-6.626222144471347
- **ROBUST_OUTLIER** `margin` value=3.966e+04 d1=0.0 d12=883.0 z=5.945060097345133
- **PERSISTENT_UP** `interconnector_net` value=1.066e+04 d1=86.0 d12=3950.0 z=5.1924365561584365
- **ROBUST_OUTLIER** `interconnector_net` value=1.066e+04 d1=86.0 d12=3950.0 z=5.1924365561584365
- **ROBUST_OUTLIER** `imbalance` value=-7365 d1=0.0 d12=89.0 z=5.010495285714286
- **ROBUST_OUTLIER** `ind_generation` value=1.366e+04 d1=0.0 d12=-302.0 z=3.74035225
- **CHANGE_POINT** `ps_gen` value=-20 d1=-3.0 d12=80.0 z=-1.0632350738916256
- **CHANGE_POINT** `residual_proxy` value=1.329e+04 d1=0.0 d12=1087.0 z=0.35293068313953485
- **REVERSAL** `ps_gen` value=-20 d1=-3.0 d12=80.0 z=-1.0632350738916256
- **PERSISTENT_DOWN** `wind_gen` value=1.044e+04 d1=-116.0 d12=-183.0 z=0.7736006346306593
- **ACCELERATION** `wind_gen` value=1.044e+04 d1=-116.0 d12=-183.0 z=0.7736006346306593

## Nearest historical live analogues

- `2026-09-21T09:22:16.225384Z` distance=0.443 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:26:26.475864Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:30:39.158321Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:34:50.037660Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:39:02.425016Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
