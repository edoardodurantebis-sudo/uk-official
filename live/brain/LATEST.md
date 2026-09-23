# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T10:14:00.341193Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `imbalance` value=-3948 d1=0.0 d12=3417.0 z=15.723546348529412
- **CHANGE_POINT** `ind_demand` value=-1.27e+04 d1=0.0 d12=-15.0 z=-15.625679208333333
- **ROBUST_OUTLIER** `imbalance` value=-3948 d1=0.0 d12=3417.0 z=15.723546348529412
- **ROBUST_OUTLIER** `ind_demand` value=-1.27e+04 d1=0.0 d12=-15.0 z=-15.625679208333333
- **CHANGE_POINT** `ind_generation` value=1.708e+04 d1=0.0 d12=1167.0 z=8.259360948815566
- **ROBUST_OUTLIER** `ind_generation` value=1.708e+04 d1=0.0 d12=1167.0 z=8.259360948815566
- **CHANGE_POINT** `interconnector_net` value=1.16e+04 d1=-47.0 d12=747.0 z=4.896607777004321
- **ROBUST_OUTLIER** `margin` value=4.071e+04 d1=0.0 d12=-14.0 z=6.053193394431554
- **CHANGE_POINT** `ps_gen` value=-812 d1=-60.0 d12=-1251.0 z=-3.5676957828947367
- **REVERSAL** `interconnector_net` value=1.16e+04 d1=-47.0 d12=747.0 z=4.896607777004321
- **ROBUST_OUTLIER** `interconnector_net` value=1.16e+04 d1=-47.0 d12=747.0 z=4.896607777004321
- **PERSISTENT_DOWN** `ps_gen` value=-812 d1=-60.0 d12=-1251.0 z=-3.5676957828947367
- **ROBUST_OUTLIER** `ps_gen` value=-812 d1=-60.0 d12=-1251.0 z=-3.5676957828947367
- **REVERSAL** `ccgt_gen` value=2113 d1=-1.0 d12=176.0 z=-2.930690287539936
- **CHANGE_POINT** `nuclear_gen` value=3802 d1=1.0 d12=2495.0 z=-0.1686224375

## Nearest historical live analogues

- `2026-09-21T10:33:45.224867Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:37:58.343383Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:42:10.019375Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:46:20.592599Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:50:33.489846Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
