# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T07:53:44.344645Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **ROBUST_OUTLIER** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **PERSISTENT_DOWN** `ps_gen` value=-20 d1=-2.0 d12=-273.0 z=-36.872106333333335
- **ROBUST_OUTLIER** `ps_gen` value=-20 d1=-2.0 d12=-273.0 z=-36.872106333333335
- **CHANGE_POINT** `ind_generation` value=1.396e+04 d1=0.0 d12=260.0 z=12.10944388372093
- **ROBUST_OUTLIER** `ind_generation` value=1.396e+04 d1=0.0 d12=260.0 z=12.10944388372093
- **CHANGE_POINT** `imbalance` value=-7454 d1=0.0 d12=14.0 z=8.25073508139535
- **ROBUST_OUTLIER** `imbalance` value=-7454 d1=0.0 d12=14.0 z=8.25073508139535
- **PERSISTENT_UP** `biomass_gen` value=2569 d1=14.0 d12=17.0 z=-6.1336411640625
- **ACCELERATION** `biomass_gen` value=2569 d1=14.0 d12=17.0 z=-6.1336411640625
- **ROBUST_OUTLIER** `biomass_gen` value=2569 d1=14.0 d12=17.0 z=-6.1336411640625
- **CHANGE_POINT** `ccgt_gen` value=7445 d1=-245.0 d12=-2693.0 z=-4.12692606650641
- **CHANGE_POINT** `thermal_base` value=1.125e+04 d1=-250.0 d12=-2692.0 z=-3.3358910399728994
- **CHANGE_POINT** `interconnector_net` value=3799 d1=0.0 d12=6425.0 z=2.681124204286489
- **PERSISTENT_DOWN** `ccgt_gen` value=7445 d1=-245.0 d12=-2693.0 z=-4.12692606650641

## Nearest historical live analogues

- `2026-09-23T05:21:50.517884Z` distance=0.290 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:26:03.675558Z` distance=0.290 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:30:15.575715Z` distance=0.290 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T06:50:14.011711Z` distance=0.290 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:54:26.763021Z` distance=0.290 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
