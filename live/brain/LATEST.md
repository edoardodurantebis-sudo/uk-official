# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T07:52:37.478189Z`  
Memory snapshots: **1135**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.174e+04 d1=0.0 d12=-334.0 z=-10.023667118055556
- **CHANGE_POINT** `wind_gen` value=1.24e+04 d1=-19.0 d12=-1139.0 z=-3.7904240583976834
- **ROBUST_OUTLIER** `interconnector_net` value=3433 d1=0.0 d12=3630.0 z=4.701816367288801
- **ROBUST_OUTLIER** `wind_gen` value=1.24e+04 d1=-19.0 d12=-1139.0 z=-3.7904240583976834
- **CHANGE_POINT** `ind_generation` value=2.772e+04 d1=0.0 d12=343.0 z=1.528047575221239
- **PERSISTENT_DOWN** `residual_proxy` value=8097 d1=0.0 d12=-444.0 z=-3.4848637083333336
- **ACCELERATION** `residual_proxy` value=8097 d1=0.0 d12=-444.0 z=-3.4848637083333336
- **ROBUST_OUTLIER** `residual_proxy` value=8097 d1=0.0 d12=-444.0 z=-3.4848637083333336
- **CHANGE_POINT** `imbalance` value=1.022e+04 d1=0.0 d12=-347.0 z=-1.17023971625
- **CHANGE_POINT** `margin` value=3.776e+04 d1=0.0 d12=-189.0 z=-1.1654448741496597
- **CHANGE_POINT** `biomass_gen` value=2163 d1=0.0 d12=-12.0 z=0.46746814356435645
- **PERSISTENT_DOWN** `ccgt_gen` value=4323 d1=-41.0 d12=-248.0 z=0.8882960789623717
- **PERSISTENT_DOWN** `thermal_base` value=7657 d1=-43.0 d12=-241.0 z=0.878210070418552
- **PERSISTENT_DOWN** `ps_gen` value=598 d1=0.0 d12=-286.0 z=0.620810634948097
- **PERSISTENT_DOWN** `biomass_gen` value=2163 d1=0.0 d12=-12.0 z=0.46746814356435645

## Nearest historical live analogues

- `2026-09-18T06:53:49.549140Z` distance=0.438 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T06:58:01.482012Z` distance=0.438 → {'next30m_imbalance_delta': -347.0, 'next30m_margin_delta': -189.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T03:32:11.466334Z` distance=0.632 → {'next30m_imbalance_delta': 521.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T03:36:24.269730Z` distance=0.632 → {'next30m_imbalance_delta': 521.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T03:40:35.454286Z` distance=0.632 → {'next30m_imbalance_delta': 521.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
