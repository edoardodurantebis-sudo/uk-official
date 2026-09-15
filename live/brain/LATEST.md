# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T00:18:17.511389Z`  
Memory snapshots: **39**  
Current physical regime: **BALANCED**

Regime read: residual high, margin high.

## Active patterns

- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=4457.0 z=9.019316612867646
- **CHANGE_POINT** `biomass_gen` value=2855 d1=47.0 d12=178.0 z=7.706404164893617
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=4457.0 z=9.019316612867646
- **PERSISTENT_UP** `biomass_gen` value=2855 d1=47.0 d12=178.0 z=7.706404164893617
- **ROBUST_OUTLIER** `biomass_gen` value=2855 d1=47.0 d12=178.0 z=7.706404164893617
- **CHANGE_POINT** `margin` value=3.272e+04 d1=0.0 d12=239.0 z=3.34546916
- **CHANGE_POINT** `imbalance` value=210 d1=0.0 d12=23.0 z=2.523897129032258
- **CHANGE_POINT** `ind_generation` value=2.07e+04 d1=0.0 d12=23.0 z=2.50910187
- **ROBUST_OUTLIER** `margin` value=3.272e+04 d1=0.0 d12=239.0 z=3.34546916
- **CHANGE_POINT** `wind_gen` value=1.193e+04 d1=-90.0 d12=-382.0 z=-1.0565512196843854
- **CHANGE_POINT** `ind_demand` value=-1.227e+04 d1=0.0 d12=0.0 z=-0.67448975
- **REVERSAL** `interconnector_net` value=-349 d1=-46.0 d12=2251.0 z=2.5140609193654266
- **CHANGE_POINT** `ps_gen` value=-14 d1=0.0 d12=122.0 z=None
- **PERSISTENT_DOWN** `ccgt_gen` value=3842 d1=-63.0 d12=-930.0 z=-1.0995740188492062
- **PERSISTENT_DOWN** `thermal_base` value=7156 d1=-63.0 d12=-932.0 z=-1.0982949534066329

## Nearest historical live analogues

- `2026-09-14T23:19:39.979677Z` distance=8.198 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 4546.0}
- `2026-09-14T22:54:28.088906Z` distance=8.221 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': -8.0}
- `2026-09-14T23:11:14.299399Z` distance=8.231 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 4544.0}
- `2026-09-14T23:15:27.902002Z` distance=8.231 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 4544.0}
- `2026-09-14T23:02:51.731221Z` distance=8.236 → {'next30m_imbalance_delta': 250.0, 'next30m_margin_delta': 9.0, 'next30m_residual_proxy_delta': 158.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
