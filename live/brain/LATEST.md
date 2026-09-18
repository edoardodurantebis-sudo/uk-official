# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T14:42:37.911201Z`  
Memory snapshots: **1232**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=-22.0 z=-14.8387745
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-6.528097223214285
- **CHANGE_POINT** `imbalance` value=8550 d1=0.0 d12=-385.0 z=-4.350458887499999
- **CHANGE_POINT** `wind_gen` value=1.675e+04 d1=254.0 d12=1122.0 z=3.7167748822178477
- **CHANGE_POINT** `biomass_gen` value=1481 d1=-5.0 d12=438.0 z=3.08579060625
- **ROBUST_OUTLIER** `imbalance` value=8550 d1=0.0 d12=-385.0 z=-4.350458887499999
- **PERSISTENT_UP** `wind_gen` value=1.675e+04 d1=254.0 d12=1122.0 z=3.7167748822178477
- **ROBUST_OUTLIER** `wind_gen` value=1.675e+04 d1=254.0 d12=1122.0 z=3.7167748822178477
- **CHANGE_POINT** `margin` value=3.83e+04 d1=0.0 d12=122.0 z=1.4716139999999998
- **ROBUST_OUTLIER** `residual_proxy` value=9748 d1=0.0 d12=380.0 z=3.3488416087500004
- **REVERSAL** `biomass_gen` value=1481 d1=-5.0 d12=438.0 z=3.08579060625
- **ROBUST_OUTLIER** `biomass_gen` value=1481 d1=-5.0 d12=438.0 z=3.08579060625
- **CHANGE_POINT** `ps_gen` value=-470 d1=3.0 d12=234.0 z=1.0633537385204082
- **PERSISTENT_DOWN** `interconnector_net` value=5020 d1=-1.0 d12=-1460.0 z=-0.3936935879828326
- **REVERSAL** `thermal_base` value=5820 d1=2.0 d12=-1.0 z=-0.2911731707650273

## Nearest historical live analogues

- `2026-09-18T13:22:08.039057Z` distance=0.147 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:26:20.440549Z` distance=0.147 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:30:31.422218Z` distance=0.147 → {'next30m_imbalance_delta': -7.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:34:41.646705Z` distance=0.147 → {'next30m_imbalance_delta': -7.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:38:52.307026Z` distance=0.147 → {'next30m_imbalance_delta': -7.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
