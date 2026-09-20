# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T10:15:54.659344Z`  
Memory snapshots: **1797**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.601e+04 d1=0.0 d12=33.0 z=23.89379939375
- **ROBUST_OUTLIER** `ind_generation` value=1.601e+04 d1=0.0 d12=33.0 z=23.89379939375
- **CHANGE_POINT** `margin` value=3.929e+04 d1=0.0 d12=399.0 z=21.6817796
- **ROBUST_OUTLIER** `margin` value=3.929e+04 d1=0.0 d12=399.0 z=21.6817796
- **CHANGE_POINT** `imbalance` value=-4154 d1=0.0 d12=33.0 z=7.154506659919028
- **ROBUST_OUTLIER** `imbalance` value=-4154 d1=0.0 d12=33.0 z=7.154506659919028
- **CHANGE_POINT** `ind_demand` value=-1.236e+04 d1=0.0 d12=17.0 z=-4.384183375
- **CHANGE_POINT** `wind_gen` value=1.395e+04 d1=-88.0 d12=-996.0 z=-2.9916363552631577
- **ROBUST_OUTLIER** `ind_demand` value=-1.236e+04 d1=0.0 d12=17.0 z=-4.384183375
- **CHANGE_POINT** `ps_gen` value=-585 d1=-111.0 d12=347.0 z=1.3369350401785716
- **PERSISTENT_UP** `ccgt_gen` value=2460 d1=92.0 d12=18.0 z=-3.005555973901099
- **ACCELERATION** `ccgt_gen` value=2460 d1=92.0 d12=18.0 z=-3.005555973901099
- **ROBUST_OUTLIER** `ccgt_gen` value=2460 d1=92.0 d12=18.0 z=-3.005555973901099
- **PERSISTENT_UP** `thermal_base` value=5797 d1=91.0 d12=17.0 z=-2.9969086694139198
- **ACCELERATION** `thermal_base` value=5797 d1=91.0 d12=17.0 z=-2.9969086694139198

## Nearest historical live analogues

- `2026-09-20T09:20:07.153673Z` distance=0.143 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T07:22:31.595881Z` distance=0.456 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:26:42.911856Z` distance=0.456 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:30:56.792344Z` distance=0.456 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:35:11.628590Z` distance=0.456 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
