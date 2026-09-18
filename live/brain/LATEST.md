# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T02:07:28.761763Z`  
Memory snapshots: **1053**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.122e+04 d1=0.0 d12=1.0 z=-20.571937375
- **ROBUST_OUTLIER** `ind_demand` value=-1.122e+04 d1=0.0 d12=1.0 z=-20.571937375
- **CHANGE_POINT** `imbalance` value=1.016e+04 d1=0.0 d12=32.0 z=10.767747080357143
- **CHANGE_POINT** `ind_generation` value=2.698e+04 d1=0.0 d12=32.0 z=10.767747080357143
- **ROBUST_OUTLIER** `imbalance` value=1.016e+04 d1=0.0 d12=32.0 z=10.767747080357143
- **ROBUST_OUTLIER** `ind_generation` value=2.698e+04 d1=0.0 d12=32.0 z=10.767747080357143
- **CHANGE_POINT** `ccgt_gen` value=3243 d1=-259.0 d12=-448.0 z=-1.2764773444625408
- **CHANGE_POINT** `thermal_base` value=6579 d1=-259.0 d12=-444.0 z=-1.2664002290468364
- **CHANGE_POINT** `wind_gen` value=1.447e+04 d1=-36.0 d12=352.0 z=-0.6212405592105263
- **PERSISTENT_UP** `nuclear_gen` value=3336 d1=0.0 d12=4.0 z=2.5293365625
- **ACCELERATION** `nuclear_gen` value=3336 d1=0.0 d12=4.0 z=2.5293365625
- **CHANGE_POINT** `biomass_gen` value=1878 d1=-47.0 d12=-78.0 z=-0.3086648008474576
- **PERSISTENT_DOWN** `ccgt_gen` value=3243 d1=-259.0 d12=-448.0 z=-1.2764773444625408
- **PERSISTENT_DOWN** `thermal_base` value=6579 d1=-259.0 d12=-444.0 z=-1.2664002290468364
- **REVERSAL** `wind_gen` value=1.447e+04 d1=-36.0 d12=352.0 z=-0.6212405592105263

## Nearest historical live analogues

- `2026-09-18T00:55:05.130155Z` distance=0.045 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:59:16.440589Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:03:26.672918Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:07:37.196261Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:11:47.784139Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
