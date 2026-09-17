# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T02:05:58.149809Z`  
Memory snapshots: **711**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2022 d1=-35.0 d12=-992.0 z=-319.30344765
- **PERSISTENT_DOWN** `biomass_gen` value=2022 d1=-35.0 d12=-992.0 z=-319.30344765
- **ROBUST_OUTLIER** `biomass_gen` value=2022 d1=-35.0 d12=-992.0 z=-319.30344765
- **CHANGE_POINT** `ind_demand` value=-1.153e+04 d1=0.0 d12=220.0 z=31.835916200000003
- **ROBUST_OUTLIER** `ind_demand` value=-1.153e+04 d1=0.0 d12=220.0 z=31.835916200000003
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `ccgt_gen` value=4089 d1=12.0 d12=-699.0 z=-2.018347670518323
- **CHANGE_POINT** `thermal_base` value=7403 d1=13.0 d12=-705.0 z=-2.0174529886025767
- **PERSISTENT_UP** `interconnector_net` value=-6584 d1=113.0 d12=43.0 z=-3.236358770986745
- **ACCELERATION** `interconnector_net` value=-6584 d1=113.0 d12=43.0 z=-3.236358770986745
- **ROBUST_OUTLIER** `interconnector_net` value=-6584 d1=113.0 d12=43.0 z=-3.236358770986745
- **CHANGE_POINT** `ps_gen` value=-581 d1=16.0 d12=-269.0 z=-1.034430725592417
- **CHANGE_POINT** `margin` value=3.456e+04 d1=0.0 d12=50.0 z=0.9046306095800525
- **REVERSAL** `ccgt_gen` value=4089 d1=12.0 d12=-699.0 z=-2.018347670518323

## Nearest historical live analogues

- `2026-09-17T00:54:40.714610Z` distance=0.483 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:58:51.888099Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:03:09.320399Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:07:19.944210Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:11:31.123687Z` distance=0.483 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
