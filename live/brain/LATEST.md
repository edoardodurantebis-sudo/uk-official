# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T07:57:08.303844Z`  
Memory snapshots: **2105**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.825e+04 d1=0.0 d12=101.0 z=21.7063065
- **ROBUST_OUTLIER** `margin` value=3.825e+04 d1=0.0 d12=101.0 z=21.7063065
- **ROBUST_OUTLIER** `ind_demand` value=-1.283e+04 d1=0.0 d12=-274.0 z=-12.64361695
- **CHANGE_POINT** `ind_generation` value=1.797e+04 d1=0.0 d12=1307.0 z=5.893354190625
- **ROBUST_OUTLIER** `ind_generation` value=1.797e+04 d1=0.0 d12=1307.0 z=5.893354190625
- **CHANGE_POINT** `imbalance` value=-3297 d1=0.0 d12=1061.0 z=1.597363026984127
- **CHANGE_POINT** `ps_gen` value=-10 d1=0.0 d12=-234.0 z=0.01143202966101695
- **PERSISTENT_UP** `wind_gen` value=4364 d1=5.0 d12=158.0 z=1.6805722262569833
- **ACCELERATION** `wind_gen` value=4364 d1=5.0 d12=158.0 z=1.6805722262569833
- **ACCELERATION** `nuclear_gen` value=3501 d1=0.0 d12=2.0 z=1.6242814387755102
- **REVERSAL** `interconnector_net` value=1.066e+04 d1=-20.0 d12=1380.0 z=0.321005270783848
- **ACCELERATION** `biomass_gen` value=3021 d1=-8.0 d12=-5.0 z=0.30658625
- **PERSISTENT_UP** `residual_proxy` value=1.23e+04 d1=0.0 d12=982.0 z=0.18236527522639068
- **PERSISTENT_UP** `demand_forecast` value=2.109e+04 d1=0.0 d12=982.0 z=None
- **PERSISTENT_UP** `ts_demand_forecast` value=2.159e+04 d1=0.0 d12=569.0 z=None

## Nearest historical live analogues

- `2026-09-21T06:53:56.422040Z` distance=0.338 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.338 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.338 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:49:44.005596Z` distance=0.830 → {'next30m_imbalance_delta': -491.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:20:09.477286Z` distance=0.831 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
