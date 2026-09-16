# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T01:39:11.726100Z`  
Memory snapshots: **400**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.216e+04 d1=0.0 d12=-64.0 z=-55.08332958333333
- **ROBUST_OUTLIER** `ind_demand` value=-1.216e+04 d1=0.0 d12=-64.0 z=-55.08332958333333
- **ROBUST_OUTLIER** `margin` value=3.604e+04 d1=0.0 d12=373.0 z=6.017158559210526
- **ROBUST_OUTLIER** `imbalance` value=5960 d1=0.0 d12=-75.0 z=3.135465864864865
- **ROBUST_OUTLIER** `ind_generation` value=2.508e+04 d1=0.0 d12=-75.0 z=3.135465864864865
- **CHANGE_POINT** `interconnector_net` value=4596 d1=-2.0 d12=445.0 z=0.842478485138367
- **CHANGE_POINT** `ccgt_gen` value=3245 d1=-2.0 d12=1.0 z=-0.43296587544910176
- **PERSISTENT_UP** `nuclear_gen` value=3332 d1=2.0 d12=5.0 z=1.5738094166666665
- **ACCELERATION** `nuclear_gen` value=3332 d1=2.0 d12=5.0 z=1.5738094166666665
- **REVERSAL** `biomass_gen` value=3228 d1=-3.0 d12=29.0 z=-1.3008016607142856
- **REVERSAL** `interconnector_net` value=4596 d1=-2.0 d12=445.0 z=0.842478485138367
- **REVERSAL** `wind_gen` value=1.03e+04 d1=43.0 d12=-669.0 z=-0.7153679166666667
- **REVERSAL** `ccgt_gen` value=3245 d1=-2.0 d12=1.0 z=-0.43296587544910176
- **ACCELERATION** `ccgt_gen` value=3245 d1=-2.0 d12=1.0 z=-0.43296587544910176
- **PERSISTENT_UP** `thermal_base` value=6577 d1=0.0 d12=6.0 z=-0.4234791587635054

## Nearest historical live analogues

- `2026-09-15T23:32:16.606471Z` distance=0.278 → {'next30m_imbalance_delta': 39.0, 'next30m_margin_delta': -78.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T23:36:27.405223Z` distance=0.278 → {'next30m_imbalance_delta': 39.0, 'next30m_margin_delta': -78.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T23:41:14.503194Z` distance=0.278 → {'next30m_imbalance_delta': 39.0, 'next30m_margin_delta': -78.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T23:45:24.499489Z` distance=0.278 → {'next30m_imbalance_delta': 39.0, 'next30m_margin_delta': -78.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T00:23:43.289309Z` distance=0.315 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
