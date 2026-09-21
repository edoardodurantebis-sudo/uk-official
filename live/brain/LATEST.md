# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T11:32:38.703181Z`  
Memory snapshots: **2156**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=0.0 d12=587.0 z=14.786890673076924
- **PERSISTENT_UP** `ind_demand` value=-1.224e+04 d1=0.0 d12=587.0 z=14.786890673076924
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=587.0 z=14.786890673076924
- **CHANGE_POINT** `nuclear_gen` value=3515 d1=-3.0 d12=20.0 z=2.697959
- **CHANGE_POINT** `margin` value=3.668e+04 d1=182.0 d12=-4335.0 z=-1.5156412114825584
- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=-104.0 d12=1004.0 z=1.0682912189440994
- **PERSISTENT_UP** `ccgt_gen` value=7140 d1=155.0 d12=182.0 z=-2.7926745819148935
- **ACCELERATION** `ccgt_gen` value=7140 d1=155.0 d12=182.0 z=-2.7926745819148935
- **REVERSAL** `nuclear_gen` value=3515 d1=-3.0 d12=20.0 z=2.697959
- **PERSISTENT_UP** `thermal_base` value=1.066e+04 d1=152.0 d12=202.0 z=-2.559974555854643
- **ACCELERATION** `thermal_base` value=1.066e+04 d1=152.0 d12=202.0 z=-2.559974555854643
- **CHANGE_POINT** `ind_generation` value=1.849e+04 d1=0.0 d12=-6238.0 z=0.2668027549732211
- **CHANGE_POINT** `imbalance` value=-3015 d1=0.0 d12=-6583.0 z=0.25738309810554805
- **REVERSAL** `margin` value=3.668e+04 d1=182.0 d12=-4335.0 z=-1.5156412114825584
- **REVERSAL** `residual_proxy` value=1.208e+04 d1=-104.0 d12=1004.0 z=1.0682912189440994

## Nearest historical live analogues

- `2026-09-19T07:48:55.634175Z` distance=0.474 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T07:53:08.075404Z` distance=0.474 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T07:57:20.386172Z` distance=0.474 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:01:30.536514Z` distance=0.474 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3120.0}
- `2026-09-19T08:05:42.408180Z` distance=0.474 → {'next30m_imbalance_delta': 540.0, 'next30m_margin_delta': 589.0, 'next30m_residual_proxy_delta': -3235.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
