# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T18:47:16.363272Z`  
Memory snapshots: **1918**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **PERSISTENT_DOWN** `ccgt_gen` value=8723 d1=-174.0 d12=-175.0 z=11.153802836791149
- **ROBUST_OUTLIER** `ccgt_gen` value=8723 d1=-174.0 d12=-175.0 z=11.153802836791149
- **PERSISTENT_DOWN** `thermal_base` value=1.206e+04 d1=-167.0 d12=-172.0 z=11.07310470233196
- **ROBUST_OUTLIER** `thermal_base` value=1.206e+04 d1=-167.0 d12=-172.0 z=11.07310470233196
- **CHANGE_POINT** `biomass_gen` value=2336 d1=4.0 d12=77.0 z=2.025009180936073
- **CHANGE_POINT** `interconnector_net` value=9874 d1=0.0 d12=-169.0 z=0.622855412531256
- **PERSISTENT_UP** `biomass_gen` value=2336 d1=4.0 d12=77.0 z=2.025009180936073
- **ACCELERATION** `biomass_gen` value=2336 d1=4.0 d12=77.0 z=2.025009180936073
- **PERSISTENT_UP** `nuclear_gen` value=3341 d1=7.0 d12=3.0 z=2.0234692499999998
- **ACCELERATION** `nuclear_gen` value=3341 d1=7.0 d12=3.0 z=2.0234692499999998
- **PERSISTENT_DOWN** `wind_gen` value=5841 d1=-106.0 d12=-970.0 z=-1.333417925189394
- **REVERSAL** `ps_gen` value=224 d1=2.0 d12=-64.0 z=1.1185288354166667

## Nearest historical live analogues

- `2026-09-20T17:52:35.892709Z` distance=0.013 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:49:59.741529Z` distance=0.032 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:24:12.719546Z` distance=0.038 → {'next30m_imbalance_delta': 81.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:28:27.793665Z` distance=0.038 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:32:40.592900Z` distance=0.038 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
