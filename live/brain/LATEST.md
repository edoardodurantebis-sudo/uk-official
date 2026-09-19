# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T03:32:06.717243Z`  
Memory snapshots: **1360**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **ROBUST_OUTLIER** `margin` value=3.831e+04 d1=0.0 d12=2.0 z=6.53123925621118
- **CHANGE_POINT** `biomass_gen` value=746 d1=-43.0 d12=-197.0 z=-4.078068796153846
- **CHANGE_POINT** `imbalance` value=9422 d1=0.0 d12=166.0 z=2.2514657852112676
- **CHANGE_POINT** `ind_generation` value=2.662e+04 d1=0.0 d12=166.0 z=2.2295633402777777
- **PERSISTENT_DOWN** `biomass_gen` value=746 d1=-43.0 d12=-197.0 z=-4.078068796153846
- **ROBUST_OUTLIER** `biomass_gen` value=746 d1=-43.0 d12=-197.0 z=-4.078068796153846
- **PERSISTENT_UP** `imbalance` value=9422 d1=0.0 d12=166.0 z=2.2514657852112676
- **PERSISTENT_UP** `ind_generation` value=2.662e+04 d1=0.0 d12=166.0 z=2.2295633402777777
- **REVERSAL** `ccgt_gen` value=3058 d1=-1.0 d12=2.0 z=-2.1010959475703324
- **ACCELERATION** `ccgt_gen` value=3058 d1=-1.0 d12=2.0 z=-2.1010959475703324
- **REVERSAL** `thermal_base` value=6400 d1=-2.0 d12=3.0 z=-2.041971462593516
- **ACCELERATION** `thermal_base` value=6400 d1=-2.0 d12=3.0 z=-2.041971462593516
- **PERSISTENT_UP** `ind_demand` value=-1.088e+04 d1=0.0 d12=5.0 z=2.0234692499999998
- **REVERSAL** `nuclear_gen` value=3342 d1=-1.0 d12=1.0 z=1.0117346249999999
- **PERSISTENT_UP** `interconnector_net` value=-1.114e+04 d1=20.0 d12=43.0 z=-0.9544257464664311

## Nearest historical live analogues

- `2026-09-19T02:20:35.608449Z` distance=0.315 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:24:50.521130Z` distance=0.315 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:29:01.647315Z` distance=0.315 → {'next30m_imbalance_delta': 140.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:33:15.620122Z` distance=0.315 → {'next30m_imbalance_delta': 140.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T02:37:27.246722Z` distance=0.315 → {'next30m_imbalance_delta': 140.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
