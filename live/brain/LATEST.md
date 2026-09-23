# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T04:27:06.581467Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.853e+04 d1=0.0 d12=-44.0 z=79.52847324999999
- **PERSISTENT_DOWN** `margin` value=3.853e+04 d1=0.0 d12=-44.0 z=79.52847324999999
- **ACCELERATION** `margin` value=3.853e+04 d1=0.0 d12=-44.0 z=79.52847324999999
- **ROBUST_OUTLIER** `margin` value=3.853e+04 d1=0.0 d12=-44.0 z=79.52847324999999
- **CHANGE_POINT** `ccgt_gen` value=8014 d1=-281.0 d12=-1149.0 z=-3.3124510964849354
- **CHANGE_POINT** `thermal_base` value=1.177e+04 d1=-280.0 d12=-1113.0 z=-3.162022978412256
- **CHANGE_POINT** `nuclear_gen` value=3757 d1=1.0 d12=36.0 z=2.6979589999999996
- **CHANGE_POINT** `wind_gen` value=8949 d1=332.0 d12=2488.0 z=2.512696190378289
- **CHANGE_POINT** `imbalance` value=-8037 d1=0.0 d12=-45.0 z=-1.4613944583333334
- **CHANGE_POINT** `ind_generation` value=1.314e+04 d1=0.0 d12=-45.0 z=-1.4613944583333334
- **PERSISTENT_DOWN** `ccgt_gen` value=8014 d1=-281.0 d12=-1149.0 z=-3.3124510964849354
- **ROBUST_OUTLIER** `ccgt_gen` value=8014 d1=-281.0 d12=-1149.0 z=-3.3124510964849354
- **PERSISTENT_DOWN** `thermal_base` value=1.177e+04 d1=-280.0 d12=-1113.0 z=-3.162022978412256
- **ROBUST_OUTLIER** `thermal_base` value=1.177e+04 d1=-280.0 d12=-1113.0 z=-3.162022978412256
- **CHANGE_POINT** `ps_gen` value=144 d1=0.0 d12=15.0 z=-1.1241495833333335

## Nearest historical live analogues

- `2026-09-23T03:32:33.216215Z` distance=0.024 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:19:16.764355Z` distance=0.378 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:53:56.422040Z` distance=0.402 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.402 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.402 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
