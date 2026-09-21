# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T08:13:56.421568Z`  
Memory snapshots: **2109**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.825e+04 d1=0.0 d12=0.0 z=23.21231798170732
- **ROBUST_OUTLIER** `margin` value=3.825e+04 d1=0.0 d12=0.0 z=23.21231798170732
- **ROBUST_OUTLIER** `ind_demand` value=-1.283e+04 d1=0.0 d12=0.0 z=-12.19998126754386
- **CHANGE_POINT** `ind_generation` value=1.797e+04 d1=0.0 d12=0.0 z=6.259896509197325
- **ROBUST_OUTLIER** `ind_generation` value=1.797e+04 d1=0.0 d12=0.0 z=6.259896509197325
- **CHANGE_POINT** `ps_gen` value=-10 d1=0.0 d12=-234.0 z=0.01143202966101695
- **PERSISTENT_UP** `wind_gen` value=4451 d1=0.0 d12=231.0 z=2.008396853351955
- **PERSISTENT_UP** `biomass_gen` value=3028 d1=1.0 d12=0.0 z=1.3489795
- **ACCELERATION** `biomass_gen` value=3028 d1=1.0 d12=0.0 z=1.3489795
- **PERSISTENT_DOWN** `thermal_base` value=1.225e+04 d1=-57.0 d12=-81.0 z=0.5428317070960699
- **ACCELERATION** `thermal_base` value=1.225e+04 d1=-57.0 d12=-81.0 z=0.5428317070960699
- **PERSISTENT_DOWN** `ccgt_gen` value=8751 d1=-57.0 d12=-80.0 z=0.5247782400700934
- **ACCELERATION** `ccgt_gen` value=8751 d1=-57.0 d12=-80.0 z=0.5247782400700934

## Nearest historical live analogues

- `2026-09-21T07:19:16.764355Z` distance=0.328 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:53:56.422040Z` distance=0.331 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.331 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.331 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:06:37.268181Z` distance=0.331 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
