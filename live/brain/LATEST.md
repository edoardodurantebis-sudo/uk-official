# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T03:03:00.639806Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.868e+04 d1=0.0 d12=1467.0 z=98.003360675
- **ROBUST_OUTLIER** `margin` value=3.868e+04 d1=0.0 d12=1467.0 z=98.003360675
- **CHANGE_POINT** `ind_demand` value=-1.242e+04 d1=0.0 d12=14.0 z=6.6324825416666675
- **PERSISTENT_UP** `ind_demand` value=-1.242e+04 d1=0.0 d12=14.0 z=6.6324825416666675
- **ROBUST_OUTLIER** `ind_demand` value=-1.242e+04 d1=0.0 d12=14.0 z=6.6324825416666675
- **CHANGE_POINT** `interconnector_net` value=-836 d1=-388.0 d12=-1397.0 z=-2.128455596930786
- **PERSISTENT_UP** `biomass_gen` value=2874 d1=6.0 d12=27.0 z=-4.0469385
- **ACCELERATION** `biomass_gen` value=2874 d1=6.0 d12=27.0 z=-4.0469385
- **ROBUST_OUTLIER** `biomass_gen` value=2874 d1=6.0 d12=27.0 z=-4.0469385
- **REVERSAL** `ps_gen` value=141 d1=1.0 d12=-3.0 z=-4.0469384999999996
- **ROBUST_OUTLIER** `ps_gen` value=141 d1=1.0 d12=-3.0 z=-4.0469384999999996
- **PERSISTENT_DOWN** `interconnector_net` value=-836 d1=-388.0 d12=-1397.0 z=-2.128455596930786
- **PERSISTENT_UP** `wind_gen` value=5528 d1=82.0 d12=245.0 z=1.8068476132344553
- **REVERSAL** `nuclear_gen` value=3726 d1=1.0 d12=-7.0 z=-1.1803570625
- **ACCELERATION** `nuclear_gen` value=3726 d1=1.0 d12=-7.0 z=-1.1803570625

## Nearest historical live analogues

- `2026-09-22T08:51:52.795165Z` distance=0.668 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T08:56:04.489976Z` distance=0.668 → {'next30m_imbalance_delta': 2450.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1386.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T09:00:17.050310Z` distance=0.668 → {'next30m_imbalance_delta': 2450.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1386.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T09:04:32.088798Z` distance=0.668 → {'next30m_imbalance_delta': 2450.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1386.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T09:08:44.091938Z` distance=0.668 → {'next30m_imbalance_delta': 2450.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1386.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
