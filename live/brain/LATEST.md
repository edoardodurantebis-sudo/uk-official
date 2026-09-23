# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T09:18:58.254124Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-6.0 z=-14.77745725
- **ROBUST_OUTLIER** `margin` value=3.966e+04 d1=0.0 d12=360.0 z=5.930648612612613
- **PERSISTENT_DOWN** `ccgt_gen` value=2913 d1=-59.0 d12=-2248.0 z=-5.812625903050491
- **ROBUST_OUTLIER** `ccgt_gen` value=2913 d1=-59.0 d12=-2248.0 z=-5.812625903050491
- **PERSISTENT_DOWN** `thermal_base` value=6713 d1=-63.0 d12=-2249.0 z=-5.584445664179104
- **ROBUST_OUTLIER** `thermal_base` value=6713 d1=-63.0 d12=-2249.0 z=-5.584445664179104
- **PERSISTENT_UP** `interconnector_net` value=1.082e+04 d1=68.0 d12=3752.0 z=5.251724314975583
- **ROBUST_OUTLIER** `interconnector_net` value=1.082e+04 d1=68.0 d12=3752.0 z=5.251724314975583
- **ROBUST_OUTLIER** `imbalance` value=-7365 d1=0.0 d12=-94.0 z=3.7583508457711443
- **CHANGE_POINT** `ps_gen` value=-19 d1=0.0 d12=48.0 z=-0.8579283849372384
- **CHANGE_POINT** `residual_proxy` value=1.329e+04 d1=0.0 d12=309.0 z=0.35293068313953485
- **PERSISTENT_UP** `ps_gen` value=-19 d1=0.0 d12=48.0 z=-0.8579283849372384
- **REVERSAL** `wind_gen` value=1.037e+04 d1=-13.0 d12=47.0 z=0.7406106555299539
- **REVERSAL** `biomass_gen` value=2691 d1=-2.0 d12=354.0 z=0.531682473941368
- **ACCELERATION** `nuclear_gen` value=3800 d1=-4.0 d12=-1.0 z=-0.3747165277777778

## Nearest historical live analogues

- `2026-09-23T08:23:54.266782Z` distance=0.191 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 309.0}
- `2026-09-23T08:19:43.705627Z` distance=0.192 → {'next30m_imbalance_delta': 183.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 309.0}
- `2026-09-21T09:22:16.225384Z` distance=0.443 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:26:26.475864Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}
- `2026-09-21T09:30:39.158321Z` distance=0.443 → {'next30m_imbalance_delta': 154.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 140.0, 'next30m_residual_proxy_delta': -110.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
