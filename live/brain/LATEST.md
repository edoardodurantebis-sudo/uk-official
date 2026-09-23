# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T08:15:30.534513Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **PERSISTENT_DOWN** `ps_gen` value=-100 d1=0.0 d12=-78.0 z=-41.14387475
- **ACCELERATION** `ps_gen` value=-100 d1=0.0 d12=-78.0 z=-41.14387475
- **ROBUST_OUTLIER** `ps_gen` value=-100 d1=0.0 d12=-78.0 z=-41.14387475
- **CHANGE_POINT** `ind_demand` value=-1.265e+04 d1=0.0 d12=0.0 z=-38.9517830625
- **ROBUST_OUTLIER** `ind_demand` value=-1.265e+04 d1=0.0 d12=0.0 z=-38.9517830625
- **CHANGE_POINT** `biomass_gen` value=2375 d1=0.0 d12=-189.0 z=-8.977363573943661
- **ROBUST_OUTLIER** `ind_generation` value=1.396e+04 d1=0.0 d12=0.0 z=10.940933734210526
- **CHANGE_POINT** `imbalance` value=-7454 d1=0.0 d12=0.0 z=7.4477868184210525
- **PERSISTENT_DOWN** `biomass_gen` value=2375 d1=0.0 d12=-189.0 z=-8.977363573943661
- **ROBUST_OUTLIER** `biomass_gen` value=2375 d1=0.0 d12=-189.0 z=-8.977363573943661
- **ROBUST_OUTLIER** `imbalance` value=-7454 d1=0.0 d12=0.0 z=7.4477868184210525
- **CHANGE_POINT** `ccgt_gen` value=6366 d1=0.0 d12=-2827.0 z=-4.650386351392251
- **CHANGE_POINT** `thermal_base` value=1.018e+04 d1=0.0 d12=-2826.0 z=-4.491470159963986
- **CHANGE_POINT** `interconnector_net` value=6711 d1=0.0 d12=6412.0 z=3.746839967715681
- **PERSISTENT_DOWN** `ccgt_gen` value=6366 d1=0.0 d12=-2827.0 z=-4.650386351392251

## Nearest historical live analogues

- `2026-09-23T05:21:50.517884Z` distance=0.289 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:26:03.675558Z` distance=0.289 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:30:15.575715Z` distance=0.289 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T07:19:46.888406Z` distance=0.290 → {'next30m_imbalance_delta': 14.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:50:14.011711Z` distance=0.290 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
