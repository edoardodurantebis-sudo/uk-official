# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T03:34:42.534683Z`  
Memory snapshots: **732**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2033 d1=1.0 d12=-2.0 z=-175.5172216111111
- **REVERSAL** `biomass_gen` value=2033 d1=1.0 d12=-2.0 z=-175.5172216111111
- **ACCELERATION** `biomass_gen` value=2033 d1=1.0 d12=-2.0 z=-175.5172216111111
- **ROBUST_OUTLIER** `biomass_gen` value=2033 d1=1.0 d12=-2.0 z=-175.5172216111111
- **ROBUST_OUTLIER** `ind_demand` value=-1.152e+04 d1=0.0 d12=11.0 z=33.31979365
- **CHANGE_POINT** `interconnector_net` value=-9823 d1=-1563.0 d12=-3354.0 z=-10.147592427130045
- **ROBUST_OUTLIER** `margin` value=3.585e+04 d1=0.0 d12=1.0 z=11.051880240963856
- **PERSISTENT_DOWN** `interconnector_net` value=-9823 d1=-1563.0 d12=-3354.0 z=-10.147592427130045
- **ACCELERATION** `interconnector_net` value=-9823 d1=-1563.0 d12=-3354.0 z=-10.147592427130045
- **ROBUST_OUTLIER** `interconnector_net` value=-9823 d1=-1563.0 d12=-3354.0 z=-10.147592427130045
- **CHANGE_POINT** `ind_generation` value=2.565e+04 d1=0.0 d12=15.0 z=0.3709693625
- **CHANGE_POINT** `nuclear_gen` value=3313 d1=2.0 d12=-2.0 z=0.2697959
- **CHANGE_POINT** `imbalance` value=6527 d1=0.0 d12=15.0 z=0.07708454285714286
- **PERSISTENT_UP** `wind_gen` value=1.349e+04 d1=148.0 d12=78.0 z=0.7455110540668348
- **ACCELERATION** `wind_gen` value=1.349e+04 d1=148.0 d12=78.0 z=0.7455110540668348

## Nearest historical live analogues

- `2026-09-17T02:22:41.615797Z` distance=0.591 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:26:53.112988Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:31:05.012181Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:35:17.375315Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T02:39:29.397540Z` distance=0.591 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 11.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
