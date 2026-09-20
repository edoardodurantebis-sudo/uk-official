# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T05:32:50.061317Z`  
Memory snapshots: **1730**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-6811 d1=0.0 d12=-48.0 z=-39.53547611538462
- **CHANGE_POINT** `ind_generation` value=1.314e+04 d1=0.0 d12=-48.0 z=-39.53547611538462
- **PERSISTENT_DOWN** `imbalance` value=-6811 d1=0.0 d12=-48.0 z=-39.53547611538462
- **ROBUST_OUTLIER** `imbalance` value=-6811 d1=0.0 d12=-48.0 z=-39.53547611538462
- **PERSISTENT_DOWN** `ind_generation` value=1.314e+04 d1=0.0 d12=-48.0 z=-39.53547611538462
- **ROBUST_OUTLIER** `ind_generation` value=1.314e+04 d1=0.0 d12=-48.0 z=-39.53547611538462
- **ROBUST_OUTLIER** `margin` value=3.752e+04 d1=0.0 d12=7.0 z=11.50600161764706
- **CHANGE_POINT** `biomass_gen` value=1201 d1=-8.0 d12=-28.0 z=-0.022114418032786885
- **CHANGE_POINT** `ps_gen` value=-693 d1=-1.0 d12=7.0 z=0.011241495833333334
- **PERSISTENT_DOWN** `ind_demand` value=-1.232e+04 d1=0.0 d12=-4.0 z=-0.8571640572916667
- **REVERSAL** `ccgt_gen` value=3427 d1=43.0 d12=-737.0 z=-0.5654597111727417
- **REVERSAL** `thermal_base` value=6761 d1=38.0 d12=-740.0 z=-0.5626126622807017
- **PERSISTENT_UP** `interconnector_net` value=-1.125e+04 d1=666.0 d12=1409.0 z=-0.4459026488970588
- **ACCELERATION** `interconnector_net` value=-1.125e+04 d1=666.0 d12=1409.0 z=-0.4459026488970588
- **PERSISTENT_DOWN** `nuclear_gen` value=3334 d1=-5.0 d12=-3.0 z=0.22482991666666666

## Nearest historical live analogues

- `2026-09-20T04:20:43.261806Z` distance=0.043 → {'next30m_imbalance_delta': -236.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:24:55.304349Z` distance=0.043 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:29:05.930316Z` distance=0.043 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:33:18.594038Z` distance=0.043 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 3.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T04:38:07.201517Z` distance=0.043 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 3.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
