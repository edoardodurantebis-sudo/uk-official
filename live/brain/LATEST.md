# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T00:09:31.504316Z`  
Memory snapshots: **2334**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.238e+04 d1=0.0 d12=-3.0 z=-11.562681428571429
- **ROBUST_OUTLIER** `ind_demand` value=-1.238e+04 d1=0.0 d12=-3.0 z=-11.562681428571429
- **CHANGE_POINT** `imbalance` value=-2010 d1=0.0 d12=483.0 z=2.2601892103365384
- **CHANGE_POINT** `ind_generation` value=1.945e+04 d1=0.0 d12=483.0 z=2.2601892103365384
- **CHANGE_POINT** `ps_gen` value=-284 d1=1.0 d12=-146.0 z=-1.3002348626050422
- **CHANGE_POINT** `margin` value=3.622e+04 d1=0.0 d12=-16.0 z=1.024705581730769
- **CHANGE_POINT** `biomass_gen` value=3004 d1=0.0 d12=0.0 z=-0.35330415476190474
- **REVERSAL** `thermal_base` value=1.489e+04 d1=-25.0 d12=193.0 z=-1.398423423582296
- **REVERSAL** `ccgt_gen` value=1.124e+04 d1=-27.0 d12=184.0 z=-1.3400204331119545
- **REVERSAL** `ps_gen` value=-284 d1=1.0 d12=-146.0 z=-1.3002348626050422
- **PERSISTENT_UP** `interconnector_net` value=3631 d1=126.0 d12=501.0 z=-1.1963139173094037
- **PERSISTENT_UP** `nuclear_gen` value=3652 d1=2.0 d12=9.0 z=0.9420559318181818
- **REVERSAL** `wind_gen` value=3680 d1=-32.0 d12=89.0 z=0.16418500493421054
- **ACCELERATION** `wind_gen` value=3680 d1=-32.0 d12=89.0 z=0.16418500493421054
- **PERSISTENT_DOWN** `frequency` value=50.09 d1=0.0 d12=-0.015999999999998238 z=None

## Nearest historical live analogues

- `2026-09-21T22:52:30.792878Z` distance=0.277 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T22:56:44.809172Z` distance=0.277 → {'next30m_imbalance_delta': 477.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -67.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T23:00:57.207752Z` distance=0.277 → {'next30m_imbalance_delta': 477.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -67.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T23:05:43.970208Z` distance=0.277 → {'next30m_imbalance_delta': 477.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -67.0, 'next30m_residual_proxy_delta': -882.0}
- `2026-09-21T23:09:56.346083Z` distance=0.277 → {'next30m_imbalance_delta': 477.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -67.0, 'next30m_residual_proxy_delta': -882.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
