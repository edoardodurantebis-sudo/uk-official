# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T21:58:28.957668Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.653e+04 d1=-157.0 d12=-1778.0 z=-4.413062108853411
- **CHANGE_POINT** `ccgt_gen` value=1.279e+04 d1=-156.0 d12=-1773.0 z=-4.39098658573487
- **CHANGE_POINT** `interconnector_net` value=4762 d1=2.0 d12=-1146.0 z=-2.710368443452381
- **CHANGE_POINT** `ps_gen` value=143 d1=0.0 d12=0.0 z=-2.4510271593220336
- **PERSISTENT_DOWN** `thermal_base` value=1.653e+04 d1=-157.0 d12=-1778.0 z=-4.413062108853411
- **ROBUST_OUTLIER** `thermal_base` value=1.653e+04 d1=-157.0 d12=-1778.0 z=-4.413062108853411
- **PERSISTENT_DOWN** `ccgt_gen` value=1.279e+04 d1=-156.0 d12=-1773.0 z=-4.39098658573487
- **ROBUST_OUTLIER** `ccgt_gen` value=1.279e+04 d1=-156.0 d12=-1773.0 z=-4.39098658573487
- **CHANGE_POINT** `margin` value=3.721e+04 d1=0.0 d12=-1.0 z=1.6267105735294118
- **CHANGE_POINT** `wind_gen` value=2440 d1=-25.0 d12=136.0 z=1.5602150496124032
- **REVERSAL** `interconnector_net` value=4762 d1=2.0 d12=-1146.0 z=-2.710368443452381
- **PERSISTENT_DOWN** `nuclear_gen` value=3737 d1=-1.0 d12=-5.0 z=2.0234692499999998
- **PERSISTENT_DOWN** `margin` value=3.721e+04 d1=0.0 d12=-1.0 z=1.6267105735294118
- **REVERSAL** `wind_gen` value=2440 d1=-25.0 d12=136.0 z=1.5602150496124032
- **PERSISTENT_DOWN** `ind_generation` value=1.312e+04 d1=0.0 d12=-13.0 z=-1.2625064551282053

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.001 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:55:13.117327Z` distance=0.002 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:59:27.826421Z` distance=0.002 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:03:40.476515Z` distance=0.002 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T17:22:55.061007Z` distance=0.021 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
