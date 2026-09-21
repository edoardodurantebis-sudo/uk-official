# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T01:02:22.746088Z`  
Memory snapshots: **2007**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `imbalance` value=-4908 d1=0.0 d12=321.0 z=2.638941146875
- **CHANGE_POINT** `ind_generation` value=1.57e+04 d1=0.0 d12=321.0 z=2.638941146875
- **CHANGE_POINT** `interconnector_net` value=1.125e+04 d1=176.0 d12=1025.0 z=0.89369891875
- **CHANGE_POINT** `ccgt_gen` value=5449 d1=44.0 d12=-377.0 z=-0.6753271053693359
- **CHANGE_POINT** `thermal_base` value=8787 d1=46.0 d12=-375.0 z=-0.6711424063275434
- **PERSISTENT_DOWN** `wind_gen` value=4840 d1=-77.0 d12=-230.0 z=-2.405610501547988
- **PERSISTENT_UP** `interconnector_net` value=1.125e+04 d1=176.0 d12=1025.0 z=0.89369891875
- **REVERSAL** `ccgt_gen` value=5449 d1=44.0 d12=-377.0 z=-0.6753271053693359
- **ACCELERATION** `nuclear_gen` value=3338 d1=2.0 d12=2.0 z=0.67448975
- **REVERSAL** `thermal_base` value=8787 d1=46.0 d12=-375.0 z=-0.6711424063275434
- **REVERSAL** `biomass_gen` value=3015 d1=-4.0 d12=23.0 z=0.6244534183976261
- **PERSISTENT_UP** `ind_demand` value=-1.184e+04 d1=0.0 d12=1.0 z=None

## Nearest historical live analogues

- `2026-09-21T00:03:26.283660Z` distance=0.006 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T00:07:41.732348Z` distance=0.006 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T23:53:21.201980Z` distance=1.154 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T23:57:34.023150Z` distance=1.154 → {'next30m_imbalance_delta': -38.0, 'next30m_margin_delta': -9.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T23:32:17.355228Z` distance=1.157 → {'next30m_imbalance_delta': 232.0, 'next30m_margin_delta': -76.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
