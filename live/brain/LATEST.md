# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T16:38:28.589008Z`  
Memory snapshots: **918**  
Current physical regime: **TIGHT**

Regime read: residual high, wind falling.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=4819 d1=79.0 d12=1554.0 z=14.10051481
- **CHANGE_POINT** `thermal_base` value=8133 d1=81.0 d12=1559.0 z=13.781595530141843
- **PERSISTENT_UP** `ccgt_gen` value=4819 d1=79.0 d12=1554.0 z=14.10051481
- **ROBUST_OUTLIER** `ccgt_gen` value=4819 d1=79.0 d12=1554.0 z=14.10051481
- **PERSISTENT_UP** `thermal_base` value=8133 d1=81.0 d12=1559.0 z=13.781595530141843
- **ROBUST_OUTLIER** `thermal_base` value=8133 d1=81.0 d12=1559.0 z=13.781595530141843
- **CHANGE_POINT** `biomass_gen` value=3050 d1=-19.0 d12=214.0 z=10.4699204375
- **PERSISTENT_UP** `ps_gen` value=-30 d1=224.0 d12=229.0 z=11.362558096153846
- **ACCELERATION** `ps_gen` value=-30 d1=224.0 d12=229.0 z=11.362558096153846
- **ROBUST_OUTLIER** `ps_gen` value=-30 d1=224.0 d12=229.0 z=11.362558096153846
- **REVERSAL** `biomass_gen` value=3050 d1=-19.0 d12=214.0 z=10.4699204375
- **ROBUST_OUTLIER** `biomass_gen` value=3050 d1=-19.0 d12=214.0 z=10.4699204375
- **CHANGE_POINT** `imbalance` value=1.162e+04 d1=0.0 d12=-34.0 z=-8.171702740384616
- **ROBUST_OUTLIER** `imbalance` value=1.162e+04 d1=0.0 d12=-34.0 z=-8.171702740384616
- **PERSISTENT_UP** `residual_proxy` value=-2590 d1=0.0 d12=81.0 z=5.0514977021276595

## Nearest historical live analogues

- `2026-09-17T10:57:20.878127Z` distance=0.177 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:01:31.274983Z` distance=0.177 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:05:43.396655Z` distance=0.177 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:09:56.284661Z` distance=0.177 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:14:08.992825Z` distance=0.177 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
