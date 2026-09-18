# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T07:56:50.864202Z`  
Memory snapshots: **1136**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=-334.0 z=-10.023667118055556
- **CHANGE_POINT** `wind_gen` value=1.244e+04 d1=41.0 d12=-594.0 z=-3.363910905063291
- **REVERSAL** `interconnector_net` value=3373 d1=-60.0 d12=2351.0 z=4.43642548889511
- **ROBUST_OUTLIER** `interconnector_net` value=3373 d1=-60.0 d12=2351.0 z=4.43642548889511
- **CHANGE_POINT** `ind_generation` value=2.772e+04 d1=0.0 d12=343.0 z=1.528047575221239
- **PERSISTENT_DOWN** `residual_proxy` value=8097 d1=0.0 d12=-444.0 z=-3.4848637083333336
- **ROBUST_OUTLIER** `residual_proxy` value=8097 d1=0.0 d12=-444.0 z=-3.4848637083333336
- **REVERSAL** `wind_gen` value=1.244e+04 d1=41.0 d12=-594.0 z=-3.363910905063291
- **ROBUST_OUTLIER** `wind_gen` value=1.244e+04 d1=41.0 d12=-594.0 z=-3.363910905063291
- **CHANGE_POINT** `imbalance` value=1.022e+04 d1=0.0 d12=-347.0 z=-1.17023971625
- **CHANGE_POINT** `margin` value=3.776e+04 d1=0.0 d12=-189.0 z=-1.1654448741496597
- **CHANGE_POINT** `biomass_gen` value=2169 d1=6.0 d12=-8.0 z=0.548022921875
- **PERSISTENT_UP** `nuclear_gen` value=3341 d1=7.0 d12=11.0 z=1.5738094166666665
- **ACCELERATION** `nuclear_gen` value=3341 d1=7.0 d12=11.0 z=1.5738094166666665
- **REVERSAL** `thermal_base` value=7666 d1=9.0 d12=-156.0 z=0.8879262587274775

## Nearest historical live analogues

- `2026-09-18T06:53:49.549140Z` distance=0.438 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T06:58:01.482012Z` distance=0.438 → {'next30m_imbalance_delta': -347.0, 'next30m_margin_delta': -189.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T07:02:14.066477Z` distance=0.438 → {'next30m_imbalance_delta': -347.0, 'next30m_margin_delta': -189.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T03:32:11.466334Z` distance=0.632 → {'next30m_imbalance_delta': 521.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T03:36:24.269730Z` distance=0.632 → {'next30m_imbalance_delta': 521.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
