# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T07:09:19.225959Z`  
Memory snapshots: **783**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=2.646e+04 d1=0.0 d12=54.0 z=17.64552216935484
- **ROBUST_OUTLIER** `imbalance` value=7338 d1=0.0 d12=54.0 z=9.9264529245283
- **CHANGE_POINT** `ind_demand` value=-1.213e+04 d1=0.0 d12=-674.0 z=-6.668745431451613
- **ROBUST_OUTLIER** `ind_demand` value=-1.213e+04 d1=0.0 d12=-674.0 z=-6.668745431451613
- **CHANGE_POINT** `margin` value=3.573e+04 d1=0.0 d12=-42.0 z=-3.2844718260869565
- **CHANGE_POINT** `ps_gen` value=219 d1=-7.0 d12=-236.0 z=1.496298460385439
- **ROBUST_OUTLIER** `margin` value=3.573e+04 d1=0.0 d12=-42.0 z=-3.2844718260869565
- **CHANGE_POINT** `wind_gen` value=1.4e+04 d1=0.0 d12=149.0 z=0.7782574038461538
- **PERSISTENT_UP** `interconnector_net` value=-1762 d1=2183.0 d12=5012.0 z=2.4875062996141124
- **ACCELERATION** `interconnector_net` value=-1762 d1=2183.0 d12=5012.0 z=2.4875062996141124
- **PERSISTENT_DOWN** `ps_gen` value=219 d1=-7.0 d12=-236.0 z=1.496298460385439
- **REVERSAL** `thermal_base` value=7840 d1=-476.0 d12=31.0 z=1.0432701743674369
- **ACCELERATION** `thermal_base` value=7840 d1=-476.0 d12=31.0 z=1.0432701743674369
- **REVERSAL** `ccgt_gen` value=4530 d1=-472.0 d12=34.0 z=1.0432009415477497
- **ACCELERATION** `ccgt_gen` value=4530 d1=-472.0 d12=34.0 z=1.0432009415477497

## Nearest historical live analogues

- `2026-09-16T00:52:57.444665Z` distance=0.797 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T00:57:07.708523Z` distance=0.797 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:01:32.433373Z` distance=0.797 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:05:42.750302Z` distance=0.797 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T01:09:54.472696Z` distance=0.797 → {'next30m_imbalance_delta': -39.0, 'next30m_margin_delta': 377.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
