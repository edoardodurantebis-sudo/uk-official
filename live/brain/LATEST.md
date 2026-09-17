# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T01:49:11.431313Z`  
Memory snapshots: **707**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2389 d1=-150.0 d12=-815.0 z=-275.529062875
- **PERSISTENT_DOWN** `biomass_gen` value=2389 d1=-150.0 d12=-815.0 z=-275.529062875
- **ROBUST_OUTLIER** `biomass_gen` value=2389 d1=-150.0 d12=-815.0 z=-275.529062875
- **ROBUST_OUTLIER** `ind_demand` value=-1.165e+04 d1=0.0 d12=100.0 z=16.32265195
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `ccgt_gen` value=4065 d1=4.0 d12=-457.0 z=-2.9688457190026956
- **CHANGE_POINT** `thermal_base` value=7377 d1=4.0 d12=-455.0 z=-2.9603781407440612
- **ROBUST_OUTLIER** `interconnector_net` value=-6663 d1=0.0 d12=17.0 z=-3.327829325305074
- **REVERSAL** `ccgt_gen` value=4065 d1=4.0 d12=-457.0 z=-2.9688457190026956
- **REVERSAL** `thermal_base` value=7377 d1=4.0 d12=-455.0 z=-2.9603781407440612
- **CHANGE_POINT** `ps_gen` value=-308 d1=0.0 d12=-2.0 z=-0.7059970566608996
- **PERSISTENT_UP** `wind_gen` value=1.306e+04 d1=55.0 d12=803.0 z=1.1535866304664721
- **PERSISTENT_UP** `margin` value=3.456e+04 d1=69.0 d12=50.0 z=0.8679283198113207
- **ACCELERATION** `margin` value=3.456e+04 d1=69.0 d12=50.0 z=0.8679283198113207

## Nearest historical live analogues

- `2026-09-17T00:54:40.714610Z` distance=0.221 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:50:29.902043Z` distance=0.256 → {'next30m_imbalance_delta': -43.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:03:44.260171Z` distance=0.256 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:07:55.537385Z` distance=0.256 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:12:06.744150Z` distance=0.256 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
