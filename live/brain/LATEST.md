# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T11:12:17.771758Z`  
Memory snapshots: **2490**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.7e+04 d1=0.0 d12=-3381.0 z=-29.565134041666667
- **ROBUST_OUTLIER** `margin` value=3.7e+04 d1=0.0 d12=-3381.0 z=-29.565134041666667
- **ROBUST_OUTLIER** `wind_forecast` value=1.301e+04 d1=0.0 d12=614.0 z=8.488389872641509
- **CHANGE_POINT** `ind_generation` value=1.496e+04 d1=0.0 d12=-11158.0 z=-5.098839368539325
- **ROBUST_OUTLIER** `ind_generation` value=1.496e+04 d1=0.0 d12=-11158.0 z=-5.098839368539325
- **CHANGE_POINT** `thermal_base` value=1.237e+04 d1=-49.0 d12=-1090.0 z=-3.0938251722903884
- **CHANGE_POINT** `ccgt_gen` value=8716 d1=-40.0 d12=-1095.0 z=-3.0885981095505617
- **CHANGE_POINT** `imbalance` value=-6230 d1=0.0 d12=-11397.0 z=-3.016169793777135
- **CHANGE_POINT** `ps_gen` value=-164 d1=3.0 d12=-64.0 z=1.3489794999999998
- **PERSISTENT_DOWN** `thermal_base` value=1.237e+04 d1=-49.0 d12=-1090.0 z=-3.0938251722903884
- **ROBUST_OUTLIER** `thermal_base` value=1.237e+04 d1=-49.0 d12=-1090.0 z=-3.0938251722903884
- **PERSISTENT_DOWN** `ccgt_gen` value=8716 d1=-40.0 d12=-1095.0 z=-3.0885981095505617
- **ROBUST_OUTLIER** `ccgt_gen` value=8716 d1=-40.0 d12=-1095.0 z=-3.0885981095505617
- **ROBUST_OUTLIER** `imbalance` value=-6230 d1=0.0 d12=-11397.0 z=-3.016169793777135
- **CHANGE_POINT** `interconnector_net` value=1.095e+04 d1=-23.0 d12=44.0 z=0.6794911700273188

## Nearest historical live analogues

- `2026-09-22T05:53:47.929906Z` distance=0.390 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 41.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:57:59.458366Z` distance=0.390 → {'next30m_imbalance_delta': 198.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 41.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T06:02:11.446633Z` distance=0.390 → {'next30m_imbalance_delta': 198.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 41.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T06:06:26.622431Z` distance=0.390 → {'next30m_imbalance_delta': 198.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 41.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T06:11:17.063153Z` distance=0.390 → {'next30m_imbalance_delta': 198.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 41.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
