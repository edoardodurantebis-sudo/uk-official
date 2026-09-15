# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T18:32:54.292117Z`  
Memory snapshots: **299**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=3263 d1=0.0 d12=55.0 z=40.95501762
- **ROBUST_OUTLIER** `biomass_gen` value=3263 d1=0.0 d12=55.0 z=40.95501762
- **PERSISTENT_UP** `ind_demand` value=-1.191e+04 d1=0.0 d12=9.0 z=5.395918
- **ROBUST_OUTLIER** `ind_demand` value=-1.191e+04 d1=0.0 d12=9.0 z=5.395918
- **CHANGE_POINT** `ccgt_gen` value=1.067e+04 d1=-11.0 d12=229.0 z=2.8715862130422374
- **CHANGE_POINT** `thermal_base` value=1.399e+04 d1=-9.0 d12=236.0 z=2.8645139254348444
- **CHANGE_POINT** `margin` value=3.566e+04 d1=0.0 d12=835.0 z=2.206545039285714
- **CHANGE_POINT** `ps_gen` value=807 d1=2.0 d12=302.0 z=0.9774851454781319
- **REVERSAL** `ccgt_gen` value=1.067e+04 d1=-11.0 d12=229.0 z=2.8715862130422374
- **REVERSAL** `thermal_base` value=1.399e+04 d1=-9.0 d12=236.0 z=2.8645139254348444
- **CHANGE_POINT** `imbalance` value=5737 d1=0.0 d12=-35.0 z=-0.42922075000000004
- **CHANGE_POINT** `ind_generation` value=2.486e+04 d1=0.0 d12=-35.0 z=-0.42922075000000004
- **PERSISTENT_DOWN** `wind_gen` value=9863 d1=-50.0 d12=-859.0 z=-1.600455925308642
- **PERSISTENT_UP** `interconnector_net` value=-1486 d1=190.0 d12=288.0 z=-1.3335709329085006
- **ACCELERATION** `interconnector_net` value=-1486 d1=190.0 d12=288.0 z=-1.3335709329085006

## Nearest historical live analogues

- `2026-09-15T11:22:30.581865Z` distance=0.172 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:26:42.593420Z` distance=0.172 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:30:55.285075Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:35:06.452199Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:39:18.571623Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
