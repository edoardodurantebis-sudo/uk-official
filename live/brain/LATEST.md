# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T03:36:24.269730Z`  
Memory snapshots: **1074**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `margin` value=3.817e+04 d1=0.0 d12=-46.0 z=11.292488185567011
- **ROBUST_OUTLIER** `margin` value=3.817e+04 d1=0.0 d12=-46.0 z=11.292488185567011
- **CHANGE_POINT** `interconnector_net` value=-6990 d1=17.0 d12=-1667.0 z=-2.254437867463026
- **CHANGE_POINT** `ind_demand` value=-1.125e+04 d1=0.0 d12=-45.0 z=-2.0234692499999998
- **REVERSAL** `interconnector_net` value=-6990 d1=17.0 d12=-1667.0 z=-2.254437867463026
- **ACCELERATION** `interconnector_net` value=-6990 d1=17.0 d12=-1667.0 z=-2.254437867463026
- **PERSISTENT_UP** `nuclear_gen` value=3336 d1=5.0 d12=6.0 z=1.3489794999999998
- **ACCELERATION** `nuclear_gen` value=3336 d1=5.0 d12=6.0 z=1.3489794999999998
- **REVERSAL** `wind_gen` value=1.376e+04 d1=75.0 d12=-254.0 z=-1.2985140798561152
- **PERSISTENT_DOWN** `ps_gen` value=180 d1=-281.0 d12=-254.0 z=-0.3329396212765957
- **ACCELERATION** `ps_gen` value=180 d1=-281.0 d12=-254.0 z=-0.3329396212765957
- **PERSISTENT_UP** `biomass_gen` value=1924 d1=40.0 d12=174.0 z=-0.10613798096446701
- **PERSISTENT_UP** `ccgt_gen` value=3747 d1=37.0 d12=327.0 z=-0.07946860088365243
- **PERSISTENT_UP** `thermal_base` value=7083 d1=42.0 d12=333.0 z=-0.06058291167664671
- **PERSISTENT_UP** `residual_proxy` value=8469 d1=0.0 d12=11023.0 z=None

## Nearest historical live analogues

- `2026-09-14T23:53:08.620374Z` distance=5.371 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:57:18.949614Z` distance=5.371 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:32:10.678260Z` distance=5.422 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:36:23.316269Z` distance=5.422 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:40:34.642541Z` distance=5.422 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
