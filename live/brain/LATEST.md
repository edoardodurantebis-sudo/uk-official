# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T03:37:48.990972Z`  
Memory snapshots: **2383**  
Current physical regime: **LOOSE**

Regime read: margin high, wind rising.

## Active patterns

- **CHANGE_POINT** `margin` value=3.779e+04 d1=0.0 d12=-28.0 z=22.368282525510203
- **ROBUST_OUTLIER** `margin` value=3.779e+04 d1=0.0 d12=-28.0 z=22.368282525510203
- **CHANGE_POINT** `interconnector_net` value=-1461 d1=26.0 d12=-4127.0 z=-4.481486113189601
- **REVERSAL** `interconnector_net` value=-1461 d1=26.0 d12=-4127.0 z=-4.481486113189601
- **ACCELERATION** `interconnector_net` value=-1461 d1=26.0 d12=-4127.0 z=-4.481486113189601
- **ROBUST_OUTLIER** `interconnector_net` value=-1461 d1=26.0 d12=-4127.0 z=-4.481486113189601
- **CHANGE_POINT** `ind_demand` value=-1.25e+04 d1=0.0 d12=-3.0 z=-2.2739940142857145
- **CHANGE_POINT** `imbalance` value=-2644 d1=0.0 d12=11.0 z=-0.2459077213541667
- **CHANGE_POINT** `ind_generation` value=1.882e+04 d1=0.0 d12=11.0 z=-0.2459077213541667
- **CHANGE_POINT** `thermal_base` value=1.496e+04 d1=10.0 d12=636.0 z=0.17549419827586207
- **CHANGE_POINT** `ccgt_gen` value=1.13e+04 d1=3.0 d12=632.0 z=0.15972080052790347
- **PERSISTENT_DOWN** `ps_gen` value=-408 d1=-236.0 d12=-243.0 z=-1.3893335876068376
- **ACCELERATION** `ps_gen` value=-408 d1=-236.0 d12=-243.0 z=-1.3893335876068376
- **PERSISTENT_UP** `nuclear_gen` value=3657 d1=7.0 d12=4.0 z=0.94428565
- **ACCELERATION** `nuclear_gen` value=3657 d1=7.0 d12=4.0 z=0.94428565

## Nearest historical live analogues

- `2026-09-22T02:20:47.392507Z` distance=0.196 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:24:59.358718Z` distance=0.196 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:29:12.426907Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:33:26.071895Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T02:37:48.213453Z` distance=0.196 → {'next30m_imbalance_delta': -4.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 15.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
