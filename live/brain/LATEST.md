# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T18:08:49.476283Z`  
Memory snapshots: **1568**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=7019 d1=-2.0 d12=638.0 z=5.91426095823389
- **CHANGE_POINT** `thermal_base` value=1.034e+04 d1=0.0 d12=628.0 z=5.846639603896104
- **REVERSAL** `ccgt_gen` value=7019 d1=-2.0 d12=638.0 z=5.91426095823389
- **ROBUST_OUTLIER** `ccgt_gen` value=7019 d1=-2.0 d12=638.0 z=5.91426095823389
- **PERSISTENT_UP** `thermal_base` value=1.034e+04 d1=0.0 d12=628.0 z=5.846639603896104
- **ROBUST_OUTLIER** `thermal_base` value=1.034e+04 d1=0.0 d12=628.0 z=5.846639603896104
- **CHANGE_POINT** `ind_generation` value=1.681e+04 d1=0.0 d12=11.0 z=2.5480723888888885
- **CHANGE_POINT** `margin` value=3.63e+04 d1=0.0 d12=42.0 z=-2.2436152100694446
- **CHANGE_POINT** `nuclear_gen` value=3326 d1=2.0 d12=-10.0 z=-1.686224375
- **PERSISTENT_UP** `ps_gen` value=824 d1=0.0 d12=29.0 z=3.5022668608786613
- **ACCELERATION** `ps_gen` value=824 d1=0.0 d12=29.0 z=3.5022668608786613
- **ROBUST_OUTLIER** `ps_gen` value=824 d1=0.0 d12=29.0 z=3.5022668608786613
- **CHANGE_POINT** `imbalance` value=-3139 d1=0.0 d12=11.0 z=1.187688472826087
- **ROBUST_OUTLIER** `residual_proxy` value=1.259e+04 d1=0.0 d12=0.0 z=-3.1556484732142858
- **CHANGE_POINT** `biomass_gen` value=753 d1=-6.0 d12=148.0 z=1.0429610023148148

## Nearest historical live analogues

- `2026-09-19T16:52:42.433757Z` distance=0.014 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T16:56:53.146650Z` distance=0.014 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:01:39.109374Z` distance=0.014 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:05:49.699644Z` distance=0.014 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:10:02.143135Z` distance=0.014 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
