# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T16:02:01.837591Z`  
Memory snapshots: **1879**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1638 d1=101.0 d12=708.0 z=354.444363625
- **PERSISTENT_UP** `biomass_gen` value=1638 d1=101.0 d12=708.0 z=354.444363625
- **ROBUST_OUTLIER** `biomass_gen` value=1638 d1=101.0 d12=708.0 z=354.444363625
- **CHANGE_POINT** `ccgt_gen` value=4010 d1=63.0 d12=1304.0 z=62.01451472857143
- **PERSISTENT_UP** `ccgt_gen` value=4010 d1=63.0 d12=1304.0 z=62.01451472857143
- **ROBUST_OUTLIER** `ccgt_gen` value=4010 d1=63.0 d12=1304.0 z=62.01451472857143
- **CHANGE_POINT** `thermal_base` value=7346 d1=62.0 d12=1305.0 z=55.72323011538462
- **PERSISTENT_UP** `thermal_base` value=7346 d1=62.0 d12=1305.0 z=55.72323011538462
- **ROBUST_OUTLIER** `thermal_base` value=7346 d1=62.0 d12=1305.0 z=55.72323011538462
- **CHANGE_POINT** `imbalance` value=-5166 d1=0.0 d12=-8.0 z=14.371820057692307
- **PERSISTENT_DOWN** `imbalance` value=-5166 d1=0.0 d12=-8.0 z=14.371820057692307
- **ACCELERATION** `imbalance` value=-5166 d1=0.0 d12=-8.0 z=14.371820057692307
- **ROBUST_OUTLIER** `imbalance` value=-5166 d1=0.0 d12=-8.0 z=14.371820057692307
- **CHANGE_POINT** `interconnector_net` value=8449 d1=503.0 d12=3455.0 z=6.14621858448469
- **PERSISTENT_UP** `interconnector_net` value=8449 d1=503.0 d12=3455.0 z=6.14621858448469

## Nearest historical live analogues

- `2026-09-20T14:54:10.136499Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:58:25.329493Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:02:37.176302Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:06:50.185709Z` distance=0.005 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T10:57:55.935414Z` distance=0.060 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -13.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
