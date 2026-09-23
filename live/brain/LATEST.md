# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T09:48:27.182675Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `nuclear_gen` value=3611 d1=-188.0 d12=-188.0 z=-28.70328602777778
- **ACCELERATION** `nuclear_gen` value=3611 d1=-188.0 d12=-188.0 z=-28.70328602777778
- **ROBUST_OUTLIER** `nuclear_gen` value=3611 d1=-188.0 d12=-188.0 z=-28.70328602777778
- **CHANGE_POINT** `ind_demand` value=-1.268e+04 d1=0.0 d12=-22.0 z=-14.782567020833334
- **ROBUST_OUTLIER** `ind_demand` value=-1.268e+04 d1=0.0 d12=-22.0 z=-14.782567020833334
- **CHANGE_POINT** `imbalance` value=-5115 d1=0.0 d12=2250.0 z=12.742387439189189
- **ROBUST_OUTLIER** `imbalance` value=-5115 d1=0.0 d12=2250.0 z=12.742387439189189
- **CHANGE_POINT** `ind_generation` value=1.591e+04 d1=0.0 d12=2250.0 z=10.651317302083333
- **ROBUST_OUTLIER** `ind_generation` value=1.591e+04 d1=0.0 d12=2250.0 z=10.651317302083333
- **CHANGE_POINT** `margin` value=4.072e+04 d1=0.0 d12=1065.0 z=6.440715848039216
- **CHANGE_POINT** `interconnector_net` value=1.137e+04 d1=23.0 d12=1400.0 z=5.452277968258275
- **ROBUST_OUTLIER** `margin` value=4.072e+04 d1=0.0 d12=1065.0 z=6.440715848039216
- **PERSISTENT_UP** `interconnector_net` value=1.137e+04 d1=23.0 d12=1400.0 z=5.452277968258275
- **ROBUST_OUTLIER** `interconnector_net` value=1.137e+04 d1=23.0 d12=1400.0 z=5.452277968258275
- **PERSISTENT_DOWN** `ccgt_gen` value=2464 d1=-303.0 d12=-936.0 z=-4.8286725032651905

## Nearest historical live analogues

- `2026-09-21T10:33:45.224867Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:37:58.343383Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:42:10.019375Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:46:20.592599Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:50:33.489846Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
