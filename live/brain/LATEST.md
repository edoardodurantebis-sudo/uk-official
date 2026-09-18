# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T01:46:29.644406Z`  
Memory snapshots: **1048**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=1.013e+04 d1=0.0 d12=-2.0 z=14.714526388157893
- **CHANGE_POINT** `ind_generation` value=2.694e+04 d1=0.0 d12=-2.0 z=14.714526388157893
- **ROBUST_OUTLIER** `imbalance` value=1.013e+04 d1=0.0 d12=-2.0 z=14.714526388157893
- **ROBUST_OUTLIER** `ind_generation` value=2.694e+04 d1=0.0 d12=-2.0 z=14.714526388157893
- **ROBUST_OUTLIER** `ind_demand` value=-1.119e+04 d1=0.0 d12=31.0 z=-10.454591125
- **CHANGE_POINT** `margin` value=3.67e+04 d1=0.0 d12=100.0 z=2.545244339622642
- **PERSISTENT_UP** `nuclear_gen` value=3337 d1=3.0 d12=11.0 z=3.0833817142857143
- **ROBUST_OUTLIER** `nuclear_gen` value=3337 d1=3.0 d12=11.0 z=3.0833817142857143
- **PERSISTENT_UP** `wind_gen` value=1.421e+04 d1=89.0 d12=108.0 z=-1.3693001645422944
- **ACCELERATION** `wind_gen` value=1.421e+04 d1=89.0 d12=108.0 z=-1.3693001645422944
- **REVERSAL** `ccgt_gen` value=3744 d1=54.0 d12=-43.0 z=-0.790541662867647
- **ACCELERATION** `ccgt_gen` value=3744 d1=54.0 d12=-43.0 z=-0.790541662867647
- **REVERSAL** `thermal_base` value=7081 d1=57.0 d12=-32.0 z=-0.7754134014814815
- **ACCELERATION** `thermal_base` value=7081 d1=57.0 d12=-32.0 z=-0.7754134014814815
- **REVERSAL** `ps_gen` value=533 d1=-1.0 d12=237.0 z=0.7722418876811594

## Nearest historical live analogues

- `2026-09-18T00:50:53.445195Z` distance=0.046 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:25:46.059957Z` distance=0.074 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:29:58.615763Z` distance=0.074 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:34:09.969710Z` distance=0.074 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:38:21.465575Z` distance=0.074 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 62.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
