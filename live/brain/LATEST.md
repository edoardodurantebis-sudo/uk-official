# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T17:56:16.581977Z`  
Memory snapshots: **1565**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=730 d1=48.0 d12=125.0 z=6.373239882653062
- **CHANGE_POINT** `ccgt_gen` value=6985 d1=71.0 d12=1145.0 z=6.06078363941736
- **CHANGE_POINT** `thermal_base` value=1.031e+04 d1=66.0 d12=1135.0 z=5.995641197523584
- **PERSISTENT_UP** `biomass_gen` value=730 d1=48.0 d12=125.0 z=6.373239882653062
- **ROBUST_OUTLIER** `biomass_gen` value=730 d1=48.0 d12=125.0 z=6.373239882653062
- **PERSISTENT_UP** `ccgt_gen` value=6985 d1=71.0 d12=1145.0 z=6.06078363941736
- **ROBUST_OUTLIER** `ccgt_gen` value=6985 d1=71.0 d12=1145.0 z=6.06078363941736
- **PERSISTENT_UP** `thermal_base` value=1.031e+04 d1=66.0 d12=1135.0 z=5.995641197523584
- **ROBUST_OUTLIER** `thermal_base` value=1.031e+04 d1=66.0 d12=1135.0 z=5.995641197523584
- **CHANGE_POINT** `ind_generation` value=1.681e+04 d1=-3.0 d12=11.0 z=2.7376348676470585
- **CHANGE_POINT** `margin` value=3.63e+04 d1=0.0 d12=42.0 z=-2.2436152100694446
- **REVERSAL** `ps_gen` value=806 d1=9.0 d12=-110.0 z=3.4853340638075316
- **ROBUST_OUTLIER** `ps_gen` value=806 d1=9.0 d12=-110.0 z=3.4853340638075316
- **CHANGE_POINT** `imbalance` value=-3139 d1=-3.0 d12=11.0 z=1.187688472826087
- **ROBUST_OUTLIER** `residual_proxy` value=1.259e+04 d1=0.0 d12=0.0 z=-3.1556484732142858

## Nearest historical live analogues

- `2026-09-19T16:52:42.433757Z` distance=0.014 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T16:56:53.146650Z` distance=0.014 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:01:39.109374Z` distance=0.014 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:50:05.858742Z` distance=0.161 → {'next30m_imbalance_delta': 94.0, 'next30m_margin_delta': 122.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T11:24:42.200097Z` distance=0.166 → {'next30m_imbalance_delta': 24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -122.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
