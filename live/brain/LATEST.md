# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T08:02:12.092833Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **ROBUST_OUTLIER** `ind_demand` value=-1.265e+04 d1=0.0 d12=-243.0 z=-38.9517830625
- **ROBUST_OUTLIER** `ps_gen` value=-19 d1=0.0 d12=270.0 z=-31.411951214285715
- **ROBUST_OUTLIER** `ind_generation` value=1.396e+04 d1=0.0 d12=260.0 z=12.10944388372093
- **CHANGE_POINT** `imbalance` value=-7454 d1=0.0 d12=14.0 z=8.25073508139535
- **CHANGE_POINT** `biomass_gen` value=2477 d1=-87.0 d12=-80.0 z=-8.051721390625
- **ROBUST_OUTLIER** `imbalance` value=-7454 d1=0.0 d12=14.0 z=8.25073508139535
- **PERSISTENT_DOWN** `biomass_gen` value=2477 d1=-87.0 d12=-80.0 z=-8.051721390625
- **ACCELERATION** `biomass_gen` value=2477 d1=-87.0 d12=-80.0 z=-8.051721390625
- **ROBUST_OUTLIER** `biomass_gen` value=2477 d1=-87.0 d12=-80.0 z=-8.051721390625
- **CHANGE_POINT** `ccgt_gen` value=7389 d1=36.0 d12=-2247.0 z=-3.3715518221409577
- **CHANGE_POINT** `thermal_base` value=1.119e+04 d1=30.0 d12=-2255.0 z=-3.2398342288411457
- **CHANGE_POINT** `interconnector_net` value=4554 d1=760.0 d12=4247.0 z=2.957434438279978
- **ROBUST_OUTLIER** `residual_proxy` value=1.22e+04 d1=0.0 d12=-1169.0 z=-3.9096876787790698
- **REVERSAL** `ccgt_gen` value=7389 d1=36.0 d12=-2247.0 z=-3.3715518221409577

## Nearest historical live analogues

- `2026-09-23T05:21:50.517884Z` distance=0.289 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:26:03.675558Z` distance=0.289 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:30:15.575715Z` distance=0.289 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T06:50:14.011711Z` distance=0.290 → {'next30m_imbalance_delta': 443.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T06:54:26.763021Z` distance=0.290 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
