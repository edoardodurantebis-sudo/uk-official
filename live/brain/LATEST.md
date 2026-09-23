# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T08:11:16.452193Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **REVERSAL** `ps_gen` value=-100 d1=-82.0 d12=172.0 z=-41.14387475
- **ACCELERATION** `ps_gen` value=-100 d1=-82.0 d12=172.0 z=-41.14387475
- **ROBUST_OUTLIER** `ps_gen` value=-100 d1=-82.0 d12=172.0 z=-41.14387475
- **CHANGE_POINT** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **ROBUST_OUTLIER** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **ROBUST_OUTLIER** `ind_generation` value=1.396e+04 d1=0.0 d12=260.0 z=12.10944388372093
- **CHANGE_POINT** `biomass_gen` value=2375 d1=-31.0 d12=-192.0 z=-10.08572954296875
- **CHANGE_POINT** `imbalance` value=-7454 d1=0.0 d12=14.0 z=8.25073508139535
- **PERSISTENT_DOWN** `biomass_gen` value=2375 d1=-31.0 d12=-192.0 z=-10.08572954296875
- **ROBUST_OUTLIER** `biomass_gen` value=2375 d1=-31.0 d12=-192.0 z=-10.08572954296875
- **ROBUST_OUTLIER** `imbalance` value=-7454 d1=0.0 d12=14.0 z=8.25073508139535
- **CHANGE_POINT** `ccgt_gen` value=6366 d1=-460.0 d12=-3039.0 z=-4.642602339457831
- **CHANGE_POINT** `thermal_base` value=1.018e+04 d1=-455.0 d12=-3040.0 z=-4.496865669738407
- **CHANGE_POINT** `interconnector_net` value=6711 d1=983.0 d12=6398.0 z=3.746839967715681
- **PERSISTENT_DOWN** `ccgt_gen` value=6366 d1=-460.0 d12=-3039.0 z=-4.642602339457831

## Nearest historical live analogues

- `2026-09-23T05:21:50.517884Z` distance=0.289 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:26:03.675558Z` distance=0.289 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:30:15.575715Z` distance=0.289 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T06:50:14.011711Z` distance=0.290 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:54:26.763021Z` distance=0.290 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
