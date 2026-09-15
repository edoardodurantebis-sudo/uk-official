# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T21:43:02.644079Z`  
Memory snapshots: **344**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=8590 d1=-196.0 d12=-3019.0 z=-7.615796229119639
- **CHANGE_POINT** `ccgt_gen` value=5265 d1=-199.0 d12=-3022.0 z=-7.566837363508968
- **PERSISTENT_DOWN** `thermal_base` value=8590 d1=-196.0 d12=-3019.0 z=-7.615796229119639
- **ROBUST_OUTLIER** `thermal_base` value=8590 d1=-196.0 d12=-3019.0 z=-7.615796229119639
- **PERSISTENT_DOWN** `ccgt_gen` value=5265 d1=-199.0 d12=-3022.0 z=-7.566837363508968
- **ROBUST_OUTLIER** `ccgt_gen` value=5265 d1=-199.0 d12=-3022.0 z=-7.566837363508968
- **PERSISTENT_DOWN** `wind_gen` value=1.228e+04 d1=-100.0 d12=-13.0 z=5.407699480349344
- **ACCELERATION** `wind_gen` value=1.228e+04 d1=-100.0 d12=-13.0 z=5.407699480349344
- **ROBUST_OUTLIER** `wind_gen` value=1.228e+04 d1=-100.0 d12=-13.0 z=5.407699480349344
- **CHANGE_POINT** `ps_gen` value=-256 d1=1.0 d12=8.0 z=-0.6762647230263158
- **CHANGE_POINT** `interconnector_net` value=1313 d1=17.0 d12=1163.0 z=0.5774430401165397
- **PERSISTENT_UP** `nuclear_gen` value=3325 d1=3.0 d12=3.0 z=1.0117346249999999
- **ACCELERATION** `nuclear_gen` value=3325 d1=3.0 d12=3.0 z=1.0117346249999999
- **PERSISTENT_UP** `ps_gen` value=-256 d1=1.0 d12=8.0 z=-0.6762647230263158
- **PERSISTENT_UP** `interconnector_net` value=1313 d1=17.0 d12=1163.0 z=0.5774430401165397

## Nearest historical live analogues

- `2026-09-15T20:22:50.211969Z` distance=0.018 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:27:39.367678Z` distance=0.018 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:31:49.811988Z` distance=0.018 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:36:00.984640Z` distance=0.018 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:40:13.497070Z` distance=0.018 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
