# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T12:53:00.200547Z`  
Memory snapshots: **2175**  
Current physical regime: **BALANCED**

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=4.0 z=14.890658326923075
- **CHANGE_POINT** `ps_gen` value=228 d1=0.0 d12=120.0 z=7.001845976190476
- **ROBUST_OUTLIER** `ps_gen` value=228 d1=0.0 d12=120.0 z=7.001845976190476
- **ROBUST_OUTLIER** `demand_forecast` value=2.1e+04 d1=0.0 d12=0.0 z=5.481762150000001
- **CHANGE_POINT** `thermal_base` value=9433 d1=-16.0 d12=-622.0 z=-1.3602680313807531
- **CHANGE_POINT** `ccgt_gen` value=5930 d1=-10.0 d12=-616.0 z=-1.3517782126556017
- **CHANGE_POINT** `margin` value=3.627e+04 d1=-406.0 d12=-402.0 z=-0.9042609835164835
- **CHANGE_POINT** `wind_gen` value=3870 d1=-73.0 d12=246.0 z=0.5258177791734198
- **CHANGE_POINT** `ind_generation` value=1.817e+04 d1=0.0 d12=-319.0 z=-0.2852230591755319
- **CHANGE_POINT** `imbalance` value=-3333 d1=0.0 d12=-319.0 z=-0.25174617429577467
- **PERSISTENT_DOWN** `thermal_base` value=9433 d1=-16.0 d12=-622.0 z=-1.3602680313807531
- **PERSISTENT_DOWN** `ccgt_gen` value=5930 d1=-10.0 d12=-616.0 z=-1.3517782126556017
- **REVERSAL** `interconnector_net` value=1.131e+04 d1=23.0 d12=-55.0 z=1.1505466180836708
- **PERSISTENT_DOWN** `margin` value=3.627e+04 d1=-406.0 d12=-402.0 z=-0.9042609835164835
- **ACCELERATION** `margin` value=3.627e+04 d1=-406.0 d12=-402.0 z=-0.9042609835164835

## Nearest historical live analogues

- `2026-09-21T11:24:15.280087Z` distance=0.101 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 182.0, 'next30m_residual_proxy_delta': -104.0}
- `2026-09-21T11:28:26.888729Z` distance=0.101 → {'next30m_imbalance_delta': 1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 178.0, 'next30m_residual_proxy_delta': -104.0}
- `2026-09-21T10:54:44.355248Z` distance=0.101 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:58:55.909932Z` distance=0.101 → {'next30m_imbalance_delta': 856.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T11:03:12.814990Z` distance=0.101 → {'next30m_imbalance_delta': 856.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
