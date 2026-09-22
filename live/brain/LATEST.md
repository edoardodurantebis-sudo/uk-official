# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T11:25:00.789915Z`  
Memory snapshots: **2493**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.703e+04 d1=0.0 d12=-3354.0 z=-11.421359766666667
- **ROBUST_OUTLIER** `margin` value=3.703e+04 d1=0.0 d12=-3354.0 z=-11.421359766666667
- **ROBUST_OUTLIER** `wind_forecast` value=1.301e+04 d1=0.0 d12=0.0 z=8.488389872641509
- **CHANGE_POINT** `ind_generation` value=1.493e+04 d1=-23.0 d12=-11181.0 z=-5.1337006365168545
- **CHANGE_POINT** `thermal_base` value=1.212e+04 d1=0.0 d12=-1207.0 z=-3.1887421464267867
- **CHANGE_POINT** `ccgt_gen` value=8475 d1=0.0 d12=-1199.0 z=-3.1735951982071713
- **PERSISTENT_DOWN** `ind_generation` value=1.493e+04 d1=-23.0 d12=-11181.0 z=-5.1337006365168545
- **ROBUST_OUTLIER** `ind_generation` value=1.493e+04 d1=-23.0 d12=-11181.0 z=-5.1337006365168545
- **CHANGE_POINT** `imbalance` value=-6224 d1=6.0 d12=-11391.0 z=-3.0103131534008685
- **PERSISTENT_UP** `wind_gen` value=3892 d1=0.0 d12=317.0 z=3.866731314885496
- **ROBUST_OUTLIER** `wind_gen` value=3892 d1=0.0 d12=317.0 z=3.866731314885496
- **PERSISTENT_DOWN** `thermal_base` value=1.212e+04 d1=0.0 d12=-1207.0 z=-3.1887421464267867
- **ROBUST_OUTLIER** `thermal_base` value=1.212e+04 d1=0.0 d12=-1207.0 z=-3.1887421464267867
- **PERSISTENT_DOWN** `ccgt_gen` value=8475 d1=0.0 d12=-1199.0 z=-3.1735951982071713
- **ROBUST_OUTLIER** `ccgt_gen` value=8475 d1=0.0 d12=-1199.0 z=-3.1735951982071713

## Nearest historical live analogues

- `2026-09-22T05:53:47.929906Z` distance=0.377 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 41.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:57:59.458366Z` distance=0.377 → {'next30m_imbalance_delta': 198.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 41.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T06:02:11.446633Z` distance=0.377 → {'next30m_imbalance_delta': 198.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 41.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T06:06:26.622431Z` distance=0.377 → {'next30m_imbalance_delta': 198.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 41.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T06:11:17.063153Z` distance=0.377 → {'next30m_imbalance_delta': 198.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 41.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
