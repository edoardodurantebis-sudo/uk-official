# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T22:27:58.503394Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.432e+04 d1=-202.0 d12=-2890.0 z=-8.724314444121916
- **CHANGE_POINT** `ccgt_gen` value=1.058e+04 d1=-202.0 d12=-2898.0 z=-8.684784446685878
- **PERSISTENT_DOWN** `thermal_base` value=1.432e+04 d1=-202.0 d12=-2890.0 z=-8.724314444121916
- **ROBUST_OUTLIER** `thermal_base` value=1.432e+04 d1=-202.0 d12=-2890.0 z=-8.724314444121916
- **PERSISTENT_DOWN** `ccgt_gen` value=1.058e+04 d1=-202.0 d12=-2898.0 z=-8.684784446685878
- **ROBUST_OUTLIER** `ccgt_gen` value=1.058e+04 d1=-202.0 d12=-2898.0 z=-8.684784446685878
- **CHANGE_POINT** `wind_gen` value=2600 d1=32.0 d12=172.0 z=1.582875139112903
- **PERSISTENT_UP** `nuclear_gen` value=3744 d1=0.0 d12=8.0 z=2.9227889166666667
- **ACCELERATION** `nuclear_gen` value=3744 d1=0.0 d12=8.0 z=2.9227889166666667
- **CHANGE_POINT** `imbalance` value=-8047 d1=0.0 d12=-28.0 z=-0.79712425
- **CHANGE_POINT** `ind_generation` value=1.313e+04 d1=0.0 d12=-28.0 z=-0.79712425
- **PERSISTENT_UP** `ps_gen` value=145 d1=0.0 d12=2.0 z=-2.4464543474576272
- **ACCELERATION** `ps_gen` value=145 d1=0.0 d12=2.0 z=-2.4464543474576272
- **PERSISTENT_UP** `margin` value=3.723e+04 d1=0.0 d12=19.0 z=2.4202279264705884
- **REVERSAL** `interconnector_net` value=5095 d1=-24.0 d12=336.0 z=-2.3242227057074913

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.011 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:24:47.718083Z` distance=0.011 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:28:58.806773Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:33:11.512074Z` distance=0.011 → {'next30m_imbalance_delta': -35.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -1.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:55:13.117327Z` distance=0.011 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
