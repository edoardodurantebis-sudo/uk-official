# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T04:08:00.116133Z`  
Memory snapshots: **2390**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.78e+04 d1=0.0 d12=-38.0 z=23.24057073369565
- **ROBUST_OUTLIER** `margin` value=3.78e+04 d1=0.0 d12=-38.0 z=23.24057073369565
- **CHANGE_POINT** `interconnector_net` value=-2793 d1=-785.0 d12=-3201.0 z=-5.590540442258477
- **CHANGE_POINT** `imbalance` value=-3236 d1=0.0 d12=-577.0 z=-4.4052611796875
- **CHANGE_POINT** `ind_generation` value=1.822e+04 d1=0.0 d12=-577.0 z=-4.4052611796875
- **PERSISTENT_DOWN** `interconnector_net` value=-2793 d1=-785.0 d12=-3201.0 z=-5.590540442258477
- **ROBUST_OUTLIER** `interconnector_net` value=-2793 d1=-785.0 d12=-3201.0 z=-5.590540442258477
- **ROBUST_OUTLIER** `imbalance` value=-3236 d1=0.0 d12=-577.0 z=-4.4052611796875
- **ROBUST_OUTLIER** `ind_generation` value=1.822e+04 d1=0.0 d12=-577.0 z=-4.4052611796875
- **CHANGE_POINT** `ind_demand` value=-1.25e+04 d1=0.0 d12=-5.0 z=-2.370349692857143
- **CHANGE_POINT** `ps_gen` value=-449 d1=230.0 d12=-278.0 z=-1.6771096486486485
- **CHANGE_POINT** `wind_gen` value=3604 d1=-64.0 d12=-338.0 z=-0.7920613577981651
- **REVERSAL** `ps_gen` value=-449 d1=230.0 d12=-278.0 z=-1.6771096486486485
- **ACCELERATION** `ps_gen` value=-449 d1=230.0 d12=-278.0 z=-1.6771096486486485
- **PERSISTENT_UP** `ccgt_gen` value=1.166e+04 d1=360.0 d12=413.0 z=1.1810288650398406

## Nearest historical live analogues

- `2026-09-22T02:20:47.392507Z` distance=0.196 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:24:59.358718Z` distance=0.196 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:29:12.426907Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:33:26.071895Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:37:48.213453Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
