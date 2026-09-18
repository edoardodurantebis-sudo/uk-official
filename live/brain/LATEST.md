# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T05:38:06.235585Z`  
Memory snapshots: **1103**  
Current physical regime: **BALANCED**

Regime read: margin high, wind falling.

## Active patterns

- **ROBUST_OUTLIER** `imbalance` value=1.07e+04 d1=0.0 d12=-35.0 z=10.77199806617647
- **ROBUST_OUTLIER** `ind_generation` value=2.752e+04 d1=0.0 d12=-35.0 z=10.77199806617647
- **CHANGE_POINT** `thermal_base` value=8375 d1=101.0 d12=1815.0 z=4.580057923611111
- **CHANGE_POINT** `margin` value=3.802e+04 d1=0.0 d12=-143.0 z=4.409350902985074
- **CHANGE_POINT** `ccgt_gen` value=5036 d1=96.0 d12=1815.0 z=4.387457597087379
- **PERSISTENT_UP** `thermal_base` value=8375 d1=101.0 d12=1815.0 z=4.580057923611111
- **ROBUST_OUTLIER** `thermal_base` value=8375 d1=101.0 d12=1815.0 z=4.580057923611111
- **ROBUST_OUTLIER** `margin` value=3.802e+04 d1=0.0 d12=-143.0 z=4.409350902985074
- **PERSISTENT_UP** `ccgt_gen` value=5036 d1=96.0 d12=1815.0 z=4.387457597087379
- **ROBUST_OUTLIER** `ccgt_gen` value=5036 d1=96.0 d12=1815.0 z=4.387457597087379
- **CHANGE_POINT** `biomass_gen` value=2176 d1=-2.0 d12=50.0 z=1.499626956852792
- **CHANGE_POINT** `interconnector_net` value=-4785 d1=3.0 d12=2261.0 z=1.436490526699029
- **CHANGE_POINT** `ind_demand` value=-1.117e+04 d1=0.0 d12=-5.0 z=0.67448975
- **CHANGE_POINT** `ps_gen` value=296 d1=-194.0 d12=69.0 z=0.0
- **REVERSAL** `biomass_gen` value=2176 d1=-2.0 d12=50.0 z=1.499626956852792

## Nearest historical live analogues

- `2026-09-18T04:22:33.656419Z` distance=0.085 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T04:26:45.757776Z` distance=0.085 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -106.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T04:30:58.266480Z` distance=0.085 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -106.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T04:35:10.163579Z` distance=0.085 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -106.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T04:39:23.438454Z` distance=0.085 → {'next30m_imbalance_delta': 26.0, 'next30m_margin_delta': -106.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
