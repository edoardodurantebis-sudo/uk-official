# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T02:14:16.234964Z`  
Memory snapshots: **2024**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `wind_gen` value=3943 d1=71.0 d12=-461.0 z=-2.168771563164894
- **CHANGE_POINT** `ind_generation` value=1.571e+04 d1=0.0 d12=7.0 z=1.85628802991453
- **CHANGE_POINT** `imbalance` value=-4899 d1=0.0 d12=7.0 z=1.8455187627659573
- **CHANGE_POINT** `ind_demand` value=-1.183e+04 d1=0.0 d12=1.0 z=-0.67448975
- **REVERSAL** `wind_gen` value=3943 d1=71.0 d12=-461.0 z=-2.168771563164894
- **PERSISTENT_UP** `interconnector_net` value=1.237e+04 d1=23.0 d12=637.0 z=1.4010902241253644
- **REVERSAL** `nuclear_gen` value=3339 d1=-2.0 d12=6.0 z=1.0117346249999999
- **PERSISTENT_DOWN** `thermal_base` value=8499 d1=-213.0 d12=-62.0 z=-0.9555806258325404
- **ACCELERATION** `thermal_base` value=8499 d1=-213.0 d12=-62.0 z=-0.9555806258325404
- **PERSISTENT_DOWN** `ccgt_gen` value=5160 d1=-211.0 d12=-68.0 z=-0.9501563271050142
- **ACCELERATION** `ccgt_gen` value=5160 d1=-211.0 d12=-68.0 z=-0.9501563271050142
- **PERSISTENT_DOWN** `biomass_gen` value=3012 d1=0.0 d12=-19.0 z=0.581912725490196
- **PERSISTENT_DOWN** `ps_gen` value=-125 d1=-54.0 d12=-113.0 z=None
- **ACCELERATION** `ps_gen` value=-125 d1=-54.0 d12=-113.0 z=None

## Nearest historical live analogues

- `2026-09-21T00:03:26.283660Z` distance=0.015 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T00:07:41.732348Z` distance=0.015 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T00:11:53.168385Z` distance=0.015 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T00:16:11.516092Z` distance=0.015 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T00:53:59.881733Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
