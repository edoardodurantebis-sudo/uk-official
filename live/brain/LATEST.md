# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T12:19:19.796816Z`  
Memory snapshots: **1198**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1039 d1=1.0 d12=-46.0 z=-4.238726320287539
- **CHANGE_POINT** `wind_gen` value=1.448e+04 d1=187.0 d12=1814.0 z=3.3416797097839135
- **CHANGE_POINT** `ind_generation` value=2.562e+04 d1=0.0 d12=-48.0 z=-3.1175989296875
- **REVERSAL** `biomass_gen` value=1039 d1=1.0 d12=-46.0 z=-4.238726320287539
- **ROBUST_OUTLIER** `biomass_gen` value=1039 d1=1.0 d12=-46.0 z=-4.238726320287539
- **CHANGE_POINT** `ps_gen` value=-721 d1=2.0 d12=-124.0 z=-1.3871443171926006
- **PERSISTENT_UP** `wind_gen` value=1.448e+04 d1=187.0 d12=1814.0 z=3.3416797097839135
- **ROBUST_OUTLIER** `wind_gen` value=1.448e+04 d1=187.0 d12=1814.0 z=3.3416797097839135
- **ROBUST_OUTLIER** `ind_generation` value=2.562e+04 d1=0.0 d12=-48.0 z=-3.1175989296875
- **CHANGE_POINT** `margin` value=3.81e+04 d1=0.0 d12=-20.0 z=0.952716771875
- **CHANGE_POINT** `imbalance` value=8949 d1=0.0 d12=-48.0 z=-0.4573642853063344
- **REVERSAL** `ps_gen` value=-721 d1=2.0 d12=-124.0 z=-1.3871443171926006
- **PERSISTENT_DOWN** `ccgt_gen` value=2432 d1=-1.0 d12=-34.0 z=-1.1989853662123386
- **PERSISTENT_DOWN** `thermal_base` value=5767 d1=-3.0 d12=-33.0 z=-1.1940681594151212
- **REVERSAL** `nuclear_gen` value=3335 d1=-2.0 d12=1.0 z=0.0

## Nearest historical live analogues

- `2026-09-18T11:24:04.514292Z` distance=0.009 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T10:58:51.813919Z` distance=0.010 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:03:02.719756Z` distance=0.010 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:07:16.554570Z` distance=0.010 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T11:11:29.017632Z` distance=0.010 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': -2.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
