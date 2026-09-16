# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T09:35:00.318078Z`  
Memory snapshots: **513**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.451e+04 d1=0.0 d12=-2052.0 z=-78.16298525961538
- **ROBUST_OUTLIER** `margin` value=3.451e+04 d1=0.0 d12=-2052.0 z=-78.16298525961538
- **CHANGE_POINT** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1219.0 z=-53.47740160714286
- **ROBUST_OUTLIER** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1219.0 z=-53.47740160714286
- **CHANGE_POINT** `biomass_gen` value=3148 d1=0.0 d12=-90.0 z=-22.79775355
- **PERSISTENT_DOWN** `biomass_gen` value=3148 d1=0.0 d12=-90.0 z=-22.79775355
- **ROBUST_OUTLIER** `biomass_gen` value=3148 d1=0.0 d12=-90.0 z=-22.79775355
- **CHANGE_POINT** `imbalance` value=5364 d1=0.0 d12=-1743.0 z=-10.9872489182243
- **ROBUST_OUTLIER** `imbalance` value=5364 d1=0.0 d12=-1743.0 z=-10.9872489182243
- **CHANGE_POINT** `ind_generation` value=2.6e+04 d1=0.0 d12=-558.0 z=-1.6541058154761903
- **CHANGE_POINT** `thermal_base` value=9755 d1=0.0 d12=-1385.0 z=-0.9254442696596245
- **CHANGE_POINT** `ccgt_gen` value=6431 d1=0.0 d12=-1383.0 z=-0.9196507337052261
- **PERSISTENT_DOWN** `nuclear_gen` value=3324 d1=0.0 d12=-2.0 z=-1.686224375
- **ACCELERATION** `nuclear_gen` value=3324 d1=0.0 d12=-2.0 z=-1.686224375
- **PERSISTENT_DOWN** `wind_gen` value=5676 d1=0.0 d12=-900.0 z=-1.4318325646341463

## Nearest historical live analogues

- `2026-09-16T08:17:56.653795Z` distance=3.102 → {'next30m_imbalance_delta': 235.0, 'next30m_margin_delta': 235.0, 'next30m_residual_proxy_delta': -321.0}
- `2026-09-16T07:23:21.620957Z` distance=3.104 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:27:32.881343Z` distance=3.104 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:31:44.991160Z` distance=3.104 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:35:56.436252Z` distance=3.104 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
