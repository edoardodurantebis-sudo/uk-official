# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T12:40:21.941940Z`  
Memory snapshots: **2172**  
Current physical regime: **BALANCED**

Regime read: wind falling.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=4.0 z=14.890658326923075
- **ROBUST_OUTLIER** `demand_forecast` value=2.1e+04 d1=0.0 d12=0.0 z=10.963524300000001
- **CHANGE_POINT** `ps_gen` value=228 d1=0.0 d12=180.0 z=8.843310055555555
- **ROBUST_OUTLIER** `ps_gen` value=228 d1=0.0 d12=180.0 z=8.843310055555555
- **CHANGE_POINT** `thermal_base` value=9573 d1=0.0 d12=-701.0 z=-2.446142483826968
- **CHANGE_POINT** `ccgt_gen` value=6067 d1=0.0 d12=-694.0 z=-2.4127373175364544
- **CHANGE_POINT** `wind_gen` value=4059 d1=0.0 d12=628.0 z=1.0043413983979765
- **CHANGE_POINT** `margin` value=3.668e+04 d1=0.0 d12=0.0 z=-0.8755341339210748
- **PERSISTENT_DOWN** `thermal_base` value=9573 d1=0.0 d12=-701.0 z=-2.446142483826968
- **PERSISTENT_DOWN** `ccgt_gen` value=6067 d1=0.0 d12=-694.0 z=-2.4127373175364544
- **CHANGE_POINT** `ind_generation` value=1.817e+04 d1=0.0 d12=-318.0 z=-0.2749842826923077
- **CHANGE_POINT** `imbalance` value=-3333 d1=0.0 d12=-318.0 z=-0.2505697903037383
- **PERSISTENT_DOWN** `wind_forecast` value=8616 d1=0.0 d12=-307.0 z=-1.6051810329457366
- **PERSISTENT_UP** `residual_proxy` value=1.239e+04 d1=0.0 d12=307.0 z=1.4970041656314699
- **PERSISTENT_DOWN** `nuclear_gen` value=3506 d1=0.0 d12=-7.0 z=1.1241495833333335

## Nearest historical live analogues

- `2026-09-21T11:32:38.703181Z` distance=0.027 → {'next30m_imbalance_delta': 1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T11:36:50.598890Z` distance=0.027 → {'next30m_imbalance_delta': 1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T11:41:03.979554Z` distance=0.027 → {'next30m_imbalance_delta': 1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T11:45:16.809341Z` distance=0.027 → {'next30m_imbalance_delta': 1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T11:24:15.280087Z` distance=0.083 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 182.0, 'next30m_residual_proxy_delta': -104.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
