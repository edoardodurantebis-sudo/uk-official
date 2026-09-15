# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T18:20:25.201646Z`  
Memory snapshots: **296**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=3261 d1=0.0 d12=163.0 z=46.570451375
- **ROBUST_OUTLIER** `biomass_gen` value=3261 d1=0.0 d12=163.0 z=46.570451375
- **CHANGE_POINT** `ccgt_gen` value=1.07e+04 d1=0.0 d12=295.0 z=5.025658301921317
- **CHANGE_POINT** `thermal_base` value=1.401e+04 d1=0.0 d12=286.0 z=5.013799664266118
- **PERSISTENT_UP** `ccgt_gen` value=1.07e+04 d1=0.0 d12=295.0 z=5.025658301921317
- **ROBUST_OUTLIER** `ccgt_gen` value=1.07e+04 d1=0.0 d12=295.0 z=5.025658301921317
- **PERSISTENT_UP** `thermal_base` value=1.401e+04 d1=0.0 d12=286.0 z=5.013799664266118
- **ROBUST_OUTLIER** `thermal_base` value=1.401e+04 d1=0.0 d12=286.0 z=5.013799664266118
- **CHANGE_POINT** `margin` value=3.566e+04 d1=-16.0 d12=835.0 z=2.206545039285714
- **CHANGE_POINT** `ps_gen` value=804 d1=0.0 d12=304.0 z=1.0839835270570792
- **REVERSAL** `margin` value=3.566e+04 d1=-16.0 d12=835.0 z=2.206545039285714
- **CHANGE_POINT** `imbalance` value=5775 d1=0.0 d12=3.0 z=0.03679034999999999
- **CHANGE_POINT** `ind_generation` value=2.49e+04 d1=0.0 d12=3.0 z=0.03679034999999999
- **PERSISTENT_UP** `ps_gen` value=804 d1=0.0 d12=304.0 z=1.0839835270570792
- **PERSISTENT_DOWN** `wind_gen` value=1.004e+04 d1=0.0 d12=-567.0 z=-1.0028384772182255

## Nearest historical live analogues

- `2026-09-15T11:22:30.581865Z` distance=0.180 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:26:42.593420Z` distance=0.180 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:30:55.285075Z` distance=0.180 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:35:06.452199Z` distance=0.180 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:39:18.571623Z` distance=0.180 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
