# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T10:29:21.446166Z`  
Memory snapshots: **2480**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **PERSISTENT_DOWN** `ts_demand_forecast` value=2.095e+04 d1=0.0 d12=-120.0 z=-172.332131125
- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.095e+04 d1=0.0 d12=-120.0 z=-172.332131125
- **CHANGE_POINT** `margin` value=4.039e+04 d1=0.0 d12=52.0 z=158.934312
- **PERSISTENT_UP** `margin` value=4.039e+04 d1=0.0 d12=52.0 z=158.934312
- **ROBUST_OUTLIER** `margin` value=4.039e+04 d1=0.0 d12=52.0 z=158.934312
- **PERSISTENT_UP** `imbalance` value=5167 d1=0.0 d12=2737.0 z=28.532960333333335
- **ROBUST_OUTLIER** `imbalance` value=5167 d1=0.0 d12=2737.0 z=28.532960333333335
- **PERSISTENT_UP** `ind_generation` value=2.612e+04 d1=0.0 d12=2617.0 z=26.79223173611111
- **ROBUST_OUTLIER** `ind_generation` value=2.612e+04 d1=0.0 d12=2617.0 z=26.79223173611111
- **PERSISTENT_DOWN** `ind_demand` value=-1.386e+04 d1=0.0 d12=-1061.0 z=-12.37180514041096
- **ROBUST_OUTLIER** `ind_demand` value=-1.386e+04 d1=0.0 d12=-1061.0 z=-12.37180514041096
- **PERSISTENT_UP** `biomass_gen` value=3049 d1=3.0 d12=1.0 z=4.0469385
- **ACCELERATION** `biomass_gen` value=3049 d1=3.0 d12=1.0 z=4.0469385
- **ROBUST_OUTLIER** `biomass_gen` value=3049 d1=3.0 d12=1.0 z=4.0469385
- **REVERSAL** `thermal_base` value=1.346e+04 d1=6.0 d12=-721.0 z=-2.360888231801755

## Nearest historical live analogues

- `2026-09-22T09:21:25.127373Z` distance=1.202 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T09:25:39.976473Z` distance=1.202 → {'next30m_imbalance_delta': 1403.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T09:29:53.558775Z` distance=1.202 → {'next30m_imbalance_delta': 1403.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T09:34:06.811855Z` distance=1.202 → {'next30m_imbalance_delta': 1403.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -65.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:25:22.024007Z` distance=1.279 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 354.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
