# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T09:14:41.751410Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-6.0 z=-21.67360396666667
- **PERSISTENT_DOWN** `ccgt_gen` value=2972 d1=0.0 d12=-2538.0 z=-6.421813762830482
- **ROBUST_OUTLIER** `ccgt_gen` value=2972 d1=0.0 d12=-2538.0 z=-6.421813762830482
- **ROBUST_OUTLIER** `margin` value=3.966e+04 d1=0.0 d12=360.0 z=6.157841606481481
- **PERSISTENT_DOWN** `thermal_base` value=6776 d1=0.0 d12=-2540.0 z=-6.088487892218913
- **ROBUST_OUTLIER** `thermal_base` value=6776 d1=0.0 d12=-2540.0 z=-6.088487892218913
- **PERSISTENT_UP** `interconnector_net` value=1.076e+04 d1=0.0 d12=3731.0 z=5.226838095225177
- **ROBUST_OUTLIER** `interconnector_net` value=1.076e+04 d1=0.0 d12=3731.0 z=5.226838095225177
- **ROBUST_OUTLIER** `imbalance` value=-7365 d1=0.0 d12=-94.0 z=4.599532512048192
- **ROBUST_OUTLIER** `ind_generation` value=1.366e+04 d1=0.0 d12=-94.0 z=3.00486967989418
- **CHANGE_POINT** `ps_gen` value=-19 d1=0.0 d12=267.0 z=-0.94428565
- **CHANGE_POINT** `biomass_gen` value=2693 d1=0.0 d12=359.0 z=0.47271931196581196
- **CHANGE_POINT** `residual_proxy` value=1.329e+04 d1=0.0 d12=309.0 z=0.35293068313953485
- **ACCELERATION** `wind_gen` value=1.039e+04 d1=0.0 d12=30.0 z=0.7466276911764707
- **PERSISTENT_UP** `biomass_gen` value=2693 d1=0.0 d12=359.0 z=0.47271931196581196

## Nearest historical live analogues

- `2026-09-23T08:19:43.705627Z` distance=0.192 → {'next30m_imbalance_delta': 183.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 309.0}
- `2026-09-21T09:22:16.225384Z` distance=0.443 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:26:26.475864Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:30:39.158321Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:34:50.037660Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
