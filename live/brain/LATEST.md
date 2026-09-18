# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T01:29:09.319659Z`  
Memory snapshots: **1044**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=1.013e+04 d1=0.0 d12=13.0 z=28.058773600000002
- **CHANGE_POINT** `ind_generation` value=2.694e+04 d1=0.0 d12=13.0 z=28.058773600000002
- **ROBUST_OUTLIER** `imbalance` value=1.013e+04 d1=0.0 d12=13.0 z=28.058773600000002
- **ROBUST_OUTLIER** `ind_generation` value=2.694e+04 d1=0.0 d12=13.0 z=28.058773600000002
- **ACCELERATION** `ind_demand` value=-1.119e+04 d1=0.0 d12=-5.0 z=-10.454591125
- **ROBUST_OUTLIER** `ind_demand` value=-1.119e+04 d1=0.0 d12=-5.0 z=-10.454591125
- **CHANGE_POINT** `margin` value=3.67e+04 d1=0.0 d12=162.0 z=2.545244339622642
- **CHANGE_POINT** `ps_gen` value=496 d1=187.0 d12=200.0 z=0.6623367815315315
- **PERSISTENT_UP** `margin` value=3.67e+04 d1=0.0 d12=162.0 z=2.545244339622642
- **ACCELERATION** `margin` value=3.67e+04 d1=0.0 d12=162.0 z=2.545244339622642
- **REVERSAL** `nuclear_gen` value=3329 d1=-3.0 d12=7.0 z=1.7986393333333333
- **ACCELERATION** `nuclear_gen` value=3329 d1=-3.0 d12=7.0 z=1.7986393333333333
- **PERSISTENT_DOWN** `wind_gen` value=1.409e+04 d1=-38.0 d12=-167.0 z=-1.7771416520584329
- **PERSISTENT_UP** `ccgt_gen` value=3805 d1=98.0 d12=39.0 z=-0.7267323862378977
- **ACCELERATION** `ccgt_gen` value=3805 d1=98.0 d12=39.0 z=-0.7267323862378977

## Nearest historical live analogues

- `2026-09-18T00:25:46.059957Z` distance=0.074 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:29:58.615763Z` distance=0.074 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:34:09.969710Z` distance=0.074 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 62.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:21:32.376170Z` distance=0.075 → {'next30m_imbalance_delta': -25.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:04:42.630537Z` distance=0.087 → {'next30m_imbalance_delta': -25.0, 'next30m_margin_delta': 27.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
