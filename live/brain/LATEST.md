# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T17:18:42.076917Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **ROBUST_OUTLIER** `residual_proxy` value=7138 d1=0.0 d12=-453.0 z=-20.369590449999997
- **ROBUST_OUTLIER** `ps_gen` value=1508 d1=0.0 d12=151.0 z=9.619358490654205
- **CHANGE_POINT** `ccgt_gen` value=1.54e+04 d1=7.0 d12=775.0 z=2.4132031803291785
- **CHANGE_POINT** `thermal_base` value=1.913e+04 d1=6.0 d12=775.0 z=2.3726119304558226
- **PERSISTENT_DOWN** `interconnector_net` value=6584 d1=-26.0 d12=-1114.0 z=-2.8891529448818893
- **CHANGE_POINT** `ind_generation` value=1.322e+04 d1=0.0 d12=-11.0 z=-0.6834720590193705
- **CHANGE_POINT** `imbalance` value=-7954 d1=0.0 d12=-11.0 z=-0.6833118513674197
- **PERSISTENT_UP** `ccgt_gen` value=1.54e+04 d1=7.0 d12=775.0 z=2.4132031803291785
- **PERSISTENT_UP** `thermal_base` value=1.913e+04 d1=6.0 d12=775.0 z=2.3726119304558226
- **ACCELERATION** `biomass_gen` value=2903 d1=-12.0 d12=-8.0 z=-0.9218026583333334
- **ACCELERATION** `wind_gen` value=1345 d1=3.0 d12=40.0 z=-0.774544182661028
- **ACCELERATION** `nuclear_gen` value=3730 d1=-1.0 d12=0.0 z=0.1686224375

## Nearest historical live analogues

- `2026-09-22T16:23:11.219801Z` distance=0.046 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -453.0}
- `2026-09-22T14:23:37.089780Z` distance=0.046 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 15.0}
- `2026-09-22T14:27:59.397853Z` distance=0.046 → {'next30m_imbalance_delta': -11.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -37.0, 'next30m_residual_proxy_delta': 15.0}
- `2026-09-22T14:32:13.058260Z` distance=0.046 → {'next30m_imbalance_delta': -11.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -37.0, 'next30m_residual_proxy_delta': 15.0}
- `2026-09-22T14:36:27.552774Z` distance=0.046 → {'next30m_imbalance_delta': -11.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -37.0, 'next30m_residual_proxy_delta': 15.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
