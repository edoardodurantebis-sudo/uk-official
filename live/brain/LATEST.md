# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T00:07:55.537385Z`  
Memory snapshots: **683**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=-657.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=657.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6507 d1=108.0 d12=-724.0 z=-4.988611689700704
- **REVERSAL** `interconnector_net` value=-6507 d1=108.0 d12=-724.0 z=-4.988611689700704
- **ROBUST_OUTLIER** `interconnector_net` value=-6507 d1=108.0 d12=-724.0 z=-4.988611689700704
- **PERSISTENT_DOWN** `ccgt_gen` value=4644 d1=-88.0 d12=-1169.0 z=-3.464844606164384
- **ROBUST_OUTLIER** `ccgt_gen` value=4644 d1=-88.0 d12=-1169.0 z=-3.464844606164384
- **PERSISTENT_DOWN** `thermal_base` value=7960 d1=-93.0 d12=-1170.0 z=-3.4485016944760822
- **ROBUST_OUTLIER** `thermal_base` value=7960 d1=-93.0 d12=-1170.0 z=-3.4485016944760822
- **CHANGE_POINT** `imbalance` value=6451 d1=0.0 d12=-168.0 z=-0.607040775
- **CHANGE_POINT** `ind_generation` value=2.557e+04 d1=0.0 d12=-168.0 z=-0.16429878525641026
- **ACCELERATION** `nuclear_gen` value=3316 d1=-5.0 d12=-1.0 z=1.3489795
- **PERSISTENT_UP** `wind_gen` value=1.174e+04 d1=28.0 d12=762.0 z=1.2122349412910076
- **PERSISTENT_UP** `ps_gen` value=-247 d1=0.0 d12=4.0 z=-0.8181910211132437
- **PERSISTENT_DOWN** `biomass_gen` value=3205 d1=-1.0 d12=0.0 z=-0.35708280882352944

## Nearest historical live analogues

- `2026-09-16T14:21:30.462993Z` distance=0.509 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.510 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:29:54.321922Z` distance=0.510 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:34:06.314775Z` distance=0.510 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:38:16.233128Z` distance=0.510 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
