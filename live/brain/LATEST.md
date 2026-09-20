# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T10:07:29.221359Z`  
Memory snapshots: **1795**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.929e+04 d1=0.0 d12=1799.0 z=27.1022245
- **ROBUST_OUTLIER** `margin` value=3.929e+04 d1=0.0 d12=1799.0 z=27.1022245
- **CHANGE_POINT** `ind_generation` value=1.601e+04 d1=0.0 d12=2941.0 z=23.89379939375
- **ROBUST_OUTLIER** `ind_generation` value=1.601e+04 d1=0.0 d12=2941.0 z=23.89379939375
- **CHANGE_POINT** `imbalance` value=-4154 d1=0.0 d12=2941.0 z=7.154506659919028
- **ROBUST_OUTLIER** `imbalance` value=-4154 d1=0.0 d12=2941.0 z=7.154506659919028
- **CHANGE_POINT** `ind_demand` value=-1.236e+04 d1=0.0 d12=-60.0 z=-4.384183375
- **CHANGE_POINT** `wind_gen` value=1.412e+04 d1=-229.0 d12=-815.0 z=-2.6343888797923323
- **ROBUST_OUTLIER** `ind_demand` value=-1.236e+04 d1=0.0 d12=-60.0 z=-4.384183375
- **REVERSAL** `thermal_base` value=5629 d1=1.0 d12=-146.0 z=-3.6103501734496124
- **ROBUST_OUTLIER** `thermal_base` value=5629 d1=1.0 d12=-146.0 z=-3.6103501734496124
- **REVERSAL** `ccgt_gen` value=2293 d1=5.0 d12=-147.0 z=-3.6029211163127415
- **ROBUST_OUTLIER** `ccgt_gen` value=2293 d1=5.0 d12=-147.0 z=-3.6029211163127415
- **PERSISTENT_DOWN** `wind_gen` value=1.412e+04 d1=-229.0 d12=-815.0 z=-2.6343888797923323
- **CHANGE_POINT** `biomass_gen` value=618 d1=32.0 d12=32.0 z=-0.6050240282392026

## Nearest historical live analogues

- `2026-09-20T07:22:31.595881Z` distance=0.454 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:26:42.911856Z` distance=0.454 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:30:56.792344Z` distance=0.454 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:35:11.628590Z` distance=0.454 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}
- `2026-09-20T07:39:23.525158Z` distance=0.454 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1162.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
