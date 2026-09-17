# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T13:07:43.772955Z`  
Memory snapshots: **868**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.848e+04 d1=0.0 d12=-27.0 z=27.41519796354167
- **ROBUST_OUTLIER** `ind_generation` value=2.848e+04 d1=0.0 d12=-27.0 z=27.41519796354167
- **ROBUST_OUTLIER** `wind_forecast` value=1.898e+04 d1=0.0 d12=-47.0 z=-18.21122325
- **CHANGE_POINT** `wind_gen` value=1.352e+04 d1=-354.0 d12=-742.0 z=-3.0631999374201793
- **CHANGE_POINT** `biomass_gen` value=1904 d1=1.0 d12=-108.0 z=-2.686125846491228
- **ROBUST_OUTLIER** `imbalance` value=1.194e+04 d1=0.0 d12=-27.0 z=4.6214664457335335
- **ROBUST_OUTLIER** `demand_forecast` value=1.604e+04 d1=0.0 d12=0.0 z=-4.089440593835617
- **ROBUST_OUTLIER** `residual_proxy` value=-2942 d1=0.0 d12=47.0 z=-3.6916438992957747
- **PERSISTENT_DOWN** `wind_gen` value=1.352e+04 d1=-354.0 d12=-742.0 z=-3.0631999374201793
- **ROBUST_OUTLIER** `wind_gen` value=1.352e+04 d1=-354.0 d12=-742.0 z=-3.0631999374201793
- **REVERSAL** `biomass_gen` value=1904 d1=1.0 d12=-108.0 z=-2.686125846491228
- **CHANGE_POINT** `ps_gen` value=-688 d1=0.0 d12=264.0 z=0.6796189496197718
- **CHANGE_POINT** `thermal_base` value=5212 d1=-19.0 d12=92.0 z=0.07842904069767442
- **CHANGE_POINT** `ccgt_gen` value=1905 d1=-19.0 d12=96.0 z=0.0565214874301676
- **ACCELERATION** `nuclear_gen` value=3307 d1=0.0 d12=-4.0 z=-1.1241495833333335

## Nearest historical live analogues

- `2026-09-17T11:51:58.101795Z` distance=0.177 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T11:56:11.138716Z` distance=0.177 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T12:00:23.510142Z` distance=0.177 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T12:04:34.286599Z` distance=0.177 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T12:08:43.971933Z` distance=0.177 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 47.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
