# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T07:52:57.082338Z`  
Memory snapshots: **2104**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.825e+04 d1=0.0 d12=101.0 z=21.7063065
- **ROBUST_OUTLIER** `margin` value=3.825e+04 d1=0.0 d12=101.0 z=21.7063065
- **ROBUST_OUTLIER** `ind_demand` value=-1.283e+04 d1=0.0 d12=-274.0 z=-12.64361695
- **CHANGE_POINT** `ind_generation` value=1.797e+04 d1=0.0 d12=1307.0 z=5.893354190625
- **ROBUST_OUTLIER** `ind_generation` value=1.797e+04 d1=0.0 d12=1307.0 z=5.893354190625
- **CHANGE_POINT** `imbalance` value=-3297 d1=0.0 d12=1061.0 z=1.597363026984127
- **CHANGE_POINT** `interconnector_net` value=1.068e+04 d1=-5.0 d12=2165.0 z=0.3268311377672209
- **CHANGE_POINT** `ps_gen` value=-10 d1=0.0 d12=-233.0 z=0.01143202966101695
- **REVERSAL** `nuclear_gen` value=3501 d1=-3.0 d12=5.0 z=1.8011099917582416
- **ACCELERATION** `nuclear_gen` value=3501 d1=-3.0 d12=5.0 z=1.8011099917582416
- **PERSISTENT_UP** `wind_gen` value=4359 d1=66.0 d12=194.0 z=1.6617317304469275
- **PERSISTENT_UP** `biomass_gen` value=3029 d1=9.0 d12=6.0 z=1.48387745
- **ACCELERATION** `biomass_gen` value=3029 d1=9.0 d12=6.0 z=1.48387745
- **REVERSAL** `thermal_base` value=1.224e+04 d1=23.0 d12=-182.0 z=0.5624858152803168
- **REVERSAL** `ccgt_gen` value=8743 d1=26.0 d12=-187.0 z=0.5509325828426562

## Nearest historical live analogues

- `2026-09-21T06:53:56.422040Z` distance=0.345 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.345 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:49:44.005596Z` distance=0.847 → {'next30m_imbalance_delta': -491.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:20:09.477286Z` distance=0.848 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:24:24.498463Z` distance=0.848 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
