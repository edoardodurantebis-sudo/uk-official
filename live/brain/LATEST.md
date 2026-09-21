# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T11:24:15.280087Z`  
Memory snapshots: **2154**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=2.0 d12=587.0 z=14.786890673076924
- **PERSISTENT_UP** `ind_demand` value=-1.224e+04 d1=2.0 d12=587.0 z=14.786890673076924
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=2.0 d12=587.0 z=14.786890673076924
- **CHANGE_POINT** `nuclear_gen` value=3516 d1=0.0 d12=21.0 z=2.83285695
- **CHANGE_POINT** `margin` value=3.65e+04 d1=0.0 d12=-4517.0 z=-1.6940672790697675
- **ROBUST_OUTLIER** `ccgt_gen` value=6722 d1=0.0 d12=-236.0 z=-3.5924950514184397
- **ROBUST_OUTLIER** `thermal_base` value=1.024e+04 d1=0.0 d12=-215.0 z=-3.3170734138627185
- **CHANGE_POINT** `residual_proxy` value=1.218e+04 d1=0.0 d12=1108.0 z=1.2135229663561076
- **CHANGE_POINT** `interconnector_net` value=1.124e+04 d1=0.0 d12=242.0 z=0.9769037448359659
- **CHANGE_POINT** `ind_generation` value=1.849e+04 d1=752.0 d12=-6238.0 z=0.2668027549732211
- **CHANGE_POINT** `imbalance` value=-3015 d1=856.0 d12=-6583.0 z=0.25738309810554805
- **CHANGE_POINT** `biomass_gen` value=3015 d1=0.0 d12=13.0 z=0.0
- **REVERSAL** `ind_generation` value=1.849e+04 d1=752.0 d12=-6238.0 z=0.2668027549732211
- **REVERSAL** `imbalance` value=-3015 d1=856.0 d12=-6583.0 z=0.25738309810554805

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.506 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.506 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.506 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.506 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.506 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
