# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T14:21:00.093276Z`  
Memory snapshots: **1227**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-6.528097223214285
- **CHANGE_POINT** `wind_gen` value=1.603e+04 d1=-24.0 d12=942.0 z=3.9861238504098364
- **CHANGE_POINT** `biomass_gen` value=1362 d1=50.0 d12=325.0 z=2.082487103125
- **REVERSAL** `wind_gen` value=1.603e+04 d1=-24.0 d12=942.0 z=3.9861238504098364
- **ROBUST_OUTLIER** `wind_gen` value=1.603e+04 d1=-24.0 d12=942.0 z=3.9861238504098364
- **PERSISTENT_UP** `residual_proxy` value=9748 d1=380.0 d12=380.0 z=3.3488416087500004
- **ACCELERATION** `residual_proxy` value=9748 d1=380.0 d12=380.0 z=3.3488416087500004
- **ROBUST_OUTLIER** `residual_proxy` value=9748 d1=380.0 d12=380.0 z=3.3488416087500004
- **CHANGE_POINT** `ps_gen` value=-468 d1=6.0 d12=237.0 z=1.0771188354591836
- **PERSISTENT_UP** `biomass_gen` value=1362 d1=50.0 d12=325.0 z=2.082487103125
- **PERSISTENT_UP** `ps_gen` value=-468 d1=6.0 d12=237.0 z=1.0771188354591836
- **REVERSAL** `interconnector_net` value=5794 d1=22.0 d12=-281.0 z=0.67448975
- **PERSISTENT_UP** `thermal_base` value=5825 d1=5.0 d12=34.0 z=-0.5839965854134165
- **PERSISTENT_UP** `ccgt_gen` value=2489 d1=8.0 d12=24.0 z=-0.5746034816793892
- **REVERSAL** `nuclear_gen` value=3336 d1=-3.0 d12=10.0 z=0.22482991666666666

## Nearest historical live analogues

- `2026-09-18T13:22:08.039057Z` distance=0.136 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:26:20.440549Z` distance=0.136 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:57:04.108111Z` distance=0.141 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:01:14.855580Z` distance=0.141 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:05:25.405882Z` distance=0.141 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
