# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T21:54:12.694588Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.668e+04 d1=-191.0 d12=-1616.0 z=-4.105674907837446
- **CHANGE_POINT** `ccgt_gen` value=1.294e+04 d1=-189.0 d12=-1614.0 z=-4.087757764409222
- **CHANGE_POINT** `interconnector_net` value=4760 d1=0.0 d12=-1774.0 z=-2.632753649948025
- **CHANGE_POINT** `ps_gen` value=143 d1=0.0 d12=0.0 z=-2.4510271593220336
- **PERSISTENT_DOWN** `thermal_base` value=1.668e+04 d1=-191.0 d12=-1616.0 z=-4.105674907837446
- **ROBUST_OUTLIER** `thermal_base` value=1.668e+04 d1=-191.0 d12=-1616.0 z=-4.105674907837446
- **PERSISTENT_DOWN** `ccgt_gen` value=1.294e+04 d1=-189.0 d12=-1614.0 z=-4.087757764409222
- **ROBUST_OUTLIER** `ccgt_gen` value=1.294e+04 d1=-189.0 d12=-1614.0 z=-4.087757764409222
- **CHANGE_POINT** `margin` value=3.721e+04 d1=0.0 d12=-1.0 z=1.6267105735294118
- **CHANGE_POINT** `ind_generation` value=1.312e+04 d1=-35.0 d12=-13.0 z=-1.2625064551282053
- **CHANGE_POINT** `imbalance` value=-8054 d1=-35.0 d12=-13.0 z=-1.21408155
- **PERSISTENT_DOWN** `nuclear_gen` value=3738 d1=-2.0 d12=-2.0 z=2.360714125
- **ACCELERATION** `nuclear_gen` value=3738 d1=-2.0 d12=-2.0 z=2.360714125
- **PERSISTENT_UP** `wind_gen` value=2465 d1=0.0 d12=162.0 z=1.760796674092409
- **PERSISTENT_DOWN** `margin` value=3.721e+04 d1=0.0 d12=-1.0 z=1.6267105735294118

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.001 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:55:13.117327Z` distance=0.002 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:59:27.826421Z` distance=0.002 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:22:55.061007Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:27:09.876357Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
