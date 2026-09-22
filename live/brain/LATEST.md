# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T12:50:24.889254Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `nuclear_gen` value=3722 d1=0.0 d12=38.0 z=15.962924083333334
- **ROBUST_OUTLIER** `nuclear_gen` value=3722 d1=0.0 d12=38.0 z=15.962924083333334
- **ROBUST_OUTLIER** `ps_gen` value=-126 d1=0.0 d12=-113.0 z=9.667686416666667
- **ROBUST_OUTLIER** `wind_forecast` value=1.308e+04 d1=0.0 d12=75.0 z=8.76836675
- **CHANGE_POINT** `wind_gen` value=2549 d1=0.0 d12=-848.0 z=-6.352526058894231
- **PERSISTENT_DOWN** `wind_gen` value=2549 d1=0.0 d12=-848.0 z=-6.352526058894231
- **ROBUST_OUTLIER** `wind_gen` value=2549 d1=0.0 d12=-848.0 z=-6.352526058894231
- **CHANGE_POINT** `imbalance` value=-7075 d1=0.0 d12=-26.0 z=-0.8589375942556634
- **CHANGE_POINT** `ind_generation` value=1.408e+04 d1=0.0 d12=-26.0 z=-0.8497287635255648
- **CHANGE_POINT** `interconnector_net` value=1.109e+04 d1=0.0 d12=146.0 z=0.7885484108391608
- **PERSISTENT_DOWN** `biomass_gen` value=2979 d1=0.0 d12=-25.0 z=-2.1920916875
- **PERSISTENT_UP** `interconnector_net` value=1.109e+04 d1=0.0 d12=146.0 z=0.7885484108391608

## Nearest historical live analogues

- `2026-09-22T11:20:45.669526Z` distance=0.019 → {'next30m_imbalance_delta': 6.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:25:00.789915Z` distance=0.019 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:29:14.531873Z` distance=0.019 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:33:26.711703Z` distance=0.019 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T11:37:39.590020Z` distance=0.019 → {'next30m_imbalance_delta': -825.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
