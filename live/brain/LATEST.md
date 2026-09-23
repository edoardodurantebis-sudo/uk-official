# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T07:49:28.631681Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **ROBUST_OUTLIER** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **ROBUST_OUTLIER** `ps_gen` value=-18 d1=0.0 d12=-270.0 z=-36.4224465
- **CHANGE_POINT** `ind_generation` value=1.396e+04 d1=0.0 d12=260.0 z=12.10944388372093
- **ROBUST_OUTLIER** `ind_generation` value=1.396e+04 d1=0.0 d12=260.0 z=12.10944388372093
- **CHANGE_POINT** `imbalance` value=-7454 d1=0.0 d12=14.0 z=8.25073508139535
- **ROBUST_OUTLIER** `imbalance` value=-7454 d1=0.0 d12=14.0 z=8.25073508139535
- **REVERSAL** `biomass_gen` value=2555 d1=1.0 d12=-6.0 z=-6.43926933203125
- **ROBUST_OUTLIER** `biomass_gen` value=2555 d1=1.0 d12=-6.0 z=-6.43926933203125
- **CHANGE_POINT** `ccgt_gen` value=7690 d1=-377.0 d12=-2537.0 z=-3.8834955912969287
- **CHANGE_POINT** `thermal_base` value=1.15e+04 d1=-376.0 d12=-2536.0 z=-3.1182931920289856
- **CHANGE_POINT** `interconnector_net` value=3799 d1=1.0 d12=7377.0 z=2.681124204286489
- **PERSISTENT_DOWN** `residual_proxy` value=1.22e+04 d1=-1169.0 d12=-1169.0 z=-3.9096876787790698
- **ACCELERATION** `residual_proxy` value=1.22e+04 d1=-1169.0 d12=-1169.0 z=-3.9096876787790698
- **ROBUST_OUTLIER** `residual_proxy` value=1.22e+04 d1=-1169.0 d12=-1169.0 z=-3.9096876787790698

## Nearest historical live analogues

- `2026-09-23T05:21:50.517884Z` distance=0.290 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:26:03.675558Z` distance=0.290 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:30:15.575715Z` distance=0.290 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T06:50:14.011711Z` distance=0.290 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:54:26.763021Z` distance=0.290 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
