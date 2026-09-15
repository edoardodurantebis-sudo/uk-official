# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T01:08:32.145790Z`  
Memory snapshots: **51**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.235e+04 d1=0.0 d12=-77.0 z=-26.30510025
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=0.0 z=5.294097121509599
- **CHANGE_POINT** `biomass_gen` value=3162 d1=12.0 d12=307.0 z=3.153075870145631
- **CHANGE_POINT** `nuclear_gen` value=3328 d1=4.0 d12=14.0 z=3.147618833333333
- **CHANGE_POINT** `ps_gen` value=-7 d1=0.0 d12=7.0 z=1.686224375
- **CHANGE_POINT** `imbalance` value=272 d1=0.0 d12=62.0 z=1.4286240461254611
- **CHANGE_POINT** `ind_generation` value=2.076e+04 d1=0.0 d12=61.0 z=1.4233717518382352
- **PERSISTENT_UP** `biomass_gen` value=3162 d1=12.0 d12=307.0 z=3.153075870145631
- **ROBUST_OUTLIER** `biomass_gen` value=3162 d1=12.0 d12=307.0 z=3.153075870145631
- **PERSISTENT_UP** `nuclear_gen` value=3328 d1=4.0 d12=14.0 z=3.147618833333333
- **ROBUST_OUTLIER** `nuclear_gen` value=3328 d1=4.0 d12=14.0 z=3.147618833333333
- **CHANGE_POINT** `margin` value=3.267e+04 d1=0.0 d12=-52.0 z=0.6692476016839378
- **PERSISTENT_DOWN** `ccgt_gen` value=3603 d1=-1.0 d12=-239.0 z=-0.7860670409836066
- **REVERSAL** `thermal_base` value=6931 d1=3.0 d12=-225.0 z=-0.7771784976791682
- **REVERSAL** `interconnector_net` value=-303 d1=-434.0 d12=46.0 z=0.684563394410279

## Nearest historical live analogues

- `2026-09-14T23:53:08.620374Z` distance=22.229 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:57:18.949614Z` distance=22.229 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:01:29.159410Z` distance=22.229 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:05:39.935821Z` distance=22.229 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:09:52.902274Z` distance=22.229 → {'next30m_imbalance_delta': 54.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
