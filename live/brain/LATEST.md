# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T01:03:09.320399Z`  
Memory snapshots: **696**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6773 d1=-93.0 d12=-232.0 z=-5.0736027040630685
- **PERSISTENT_DOWN** `interconnector_net` value=-6773 d1=-93.0 d12=-232.0 z=-5.0736027040630685
- **ROBUST_OUTLIER** `interconnector_net` value=-6773 d1=-93.0 d12=-232.0 z=-5.0736027040630685
- **CHANGE_POINT** `margin` value=3.451e+04 d1=0.0 d12=3.0 z=1.6437565018518518
- **PERSISTENT_UP** `ccgt_gen` value=4808 d1=286.0 d12=234.0 z=-3.3385702694063926
- **ACCELERATION** `ccgt_gen` value=4808 d1=286.0 d12=234.0 z=-3.3385702694063926
- **ROBUST_OUTLIER** `ccgt_gen` value=4808 d1=286.0 d12=234.0 z=-3.3385702694063926
- **PERSISTENT_UP** `thermal_base` value=8122 d1=290.0 d12=236.0 z=-3.324051421697039
- **ACCELERATION** `thermal_base` value=8122 d1=290.0 d12=236.0 z=-3.324051421697039
- **ROBUST_OUTLIER** `thermal_base` value=8122 d1=290.0 d12=236.0 z=-3.324051421697039
- **CHANGE_POINT** `wind_gen` value=1.228e+04 d1=21.0 d12=547.0 z=1.1281944993753124
- **PERSISTENT_UP** `ind_demand` value=-1.175e+04 d1=0.0 d12=16.0 z=2.83285695
- **CHANGE_POINT** `ps_gen` value=-310 d1=-4.0 d12=-64.0 z=-0.7440799623015873

## Nearest historical live analogues

- `2026-09-17T00:03:44.260171Z` distance=0.035 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:07:55.537385Z` distance=0.035 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:51:11.579176Z` distance=0.054 → {'next30m_imbalance_delta': -152.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:55:23.288978Z` distance=0.054 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T23:59:33.595851Z` distance=0.054 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
