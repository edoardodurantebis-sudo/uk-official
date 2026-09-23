# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T06:33:22.680489Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2562 d1=-2.0 d12=2.0 z=-6.947244424999999
- **CHANGE_POINT** `nuclear_gen` value=3808 d1=4.0 d12=3.0 z=6.32334140625
- **REVERSAL** `biomass_gen` value=2562 d1=-2.0 d12=2.0 z=-6.947244424999999
- **ACCELERATION** `biomass_gen` value=2562 d1=-2.0 d12=2.0 z=-6.947244424999999
- **ROBUST_OUTLIER** `biomass_gen` value=2562 d1=-2.0 d12=2.0 z=-6.947244424999999
- **PERSISTENT_UP** `nuclear_gen` value=3808 d1=4.0 d12=3.0 z=6.32334140625
- **ACCELERATION** `nuclear_gen` value=3808 d1=4.0 d12=3.0 z=6.32334140625
- **ROBUST_OUTLIER** `nuclear_gen` value=3808 d1=4.0 d12=3.0 z=6.32334140625
- **CHANGE_POINT** `ind_demand` value=-1.241e+04 d1=0.0 d12=9.0 z=1.8548468125
- **CHANGE_POINT** `margin` value=3.887e+04 d1=0.0 d12=287.0 z=1.8492260645833334
- **ROBUST_OUTLIER** `imbalance` value=-7911 d1=0.0 d12=26.0 z=3.6422446500000003
- **ROBUST_OUTLIER** `ind_generation` value=1.326e+04 d1=0.0 d12=24.0 z=3.552312683333333
- **CHANGE_POINT** `ps_gen` value=148 d1=4.0 d12=151.0 z=0.8993196666666666
- **REVERSAL** `wind_gen` value=9120 d1=-40.0 d12=822.0 z=1.523198673020046
- **REVERSAL** `thermal_base` value=1.367e+04 d1=-5.0 d12=295.0 z=1.080525868159204

## Nearest historical live analogues

- `2026-09-23T05:34:27.904868Z` distance=0.149 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T05:38:40.844898Z` distance=0.149 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T05:21:50.517884Z` distance=0.151 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:26:03.675558Z` distance=0.151 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}
- `2026-09-23T05:30:15.575715Z` distance=0.151 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4.0, 'next30m_residual_proxy_delta': 172.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
