# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T02:31:01.988533Z`  
Memory snapshots: **2028**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.755e+04 d1=0.0 d12=1723.0 z=25.400996968085106
- **PERSISTENT_UP** `margin` value=3.755e+04 d1=0.0 d12=1723.0 z=25.400996968085106
- **ROBUST_OUTLIER** `margin` value=3.755e+04 d1=0.0 d12=1723.0 z=25.400996968085106
- **CHANGE_POINT** `ind_demand` value=-1.18e+04 d1=0.0 d12=27.0 z=1.4613944583333334
- **CHANGE_POINT** `thermal_base` value=8256 d1=-92.0 d12=-514.0 z=-1.3931049976635512
- **CHANGE_POINT** `ccgt_gen` value=4913 d1=-93.0 d12=-518.0 z=-1.3879223262124711
- **PERSISTENT_UP** `nuclear_gen` value=3343 d1=1.0 d12=4.0 z=2.360714125
- **ACCELERATION** `nuclear_gen` value=3343 d1=1.0 d12=4.0 z=2.360714125
- **PERSISTENT_DOWN** `wind_gen` value=3888 d1=-52.0 d12=-181.0 z=-2.1163460921494543
- **PERSISTENT_UP** `ind_demand` value=-1.18e+04 d1=0.0 d12=27.0 z=1.4613944583333334
- **PERSISTENT_UP** `interconnector_net` value=1.252e+04 d1=148.0 d12=285.0 z=1.4212802348377997
- **ACCELERATION** `interconnector_net` value=1.252e+04 d1=148.0 d12=285.0 z=1.4212802348377997
- **PERSISTENT_DOWN** `thermal_base` value=8256 d1=-92.0 d12=-514.0 z=-1.3931049976635512
- **PERSISTENT_DOWN** `ccgt_gen` value=4913 d1=-93.0 d12=-518.0 z=-1.3879223262124711
- **REVERSAL** `biomass_gen` value=3013 d1=2.0 d12=-6.0 z=0.56657139

## Nearest historical live analogues

- `2026-09-21T01:23:21.503053Z` distance=0.869 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:28:09.159328Z` distance=0.869 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:32:22.156789Z` distance=0.869 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:36:33.089731Z` distance=0.869 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T00:03:26.283660Z` distance=0.870 → {'next30m_imbalance_delta': 339.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -38.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
