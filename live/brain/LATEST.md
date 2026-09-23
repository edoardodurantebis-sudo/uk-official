# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T10:05:31.997058Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-3948 d1=0.0 d12=3417.0 z=15.723546348529412
- **CHANGE_POINT** `ind_demand` value=-1.27e+04 d1=0.0 d12=-37.0 z=-15.625679208333333
- **CHANGE_POINT** `ind_generation` value=1.708e+04 d1=0.0 d12=3417.0 z=15.336612172619049
- **PERSISTENT_UP** `imbalance` value=-3948 d1=0.0 d12=3417.0 z=15.723546348529412
- **ROBUST_OUTLIER** `imbalance` value=-3948 d1=0.0 d12=3417.0 z=15.723546348529412
- **PERSISTENT_DOWN** `ind_demand` value=-1.27e+04 d1=0.0 d12=-37.0 z=-15.625679208333333
- **ROBUST_OUTLIER** `ind_demand` value=-1.27e+04 d1=0.0 d12=-37.0 z=-15.625679208333333
- **PERSISTENT_UP** `ind_generation` value=1.708e+04 d1=0.0 d12=3417.0 z=15.336612172619049
- **ROBUST_OUTLIER** `ind_generation` value=1.708e+04 d1=0.0 d12=3417.0 z=15.336612172619049
- **CHANGE_POINT** `margin` value=4.071e+04 d1=0.0 d12=1051.0 z=6.3944273357843135
- **ROBUST_OUTLIER** `margin` value=4.071e+04 d1=0.0 d12=1051.0 z=6.3944273357843135
- **CHANGE_POINT** `ps_gen` value=-688 d1=0.0 d12=-669.0 z=-3.017454144736842
- **PERSISTENT_UP** `interconnector_net` value=1.163e+04 d1=0.0 d12=873.0 z=4.953667148655198
- **ROBUST_OUTLIER** `interconnector_net` value=1.163e+04 d1=0.0 d12=873.0 z=4.953667148655198
- **PERSISTENT_DOWN** `ccgt_gen` value=2130 d1=0.0 d12=-842.0 z=-3.7523847195576

## Nearest historical live analogues

- `2026-09-21T10:33:45.224867Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:37:58.343383Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:42:10.019375Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:46:20.592599Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:50:33.489846Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
