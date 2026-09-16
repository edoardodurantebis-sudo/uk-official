# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T09:30:50.292124Z`  
Memory snapshots: **512**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **PERSISTENT_DOWN** `margin` value=3.451e+04 d1=0.0 d12=-2052.0 z=-78.16298525961538
- **ROBUST_OUTLIER** `margin` value=3.451e+04 d1=0.0 d12=-2052.0 z=-78.16298525961538
- **PERSISTENT_DOWN** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1219.0 z=-53.47740160714286
- **ROBUST_OUTLIER** `ind_demand` value=-1.388e+04 d1=0.0 d12=-1219.0 z=-53.47740160714286
- **CHANGE_POINT** `biomass_gen` value=3148 d1=-15.0 d12=-88.0 z=-22.79775355
- **PERSISTENT_DOWN** `biomass_gen` value=3148 d1=-15.0 d12=-88.0 z=-22.79775355
- **ACCELERATION** `biomass_gen` value=3148 d1=-15.0 d12=-88.0 z=-22.79775355
- **ROBUST_OUTLIER** `biomass_gen` value=3148 d1=-15.0 d12=-88.0 z=-22.79775355
- **PERSISTENT_DOWN** `imbalance` value=5364 d1=0.0 d12=-1743.0 z=-10.9872489182243
- **ROBUST_OUTLIER** `imbalance` value=5364 d1=0.0 d12=-1743.0 z=-10.9872489182243
- **CHANGE_POINT** `thermal_base` value=9755 d1=-202.0 d12=-1560.0 z=-0.9254442696596245
- **CHANGE_POINT** `ccgt_gen` value=6431 d1=-197.0 d12=-1554.0 z=-0.9196507337052261
- **CHANGE_POINT** `demand_forecast` value=1.851e+04 d1=0.0 d12=0.0 z=None
- **CHANGE_POINT** `ts_demand_forecast` value=2.064e+04 d1=0.0 d12=1180.0 z=None
- **PERSISTENT_DOWN** `nuclear_gen` value=3324 d1=-5.0 d12=-6.0 z=-1.686224375

## Nearest historical live analogues

- `2026-09-16T08:31:21.232151Z` distance=3.119 → {'next30m_imbalance_delta': -402.0, 'next30m_margin_delta': -815.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:35:35.956217Z` distance=3.119 → {'next30m_imbalance_delta': -402.0, 'next30m_margin_delta': -815.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T08:17:56.653795Z` distance=3.146 → {'next30m_imbalance_delta': 235.0, 'next30m_margin_delta': 235.0, 'next30m_residual_proxy_delta': -321.0}
- `2026-09-16T07:23:21.620957Z` distance=3.149 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}
- `2026-09-16T07:27:32.881343Z` distance=3.149 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 1249.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
