# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T04:08:33.422343Z`  
Memory snapshots: **2051**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.755e+04 d1=0.0 d12=-9.0 z=33.53177614285714
- **ROBUST_OUTLIER** `margin` value=3.755e+04 d1=0.0 d12=-9.0 z=33.53177614285714
- **CHANGE_POINT** `imbalance` value=-4043 d1=0.0 d12=822.0 z=6.6299276562500005
- **CHANGE_POINT** `ind_generation` value=1.657e+04 d1=0.0 d12=822.0 z=6.6299276562500005
- **ROBUST_OUTLIER** `imbalance` value=-4043 d1=0.0 d12=822.0 z=6.6299276562500005
- **ROBUST_OUTLIER** `ind_generation` value=1.657e+04 d1=0.0 d12=822.0 z=6.6299276562500005
- **CHANGE_POINT** `thermal_base` value=1.002e+04 d1=201.0 d12=1240.0 z=2.772488254143646
- **CHANGE_POINT** `ccgt_gen` value=6686 d1=199.0 d12=1242.0 z=2.7348163633879783
- **CHANGE_POINT** `interconnector_net` value=7790 d1=-1530.0 d12=-3494.0 z=-2.0690257809568484
- **ROBUST_OUTLIER** `ind_demand` value=-1.176e+04 d1=0.0 d12=42.0 z=3.8221085833333333
- **PERSISTENT_UP** `thermal_base` value=1.002e+04 d1=201.0 d12=1240.0 z=2.772488254143646
- **PERSISTENT_UP** `ccgt_gen` value=6686 d1=199.0 d12=1242.0 z=2.7348163633879783
- **PERSISTENT_DOWN** `interconnector_net` value=7790 d1=-1530.0 d12=-3494.0 z=-2.0690257809568484
- **CHANGE_POINT** `nuclear_gen` value=3337 d1=2.0 d12=-2.0 z=0.0
- **PERSISTENT_UP** `wind_gen` value=3898 d1=29.0 d12=132.0 z=-0.691645871761658

## Nearest historical live analogues

- `2026-09-21T02:22:39.819793Z` distance=0.587 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:26:51.602433Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:31:01.988533Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:35:13.346437Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:40:00.109498Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
