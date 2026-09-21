# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T07:44:30.561555Z`  
Memory snapshots: **2102**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.825e+04 d1=0.0 d12=101.0 z=17.49994315
- **ROBUST_OUTLIER** `margin` value=3.825e+04 d1=0.0 d12=101.0 z=17.49994315
- **ROBUST_OUTLIER** `ind_demand` value=-1.283e+04 d1=0.0 d12=-274.0 z=-14.33812231443299
- **CHANGE_POINT** `ind_generation` value=1.797e+04 d1=0.0 d12=1307.0 z=5.781635379969418
- **ROBUST_OUTLIER** `ind_generation` value=1.797e+04 d1=0.0 d12=1307.0 z=5.781635379969418
- **CHANGE_POINT** `imbalance` value=-3297 d1=0.0 d12=1061.0 z=1.827290821964018
- **PERSISTENT_UP** `nuclear_gen` value=3501 d1=5.0 d12=11.0 z=2.91208273015873
- **ACCELERATION** `nuclear_gen` value=3501 d1=5.0 d12=11.0 z=2.91208273015873
- **CHANGE_POINT** `interconnector_net` value=1.069e+04 d1=16.0 d12=2230.0 z=0.32857889786223277
- **CHANGE_POINT** `ps_gen` value=-10 d1=-30.0 d12=-237.0 z=0.01143202966101695
- **REVERSAL** `wind_gen` value=4280 d1=-16.0 d12=283.0 z=1.3640518966480446
- **PERSISTENT_DOWN** `thermal_base` value=1.222e+04 d1=-8.0 d12=-193.0 z=0.5966788250999429
- **PERSISTENT_DOWN** `ccgt_gen` value=8718 d1=-13.0 d12=-204.0 z=0.5855938658986175
- **PERSISTENT_UP** `interconnector_net` value=1.069e+04 d1=16.0 d12=2230.0 z=0.32857889786223277
- **PERSISTENT_DOWN** `biomass_gen` value=3016 d1=0.0 d12=-8.0 z=-0.2697959

## Nearest historical live analogues

- `2026-09-21T06:49:44.005596Z` distance=0.845 → {'next30m_imbalance_delta': -491.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:20:09.477286Z` distance=0.846 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:24:24.498463Z` distance=0.846 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:28:37.700638Z` distance=0.846 → {'next30m_imbalance_delta': -491.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:32:53.849371Z` distance=0.846 → {'next30m_imbalance_delta': -491.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
