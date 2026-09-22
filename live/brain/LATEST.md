# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T23:52:08.319514Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.371e+04 d1=61.0 d12=-75.0 z=-8.685564939258311
- **CHANGE_POINT** `ccgt_gen` value=9983 d1=62.0 d12=-67.0 z=-8.612583584390864
- **REVERSAL** `thermal_base` value=1.371e+04 d1=61.0 d12=-75.0 z=-8.685564939258311
- **ROBUST_OUTLIER** `thermal_base` value=1.371e+04 d1=61.0 d12=-75.0 z=-8.685564939258311
- **REVERSAL** `ccgt_gen` value=9983 d1=62.0 d12=-67.0 z=-8.612583584390864
- **ROBUST_OUTLIER** `ccgt_gen` value=9983 d1=62.0 d12=-67.0 z=-8.612583584390864
- **REVERSAL** `ind_demand` value=-1.249e+04 d1=-2.0 d12=7.0 z=-5.395918
- **ROBUST_OUTLIER** `ind_demand` value=-1.249e+04 d1=-2.0 d12=7.0 z=-5.395918
- **CHANGE_POINT** `interconnector_net` value=4202 d1=-1.0 d12=-947.0 z=-1.5634181179971989
- **CHANGE_POINT** `imbalance` value=-7998 d1=51.0 d12=58.0 z=1.5076829705882353
- **CHANGE_POINT** `ind_generation` value=1.318e+04 d1=51.0 d12=58.0 z=1.5076829705882353
- **PERSISTENT_UP** `wind_gen` value=3650 d1=355.0 d12=643.0 z=2.651327609876543
- **ACCELERATION** `wind_gen` value=3650 d1=355.0 d12=643.0 z=2.651327609876543
- **PERSISTENT_UP** `imbalance` value=-7998 d1=51.0 d12=58.0 z=1.5076829705882353
- **ACCELERATION** `imbalance` value=-7998 d1=51.0 d12=58.0 z=1.5076829705882353

## Nearest historical live analogues

- `2026-09-22T22:53:13.778957Z` distance=0.025 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:57:26.907882Z` distance=0.025 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:50:58.019212Z` distance=0.025 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:19:30.437012Z` distance=0.025 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T22:23:43.484966Z` distance=0.025 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
