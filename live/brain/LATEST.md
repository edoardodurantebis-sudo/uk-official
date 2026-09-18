# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T17:46:54.993360Z`  
Memory snapshots: **1247**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=5203 d1=37.0 d12=2699.0 z=30.99223241101695
- **CHANGE_POINT** `thermal_base` value=8542 d1=38.0 d12=2701.0 z=30.72612550210084
- **PERSISTENT_UP** `ccgt_gen` value=5203 d1=37.0 d12=2699.0 z=30.99223241101695
- **ACCELERATION** `ccgt_gen` value=5203 d1=37.0 d12=2699.0 z=30.99223241101695
- **ROBUST_OUTLIER** `ccgt_gen` value=5203 d1=37.0 d12=2699.0 z=30.99223241101695
- **PERSISTENT_UP** `thermal_base` value=8542 d1=38.0 d12=2701.0 z=30.72612550210084
- **ACCELERATION** `thermal_base` value=8542 d1=38.0 d12=2701.0 z=30.72612550210084
- **ROBUST_OUTLIER** `thermal_base` value=8542 d1=38.0 d12=2701.0 z=30.72612550210084
- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=0.0 z=-14.8387745
- **CHANGE_POINT** `interconnector_net` value=-1543 d1=0.0 d12=-6563.0 z=-11.989954333550065
- **PERSISTENT_DOWN** `interconnector_net` value=-1543 d1=0.0 d12=-6563.0 z=-11.989954333550065
- **ACCELERATION** `interconnector_net` value=-1543 d1=0.0 d12=-6563.0 z=-11.989954333550065
- **ROBUST_OUTLIER** `interconnector_net` value=-1543 d1=0.0 d12=-6563.0 z=-11.989954333550065
- **CHANGE_POINT** `ps_gen` value=678 d1=0.0 d12=1143.0 z=8.964519381377551
- **PERSISTENT_UP** `ps_gen` value=678 d1=0.0 d12=1143.0 z=8.964519381377551

## Nearest historical live analogues

- `2026-09-18T14:21:00.093276Z` distance=0.072 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:25:11.108230Z` distance=0.112 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:29:22.596160Z` distance=0.112 → {'next30m_imbalance_delta': -13.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:34:10.760422Z` distance=0.112 → {'next30m_imbalance_delta': -13.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:38:23.970662Z` distance=0.112 → {'next30m_imbalance_delta': -13.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
