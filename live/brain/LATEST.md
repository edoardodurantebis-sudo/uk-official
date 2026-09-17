# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T20:13:38.559764Z`  
Memory snapshots: **969**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.652e+04 d1=0.0 d12=7.0 z=-27.467518755319148
- **ROBUST_OUTLIER** `ind_generation` value=2.652e+04 d1=0.0 d12=7.0 z=-27.467518755319148
- **ROBUST_OUTLIER** `ind_demand` value=-1.116e+04 d1=0.0 d12=0.0 z=26.97959
- **CHANGE_POINT** `imbalance` value=9708 d1=0.0 d12=7.0 z=-4.08535880221519
- **CHANGE_POINT** `interconnector_net` value=-1658 d1=-326.0 d12=-1199.0 z=-3.4122571650890867
- **ROBUST_OUTLIER** `imbalance` value=9708 d1=0.0 d12=7.0 z=-4.08535880221519
- **PERSISTENT_DOWN** `interconnector_net` value=-1658 d1=-326.0 d12=-1199.0 z=-3.4122571650890867
- **ROBUST_OUTLIER** `interconnector_net` value=-1658 d1=-326.0 d12=-1199.0 z=-3.4122571650890867
- **CHANGE_POINT** `wind_gen` value=1.599e+04 d1=-22.0 d12=621.0 z=1.37951816391839
- **CHANGE_POINT** `ps_gen` value=502 d1=-2.0 d12=95.0 z=0.6723983089147286
- **CHANGE_POINT** `ccgt_gen` value=5303 d1=-144.0 d12=-1290.0 z=0.13666517205240175
- **CHANGE_POINT** `thermal_base` value=8620 d1=-145.0 d12=-1297.0 z=0.13349072710808463
- **REVERSAL** `wind_gen` value=1.599e+04 d1=-22.0 d12=621.0 z=1.37951816391839
- **PERSISTENT_UP** `biomass_gen` value=3104 d1=98.0 d12=120.0 z=0.8923481963824289
- **ACCELERATION** `biomass_gen` value=3104 d1=98.0 d12=120.0 z=0.8923481963824289

## Nearest historical live analogues

- `2026-09-17T18:57:56.745109Z` distance=0.131 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:10:36.600451Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:14:49.284800Z` distance=0.131 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
