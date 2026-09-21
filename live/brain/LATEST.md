# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T15:17:59.133401Z`  
Memory snapshots: **2209**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.328e+04 d1=101.0 d12=1738.0 z=3.2500368171506353
- **CHANGE_POINT** `ccgt_gen` value=9788 d1=105.0 d12=1741.0 z=3.1820396966814157
- **PERSISTENT_UP** `thermal_base` value=1.328e+04 d1=101.0 d12=1738.0 z=3.2500368171506353
- **ROBUST_OUTLIER** `thermal_base` value=1.328e+04 d1=101.0 d12=1738.0 z=3.2500368171506353
- **PERSISTENT_UP** `ccgt_gen` value=9788 d1=105.0 d12=1741.0 z=3.1820396966814157
- **ROBUST_OUTLIER** `ccgt_gen` value=9788 d1=105.0 d12=1741.0 z=3.1820396966814157
- **CHANGE_POINT** `ps_gen` value=-21 d1=0.0 d12=-15.0 z=-0.7390061608695653
- **CHANGE_POINT** `wind_gen` value=3346 d1=-20.0 d12=-1005.0 z=-0.6099232098290599
- **CHANGE_POINT** `interconnector_net` value=1.124e+04 d1=0.0 d12=-242.0 z=-0.02662459539473684
- **PERSISTENT_DOWN** `biomass_gen` value=2962 d1=-5.0 d12=-24.0 z=-1.3682506357142858
- **PERSISTENT_DOWN** `ps_gen` value=-21 d1=0.0 d12=-15.0 z=-0.7390061608695653
- **ACCELERATION** `ps_gen` value=-21 d1=0.0 d12=-15.0 z=-0.7390061608695653
- **PERSISTENT_DOWN** `wind_gen` value=3346 d1=-20.0 d12=-1005.0 z=-0.6099232098290599
- **ACCELERATION** `nuclear_gen` value=3495 d1=-4.0 d12=-3.0 z=-0.5781340714285713
- **PERSISTENT_DOWN** `interconnector_net` value=1.124e+04 d1=0.0 d12=-242.0 z=-0.02662459539473684

## Nearest historical live analogues

- `2026-09-21T14:23:01.446169Z` distance=0.004 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T13:57:37.194603Z` distance=0.006 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:01:53.716346Z` distance=0.006 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:06:06.412176Z` distance=0.006 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T14:10:22.067665Z` distance=0.006 → {'next30m_imbalance_delta': 32.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -22.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
