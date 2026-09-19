# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T15:07:21.988797Z`  
Memory snapshots: **1525**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=587 d1=1.0 d12=109.0 z=74.1938725
- **ROBUST_OUTLIER** `biomass_gen` value=587 d1=1.0 d12=109.0 z=74.1938725
- **CHANGE_POINT** `ccgt_gen` value=3831 d1=-12.0 d12=641.0 z=3.4408752463768115
- **CHANGE_POINT** `thermal_base` value=7165 d1=-12.0 d12=646.0 z=3.4228554572953738
- **CHANGE_POINT** `wind_gen` value=1.389e+04 d1=317.0 d12=-559.0 z=-2.2471943513513515
- **CHANGE_POINT** `interconnector_net` value=-3404 d1=-23.0 d12=-91.0 z=-2.0399063951680674
- **REVERSAL** `ccgt_gen` value=3831 d1=-12.0 d12=641.0 z=3.4408752463768115
- **ROBUST_OUTLIER** `ccgt_gen` value=3831 d1=-12.0 d12=641.0 z=3.4408752463768115
- **REVERSAL** `thermal_base` value=7165 d1=-12.0 d12=646.0 z=3.4228554572953738
- **ROBUST_OUTLIER** `thermal_base` value=7165 d1=-12.0 d12=646.0 z=3.4228554572953738
- **CHANGE_POINT** `imbalance` value=-3174 d1=0.0 d12=65.0 z=0.30460827419354836
- **REVERSAL** `wind_gen` value=1.389e+04 d1=317.0 d12=-559.0 z=-2.2471943513513515
- **ACCELERATION** `interconnector_net` value=-3404 d1=-23.0 d12=-91.0 z=-2.0399063951680674
- **PERSISTENT_UP** `nuclear_gen` value=3334 d1=0.0 d12=5.0 z=0.6744897499999999
- **PERSISTENT_DOWN** `ps_gen` value=-547 d1=-1.0 d12=-290.0 z=0.15838220850202428

## Nearest historical live analogues

- `2026-09-19T13:51:46.286416Z` distance=0.022 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T13:55:56.183209Z` distance=0.022 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 64.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T14:00:11.889935Z` distance=0.022 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 64.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T14:04:22.992173Z` distance=0.022 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 64.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T14:08:33.763772Z` distance=0.022 → {'next30m_imbalance_delta': 9.0, 'next30m_margin_delta': 64.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
