# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T17:20:48.975917Z`  
Memory snapshots: **282**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3006 d1=15.0 d12=1004.0 z=39.273698625
- **PERSISTENT_UP** `biomass_gen` value=3006 d1=15.0 d12=1004.0 z=39.273698625
- **ROBUST_OUTLIER** `biomass_gen` value=3006 d1=15.0 d12=1004.0 z=39.273698625
- **PERSISTENT_UP** `ccgt_gen` value=1.039e+04 d1=1.0 d12=939.0 z=21.97670174154135
- **ROBUST_OUTLIER** `ccgt_gen` value=1.039e+04 d1=1.0 d12=939.0 z=21.97670174154135
- **PERSISTENT_UP** `thermal_base` value=1.371e+04 d1=3.0 d12=934.0 z=21.946273632518796
- **ROBUST_OUTLIER** `thermal_base` value=1.371e+04 d1=3.0 d12=934.0 z=21.946273632518796
- **CHANGE_POINT** `interconnector_net` value=-749 d1=17.0 d12=-3440.0 z=-7.312225327102804
- **REVERSAL** `interconnector_net` value=-749 d1=17.0 d12=-3440.0 z=-7.312225327102804
- **ROBUST_OUTLIER** `interconnector_net` value=-749 d1=17.0 d12=-3440.0 z=-7.312225327102804
- **CHANGE_POINT** `imbalance` value=5835 d1=0.0 d12=8.0 z=1.4051869791666667
- **ROBUST_OUTLIER** `ps_gen` value=501 d1=0.0 d12=377.0 z=3.2810513396226413
- **CHANGE_POINT** `ind_generation` value=2.496e+04 d1=0.0 d12=8.0 z=1.0809130608974358
- **REVERSAL** `nuclear_gen` value=3319 d1=2.0 d12=-5.0 z=-2.02346925
- **ACCELERATION** `nuclear_gen` value=3319 d1=2.0 d12=-5.0 z=-2.02346925

## Nearest historical live analogues

- `2026-09-15T16:21:57.402275Z` distance=0.096 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 53.0}
- `2026-09-15T16:26:08.230608Z` distance=0.096 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -85.0, 'next30m_residual_proxy_delta': 53.0}
- `2026-09-15T15:52:27.365496Z` distance=0.142 → {'next30m_imbalance_delta': 8.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T15:56:36.878520Z` distance=0.142 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -54.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T16:00:48.162751Z` distance=0.142 → {'next30m_imbalance_delta': 2.0, 'next30m_margin_delta': -54.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
