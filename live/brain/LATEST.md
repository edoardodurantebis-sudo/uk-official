# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T18:45:39.191580Z`  
Memory snapshots: **302**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **PERSISTENT_UP** `biomass_gen` value=3299 d1=3.0 d12=95.0 z=38.770670074074076
- **ROBUST_OUTLIER** `biomass_gen` value=3299 d1=3.0 d12=95.0 z=38.770670074074076
- **ROBUST_OUTLIER** `ind_demand` value=-1.191e+04 d1=0.0 d12=9.0 z=5.395918
- **CHANGE_POINT** `margin` value=3.566e+04 d1=0.0 d12=-16.0 z=2.206545039285714
- **CHANGE_POINT** `ccgt_gen` value=1.085e+04 d1=66.0 d12=428.0 z=1.6404941671692252
- **CHANGE_POINT** `thermal_base` value=1.417e+04 d1=65.0 d12=430.0 z=1.6392802831991953
- **CHANGE_POINT** `wind_gen` value=9916 d1=66.0 d12=-591.0 z=-1.183894596153846
- **CHANGE_POINT** `ps_gen` value=803 d1=-1.0 d12=298.0 z=0.9869179998063515
- **CHANGE_POINT** `imbalance` value=5737 d1=0.0 d12=-38.0 z=-0.43716928240740743
- **CHANGE_POINT** `ind_generation` value=2.486e+04 d1=0.0 d12=-38.0 z=-0.43716928240740743
- **PERSISTENT_UP** `ccgt_gen` value=1.085e+04 d1=66.0 d12=428.0 z=1.6404941671692252
- **PERSISTENT_UP** `thermal_base` value=1.417e+04 d1=65.0 d12=430.0 z=1.6392802831991953
- **REVERSAL** `nuclear_gen` value=3315 d1=-1.0 d12=2.0 z=-1.4988661111111112
- **REVERSAL** `interconnector_net` value=-1574 d1=-13.0 d12=224.0 z=-1.2319237330831343
- **REVERSAL** `wind_gen` value=9916 d1=66.0 d12=-591.0 z=-1.183894596153846

## Nearest historical live analogues

- `2026-09-15T17:50:55.506503Z` distance=0.030 → {'next30m_imbalance_delta': 3.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:22:30.581865Z` distance=0.172 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:26:42.593420Z` distance=0.172 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:30:55.285075Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T11:35:06.452199Z` distance=0.172 → {'next30m_imbalance_delta': -1.0, 'next30m_margin_delta': -334.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
