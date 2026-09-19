# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T23:19:40.870646Z`  
Memory snapshots: **1642**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **PERSISTENT_DOWN** `ps_gen` value=-259 d1=-72.0 d12=-243.0 z=-97.3963199
- **ROBUST_OUTLIER** `ps_gen` value=-259 d1=-72.0 d12=-243.0 z=-97.3963199
- **ROBUST_OUTLIER** `ind_demand` value=-1.189e+04 d1=0.0 d12=-14.0 z=-10.11734625
- **CHANGE_POINT** `wind_gen` value=1.595e+04 d1=138.0 d12=779.0 z=3.7671587586058517
- **CHANGE_POINT** `thermal_base` value=6862 d1=-64.0 d12=-1079.0 z=-3.375918347479424
- **CHANGE_POINT** `ccgt_gen` value=3526 d1=-62.0 d12=-1075.0 z=-3.360034828220859
- **CHANGE_POINT** `margin` value=3.606e+04 d1=0.0 d12=-9.0 z=-1.929040685
- **PERSISTENT_UP** `wind_gen` value=1.595e+04 d1=138.0 d12=779.0 z=3.7671587586058517
- **ROBUST_OUTLIER** `wind_gen` value=1.595e+04 d1=138.0 d12=779.0 z=3.7671587586058517
- **PERSISTENT_DOWN** `thermal_base` value=6862 d1=-64.0 d12=-1079.0 z=-3.375918347479424
- **ROBUST_OUTLIER** `thermal_base` value=6862 d1=-64.0 d12=-1079.0 z=-3.375918347479424
- **PERSISTENT_DOWN** `ccgt_gen` value=3526 d1=-62.0 d12=-1075.0 z=-3.360034828220859
- **ROBUST_OUTLIER** `ccgt_gen` value=3526 d1=-62.0 d12=-1075.0 z=-3.360034828220859
- **CHANGE_POINT** `imbalance` value=-3939 d1=0.0 d12=-24.0 z=-0.9757181820388349
- **CHANGE_POINT** `ind_generation` value=1.601e+04 d1=0.0 d12=-24.0 z=-0.9757181820388349

## Nearest historical live analogues

- `2026-09-19T21:22:12.336443Z` distance=0.013 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:26:23.241124Z` distance=0.013 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:30:37.100220Z` distance=0.013 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:34:48.991316Z` distance=0.013 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:38:58.734712Z` distance=0.013 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
