# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T01:57:36.523388Z`  
Memory snapshots: **709**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2132 d1=-112.0 d12=-1004.0 z=-362.20099575
- **PERSISTENT_DOWN** `biomass_gen` value=2132 d1=-112.0 d12=-1004.0 z=-362.20099575
- **ROBUST_OUTLIER** `biomass_gen` value=2132 d1=-112.0 d12=-1004.0 z=-362.20099575
- **PERSISTENT_UP** `ind_demand` value=-1.153e+04 d1=0.0 d12=220.0 z=31.835916200000003
- **ACCELERATION** `ind_demand` value=-1.153e+04 d1=0.0 d12=220.0 z=31.835916200000003
- **ROBUST_OUTLIER** `ind_demand` value=-1.153e+04 d1=0.0 d12=220.0 z=31.835916200000003
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `thermal_base` value=7378 d1=10.0 d12=-909.0 z=-2.2048246450247
- **CHANGE_POINT** `ccgt_gen` value=4066 d1=9.0 d12=-902.0 z=-2.1955281250878427
- **PERSISTENT_DOWN** `interconnector_net` value=-6685 d1=-22.0 d12=-43.0 z=-3.2917271425545436
- **ACCELERATION** `interconnector_net` value=-6685 d1=-22.0 d12=-43.0 z=-3.2917271425545436
- **ROBUST_OUTLIER** `interconnector_net` value=-6685 d1=-22.0 d12=-43.0 z=-3.2917271425545436
- **CHANGE_POINT** `ps_gen` value=-597 d1=-233.0 d12=-285.0 z=-1.0577225625000002
- **REVERSAL** `thermal_base` value=7378 d1=10.0 d12=-909.0 z=-2.2048246450247

## Nearest historical live analogues

- `2026-09-17T00:54:40.714610Z` distance=0.483 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:58:51.888099Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:03:09.320399Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:50:29.902043Z` distance=0.518 → {'next30m_imbalance_delta': -43.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:03:44.260171Z` distance=0.518 → {'next30m_imbalance_delta': 107.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
