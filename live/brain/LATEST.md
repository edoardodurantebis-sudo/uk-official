# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T02:05:53.234228Z`  
Memory snapshots: **2022**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `wind_gen` value=3872 d1=34.0 d12=-772.0 z=-2.2758745458818264
- **CHANGE_POINT** `imbalance` value=-4899 d1=0.0 d12=9.0 z=1.85628802991453
- **CHANGE_POINT** `ind_generation` value=1.571e+04 d1=0.0 d12=9.0 z=1.85628802991453
- **REVERSAL** `wind_gen` value=3872 d1=34.0 d12=-772.0 z=-2.2758745458818264
- **CHANGE_POINT** `ind_demand` value=-1.183e+04 d1=0.0 d12=11.0 z=None
- **PERSISTENT_UP** `interconnector_net` value=1.235e+04 d1=113.0 d12=615.0 z=1.8094975963541666
- **REVERSAL** `nuclear_gen` value=3341 d1=-1.0 d12=2.0 z=1.686224375
- **ACCELERATION** `nuclear_gen` value=3341 d1=-1.0 d12=2.0 z=1.686224375
- **REVERSAL** `thermal_base` value=8712 d1=-94.0 d12=278.0 z=-0.6817293537567084
- **REVERSAL** `ccgt_gen` value=5371 d1=-93.0 d12=276.0 z=-0.6804481400176678
- **ACCELERATION** `ccgt_gen` value=5371 d1=-93.0 d12=276.0 z=-0.6804481400176678
- **PERSISTENT_DOWN** `biomass_gen` value=3012 d1=-6.0 d12=-11.0 z=0.5814566810344828
- **PERSISTENT_DOWN** `ps_gen` value=-71 d1=-55.0 d12=-59.0 z=None
- **ACCELERATION** `ps_gen` value=-71 d1=-55.0 d12=-59.0 z=None

## Nearest historical live analogues

- `2026-09-21T00:03:26.283660Z` distance=0.015 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T00:07:41.732348Z` distance=0.015 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T00:11:53.168385Z` distance=0.015 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T00:16:11.516092Z` distance=0.015 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T00:53:59.881733Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
