# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T08:38:47.543853Z`  
Memory snapshots: **1146**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low, wind falling.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=3.0 z=-6.541277952830188
- **CHANGE_POINT** `wind_gen` value=1.226e+04 d1=24.0 d12=-160.0 z=-3.9576106828214974
- **REVERSAL** `wind_gen` value=1.226e+04 d1=24.0 d12=-160.0 z=-3.9576106828214974
- **ROBUST_OUTLIER** `wind_gen` value=1.226e+04 d1=24.0 d12=-160.0 z=-3.9576106828214974
- **PERSISTENT_DOWN** `interconnector_net` value=2929 d1=-1.0 d12=-504.0 z=3.417868935185185
- **ACCELERATION** `interconnector_net` value=2929 d1=-1.0 d12=-504.0 z=3.417868935185185
- **ROBUST_OUTLIER** `interconnector_net` value=2929 d1=-1.0 d12=-504.0 z=3.417868935185185
- **CHANGE_POINT** `ps_gen` value=220 d1=-154.0 d12=-378.0 z=-1.172500103046595
- **ROBUST_OUTLIER** `imbalance` value=9625 d1=0.0 d12=-593.0 z=-3.1701018249999997
- **PERSISTENT_UP** `residual_proxy` value=8755 d1=0.0 d12=658.0 z=2.679223173611111
- **CHANGE_POINT** `biomass_gen` value=2164 d1=12.0 d12=1.0 z=0.2890670357142857
- **CHANGE_POINT** `ccgt_gen` value=4005 d1=-40.0 d12=-359.0 z=-0.0011599135855546
- **CHANGE_POINT** `thermal_base` value=7339 d1=-37.0 d12=-361.0 z=-0.0005764869658119659
- **PERSISTENT_DOWN** `wind_forecast` value=7699 d1=0.0 d12=-74.0 z=-1.3677153263888888
- **ACCELERATION** `wind_forecast` value=7699 d1=0.0 d12=-74.0 z=-1.3677153263888888

## Nearest historical live analogues

- `2026-09-18T07:23:09.699179Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:27:20.707745Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:31:32.031758Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:35:44.221296Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}
- `2026-09-18T07:39:57.955920Z` distance=0.099 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -444.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
