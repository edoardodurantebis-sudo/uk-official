# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T16:35:49.660745Z`  
Memory snapshots: **1546**  
Current physical regime: **LOOSE**

Regime read: residual low, wind rising.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=607 d1=0.0 d12=1.0 z=43.84183375
- **ACCELERATION** `biomass_gen` value=607 d1=0.0 d12=1.0 z=43.84183375
- **ROBUST_OUTLIER** `biomass_gen` value=607 d1=0.0 d12=1.0 z=43.84183375
- **PERSISTENT_UP** `ps_gen` value=863 d1=190.0 d12=736.0 z=7.370473871183206
- **ROBUST_OUTLIER** `ps_gen` value=863 d1=190.0 d12=736.0 z=7.370473871183206
- **CHANGE_POINT** `thermal_base` value=7689 d1=76.0 d12=718.0 z=3.8035019695402297
- **CHANGE_POINT** `ccgt_gen` value=4359 d1=75.0 d12=719.0 z=3.754351622146119
- **CHANGE_POINT** `interconnector_net` value=535 d1=-15.0 d12=3449.0 z=2.1460620091899254
- **CHANGE_POINT** `ind_generation` value=1.68e+04 d1=0.0 d12=21.0 z=1.93915803125
- **PERSISTENT_UP** `thermal_base` value=7689 d1=76.0 d12=718.0 z=3.8035019695402297
- **ROBUST_OUTLIER** `thermal_base` value=7689 d1=76.0 d12=718.0 z=3.8035019695402297
- **PERSISTENT_UP** `ccgt_gen` value=4359 d1=75.0 d12=719.0 z=3.754351622146119
- **ROBUST_OUTLIER** `ccgt_gen` value=4359 d1=75.0 d12=719.0 z=3.754351622146119
- **PERSISTENT_DOWN** `residual_proxy` value=1.259e+04 d1=0.0 d12=-206.0 z=-3.1556484732142858
- **ACCELERATION** `residual_proxy` value=1.259e+04 d1=0.0 d12=-206.0 z=-3.1556484732142858

## Nearest historical live analogues

- `2026-09-19T14:50:38.602742Z` distance=0.069 → {'next30m_imbalance_delta': 56.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T14:54:49.696714Z` distance=0.069 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T14:59:00.358192Z` distance=0.069 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 114.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T15:03:11.018485Z` distance=0.069 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 114.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T15:07:21.988797Z` distance=0.069 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 114.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
