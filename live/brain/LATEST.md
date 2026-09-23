# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T00:38:16.702070Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `interconnector_net` value=2222 d1=11.0 d12=-1981.0 z=-2.8214886423357664
- **CHANGE_POINT** `wind_gen` value=4213 d1=31.0 d12=918.0 z=2.301628095687332
- **ROBUST_OUTLIER** `ind_demand` value=-1.248e+04 d1=0.0 d12=0.0 z=-4.0469384999999996
- **CHANGE_POINT** `imbalance` value=-8007 d1=0.0 d12=42.0 z=1.1506001617647057
- **CHANGE_POINT** `ind_generation` value=1.317e+04 d1=0.0 d12=42.0 z=1.1506001617647057
- **REVERSAL** `interconnector_net` value=2222 d1=11.0 d12=-1981.0 z=-2.8214886423357664
- **ACCELERATION** `interconnector_net` value=2222 d1=11.0 d12=-1981.0 z=-2.8214886423357664
- **PERSISTENT_DOWN** `thermal_base` value=1.362e+04 d1=-42.0 d12=-30.0 z=-2.508023150365434
- **ACCELERATION** `thermal_base` value=1.362e+04 d1=-42.0 d12=-30.0 z=-2.508023150365434
- **PERSISTENT_DOWN** `ccgt_gen` value=9889 d1=-45.0 d12=-32.0 z=-2.5007871142306044
- **ACCELERATION** `ccgt_gen` value=9889 d1=-45.0 d12=-32.0 z=-2.5007871142306044
- **PERSISTENT_UP** `wind_gen` value=4213 d1=31.0 d12=918.0 z=2.301628095687332
- **CHANGE_POINT** `biomass_gen` value=2904 d1=1.0 d12=-9.0 z=-0.2484962236842105
- **ACCELERATION** `nuclear_gen` value=3732 d1=3.0 d12=2.0 z=-0.5058673124999999
- **REVERSAL** `biomass_gen` value=2904 d1=1.0 d12=-9.0 z=-0.2484962236842105

## Nearest historical live analogues

- `2026-09-22T23:31:03.889259Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:35:16.889434Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:39:29.907531Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:43:42.870536Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:22:42.187473Z` distance=0.464 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -158.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
