# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T22:02:41.905609Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.638e+04 d1=-151.0 d12=-1722.0 z=-4.708702028301887
- **CHANGE_POINT** `ccgt_gen` value=1.263e+04 d1=-156.0 d12=-1732.0 z=-4.694215407060519
- **CHANGE_POINT** `interconnector_net` value=4760 d1=-2.0 d12=-924.0 z=-2.7469318531353135
- **PERSISTENT_DOWN** `thermal_base` value=1.638e+04 d1=-151.0 d12=-1722.0 z=-4.708702028301887
- **ROBUST_OUTLIER** `thermal_base` value=1.638e+04 d1=-151.0 d12=-1722.0 z=-4.708702028301887
- **PERSISTENT_DOWN** `ccgt_gen` value=1.263e+04 d1=-156.0 d12=-1732.0 z=-4.694215407060519
- **ROBUST_OUTLIER** `ccgt_gen` value=1.263e+04 d1=-156.0 d12=-1732.0 z=-4.694215407060519
- **CHANGE_POINT** `ps_gen` value=143 d1=0.0 d12=0.0 z=-2.4510271593220336
- **CHANGE_POINT** `wind_gen` value=2464 d1=24.0 d12=156.0 z=1.607916741486068
- **PERSISTENT_UP** `nuclear_gen` value=3742 d1=5.0 d12=10.0 z=2.9677549
- **ACCELERATION** `nuclear_gen` value=3742 d1=5.0 d12=10.0 z=2.9677549
- **PERSISTENT_DOWN** `interconnector_net` value=4760 d1=-2.0 d12=-924.0 z=-2.7469318531353135
- **PERSISTENT_DOWN** `ind_generation` value=1.312e+04 d1=0.0 d12=-13.0 z=-1.2625064551282053
- **PERSISTENT_DOWN** `imbalance` value=-8054 d1=0.0 d12=-13.0 z=-1.21408155
- **PERSISTENT_DOWN** `ind_demand` value=-1.248e+04 d1=0.0 d12=-2.0 z=-0.67448975

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.001 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:55:13.117327Z` distance=0.002 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:59:27.826421Z` distance=0.002 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:03:40.476515Z` distance=0.002 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:07:51.999414Z` distance=0.002 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
