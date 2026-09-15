# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T16:13:30.609678Z`  
Memory snapshots: **266**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=8176 d1=802.0 d12=3814.0 z=16.769972512524088
- **CHANGE_POINT** `thermal_base` value=1.15e+04 d1=803.0 d12=3811.0 z=16.618498888145314
- **PERSISTENT_UP** `ccgt_gen` value=8176 d1=802.0 d12=3814.0 z=16.769972512524088
- **ROBUST_OUTLIER** `ccgt_gen` value=8176 d1=802.0 d12=3814.0 z=16.769972512524088
- **PERSISTENT_UP** `thermal_base` value=1.15e+04 d1=803.0 d12=3811.0 z=16.618498888145314
- **ROBUST_OUTLIER** `thermal_base` value=1.15e+04 d1=803.0 d12=3811.0 z=16.618498888145314
- **PERSISTENT_DOWN** `interconnector_net` value=2598 d1=-617.0 d12=-3894.0 z=-15.010946883552633
- **ROBUST_OUTLIER** `interconnector_net` value=2598 d1=-617.0 d12=-3894.0 z=-15.010946883552633
- **CHANGE_POINT** `imbalance` value=5825 d1=0.0 d12=8.0 z=1.087886693548387
- **REVERSAL** `ps_gen` value=129 d1=-96.0 d12=227.0 z=3.0407781704545456
- **ACCELERATION** `ps_gen` value=129 d1=-96.0 d12=227.0 z=3.0407781704545456
- **ROBUST_OUTLIER** `ps_gen` value=129 d1=-96.0 d12=227.0 z=3.0407781704545456
- **CHANGE_POINT** `ind_generation` value=2.495e+04 d1=0.0 d12=8.0 z=1.023998075
- **CHANGE_POINT** `margin` value=3.497e+04 d1=0.0 d12=320.0 z=-0.3646401169467787
- **REVERSAL** `nuclear_gen` value=3322 d1=1.0 d12=-3.0 z=-1.3489794999999998

## Nearest historical live analogues

- `2026-09-15T13:25:09.783150Z` distance=0.184 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:29:22.306019Z` distance=0.184 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:33:32.333732Z` distance=0.184 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:37:45.498739Z` distance=0.184 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T13:41:57.247780Z` distance=0.184 → {'next30m_imbalance_delta': 12.0, 'next30m_margin_delta': 37.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
