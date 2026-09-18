# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T08:51:27.785288Z`  
Memory snapshots: **1149**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2072 d1=-72.0 d12=-100.0 z=-3.836160453125
- **CHANGE_POINT** `wind_gen` value=1.218e+04 d1=-68.0 d12=-369.0 z=-3.6466409811320757
- **PERSISTENT_UP** `ind_demand` value=-1.174e+04 d1=1.0 d12=4.0 z=-4.42465276
- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=1.0 d12=4.0 z=-4.42465276
- **PERSISTENT_DOWN** `biomass_gen` value=2072 d1=-72.0 d12=-100.0 z=-3.836160453125
- **ROBUST_OUTLIER** `biomass_gen` value=2072 d1=-72.0 d12=-100.0 z=-3.836160453125
- **PERSISTENT_DOWN** `wind_gen` value=1.218e+04 d1=-68.0 d12=-369.0 z=-3.6466409811320757
- **ROBUST_OUTLIER** `wind_gen` value=1.218e+04 d1=-68.0 d12=-369.0 z=-3.6466409811320757
- **REVERSAL** `interconnector_net` value=2929 d1=2.0 d12=-359.0 z=3.3219274347955836
- **ROBUST_OUTLIER** `interconnector_net` value=2929 d1=2.0 d12=-359.0 z=3.3219274347955836
- **PERSISTENT_DOWN** `imbalance` value=9602 d1=-23.0 d12=-616.0 z=-3.24766814625
- **ROBUST_OUTLIER** `imbalance` value=9602 d1=-23.0 d12=-616.0 z=-3.24766814625
- **CHANGE_POINT** `ps_gen` value=226 d1=2.0 d12=-371.0 z=-1.0554308048172758
- **CHANGE_POINT** `ccgt_gen` value=3750 d1=-184.0 d12=-533.0 z=-0.30331740262252793
- **CHANGE_POINT** `thermal_base` value=7087 d1=-179.0 d12=-536.0 z=-0.2997732222222222

## Nearest historical live analogues

- `2026-09-18T07:23:09.699179Z` distance=0.094 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:27:20.707745Z` distance=0.094 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:31:32.031758Z` distance=0.094 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:35:44.221296Z` distance=0.094 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:39:57.955920Z` distance=0.094 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
