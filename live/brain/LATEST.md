# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T10:18:13.875018Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.27e+04 d1=0.0 d12=-15.0 z=-13.889492629629629
- **ROBUST_OUTLIER** `ind_demand` value=-1.27e+04 d1=0.0 d12=-15.0 z=-13.889492629629629
- **CHANGE_POINT** `imbalance` value=-3948 d1=0.0 d12=1167.0 z=8.049771609649122
- **ROBUST_OUTLIER** `imbalance` value=-3948 d1=0.0 d12=1167.0 z=8.049771609649122
- **CHANGE_POINT** `ind_generation` value=1.708e+04 d1=0.0 d12=1167.0 z=5.553569821084337
- **CHANGE_POINT** `ps_gen` value=-870 d1=-58.0 d12=-851.0 z=-3.825066871710526
- **ROBUST_OUTLIER** `margin` value=4.071e+04 d1=0.0 d12=-14.0 z=5.746533817180616
- **ROBUST_OUTLIER** `ind_generation` value=1.708e+04 d1=0.0 d12=1167.0 z=5.553569821084337
- **REVERSAL** `interconnector_net` value=1.157e+04 d1=-24.0 d12=699.0 z=4.866640977538829
- **ROBUST_OUTLIER** `interconnector_net` value=1.157e+04 d1=-24.0 d12=699.0 z=4.866640977538829
- **PERSISTENT_DOWN** `ps_gen` value=-870 d1=-58.0 d12=-851.0 z=-3.825066871710526
- **ROBUST_OUTLIER** `ps_gen` value=-870 d1=-58.0 d12=-851.0 z=-3.825066871710526
- **PERSISTENT_DOWN** `ccgt_gen` value=2111 d1=-2.0 d12=-5.0 z=-2.7107657674050634
- **CHANGE_POINT** `nuclear_gen` value=3806 d1=4.0 d12=604.0 z=0.5058673124999999
- **PERSISTENT_UP** `nuclear_gen` value=3806 d1=4.0 d12=604.0 z=0.5058673124999999

## Nearest historical live analogues

- `2026-09-23T09:23:11.081898Z` distance=0.017 → {'next30m_imbalance_delta': 2250.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:33:45.224867Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:37:58.343383Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:42:10.019375Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:46:20.592599Z` distance=0.426 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
