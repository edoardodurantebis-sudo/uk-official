# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T00:05:59.440118Z`  
Memory snapshots: **1653**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **PERSISTENT_UP** `ps_gen` value=-144 d1=109.0 d12=43.0 z=-56.56916207608696
- **ACCELERATION** `ps_gen` value=-144 d1=109.0 d12=43.0 z=-56.56916207608696
- **ROBUST_OUTLIER** `ps_gen` value=-144 d1=109.0 d12=43.0 z=-56.56916207608696
- **ROBUST_OUTLIER** `ind_demand` value=-1.189e+04 d1=0.0 d12=-1.0 z=-10.791836
- **CHANGE_POINT** `margin` value=3.599e+04 d1=0.0 d12=-65.0 z=-2.80587736
- **REVERSAL** `wind_gen` value=1.602e+04 d1=-116.0 d12=205.0 z=3.051005174364123
- **ACCELERATION** `wind_gen` value=1.602e+04 d1=-116.0 d12=205.0 z=3.051005174364123
- **ROBUST_OUTLIER** `wind_gen` value=1.602e+04 d1=-116.0 d12=205.0 z=3.051005174364123
- **CHANGE_POINT** `imbalance` value=-3708 d1=0.0 d12=231.0 z=0.9684981025641025
- **CHANGE_POINT** `ind_generation` value=1.624e+04 d1=0.0 d12=231.0 z=0.9684981025641025
- **REVERSAL** `thermal_base` value=6579 d1=90.0 d12=-347.0 z=-2.6359654568014705
- **REVERSAL** `ccgt_gen` value=3249 d1=100.0 d12=-339.0 z=-2.6123563621444204
- **CHANGE_POINT** `biomass_gen` value=884 d1=-3.0 d12=-26.0 z=-0.3626288978494624
- **PERSISTENT_DOWN** `interconnector_net` value=-8762 d1=-305.0 d12=-721.0 z=-1.2145773398449984
- **PERSISTENT_DOWN** `nuclear_gen` value=3330 d1=-10.0 d12=-8.0 z=-0.67448975

## Nearest historical live analogues

- `2026-09-19T19:24:22.442601Z` distance=0.160 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -119.0}
- `2026-09-19T19:28:35.593770Z` distance=0.160 → {'next30m_imbalance_delta': -36.0, 'next30m_margin_delta': 40.0, 'next30m_residual_proxy_delta': -119.0}
- `2026-09-19T18:21:25.144867Z` distance=0.165 → {'next30m_imbalance_delta': -611.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T18:25:36.560673Z` distance=0.165 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T18:29:47.180961Z` distance=0.165 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
