# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T09:02:19.283651Z`  
Memory snapshots: **164**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2044 d1=1.0 d12=-992.0 z=-78.5106069
- **REVERSAL** `biomass_gen` value=2044 d1=1.0 d12=-992.0 z=-78.5106069
- **ROBUST_OUTLIER** `biomass_gen` value=2044 d1=1.0 d12=-992.0 z=-78.5106069
- **CHANGE_POINT** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=1346.0 z=56.657139
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=1346.0 z=56.657139
- **CHANGE_POINT** `wind_gen` value=1.203e+04 d1=-19.0 d12=-691.0 z=-2.966025439102564
- **CHANGE_POINT** `ps_gen` value=-775 d1=-235.0 d12=-235.0 z=-2.2450169781021896
- **CHANGE_POINT** `ccgt_gen` value=2581 d1=-168.0 d12=-418.0 z=-1.7434179502923974
- **CHANGE_POINT** `thermal_base` value=5896 d1=-167.0 d12=-414.0 z=-1.7235881956834533
- **PERSISTENT_DOWN** `wind_gen` value=1.203e+04 d1=-19.0 d12=-691.0 z=-2.966025439102564
- **PERSISTENT_UP** `interconnector_net` value=1.005e+04 d1=235.0 d12=1722.0 z=2.462210592843653
- **PERSISTENT_DOWN** `ps_gen` value=-775 d1=-235.0 d12=-235.0 z=-2.2450169781021896
- **ACCELERATION** `ps_gen` value=-775 d1=-235.0 d12=-235.0 z=-2.2450169781021896
- **PERSISTENT_UP** `ind_generation` value=2.043e+04 d1=0.0 d12=404.0 z=2.0488260075187967
- **CHANGE_POINT** `demand_forecast` value=2.007e+04 d1=0.0 d12=1346.0 z=None

## Nearest historical live analogues

- `2026-09-15T03:51:58.464857Z` distance=0.316 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:56:09.070441Z` distance=0.316 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:00:20.228720Z` distance=0.316 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:04:32.418140Z` distance=0.316 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T04:08:45.476934Z` distance=0.316 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
