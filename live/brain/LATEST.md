# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T04:31:17.660919Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **PERSISTENT_DOWN** `margin` value=3.853e+04 d1=0.0 d12=-44.0 z=79.52847324999999
- **ROBUST_OUTLIER** `margin` value=3.853e+04 d1=0.0 d12=-44.0 z=79.52847324999999
- **CHANGE_POINT** `nuclear_gen` value=3766 d1=9.0 d12=49.0 z=3.709693625
- **CHANGE_POINT** `ccgt_gen` value=8010 d1=-4.0 d12=-1126.0 z=-3.3665408105839414
- **CHANGE_POINT** `thermal_base` value=1.178e+04 d1=5.0 d12=-1077.0 z=-3.1665121036414567
- **CHANGE_POINT** `wind_gen` value=9022 d1=73.0 d12=2327.0 z=2.5231733604722795
- **PERSISTENT_UP** `nuclear_gen` value=3766 d1=9.0 d12=49.0 z=3.709693625
- **ROBUST_OUTLIER** `nuclear_gen` value=3766 d1=9.0 d12=49.0 z=3.709693625
- **CHANGE_POINT** `imbalance` value=-8037 d1=0.0 d12=-45.0 z=-1.4613944583333334
- **CHANGE_POINT** `ind_generation` value=1.314e+04 d1=0.0 d12=-45.0 z=-1.4613944583333334
- **PERSISTENT_DOWN** `ccgt_gen` value=8010 d1=-4.0 d12=-1126.0 z=-3.3665408105839414
- **ROBUST_OUTLIER** `ccgt_gen` value=8010 d1=-4.0 d12=-1126.0 z=-3.3665408105839414
- **REVERSAL** `thermal_base` value=1.178e+04 d1=5.0 d12=-1077.0 z=-3.1665121036414567
- **ROBUST_OUTLIER** `thermal_base` value=1.178e+04 d1=5.0 d12=-1077.0 z=-3.1665121036414567
- **CHANGE_POINT** `ps_gen` value=144 d1=0.0 d12=0.0 z=-1.1241495833333335

## Nearest historical live analogues

- `2026-09-23T03:32:33.216215Z` distance=0.024 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T03:36:43.352003Z` distance=0.024 → {'next30m_imbalance_delta': -89.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -23.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:19:16.764355Z` distance=0.378 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:53:56.422040Z` distance=0.402 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.402 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
