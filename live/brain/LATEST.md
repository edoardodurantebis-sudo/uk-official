# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T01:18:14.502131Z`  
Memory snapshots: **395**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.216e+04 d1=0.0 d12=-64.0 z=-55.08332958333333
- **ROBUST_OUTLIER** `ind_demand` value=-1.216e+04 d1=0.0 d12=-64.0 z=-55.08332958333333
- **ROBUST_OUTLIER** `imbalance` value=5999 d1=0.0 d12=-36.0 z=4.170436623239437
- **ROBUST_OUTLIER** `ind_generation` value=2.512e+04 d1=0.0 d12=-36.0 z=4.170436623239437
- **CHANGE_POINT** `interconnector_net` value=4409 d1=-37.0 d12=387.0 z=1.0903897452175053
- **CHANGE_POINT** `ccgt_gen` value=3244 d1=-2.0 d12=16.0 z=-0.6374468346681922
- **CHANGE_POINT** `frequency` value=49.97 d1=0.0 d12=0.0 z=None
- **CHANGE_POINT** `frequency_abs_dev` value=0.028 d1=0.0 d12=0.0 z=None
- **REVERSAL** `interconnector_net` value=4409 d1=-37.0 d12=387.0 z=1.0903897452175053
- **ACCELERATION** `interconnector_net` value=4409 d1=-37.0 d12=387.0 z=1.0903897452175053
- **REVERSAL** `thermal_base` value=6569 d1=-5.0 d12=4.0 z=-0.6391936859243698
- **ACCELERATION** `thermal_base` value=6569 d1=-5.0 d12=4.0 z=-0.6391936859243698
- **REVERSAL** `ccgt_gen` value=3244 d1=-2.0 d12=16.0 z=-0.6374468346681922
- **PERSISTENT_DOWN** `wind_gen` value=1.034e+04 d1=-63.0 d12=-307.0 z=-0.5828308770310192
- **PERSISTENT_UP** `ps_gen` value=224 d1=0.0 d12=86.0 z=0.2588950555555556

## Nearest historical live analogues

- `2026-09-16T00:23:43.289309Z` distance=0.133 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T23:49:36.074086Z` distance=0.162 → {'next30m_imbalance_delta': 39.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T23:53:48.658666Z` distance=0.164 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T23:57:59.720980Z` distance=0.164 → {'next30m_imbalance_delta': 170.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T00:02:10.447040Z` distance=0.164 → {'next30m_imbalance_delta': 170.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
