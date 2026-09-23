# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T03:15:41.518000Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-11 d1=1.0 d12=-155.0 z=-106.5693805
- **REVERSAL** `ps_gen` value=-11 d1=1.0 d12=-155.0 z=-106.5693805
- **ROBUST_OUTLIER** `ps_gen` value=-11 d1=1.0 d12=-155.0 z=-106.5693805
- **CHANGE_POINT** `margin` value=3.868e+04 d1=0.0 d12=20.0 z=98.003360675
- **ROBUST_OUTLIER** `margin` value=3.868e+04 d1=0.0 d12=20.0 z=98.003360675
- **ROBUST_OUTLIER** `ind_demand` value=-1.242e+04 d1=0.0 d12=1.0 z=5.26102005
- **CHANGE_POINT** `interconnector_net` value=-2244 d1=23.0 d12=-2805.0 z=-2.6221275786994838
- **REVERSAL** `biomass_gen` value=2881 d1=-1.0 d12=16.0 z=-3.2600337916666664
- **ROBUST_OUTLIER** `biomass_gen` value=2881 d1=-1.0 d12=16.0 z=-3.2600337916666664
- **REVERSAL** `interconnector_net` value=-2244 d1=23.0 d12=-2805.0 z=-2.6221275786994838
- **PERSISTENT_DOWN** `nuclear_gen` value=3718 d1=-6.0 d12=-11.0 z=-2.5293365625
- **PERSISTENT_UP** `wind_gen` value=5840 d1=109.0 d12=498.0 z=1.5709340709542547
- **PERSISTENT_UP** `thermal_base` value=1.31e+04 d1=40.0 d12=195.0 z=-0.8623308002973241
- **ACCELERATION** `thermal_base` value=1.31e+04 d1=40.0 d12=195.0 z=-0.8623308002973241
- **PERSISTENT_UP** `ccgt_gen` value=9377 d1=46.0 d12=206.0 z=-0.8545355477755308

## Nearest historical live analogues

- `2026-09-23T02:21:01.680995Z` distance=0.019 → {'next30m_imbalance_delta': 3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T08:51:52.795165Z` distance=0.668 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T08:56:04.489976Z` distance=0.668 → {'next30m_imbalance_delta': 2450.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1386.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T09:00:17.050310Z` distance=0.668 → {'next30m_imbalance_delta': 2450.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1386.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T09:04:32.088798Z` distance=0.668 → {'next30m_imbalance_delta': 2450.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 1386.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
