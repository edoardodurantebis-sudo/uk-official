# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T03:19:33.010874Z`  
Memory snapshots: **1357**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.831e+04 d1=0.0 d12=2.0 z=6.354831138554217
- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=2.0 z=6.354831138554217
- **CHANGE_POINT** `biomass_gen` value=812 d1=-1.0 d12=-287.0 z=-3.3932022807692306
- **CHANGE_POINT** `imbalance` value=9396 d1=0.0 d12=140.0 z=1.9251992201986754
- **CHANGE_POINT** `ind_generation` value=2.659e+04 d1=0.0 d12=140.0 z=1.847515402173913
- **PERSISTENT_DOWN** `biomass_gen` value=812 d1=-1.0 d12=-287.0 z=-3.3932022807692306
- **ROBUST_OUTLIER** `biomass_gen` value=812 d1=-1.0 d12=-287.0 z=-3.3932022807692306
- **CHANGE_POINT** `interconnector_net` value=-1.116e+04 d1=-2.0 d12=34.0 z=-1.0433093443725099
- **PERSISTENT_DOWN** `ccgt_gen` value=3057 d1=0.0 d12=-61.0 z=-2.2301959785714285
- **REVERSAL** `thermal_base` value=6398 d1=3.0 d12=-58.0 z=-2.2247567670157067
- **CHANGE_POINT** `ps_gen` value=-544 d1=-1.0 d12=125.0 z=-0.008312373679577465
- **REVERSAL** `interconnector_net` value=-1.116e+04 d1=-2.0 d12=34.0 z=-1.0433093443725099
- **PERSISTENT_UP** `nuclear_gen` value=3341 d1=3.0 d12=3.0 z=1.0117346249999999
- **ACCELERATION** `nuclear_gen` value=3341 d1=3.0 d12=3.0 z=1.0117346249999999
- **REVERSAL** `wind_gen` value=1.615e+04 d1=-1.0 d12=50.0 z=-0.18681910341726618

## Nearest historical live analogues

- `2026-09-19T02:20:35.608449Z` distance=0.004 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:24:50.521130Z` distance=0.004 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:22:06.996302Z` distance=0.274 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:26:19.516071Z` distance=0.274 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T00:30:34.705011Z` distance=0.274 → {'next30m_imbalance_delta': 65.0, 'next30m_margin_delta': -388.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
