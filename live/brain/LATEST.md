# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T01:04:25.209064Z`  
Memory snapshots: **2347**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.239e+04 d1=0.0 d12=-9.0 z=-12.429882535714286
- **ROBUST_OUTLIER** `ind_demand` value=-1.239e+04 d1=0.0 d12=-9.0 z=-12.429882535714286
- **CHANGE_POINT** `biomass_gen` value=3047 d1=1.0 d12=47.0 z=2.225816175
- **CHANGE_POINT** `nuclear_gen` value=3660 d1=-1.0 d12=10.0 z=0.7686045988372093
- **CHANGE_POINT** `ps_gen` value=-281 d1=0.0 d12=2.0 z=-0.6683802413949275
- **CHANGE_POINT** `imbalance` value=-2698 d1=0.0 d12=-688.0 z=-0.3531152220588235
- **CHANGE_POINT** `ind_generation` value=1.876e+04 d1=0.0 d12=-688.0 z=-0.3531152220588235
- **PERSISTENT_UP** `biomass_gen` value=3047 d1=1.0 d12=47.0 z=2.225816175
- **PERSISTENT_DOWN** `thermal_base` value=1.452e+04 d1=-128.0 d12=-379.0 z=-1.0025250770481144
- **PERSISTENT_DOWN** `ccgt_gen` value=1.086e+04 d1=-127.0 d12=-389.0 z=-0.9762351644736842
- **REVERSAL** `nuclear_gen` value=3660 d1=-1.0 d12=10.0 z=0.7686045988372093
- **PERSISTENT_UP** `interconnector_net` value=4058 d1=143.0 d12=378.0 z=-0.4357727626400834
- **ACCELERATION** `interconnector_net` value=4058 d1=143.0 d12=378.0 z=-0.4357727626400834
- **REVERSAL** `wind_gen` value=3644 d1=49.0 d12=-95.0 z=-0.3783722987804878
- **ACCELERATION** `wind_gen` value=3644 d1=49.0 d12=-95.0 z=-0.3783722987804878

## Nearest historical live analogues

- `2026-09-22T00:00:53.421899Z` distance=0.029 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T00:05:10.359292Z` distance=0.029 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T00:09:31.504316Z` distance=0.029 → {'next30m_imbalance_delta': 50.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T23:31:08.892013Z` distance=0.265 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 51.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T23:35:23.461931Z` distance=0.265 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 51.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
