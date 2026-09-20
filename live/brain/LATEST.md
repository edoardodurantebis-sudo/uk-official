# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T18:09:24.806977Z`  
Memory snapshots: **1909**  
Current physical regime: **BALANCED**

Regime read: residual low, margin low.

## Active patterns

- **REVERSAL** `biomass_gen` value=2258 d1=-2.0 d12=11.0 z=187.6767729375
- **ROBUST_OUTLIER** `biomass_gen` value=2258 d1=-2.0 d12=11.0 z=187.6767729375
- **PERSISTENT_UP** `ccgt_gen` value=9000 d1=49.0 d12=1154.0 z=49.18876646089385
- **ROBUST_OUTLIER** `ccgt_gen` value=9000 d1=49.0 d12=1154.0 z=49.18876646089385
- **PERSISTENT_UP** `thermal_base` value=1.234e+04 d1=46.0 d12=1151.0 z=47.855780903532604
- **ROBUST_OUTLIER** `thermal_base` value=1.234e+04 d1=46.0 d12=1151.0 z=47.855780903532604
- **CHANGE_POINT** `margin` value=3.546e+04 d1=0.0 d12=-424.0 z=-15.657797767857144
- **ROBUST_OUTLIER** `margin` value=3.546e+04 d1=0.0 d12=-424.0 z=-15.657797767857144
- **ROBUST_OUTLIER** `imbalance` value=-5165 d1=0.0 d12=25.0 z=3.989360106707317
- **PERSISTENT_UP** `ps_gen` value=530 d1=308.0 d12=363.0 z=3.5840871154336735
- **ACCELERATION** `ps_gen` value=530 d1=308.0 d12=363.0 z=3.5840871154336735
- **ROBUST_OUTLIER** `ps_gen` value=530 d1=308.0 d12=363.0 z=3.5840871154336735
- **CHANGE_POINT** `wind_gen` value=6542 d1=-67.0 d12=-875.0 z=-1.287368649907919
- **PERSISTENT_DOWN** `wind_gen` value=6542 d1=-67.0 d12=-875.0 z=-1.287368649907919
- **PERSISTENT_DOWN** `interconnector_net` value=9946 d1=-43.0 d12=-1008.0 z=0.9247370022759248

## Nearest historical live analogues

- `2026-09-20T14:49:59.741529Z` distance=0.041 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:24:12.719546Z` distance=0.046 → {'next30m_imbalance_delta': 81.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:28:27.793665Z` distance=0.046 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:32:40.592900Z` distance=0.046 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}
- `2026-09-20T14:36:50.929973Z` distance=0.046 → {'next30m_imbalance_delta': 492.0, 'next30m_margin_delta': 521.0, 'next30m_residual_proxy_delta': -494.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
