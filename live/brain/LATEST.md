# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T09:52:40.900319Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.268e+04 d1=0.0 d12=-22.0 z=-14.782567020833334
- **ROBUST_OUTLIER** `ind_demand` value=-1.268e+04 d1=0.0 d12=-22.0 z=-14.782567020833334
- **CHANGE_POINT** `imbalance` value=-5115 d1=0.0 d12=2250.0 z=11.093372594117646
- **CHANGE_POINT** `ind_generation` value=1.591e+04 d1=0.0 d12=2250.0 z=10.651317302083333
- **ROBUST_OUTLIER** `imbalance` value=-5115 d1=0.0 d12=2250.0 z=11.093372594117646
- **ROBUST_OUTLIER** `ind_generation` value=1.591e+04 d1=0.0 d12=2250.0 z=10.651317302083333
- **CHANGE_POINT** `margin` value=4.072e+04 d1=0.0 d12=1065.0 z=6.440715848039216
- **ROBUST_OUTLIER** `margin` value=4.072e+04 d1=0.0 d12=1065.0 z=6.440715848039216
- **PERSISTENT_UP** `interconnector_net` value=1.14e+04 d1=25.0 d12=821.0 z=5.461427313754748
- **ROBUST_OUTLIER** `interconnector_net` value=1.14e+04 d1=25.0 d12=821.0 z=5.461427313754748
- **PERSISTENT_DOWN** `ccgt_gen` value=2432 d1=-32.0 d12=-656.0 z=-4.565413945266273
- **ACCELERATION** `ccgt_gen` value=2432 d1=-32.0 d12=-656.0 z=-4.565413945266273
- **ROBUST_OUTLIER** `ccgt_gen` value=2432 d1=-32.0 d12=-656.0 z=-4.565413945266273
- **CHANGE_POINT** `ps_gen` value=-574 d1=-5.0 d12=-557.0 z=-2.511586832236842
- **REVERSAL** `thermal_base` value=6241 d1=166.0 d12=-646.0 z=-4.352321830278782

## Nearest historical live analogues

- `2026-09-21T10:33:45.224867Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:37:58.343383Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:42:10.019375Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:46:20.592599Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}
- `2026-09-21T10:50:33.489846Z` distance=0.428 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
