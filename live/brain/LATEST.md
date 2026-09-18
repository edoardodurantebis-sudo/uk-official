# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T02:11:41.515221Z`  
Memory snapshots: **1054**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.122e+04 d1=0.0 d12=1.0 z=-20.571937375
- **ROBUST_OUTLIER** `ind_demand` value=-1.122e+04 d1=0.0 d12=1.0 z=-20.571937375
- **CHANGE_POINT** `imbalance` value=1.016e+04 d1=0.0 d12=32.0 z=10.767747080357143
- **CHANGE_POINT** `ind_generation` value=2.698e+04 d1=0.0 d12=32.0 z=10.767747080357143
- **ROBUST_OUTLIER** `imbalance` value=1.016e+04 d1=0.0 d12=32.0 z=10.767747080357143
- **ROBUST_OUTLIER** `ind_generation` value=2.698e+04 d1=0.0 d12=32.0 z=10.767747080357143
- **CHANGE_POINT** `ccgt_gen` value=3206 d1=-37.0 d12=-485.0 z=-1.334878668989547
- **CHANGE_POINT** `thermal_base` value=6531 d1=-48.0 d12=-492.0 z=-1.330829168185764
- **CHANGE_POINT** `wind_gen` value=1.445e+04 d1=-15.0 d12=337.0 z=-0.6211844483667017
- **CHANGE_POINT** `biomass_gen` value=1859 d1=-19.0 d12=-97.0 z=-0.3944384502923977
- **PERSISTENT_DOWN** `ccgt_gen` value=3206 d1=-37.0 d12=-485.0 z=-1.334878668989547
- **ACCELERATION** `ccgt_gen` value=3206 d1=-37.0 d12=-485.0 z=-1.334878668989547
- **PERSISTENT_DOWN** `thermal_base` value=6531 d1=-48.0 d12=-492.0 z=-1.330829168185764
- **ACCELERATION** `thermal_base` value=6531 d1=-48.0 d12=-492.0 z=-1.330829168185764
- **PERSISTENT_DOWN** `nuclear_gen` value=3325 d1=-11.0 d12=-7.0 z=0.67448975

## Nearest historical live analogues

- `2026-09-18T00:55:05.130155Z` distance=0.045 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:59:16.440589Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:03:26.672918Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:07:37.196261Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:11:47.784139Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
