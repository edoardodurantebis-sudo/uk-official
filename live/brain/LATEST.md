# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T07:48:44.463404Z`  
Memory snapshots: **2103**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.825e+04 d1=0.0 d12=101.0 z=21.7063065
- **ROBUST_OUTLIER** `margin` value=3.825e+04 d1=0.0 d12=101.0 z=21.7063065
- **ROBUST_OUTLIER** `ind_demand` value=-1.283e+04 d1=0.0 d12=-274.0 z=-12.64361695
- **CHANGE_POINT** `ind_generation` value=1.797e+04 d1=0.0 d12=1307.0 z=5.893354190625
- **ROBUST_OUTLIER** `ind_generation` value=1.797e+04 d1=0.0 d12=1307.0 z=5.893354190625
- **CHANGE_POINT** `imbalance` value=-3297 d1=0.0 d12=1061.0 z=1.597363026984127
- **CHANGE_POINT** `interconnector_net` value=1.068e+04 d1=-1.0 d12=2254.0 z=0.3282876045130641
- **PERSISTENT_UP** `nuclear_gen` value=3504 d1=3.0 d12=7.0 z=2.0555878095238094
- **CHANGE_POINT** `ps_gen` value=-10 d1=0.0 d12=-232.0 z=0.01143202966101695
- **REVERSAL** `thermal_base` value=1.222e+04 d1=2.0 d12=-199.0 z=0.5869543443239988
- **PERSISTENT_DOWN** `ccgt_gen` value=8717 d1=-1.0 d12=-206.0 z=0.5529430443510738
- **REVERSAL** `interconnector_net` value=1.068e+04 d1=-1.0 d12=2254.0 z=0.3282876045130641
- **REVERSAL** `biomass_gen` value=3020 d1=4.0 d12=-6.0 z=0.2697959
- **ACCELERATION** `biomass_gen` value=3020 d1=4.0 d12=-6.0 z=0.2697959
- **PERSISTENT_UP** `residual_proxy` value=1.23e+04 d1=982.0 d12=982.0 z=0.18236527522639068

## Nearest historical live analogues

- `2026-09-21T06:53:56.422040Z` distance=0.345 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:49:44.005596Z` distance=0.847 → {'next30m_imbalance_delta': -491.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:20:09.477286Z` distance=0.848 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:24:24.498463Z` distance=0.848 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:28:37.700638Z` distance=0.848 → {'next30m_imbalance_delta': -491.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
