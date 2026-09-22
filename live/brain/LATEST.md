# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T22:19:30.437012Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.474e+04 d1=-354.0 d12=-2803.0 z=-7.909836255442671
- **CHANGE_POINT** `ccgt_gen` value=1.1e+04 d1=-354.0 d12=-2808.0 z=-7.860624060518732
- **PERSISTENT_DOWN** `thermal_base` value=1.474e+04 d1=-354.0 d12=-2803.0 z=-7.909836255442671
- **ROBUST_OUTLIER** `thermal_base` value=1.474e+04 d1=-354.0 d12=-2803.0 z=-7.909836255442671
- **PERSISTENT_DOWN** `ccgt_gen` value=1.1e+04 d1=-354.0 d12=-2808.0 z=-7.860624060518732
- **ROBUST_OUTLIER** `ccgt_gen` value=1.1e+04 d1=-354.0 d12=-2808.0 z=-7.860624060518732
- **CHANGE_POINT** `ps_gen` value=144 d1=0.0 d12=1.0 z=-2.4487407533898304
- **CHANGE_POINT** `wind_gen` value=2564 d1=46.0 d12=226.0 z=1.6584053332127353
- **CHANGE_POINT** `ind_generation` value=1.312e+04 d1=0.0 d12=-35.0 z=-0.9401978333333334
- **CHANGE_POINT** `imbalance` value=-8054 d1=0.0 d12=-35.0 z=-0.9254626802325582
- **CHANGE_POINT** `biomass_gen` value=2917 d1=6.0 d12=0.0 z=0.4884236120689655
- **PERSISTENT_UP** `ps_gen` value=144 d1=0.0 d12=1.0 z=-2.4487407533898304
- **PERSISTENT_UP** `margin` value=3.723e+04 d1=20.0 d12=19.0 z=2.4202279264705884
- **ACCELERATION** `margin` value=3.723e+04 d1=20.0 d12=19.0 z=2.4202279264705884
- **PERSISTENT_UP** `wind_gen` value=2564 d1=46.0 d12=226.0 z=1.6584053332127353

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.011 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:24:47.718083Z` distance=0.011 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:55:13.117327Z` distance=0.011 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:59:27.826421Z` distance=0.011 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:03:40.476515Z` distance=0.011 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
