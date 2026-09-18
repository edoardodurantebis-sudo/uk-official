# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T08:01:05.020362Z`  
Memory snapshots: **1137**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=-334.0 z=-10.023667118055556
- **CHANGE_POINT** `wind_gen` value=1.255e+04 d1=102.0 d12=-265.0 z=-3.119056049001815
- **REVERSAL** `interconnector_net` value=3288 d1=-85.0 d12=1737.0 z=4.2462195625
- **ROBUST_OUTLIER** `interconnector_net` value=3288 d1=-85.0 d12=1737.0 z=4.2462195625
- **CHANGE_POINT** `ind_generation` value=2.772e+04 d1=0.0 d12=343.0 z=1.528047575221239
- **ROBUST_OUTLIER** `residual_proxy` value=8097 d1=0.0 d12=-444.0 z=-3.4848637083333336
- **CHANGE_POINT** `imbalance` value=1.022e+04 d1=0.0 d12=-347.0 z=-1.17023971625
- **CHANGE_POINT** `margin` value=3.776e+04 d1=0.0 d12=-189.0 z=-1.1654448741496597
- **REVERSAL** `wind_gen` value=1.255e+04 d1=102.0 d12=-265.0 z=-3.119056049001815
- **ROBUST_OUTLIER** `wind_gen` value=1.255e+04 d1=102.0 d12=-265.0 z=-3.119056049001815
- **CHANGE_POINT** `biomass_gen` value=2172 d1=3.0 d12=-3.0 z=0.59017853125
- **REVERSAL** `nuclear_gen` value=3340 d1=-1.0 d12=4.0 z=1.3489794999999998
- **ACCELERATION** `nuclear_gen` value=3340 d1=-1.0 d12=4.0 z=1.3489794999999998
- **PERSISTENT_DOWN** `thermal_base` value=7623 d1=-43.0 d12=-109.0 z=0.8116359991666666
- **ACCELERATION** `thermal_base` value=7623 d1=-43.0 d12=-109.0 z=0.8116359991666666

## Nearest historical live analogues

- `2026-09-18T06:53:49.549140Z` distance=0.438 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T06:58:01.482012Z` distance=0.438 → {'next30m_imbalance_delta': -347.0, 'next30m_margin_delta': -189.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T07:02:14.066477Z` distance=0.438 → {'next30m_imbalance_delta': -347.0, 'next30m_margin_delta': -189.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T07:06:24.378452Z` distance=0.438 → {'next30m_imbalance_delta': -347.0, 'next30m_margin_delta': -189.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T03:32:11.466334Z` distance=0.632 → {'next30m_imbalance_delta': 521.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
