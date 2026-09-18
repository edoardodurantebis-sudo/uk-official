# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T08:56:14.868801Z`  
Memory snapshots: **1150**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=1973 d1=-99.0 d12=-199.0 z=-8.00956578125
- **PERSISTENT_DOWN** `biomass_gen` value=1973 d1=-99.0 d12=-199.0 z=-8.00956578125
- **ROBUST_OUTLIER** `biomass_gen` value=1973 d1=-99.0 d12=-199.0 z=-8.00956578125
- **CHANGE_POINT** `wind_gen` value=1.219e+04 d1=15.0 d12=-354.0 z=-3.4560631818181817
- **PERSISTENT_UP** `ind_demand` value=-1.174e+04 d1=0.0 d12=4.0 z=-4.42465276
- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=4.0 z=-4.42465276
- **REVERSAL** `wind_gen` value=1.219e+04 d1=15.0 d12=-354.0 z=-3.4560631818181817
- **ROBUST_OUTLIER** `wind_gen` value=1.219e+04 d1=15.0 d12=-354.0 z=-3.4560631818181817
- **PERSISTENT_DOWN** `imbalance` value=9602 d1=0.0 d12=-616.0 z=-3.24766814625
- **ROBUST_OUTLIER** `imbalance` value=9602 d1=0.0 d12=-616.0 z=-3.24766814625
- **CHANGE_POINT** `ps_gen` value=227 d1=1.0 d12=-370.0 z=-1.0171565683279744
- **PERSISTENT_DOWN** `interconnector_net` value=2872 d1=-57.0 d12=-452.0 z=2.812491665554683
- **CHANGE_POINT** `ccgt_gen` value=3592 d1=-158.0 d12=-691.0 z=-0.4959657320333042
- **CHANGE_POINT** `thermal_base` value=6929 d1=-158.0 d12=-694.0 z=-0.4924658786026201
- **PERSISTENT_DOWN** `ind_generation` value=2.725e+04 d1=0.0 d12=-476.0 z=-1.392146844

## Nearest historical live analogues

- `2026-09-18T07:23:09.699179Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:27:20.707745Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:31:32.031758Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:35:44.221296Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:39:57.955920Z` distance=0.093 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
