# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T18:29:14.865264Z`  
Memory snapshots: **1257**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=4703 d1=-134.0 d12=1967.0 z=25.276217580508472
- **CHANGE_POINT** `thermal_base` value=8037 d1=-132.0 d12=1967.0 z=25.001464598739496
- **REVERSAL** `ccgt_gen` value=4703 d1=-134.0 d12=1967.0 z=25.276217580508472
- **ROBUST_OUTLIER** `ccgt_gen` value=4703 d1=-134.0 d12=1967.0 z=25.276217580508472
- **REVERSAL** `thermal_base` value=8037 d1=-132.0 d12=1967.0 z=25.001464598739496
- **ROBUST_OUTLIER** `thermal_base` value=8037 d1=-132.0 d12=1967.0 z=25.001464598739496
- **CHANGE_POINT** `ind_generation` value=2.623e+04 d1=0.0 d12=655.0 z=18.09392068478261
- **PERSISTENT_UP** `ind_generation` value=2.623e+04 d1=0.0 d12=655.0 z=18.09392068478261
- **ROBUST_OUTLIER** `ind_generation` value=2.623e+04 d1=0.0 d12=655.0 z=18.09392068478261
- **CHANGE_POINT** `interconnector_net` value=-872 d1=0.0 d12=-5916.0 z=-10.812886395318596
- **ROBUST_OUTLIER** `interconnector_net` value=-872 d1=0.0 d12=-5916.0 z=-10.812886395318596
- **PERSISTENT_UP** `ps_gen` value=523 d1=10.0 d12=297.0 z=7.897724368622449
- **ROBUST_OUTLIER** `ps_gen` value=523 d1=10.0 d12=297.0 z=7.897724368622449
- **PERSISTENT_UP** `ind_demand` value=-1.074e+04 d1=0.0 d12=31.0 z=6.07040775
- **ACCELERATION** `ind_demand` value=-1.074e+04 d1=0.0 d12=31.0 z=6.07040775

## Nearest historical live analogues

- `2026-09-18T15:24:41.804681Z` distance=0.109 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T15:29:30.162883Z` distance=0.109 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T15:33:43.267823Z` distance=0.109 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': -377.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T14:21:00.093276Z` distance=0.174 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:31:54.164710Z` distance=0.193 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
