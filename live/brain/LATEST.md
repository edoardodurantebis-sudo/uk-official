# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T12:37:39.628217Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

Regime read: wind rising.

## Active patterns

- **CHANGE_POINT** `nuclear_gen` value=3737 d1=0.0 d12=59.0 z=19.335372833333334
- **PERSISTENT_UP** `nuclear_gen` value=3737 d1=0.0 d12=59.0 z=19.335372833333334
- **ROBUST_OUTLIER** `nuclear_gen` value=3737 d1=0.0 d12=59.0 z=19.335372833333334
- **CHANGE_POINT** `ps_gen` value=-126 d1=0.0 d12=-119.0 z=9.667686416666667
- **PERSISTENT_DOWN** `ps_gen` value=-126 d1=0.0 d12=-119.0 z=9.667686416666667
- **ROBUST_OUTLIER** `ps_gen` value=-126 d1=0.0 d12=-119.0 z=9.667686416666667
- **PERSISTENT_UP** `wind_forecast` value=1.308e+04 d1=0.0 d12=75.0 z=8.76836675
- **ACCELERATION** `wind_forecast` value=1.308e+04 d1=0.0 d12=75.0 z=8.76836675
- **ROBUST_OUTLIER** `wind_forecast` value=1.308e+04 d1=0.0 d12=75.0 z=8.76836675
- **CHANGE_POINT** `wind_gen` value=2643 d1=-63.0 d12=-908.0 z=-6.2998733350515455
- **PERSISTENT_DOWN** `wind_gen` value=2643 d1=-63.0 d12=-908.0 z=-6.2998733350515455
- **ROBUST_OUTLIER** `wind_gen` value=2643 d1=-63.0 d12=-908.0 z=-6.2998733350515455
- **CHANGE_POINT** `ind_generation` value=1.408e+04 d1=0.0 d12=-851.0 z=-1.0482169272093877
- **CHANGE_POINT** `imbalance` value=-7075 d1=0.0 d12=-851.0 z=-0.8606086790693904
- **CHANGE_POINT** `interconnector_net` value=1.104e+04 d1=24.0 d12=99.0 z=0.7424182200829383

## Nearest historical live analogues

- `2026-09-22T11:20:45.669526Z` distance=0.019 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:25:00.789915Z` distance=0.019 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:29:14.531873Z` distance=0.019 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:33:26.711703Z` distance=0.019 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:37:39.590020Z` distance=0.019 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
