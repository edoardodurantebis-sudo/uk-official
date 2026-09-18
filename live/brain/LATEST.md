# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T02:15:53.756452Z`  
Memory snapshots: **1055**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=1.016e+04 d1=0.0 d12=34.0 z=10.349928922413792
- **CHANGE_POINT** `ind_generation` value=2.698e+04 d1=0.0 d12=34.0 z=10.349928922413792
- **ROBUST_OUTLIER** `imbalance` value=1.016e+04 d1=0.0 d12=34.0 z=10.349928922413792
- **ROBUST_OUTLIER** `ind_generation` value=2.698e+04 d1=0.0 d12=34.0 z=10.349928922413792
- **CHANGE_POINT** `ind_demand` value=-1.122e+04 d1=0.0 d12=-30.0 z=-3.79844227631579
- **ROBUST_OUTLIER** `ind_demand` value=-1.122e+04 d1=0.0 d12=-30.0 z=-3.79844227631579
- **CHANGE_POINT** `ccgt_gen` value=3229 d1=23.0 d12=-478.0 z=-1.413558305851064
- **CHANGE_POINT** `thermal_base` value=6554 d1=23.0 d12=-485.0 z=-1.3965989027924133
- **CHANGE_POINT** `wind_gen` value=1.433e+04 d1=-120.0 d12=200.0 z=-0.7678343136160715
- **CHANGE_POINT** `biomass_gen` value=1858 d1=-1.0 d12=-97.0 z=-0.4276733115141956
- **REVERSAL** `ccgt_gen` value=3229 d1=23.0 d12=-478.0 z=-1.413558305851064
- **REVERSAL** `thermal_base` value=6554 d1=23.0 d12=-485.0 z=-1.3965989027924133
- **REVERSAL** `wind_gen` value=1.433e+04 d1=-120.0 d12=200.0 z=-0.7678343136160715
- **ACCELERATION** `wind_gen` value=1.433e+04 d1=-120.0 d12=200.0 z=-0.7678343136160715
- **PERSISTENT_DOWN** `nuclear_gen` value=3325 d1=0.0 d12=-7.0 z=0.67448975

## Nearest historical live analogues

- `2026-09-18T00:55:05.130155Z` distance=0.045 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:59:16.440589Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:03:26.672918Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:07:37.196261Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:11:47.784139Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
