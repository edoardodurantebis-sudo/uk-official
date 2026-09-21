# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T04:16:58.334967Z`  
Memory snapshots: **2053**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.755e+04 d1=0.0 d12=-17.0 z=28.886480774691357
- **ROBUST_OUTLIER** `margin` value=3.755e+04 d1=0.0 d12=-17.0 z=28.886480774691357
- **CHANGE_POINT** `imbalance` value=-4043 d1=0.0 d12=777.0 z=6.6983809655172415
- **CHANGE_POINT** `ind_generation` value=1.657e+04 d1=0.0 d12=777.0 z=6.6983809655172415
- **ROBUST_OUTLIER** `imbalance` value=-4043 d1=0.0 d12=777.0 z=6.6983809655172415
- **ROBUST_OUTLIER** `ind_generation` value=1.657e+04 d1=0.0 d12=777.0 z=6.6983809655172415
- **CHANGE_POINT** `thermal_base` value=1.056e+04 d1=237.0 d12=1430.0 z=4.116499137200737
- **CHANGE_POINT** `ccgt_gen` value=7210 d1=215.0 d12=1417.0 z=4.022366924408014
- **CHANGE_POINT** `interconnector_net` value=7241 d1=24.0 d12=-3994.0 z=-2.153157035684299
- **PERSISTENT_UP** `thermal_base` value=1.056e+04 d1=237.0 d12=1430.0 z=4.116499137200737
- **ROBUST_OUTLIER** `thermal_base` value=1.056e+04 d1=237.0 d12=1430.0 z=4.116499137200737
- **PERSISTENT_UP** `ccgt_gen` value=7210 d1=215.0 d12=1417.0 z=4.022366924408014
- **ROBUST_OUTLIER** `ccgt_gen` value=7210 d1=215.0 d12=1417.0 z=4.022366924408014
- **ROBUST_OUTLIER** `ind_demand` value=-1.176e+04 d1=0.0 d12=38.0 z=3.8221085833333333
- **PERSISTENT_UP** `nuclear_gen` value=3354 d1=22.0 d12=13.0 z=3.8221085833333333

## Nearest historical live analogues

- `2026-09-21T03:22:03.307428Z` distance=0.587 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -6418.0}
- `2026-09-21T02:22:39.819793Z` distance=0.587 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:26:51.602433Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:31:01.988533Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T02:35:13.346437Z` distance=0.587 → {'next30m_imbalance_delta': 39.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
