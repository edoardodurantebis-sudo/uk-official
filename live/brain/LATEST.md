# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T18:41:17.608634Z`  
Memory snapshots: **301**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=3296 d1=13.0 d12=92.0 z=39.43856104245283
- **ROBUST_OUTLIER** `biomass_gen` value=3296 d1=13.0 d12=92.0 z=39.43856104245283
- **ROBUST_OUTLIER** `ind_demand` value=-1.191e+04 d1=0.0 d12=9.0 z=5.395918
- **CHANGE_POINT** `margin` value=3.566e+04 d1=0.0 d12=-16.0 z=2.206545039285714
- **CHANGE_POINT** `ccgt_gen` value=1.079e+04 d1=117.0 d12=362.0 z=2.001234900521055
- **CHANGE_POINT** `thermal_base` value=1.41e+04 d1=116.0 d12=365.0 z=2.0004883385860306
- **CHANGE_POINT** `wind_gen` value=9850 d1=39.0 d12=-657.0 z=-1.4616517008009153
- **CHANGE_POINT** `ps_gen` value=804 d1=-4.0 d12=299.0 z=0.9862723771186441
- **CHANGE_POINT** `imbalance` value=5737 d1=0.0 d12=-35.0 z=-0.42922075000000004
- **CHANGE_POINT** `ind_generation` value=2.486e+04 d1=0.0 d12=-35.0 z=-0.42922075000000004
- **PERSISTENT_UP** `ccgt_gen` value=1.079e+04 d1=117.0 d12=362.0 z=2.001234900521055
- **PERSISTENT_UP** `thermal_base` value=1.41e+04 d1=116.0 d12=365.0 z=2.0004883385860306
- **REVERSAL** `wind_gen` value=9850 d1=39.0 d12=-657.0 z=-1.4616517008009153
- **REVERSAL** `nuclear_gen` value=3316 d1=-1.0 d12=3.0 z=-1.3489795
- **ACCELERATION** `nuclear_gen` value=3316 d1=-1.0 d12=3.0 z=-1.3489795

## Nearest historical live analogues

- `2026-09-15T11:22:30.581865Z` distance=0.172 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:26:42.593420Z` distance=0.172 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:30:55.285075Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:35:06.452199Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:39:18.571623Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
