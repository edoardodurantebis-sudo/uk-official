# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T17:59:22.215947Z`  
Memory snapshots: **291**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=3206 d1=2.0 d12=310.0 z=56.59932559285714
- **ROBUST_OUTLIER** `biomass_gen` value=3206 d1=2.0 d12=310.0 z=56.59932559285714
- **CHANGE_POINT** `ccgt_gen` value=1.041e+04 d1=-17.0 d12=31.0 z=9.643473964102563
- **CHANGE_POINT** `thermal_base` value=1.372e+04 d1=-18.0 d12=21.0 z=9.587636241908008
- **REVERSAL** `ccgt_gen` value=1.041e+04 d1=-17.0 d12=31.0 z=9.643473964102563
- **ACCELERATION** `ccgt_gen` value=1.041e+04 d1=-17.0 d12=31.0 z=9.643473964102563
- **ROBUST_OUTLIER** `ccgt_gen` value=1.041e+04 d1=-17.0 d12=31.0 z=9.643473964102563
- **REVERSAL** `thermal_base` value=1.372e+04 d1=-18.0 d12=21.0 z=9.587636241908008
- **ACCELERATION** `thermal_base` value=1.372e+04 d1=-18.0 d12=21.0 z=9.587636241908008
- **ROBUST_OUTLIER** `thermal_base` value=1.372e+04 d1=-18.0 d12=21.0 z=9.587636241908008
- **CHANGE_POINT** `nuclear_gen` value=3312 d1=-1.0 d12=-10.0 z=-2.5293365625
- **CHANGE_POINT** `margin` value=3.567e+04 d1=0.0 d12=842.0 z=2.2579347345238094
- **PERSISTENT_DOWN** `nuclear_gen` value=3312 d1=-1.0 d12=-10.0 z=-2.5293365625
- **PERSISTENT_UP** `margin` value=3.567e+04 d1=0.0 d12=842.0 z=2.2579347345238094
- **REVERSAL** `interconnector_net` value=-1797 d1=1.0 d12=-1286.0 z=-2.1046716088086983

## Nearest historical live analogues

- `2026-09-15T11:22:30.581865Z` distance=0.186 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:26:42.593420Z` distance=0.186 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:30:55.285075Z` distance=0.186 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:35:06.452199Z` distance=0.186 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:39:18.571623Z` distance=0.186 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
