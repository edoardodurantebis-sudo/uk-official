# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T21:19:38.384301Z`  
Memory snapshots: **1954**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=1.52e+04 d1=0.0 d12=-45.0 z=-16.120305025
- **ROBUST_OUTLIER** `ind_generation` value=1.52e+04 d1=0.0 d12=-45.0 z=-16.120305025
- **CHANGE_POINT** `imbalance` value=-5405 d1=0.0 d12=-45.0 z=-11.225436553571429
- **ROBUST_OUTLIER** `imbalance` value=-5405 d1=0.0 d12=-45.0 z=-11.225436553571429
- **CHANGE_POINT** `biomass_gen` value=2684 d1=36.0 d12=241.0 z=1.5627522076502733
- **CHANGE_POINT** `interconnector_net` value=1.109e+04 d1=-13.0 d12=119.0 z=0.7886654245481928
- **CHANGE_POINT** `thermal_base` value=1.021e+04 d1=-125.0 d12=-691.0 z=-0.3361801713693765
- **CHANGE_POINT** `ccgt_gen` value=6879 d1=-130.0 d12=-690.0 z=-0.3355154141025641
- **CHANGE_POINT** `margin` value=3.554e+04 d1=0.0 d12=-5.0 z=-0.16306345604395603
- **PERSISTENT_UP** `biomass_gen` value=2684 d1=36.0 d12=241.0 z=1.5627522076502733
- **REVERSAL** `interconnector_net` value=1.109e+04 d1=-13.0 d12=119.0 z=0.7886654245481928
- **REVERSAL** `nuclear_gen` value=3335 d1=5.0 d12=-1.0 z=-0.337244875
- **ACCELERATION** `nuclear_gen` value=3335 d1=5.0 d12=-1.0 z=-0.337244875
- **PERSISTENT_DOWN** `thermal_base` value=1.021e+04 d1=-125.0 d12=-691.0 z=-0.3361801713693765
- **PERSISTENT_DOWN** `ccgt_gen` value=6879 d1=-130.0 d12=-690.0 z=-0.3355154141025641

## Nearest historical live analogues

- `2026-09-20T20:20:49.115047Z` distance=0.002 → {'next30m_imbalance_delta': -23.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T20:25:01.027505Z` distance=0.002 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T19:51:24.368585Z` distance=0.003 → {'next30m_imbalance_delta': 1.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T19:55:37.480854Z` distance=0.003 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T19:59:48.365587Z` distance=0.003 → {'next30m_imbalance_delta': -23.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -2.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
