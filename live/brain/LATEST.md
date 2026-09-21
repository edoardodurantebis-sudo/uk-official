# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T08:18:08.153527Z`  
Memory snapshots: **2110**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.825e+04 d1=0.0 d12=0.0 z=20.615925836956524
- **ROBUST_OUTLIER** `margin` value=3.825e+04 d1=0.0 d12=0.0 z=20.615925836956524
- **ROBUST_OUTLIER** `ind_demand` value=-1.283e+04 d1=0.0 d12=0.0 z=-11.786422580508475
- **CHANGE_POINT** `ind_generation` value=1.797e+04 d1=0.0 d12=0.0 z=6.681815724820144
- **ROBUST_OUTLIER** `ind_generation` value=1.797e+04 d1=0.0 d12=0.0 z=6.681815724820144
- **CHANGE_POINT** `ps_gen` value=-10 d1=0.0 d12=-471.0 z=0.01143202966101695
- **REVERSAL** `wind_gen` value=4353 d1=-98.0 d12=84.0 z=1.6391231354748603
- **ACCELERATION** `wind_gen` value=4353 d1=-98.0 d12=84.0 z=1.6391231354748603
- **REVERSAL** `nuclear_gen` value=3496 d1=-3.0 d12=2.0 z=0.9093121074074074
- **ACCELERATION** `nuclear_gen` value=3496 d1=-3.0 d12=2.0 z=0.9093121074074074
- **PERSISTENT_DOWN** `residual_proxy` value=1.132e+04 d1=-982.0 d12=0.0 z=-0.6744897500000001
- **ACCELERATION** `residual_proxy` value=1.132e+04 d1=-982.0 d12=0.0 z=-0.6744897500000001
- **PERSISTENT_DOWN** `thermal_base` value=1.224e+04 d1=-12.0 d12=-68.0 z=0.5492453951122545
- **ACCELERATION** `thermal_base` value=1.224e+04 d1=-12.0 d12=-68.0 z=0.5492453951122545
- **PERSISTENT_DOWN** `ccgt_gen` value=8742 d1=-9.0 d12=-70.0 z=0.5317765535264484

## Nearest historical live analogues

- `2026-09-21T07:23:29.263598Z` distance=0.000 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 982.0}
- `2026-09-21T07:19:16.764355Z` distance=0.323 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:53:56.422040Z` distance=0.327 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.327 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.327 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
