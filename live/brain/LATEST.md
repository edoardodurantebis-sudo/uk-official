# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T07:43:13.159815Z`  
Memory snapshots: **791**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.558e+04 d1=0.0 d12=-154.0 z=-7.800620586956522
- **ROBUST_OUTLIER** `margin` value=3.558e+04 d1=0.0 d12=-154.0 z=-7.800620586956522
- **CHANGE_POINT** `interconnector_net` value=3985 d1=24.0 d12=9394.0 z=5.045548932505212
- **ROBUST_OUTLIER** `ind_demand` value=-1.214e+04 d1=0.0 d12=-9.0 z=-6.766655233870968
- **CHANGE_POINT** `wind_gen` value=1.5e+04 d1=278.0 d12=941.0 z=3.587975359770115
- **PERSISTENT_UP** `interconnector_net` value=3985 d1=24.0 d12=9394.0 z=5.045548932505212
- **ROBUST_OUTLIER** `interconnector_net` value=3985 d1=24.0 d12=9394.0 z=5.045548932505212
- **CHANGE_POINT** `biomass_gen` value=2321 d1=-149.0 d12=-873.0 z=-2.415614453488372
- **PERSISTENT_UP** `wind_gen` value=1.5e+04 d1=278.0 d12=941.0 z=3.587975359770115
- **ROBUST_OUTLIER** `wind_gen` value=1.5e+04 d1=278.0 d12=941.0 z=3.587975359770115
- **CHANGE_POINT** `ps_gen` value=223 d1=0.0 d12=-3.0 z=1.4609280062240664
- **CHANGE_POINT** `ind_generation` value=2.653e+04 d1=0.0 d12=69.0 z=0.9742629722222221
- **CHANGE_POINT** `imbalance` value=7157 d1=0.0 d12=-181.0 z=-0.5050973470319635
- **PERSISTENT_DOWN** `biomass_gen` value=2321 d1=-149.0 d12=-873.0 z=-2.415614453488372
- **REVERSAL** `nuclear_gen` value=3315 d1=-1.0 d12=3.0 z=1.0117346249999999

## Nearest historical live analogues

- `2026-09-17T06:23:11.376027Z` distance=0.604 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:27:23.488219Z` distance=0.604 → {'next30m_imbalance_delta': -21.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:31:35.953435Z` distance=0.604 → {'next30m_imbalance_delta': -21.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:35:47.177085Z` distance=0.604 → {'next30m_imbalance_delta': -21.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T06:39:57.616616Z` distance=0.604 → {'next30m_imbalance_delta': -21.0, 'next30m_margin_delta': -42.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
