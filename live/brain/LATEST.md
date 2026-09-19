# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T18:21:25.144867Z`  
Memory snapshots: **1571**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.62e+04 d1=-100.0 d12=-50.0 z=-2.712010869791667
- **CHANGE_POINT** `ind_generation` value=1.681e+04 d1=0.0 d12=-3.0 z=2.4139633157894735
- **ACCELERATION** `ccgt_gen` value=6753 d1=15.0 d12=57.0 z=4.171650544772508
- **ROBUST_OUTLIER** `ccgt_gen` value=6753 d1=15.0 d12=57.0 z=4.171650544772508
- **ACCELERATION** `thermal_base` value=1.008e+04 d1=14.0 d12=58.0 z=4.143015961982676
- **ROBUST_OUTLIER** `thermal_base` value=1.008e+04 d1=14.0 d12=58.0 z=4.143015961982676
- **CHANGE_POINT** `biomass_gen` value=835 d1=54.0 d12=227.0 z=1.534618880733945
- **PERSISTENT_DOWN** `margin` value=3.62e+04 d1=-100.0 d12=-50.0 z=-2.712010869791667
- **ACCELERATION** `margin` value=3.62e+04 d1=-100.0 d12=-50.0 z=-2.712010869791667
- **CHANGE_POINT** `imbalance` value=-3139 d1=0.0 d12=-3.0 z=0.6212405592105263
- **PERSISTENT_UP** `biomass_gen` value=835 d1=54.0 d12=227.0 z=1.534618880733945
- **REVERSAL** `nuclear_gen` value=3328 d1=-1.0 d12=1.0 z=-0.67448975
- **ACCELERATION** `wind_gen` value=1.432e+04 d1=-46.0 d12=-190.0 z=-0.54976191571835
- **REVERSAL** `interconnector_net` value=-2106 d1=-1.0 d12=808.0 z=0.43482781401045073

## Nearest historical live analogues

- `2026-09-19T17:22:38.318939Z` distance=0.017 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:26:48.291042Z` distance=0.017 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T16:52:42.433757Z` distance=0.020 → {'next30m_imbalance_delta': 1.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T16:56:53.146650Z` distance=0.020 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T17:01:39.109374Z` distance=0.020 → {'next30m_imbalance_delta': 14.0, 'next30m_margin_delta': -8.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
