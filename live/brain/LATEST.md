# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T10:50:36.865474Z`  
Memory snapshots: **2485**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=4.039e+04 d1=0.0 d12=117.0 z=120.57085737931035
- **ROBUST_OUTLIER** `margin` value=4.039e+04 d1=0.0 d12=117.0 z=120.57085737931035
- **ROBUST_OUTLIER** `ind_generation` value=2.612e+04 d1=0.0 d12=1214.0 z=11.81342272247191
- **ROBUST_OUTLIER** `wind_forecast` value=1.301e+04 d1=0.0 d12=614.0 z=8.488389872641509
- **ROBUST_OUTLIER** `imbalance` value=5167 d1=0.0 d12=1334.0 z=8.108518600940666
- **ROBUST_OUTLIER** `ind_demand` value=-1.386e+04 d1=0.0 d12=-767.0 z=-4.7133986101190475
- **PERSISTENT_DOWN** `biomass_gen` value=3046 d1=-2.0 d12=-2.0 z=3.37244875
- **ACCELERATION** `biomass_gen` value=3046 d1=-2.0 d12=-2.0 z=3.37244875
- **ROBUST_OUTLIER** `biomass_gen` value=3046 d1=-2.0 d12=-2.0 z=3.37244875
- **PERSISTENT_DOWN** `thermal_base` value=1.241e+04 d1=-183.0 d12=-1079.0 z=-3.0928332263810017
- **ROBUST_OUTLIER** `thermal_base` value=1.241e+04 d1=-183.0 d12=-1079.0 z=-3.0928332263810017
- **PERSISTENT_DOWN** `ccgt_gen` value=8760 d1=-185.0 d12=-1080.0 z=-3.078724935989717
- **ROBUST_OUTLIER** `ccgt_gen` value=8760 d1=-185.0 d12=-1080.0 z=-3.078724935989717
- **REVERSAL** `residual_proxy` value=7680 d1=487.0 d12=-247.0 z=-0.9152397041184971
- **ACCELERATION** `residual_proxy` value=7680 d1=487.0 d12=-247.0 z=-0.9152397041184971

## Nearest historical live analogues

- `2026-09-22T09:50:55.170377Z` distance=0.872 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T09:55:11.927121Z` distance=0.872 → {'next30m_imbalance_delta': 1334.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 117.0, 'next30m_residual_proxy_delta': -120.0}
- `2026-09-22T09:21:25.127373Z` distance=1.202 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T09:25:39.976473Z` distance=1.202 → {'next30m_imbalance_delta': 1403.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T09:29:53.558775Z` distance=1.202 → {'next30m_imbalance_delta': 1403.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
