# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T06:28:10.123987Z`  
Memory snapshots: **2423**  
Current physical regime: **BALANCED**

## Active patterns

- **PERSISTENT_UP** `ccgt_gen` value=1.422e+04 d1=3.0 d12=481.0 z=3.8881962834472654
- **ROBUST_OUTLIER** `ccgt_gen` value=1.422e+04 d1=3.0 d12=481.0 z=3.8881962834472654
- **REVERSAL** `thermal_base` value=1.787e+04 d1=-7.0 d12=470.0 z=3.8763400183105468
- **ROBUST_OUTLIER** `thermal_base` value=1.787e+04 d1=-7.0 d12=470.0 z=3.8763400183105468
- **CHANGE_POINT** `ps_gen` value=-173 d1=1.0 d12=-155.0 z=0.67448975
- **CHANGE_POINT** `imbalance` value=-3011 d1=0.0 d12=251.0 z=-0.4126290235294117
- **CHANGE_POINT** `ind_generation` value=1.845e+04 d1=0.0 d12=251.0 z=-0.4126290235294117
- **PERSISTENT_DOWN** `nuclear_gen` value=3645 d1=-10.0 d12=-11.0 z=-2.02346925
- **ACCELERATION** `nuclear_gen` value=3645 d1=-10.0 d12=-11.0 z=-2.02346925
- **CHANGE_POINT** `ind_demand` value=-1.248e+04 d1=0.0 d12=-1.0 z=0.015685808139534883
- **PERSISTENT_DOWN** `wind_gen` value=3407 d1=-29.0 d12=-44.0 z=-1.2390083451086957
- **REVERSAL** `interconnector_net` value=-647 d1=-53.0 d12=1069.0 z=-0.8574769589887641
- **PERSISTENT_UP** `biomass_gen` value=3030 d1=6.0 d12=1.0 z=-0.8331932205882353
- **ACCELERATION** `biomass_gen` value=3030 d1=6.0 d12=1.0 z=-0.8331932205882353
- **REVERSAL** `ps_gen` value=-173 d1=1.0 d12=-155.0 z=0.67448975

## Nearest historical live analogues

- `2026-09-22T05:32:49.824009Z` distance=0.008 → {'next30m_imbalance_delta': 53.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T05:24:23.506139Z` distance=0.065 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': -696.0}
- `2026-09-22T05:28:36.987525Z` distance=0.065 → {'next30m_imbalance_delta': 53.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': -696.0}
- `2026-09-22T03:33:35.816390Z` distance=0.070 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:37:48.990972Z` distance=0.070 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
