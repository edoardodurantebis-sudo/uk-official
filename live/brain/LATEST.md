# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T12:50:55.777126Z`  
Memory snapshots: **864**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.848e+04 d1=0.0 d12=-24.0 z=27.45735357291667
- **ROBUST_OUTLIER** `ind_generation` value=2.848e+04 d1=0.0 d12=-24.0 z=27.45735357291667
- **ROBUST_OUTLIER** `wind_forecast` value=1.898e+04 d1=0.0 d12=-47.0 z=-18.21122325
- **CHANGE_POINT** `imbalance` value=1.194e+04 d1=0.0 d12=-24.0 z=4.709118170912547
- **ROBUST_OUTLIER** `imbalance` value=1.194e+04 d1=0.0 d12=-24.0 z=4.709118170912547
- **ROBUST_OUTLIER** `demand_forecast` value=1.604e+04 d1=0.0 d12=0.0 z=-4.089440593835617
- **CHANGE_POINT** `biomass_gen` value=1934 d1=-38.0 d12=-83.0 z=-1.8711651129032258
- **CHANGE_POINT** `wind_gen` value=1.425e+04 d1=116.0 d12=-658.0 z=-1.8158676794380588
- **ROBUST_OUTLIER** `residual_proxy` value=-2942 d1=0.0 d12=47.0 z=-3.6916438992957747
- **PERSISTENT_DOWN** `nuclear_gen` value=3300 d1=-4.0 d12=-13.0 z=-2.6979589999999996
- **CHANGE_POINT** `margin` value=3.645e+04 d1=0.0 d12=-270.0 z=0.67448975
- **CHANGE_POINT** `ps_gen` value=-928 d1=-55.0 d12=11.0 z=-0.5890662460422164
- **CHANGE_POINT** `ccgt_gen` value=1917 d1=24.0 d12=100.0 z=0.09887807853403141
- **CHANGE_POINT** `thermal_base` value=5217 d1=20.0 d12=87.0 z=0.0556280206185567
- **PERSISTENT_DOWN** `biomass_gen` value=1934 d1=-38.0 d12=-83.0 z=-1.8711651129032258

## Nearest historical live analogues

- `2026-09-17T11:51:58.101795Z` distance=0.169 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T11:56:11.138716Z` distance=0.169 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -270.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T10:57:20.878127Z` distance=0.224 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:01:31.274983Z` distance=0.224 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:05:43.396655Z` distance=0.224 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
