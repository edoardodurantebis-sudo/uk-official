# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T13:16:11.774914Z`  
Memory snapshots: **870**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **ROBUST_OUTLIER** `ind_generation` value=2.848e+04 d1=0.0 d12=-3.0 z=26.563995305555554
- **ROBUST_OUTLIER** `wind_forecast` value=1.898e+04 d1=0.0 d12=-47.0 z=-18.21122325
- **ROBUST_OUTLIER** `imbalance` value=1.194e+04 d1=0.0 d12=-3.0 z=4.526597633064516
- **CHANGE_POINT** `biomass_gen` value=1927 d1=22.0 d12=-84.0 z=-2.1680027678571427
- **ROBUST_OUTLIER** `demand_forecast` value=1.604e+04 d1=0.0 d12=0.0 z=-4.089440593835617
- **ROBUST_OUTLIER** `residual_proxy` value=-2942 d1=0.0 d12=47.0 z=-3.6916438992957747
- **REVERSAL** `wind_gen` value=1.349e+04 d1=36.0 d12=-656.0 z=-3.116607810344828
- **ROBUST_OUTLIER** `wind_gen` value=1.349e+04 d1=36.0 d12=-656.0 z=-3.116607810344828
- **CHANGE_POINT** `ps_gen` value=-685 d1=1.0 d12=268.0 z=0.6950065484790875
- **CHANGE_POINT** `thermal_base` value=5262 d1=20.0 d12=146.0 z=0.4817783928571429
- **CHANGE_POINT** `ccgt_gen` value=1953 d1=17.0 d12=145.0 z=0.42060877668539326
- **REVERSAL** `biomass_gen` value=1927 d1=22.0 d12=-84.0 z=-2.1680027678571427
- **PERSISTENT_UP** `ps_gen` value=-685 d1=1.0 d12=268.0 z=0.6950065484790875
- **PERSISTENT_UP** `nuclear_gen` value=3309 d1=3.0 d12=1.0 z=-0.4817783928571429
- **ACCELERATION** `nuclear_gen` value=3309 d1=3.0 d12=1.0 z=-0.4817783928571429

## Nearest historical live analogues

- `2026-09-17T12:21:21.942046Z` distance=0.033 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 47.0}
- `2026-09-17T11:51:58.101795Z` distance=0.171 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T11:56:11.138716Z` distance=0.171 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T12:00:23.510142Z` distance=0.171 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T12:04:34.286599Z` distance=0.171 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
