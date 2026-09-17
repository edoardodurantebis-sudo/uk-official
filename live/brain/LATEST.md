# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T12:46:31.728426Z`  
Memory snapshots: **863**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.848e+04 d1=0.0 d12=-24.0 z=27.45735357291667
- **ROBUST_OUTLIER** `ind_generation` value=2.848e+04 d1=0.0 d12=-24.0 z=27.45735357291667
- **ROBUST_OUTLIER** `wind_forecast` value=1.898e+04 d1=0.0 d12=-47.0 z=-18.21122325
- **CHANGE_POINT** `imbalance` value=1.194e+04 d1=0.0 d12=-24.0 z=4.79648738755796
- **ROBUST_OUTLIER** `imbalance` value=1.194e+04 d1=0.0 d12=-24.0 z=4.79648738755796
- **ROBUST_OUTLIER** `demand_forecast` value=1.604e+04 d1=0.0 d12=0.0 z=-4.089440593835617
- **CHANGE_POINT** `wind_gen` value=1.413e+04 d1=-6.0 d12=-774.0 z=-2.0157164942528736
- **ROBUST_OUTLIER** `residual_proxy` value=-2942 d1=0.0 d12=47.0 z=-3.6916438992957747
- **CHANGE_POINT** `ps_gen` value=-873 d1=-223.0 d12=66.0 z=-0.4276485128205128
- **CHANGE_POINT** `thermal_base` value=5197 d1=-18.0 d12=67.0 z=-0.2771875684931507
- **CHANGE_POINT** `ccgt_gen` value=1893 d1=-14.0 d12=76.0 z=-0.2616348140569395
- **PERSISTENT_DOWN** `wind_gen` value=1.413e+04 d1=-6.0 d12=-774.0 z=-2.0157164942528736
- **PERSISTENT_DOWN** `nuclear_gen` value=3304 d1=-4.0 d12=-9.0 z=-1.7986393333333333
- **ACCELERATION** `nuclear_gen` value=3304 d1=-4.0 d12=-9.0 z=-1.7986393333333333
- **PERSISTENT_DOWN** `biomass_gen` value=1972 d1=0.0 d12=-45.0 z=-1.027299773076923

## Nearest historical live analogues

- `2026-09-17T11:51:58.101795Z` distance=0.169 → {'next30m_imbalance_delta': -14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T10:57:20.878127Z` distance=0.223 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:01:31.274983Z` distance=0.223 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:05:43.396655Z` distance=0.223 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}
- `2026-09-17T11:09:56.284661Z` distance=0.223 → {'next30m_imbalance_delta': 35.0, 'next30m_margin_delta': 276.0, 'next30m_residual_proxy_delta': -54.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
