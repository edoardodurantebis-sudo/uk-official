# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T18:37:05.511843Z`  
Memory snapshots: **300**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=3283 d1=20.0 d12=88.0 z=40.667764338235294
- **ROBUST_OUTLIER** `biomass_gen` value=3283 d1=20.0 d12=88.0 z=40.667764338235294
- **ROBUST_OUTLIER** `ind_demand` value=-1.191e+04 d1=0.0 d12=9.0 z=5.395918
- **CHANGE_POINT** `ccgt_gen` value=1.067e+04 d1=0.0 d12=231.0 z=2.526295972436888
- **CHANGE_POINT** `thermal_base` value=1.399e+04 d1=-3.0 d12=235.0 z=2.5230784101804122
- **CHANGE_POINT** `margin` value=3.566e+04 d1=0.0 d12=835.0 z=2.206545039285714
- **CHANGE_POINT** `ps_gen` value=808 d1=1.0 d12=303.0 z=0.9861081147416413
- **REVERSAL** `thermal_base` value=1.399e+04 d1=-3.0 d12=235.0 z=2.5230784101804122
- **PERSISTENT_DOWN** `wind_gen` value=9811 d1=-52.0 d12=-878.0 z=-1.7372223804878049
- **REVERSAL** `interconnector_net` value=-1536 d1=-50.0 d12=257.0 z=-1.303241911035503
- **ACCELERATION** `interconnector_net` value=-1536 d1=-50.0 d12=257.0 z=-1.303241911035503
- **REVERSAL** `nuclear_gen` value=3317 d1=-3.0 d12=4.0 z=-1.2740361944444443
- **ACCELERATION** `nuclear_gen` value=3317 d1=-3.0 d12=4.0 z=-1.2740361944444443
- **PERSISTENT_UP** `ps_gen` value=808 d1=1.0 d12=303.0 z=0.9861081147416413

## Nearest historical live analogues

- `2026-09-15T11:22:30.581865Z` distance=0.172 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:26:42.593420Z` distance=0.172 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:30:55.285075Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:35:06.452199Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:39:18.571623Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
