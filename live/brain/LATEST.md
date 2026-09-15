# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T15:56:36.878520Z`  
Memory snapshots: **262**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=6729 d1=302.0 d12=3519.0 z=13.008944889210019
- **CHANGE_POINT** `thermal_base` value=1.005e+04 d1=301.0 d12=3507.0 z=12.881077673040153
- **PERSISTENT_UP** `ccgt_gen` value=6729 d1=302.0 d12=3519.0 z=13.008944889210019
- **ROBUST_OUTLIER** `ccgt_gen` value=6729 d1=302.0 d12=3519.0 z=13.008944889210019
- **PERSISTENT_UP** `thermal_base` value=1.005e+04 d1=301.0 d12=3507.0 z=12.881077673040153
- **ROBUST_OUTLIER** `thermal_base` value=1.005e+04 d1=301.0 d12=3507.0 z=12.881077673040153
- **REVERSAL** `interconnector_net` value=5016 d1=84.0 d12=-1720.0 z=-10.719062105921052
- **ROBUST_OUTLIER** `interconnector_net` value=5016 d1=84.0 d12=-1720.0 z=-10.719062105921052
- **CHANGE_POINT** `nuclear_gen` value=3320 d1=-1.0 d12=-12.0 z=-1.7986393333333333
- **PERSISTENT_UP** `ps_gen` value=-134 d1=2.0 d12=145.0 z=3.4654818189655177
- **ROBUST_OUTLIER** `ps_gen` value=-134 d1=2.0 d12=145.0 z=3.4654818189655177
- **CHANGE_POINT** `margin` value=3.497e+04 d1=0.0 d12=344.0 z=-0.3646401169467787
- **PERSISTENT_DOWN** `nuclear_gen` value=3320 d1=-1.0 d12=-12.0 z=-1.7986393333333333
- **PERSISTENT_UP** `imbalance` value=5825 d1=8.0 d12=7.0 z=1.0406413285714287
- **ACCELERATION** `imbalance` value=5825 d1=8.0 d12=7.0 z=1.0406413285714287

## Nearest historical live analogues

- `2026-09-15T13:25:09.783150Z` distance=0.180 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:29:22.306019Z` distance=0.180 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:33:32.333732Z` distance=0.180 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:37:45.498739Z` distance=0.180 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:41:57.247780Z` distance=0.180 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
