# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T02:48:25.279780Z`  
Memory snapshots: **2032**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.755e+04 d1=0.0 d12=1716.0 z=30.473101012820514
- **ROBUST_OUTLIER** `margin` value=3.755e+04 d1=0.0 d12=1716.0 z=30.473101012820514
- **CHANGE_POINT** `thermal_base` value=8161 d1=-50.0 d12=-645.0 z=-1.6393227698675497
- **CHANGE_POINT** `ccgt_gen` value=4828 d1=-47.0 d12=-632.0 z=-1.6315117755984043
- **CHANGE_POINT** `ind_demand` value=-1.18e+04 d1=0.0 d12=26.0 z=1.4613944583333334
- **CHANGE_POINT** `interconnector_net` value=1.252e+04 d1=-4.0 d12=284.0 z=1.1895841471737825
- **PERSISTENT_DOWN** `wind_gen` value=3767 d1=-56.0 d12=-96.0 z=-2.1004779222440946
- **ACCELERATION** `wind_gen` value=3767 d1=-56.0 d12=-96.0 z=-2.1004779222440946
- **PERSISTENT_DOWN** `thermal_base` value=8161 d1=-50.0 d12=-645.0 z=-1.6393227698675497
- **PERSISTENT_DOWN** `ccgt_gen` value=4828 d1=-47.0 d12=-632.0 z=-1.6315117755984043
- **REVERSAL** `interconnector_net` value=1.252e+04 d1=-4.0 d12=284.0 z=1.1895841471737825
- **PERSISTENT_DOWN** `nuclear_gen` value=3333 d1=-3.0 d12=-13.0 z=-0.6744897499999999
- **ACCELERATION** `biomass_gen` value=3017 d1=-10.0 d12=-6.0 z=0.5691007265625

## Nearest historical live analogues

- `2026-09-21T01:53:20.720277Z` distance=0.866 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:23:21.503053Z` distance=0.869 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:28:09.159328Z` distance=0.869 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:32:22.156789Z` distance=0.869 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T01:36:33.089731Z` distance=0.869 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 7.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
