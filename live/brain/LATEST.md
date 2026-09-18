# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T17:42:43.021012Z`  
Memory snapshots: **1246**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=5166 d1=2430.0 d12=2662.0 z=30.56924731355932
- **CHANGE_POINT** `thermal_base` value=8504 d1=2434.0 d12=2663.0 z=30.29535893907563
- **PERSISTENT_UP** `ccgt_gen` value=5166 d1=2430.0 d12=2662.0 z=30.56924731355932
- **ACCELERATION** `ccgt_gen` value=5166 d1=2430.0 d12=2662.0 z=30.56924731355932
- **ROBUST_OUTLIER** `ccgt_gen` value=5166 d1=2430.0 d12=2662.0 z=30.56924731355932
- **PERSISTENT_UP** `thermal_base` value=8504 d1=2434.0 d12=2663.0 z=30.29535893907563
- **ACCELERATION** `thermal_base` value=8504 d1=2434.0 d12=2663.0 z=30.29535893907563
- **ROBUST_OUTLIER** `thermal_base` value=8504 d1=2434.0 d12=2663.0 z=30.29535893907563
- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=0.0 z=-14.8387745
- **PERSISTENT_DOWN** `interconnector_net` value=-1543 d1=-6587.0 d12=-6563.0 z=-11.989954333550065
- **ACCELERATION** `interconnector_net` value=-1543 d1=-6587.0 d12=-6563.0 z=-11.989954333550065
- **ROBUST_OUTLIER** `interconnector_net` value=-1543 d1=-6587.0 d12=-6563.0 z=-11.989954333550065
- **CHANGE_POINT** `ps_gen` value=678 d1=452.0 d12=1143.0 z=8.964519381377551
- **PERSISTENT_UP** `ps_gen` value=678 d1=452.0 d12=1143.0 z=8.964519381377551
- **ACCELERATION** `ps_gen` value=678 d1=452.0 d12=1143.0 z=8.964519381377551

## Nearest historical live analogues

- `2026-09-18T14:21:00.093276Z` distance=0.072 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:25:11.108230Z` distance=0.112 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:29:22.596160Z` distance=0.112 → {'next30m_imbalance_delta': -13.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:34:10.760422Z` distance=0.112 → {'next30m_imbalance_delta': -13.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:38:23.970662Z` distance=0.112 → {'next30m_imbalance_delta': -13.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
