# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T11:13:02.742323Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `imbalance` value=179 d1=0.0 d12=2479.0 z=10.93074365552017
- **ROBUST_OUTLIER** `imbalance` value=179 d1=0.0 d12=2479.0 z=10.93074365552017
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.005e+04 d1=0.0 d12=-975.0 z=-9.745213974137931
- **ROBUST_OUTLIER** `ind_generation` value=2.023e+04 d1=0.0 d12=1504.0 z=9.633248573851203
- **ROBUST_OUTLIER** `residual_proxy` value=1.238e+04 d1=0.0 d12=-911.0 z=-7.493416612804879
- **CHANGE_POINT** `ccgt_gen` value=2158 d1=23.0 d12=43.0 z=-1.6441251485176103
- **CHANGE_POINT** `ind_demand` value=-1.222e+04 d1=0.0 d12=1512.0 z=1.2409443452380953
- **CHANGE_POINT** `biomass_gen` value=2730 d1=11.0 d12=58.0 z=1.2215758805555554
- **ROBUST_OUTLIER** `demand_forecast` value=1.955e+04 d1=0.0 d12=-729.0 z=-3.189594751278772
- **PERSISTENT_UP** `ps_gen` value=-740 d1=1.0 d12=132.0 z=-3.028919809006211
- **ROBUST_OUTLIER** `ps_gen` value=-740 d1=1.0 d12=132.0 z=-3.028919809006211
- **CHANGE_POINT** `nuclear_gen` value=3801 d1=-3.0 d12=-10.0 z=-0.6744897499999999
- **CHANGE_POINT** `margin` value=3.894e+04 d1=0.0 d12=-1844.0 z=0.2547024230769231
- **PERSISTENT_UP** `ccgt_gen` value=2158 d1=23.0 d12=43.0 z=-1.6441251485176103
- **ACCELERATION** `ccgt_gen` value=2158 d1=23.0 d12=43.0 z=-1.6441251485176103

## Nearest historical live analogues

- `2026-09-23T06:20:46.707492Z` distance=0.224 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:24:57.207675Z` distance=0.224 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:29:10.567050Z` distance=0.224 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:33:22.680489Z` distance=0.224 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:37:35.207990Z` distance=0.224 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -86.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
