# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T19:49:47.342713Z`  
Memory snapshots: **1276**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.089e+04 d1=0.0 d12=-6.0 z=-19.6951007
- **CHANGE_POINT** `ccgt_gen` value=4114 d1=-106.0 d12=-1049.0 z=18.54275211016949
- **CHANGE_POINT** `thermal_base` value=7450 d1=-106.0 d12=-1049.0 z=18.34725479621849
- **CHANGE_POINT** `ind_generation` value=2.623e+04 d1=0.0 d12=-5.0 z=18.09392068478261
- **ROBUST_OUTLIER** `ind_demand` value=-1.089e+04 d1=0.0 d12=-6.0 z=-19.6951007
- **PERSISTENT_DOWN** `ccgt_gen` value=4114 d1=-106.0 d12=-1049.0 z=18.54275211016949
- **ROBUST_OUTLIER** `ccgt_gen` value=4114 d1=-106.0 d12=-1049.0 z=18.54275211016949
- **PERSISTENT_DOWN** `thermal_base` value=7450 d1=-106.0 d12=-1049.0 z=18.34725479621849
- **ROBUST_OUTLIER** `thermal_base` value=7450 d1=-106.0 d12=-1049.0 z=18.34725479621849
- **ROBUST_OUTLIER** `ind_generation` value=2.623e+04 d1=0.0 d12=-5.0 z=18.09392068478261
- **REVERSAL** `interconnector_net` value=-1360 d1=16.0 d12=-994.0 z=-5.699327815409836
- **ROBUST_OUTLIER** `interconnector_net` value=-1360 d1=16.0 d12=-994.0 z=-5.699327815409836
- **ROBUST_OUTLIER** `margin` value=3.75e+04 d1=0.0 d12=-21.0 z=-4.591129093749999
- **CHANGE_POINT** `biomass_gen` value=1629 d1=5.0 d12=100.0 z=0.6886759588910134
- **REVERSAL** `ps_gen` value=411 d1=-53.0 d12=117.0 z=2.371505961

## Nearest historical live analogues

- `2026-09-18T18:54:36.333288Z` distance=0.301 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:51:12.400587Z` distance=0.326 → {'next30m_imbalance_delta': 590.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:55:26.775797Z` distance=0.326 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T17:59:39.675441Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T18:03:52.862865Z` distance=0.326 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': 120.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
