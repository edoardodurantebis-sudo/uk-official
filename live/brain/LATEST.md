# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T08:34:36.525091Z`  
Memory snapshots: **1145**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low, wind falling.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=3.0 z=-6.541277952830188
- **CHANGE_POINT** `imbalance` value=9625 d1=0.0 d12=-593.0 z=-3.1701018249999997
- **PERSISTENT_DOWN** `wind_gen` value=1.224e+04 d1=-24.0 d12=-137.0 z=-4.001972516666666
- **ROBUST_OUTLIER** `wind_gen` value=1.224e+04 d1=-24.0 d12=-137.0 z=-4.001972516666666
- **PERSISTENT_DOWN** `interconnector_net` value=2930 d1=-226.0 d12=-503.0 z=3.494240401202749
- **ACCELERATION** `interconnector_net` value=2930 d1=-226.0 d12=-503.0 z=3.494240401202749
- **ROBUST_OUTLIER** `interconnector_net` value=2930 d1=-226.0 d12=-503.0 z=3.494240401202749
- **ROBUST_OUTLIER** `imbalance` value=9625 d1=0.0 d12=-593.0 z=-3.1701018249999997
- **PERSISTENT_UP** `residual_proxy` value=8755 d1=74.0 d12=214.0 z=2.679223173611111
- **CHANGE_POINT** `ps_gen` value=374 d1=-223.0 d12=-224.0 z=-0.4351546774193548
- **CHANGE_POINT** `ccgt_gen` value=4045 d1=27.0 d12=-383.0 z=0.09829868950504125
- **CHANGE_POINT** `thermal_base` value=7376 d1=21.0 d12=-388.0 z=0.09811881999085087
- **CHANGE_POINT** `biomass_gen` value=2152 d1=5.0 d12=-20.0 z=0.02498110185185185
- **PERSISTENT_DOWN** `wind_forecast` value=7699 d1=-74.0 d12=-74.0 z=-1.3677153263888888
- **ACCELERATION** `wind_forecast` value=7699 d1=-74.0 d12=-74.0 z=-1.3677153263888888

## Nearest historical live analogues

- `2026-09-18T07:23:09.699179Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:27:20.707745Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:31:32.031758Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:35:44.221296Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:39:57.955920Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
