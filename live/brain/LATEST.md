# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T01:58:49.966951Z`  
Memory snapshots: **63**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.232e+04 d1=0.0 d12=32.0 z=-1.785414044117647
- **CHANGE_POINT** `thermal_base` value=6682 d1=-53.0 d12=-249.0 z=-0.843781324156746
- **CHANGE_POINT** `ccgt_gen` value=3359 d1=-48.0 d12=-244.0 z=-0.8409609689646712
- **PERSISTENT_UP** `biomass_gen` value=3187 d1=3.0 d12=25.0 z=2.8322853485169492
- **CHANGE_POINT** `wind_gen` value=1.244e+04 d1=-104.0 d12=329.0 z=0.19221210492227978
- **PERSISTENT_DOWN** `nuclear_gen` value=3323 d1=-5.0 d12=-5.0 z=1.1803570625
- **ACCELERATION** `nuclear_gen` value=3323 d1=-5.0 d12=-5.0 z=1.1803570625
- **PERSISTENT_UP** `margin` value=3.273e+04 d1=0.0 d12=65.0 z=0.8541277236180904
- **PERSISTENT_DOWN** `thermal_base` value=6682 d1=-53.0 d12=-249.0 z=-0.843781324156746
- **PERSISTENT_DOWN** `ccgt_gen` value=3359 d1=-48.0 d12=-244.0 z=-0.8409609689646712
- **PERSISTENT_DOWN** `ind_generation` value=2.073e+04 d1=0.0 d12=-27.0 z=0.45768947321428566
- **PERSISTENT_DOWN** `imbalance` value=244 d1=0.0 d12=-28.0 z=0.45230489117647055
- **REVERSAL** `wind_gen` value=1.244e+04 d1=-104.0 d12=329.0 z=0.19221210492227978
- **PERSISTENT_DOWN** `interconnector_net` value=-1684 d1=-85.0 d12=-1381.0 z=-0.04119994064861461

## Nearest historical live analogues

- `2026-09-15T00:51:49.246305Z` distance=1.351 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:55:59.461560Z` distance=1.351 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 25.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T01:00:10.370005Z` distance=1.351 → {'next30m_imbalance_delta': -26.0, 'next30m_margin_delta': 25.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T01:04:20.750196Z` distance=1.351 → {'next30m_imbalance_delta': -26.0, 'next30m_margin_delta': 25.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T00:22:28.991704Z` distance=1.835 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
