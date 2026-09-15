# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T21:22:07.813465Z`  
Memory snapshots: **339**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=9515 d1=-220.0 d12=-3459.0 z=-6.207437270316027
- **CHANGE_POINT** `ccgt_gen` value=6192 d1=-220.0 d12=-3461.0 z=-6.1649270535313905
- **REVERSAL** `wind_gen` value=1.251e+04 d1=-117.0 d12=648.0 z=6.630631001176471
- **ROBUST_OUTLIER** `wind_gen` value=1.251e+04 d1=-117.0 d12=648.0 z=6.630631001176471
- **PERSISTENT_DOWN** `thermal_base` value=9515 d1=-220.0 d12=-3459.0 z=-6.207437270316027
- **ROBUST_OUTLIER** `thermal_base` value=9515 d1=-220.0 d12=-3459.0 z=-6.207437270316027
- **PERSISTENT_DOWN** `ccgt_gen` value=6192 d1=-220.0 d12=-3461.0 z=-6.1649270535313905
- **ROBUST_OUTLIER** `ccgt_gen` value=6192 d1=-220.0 d12=-3461.0 z=-6.1649270535313905
- **CHANGE_POINT** `ps_gen` value=-260 d1=2.0 d12=-2.0 z=-0.683364615131579
- **CHANGE_POINT** `imbalance` value=5769 d1=47.0 d12=-19.0 z=-0.10649838157894735
- **CHANGE_POINT** `ind_generation` value=2.489e+04 d1=47.0 d12=-19.0 z=-0.10649838157894735
- **PERSISTENT_UP** `margin` value=3.572e+04 d1=5.0 d12=23.0 z=0.7016869173387097
- **REVERSAL** `ps_gen` value=-260 d1=2.0 d12=-2.0 z=-0.683364615131579
- **ACCELERATION** `ps_gen` value=-260 d1=2.0 d12=-2.0 z=-0.683364615131579
- **PERSISTENT_DOWN** `biomass_gen` value=3260 d1=-1.0 d12=-14.0 z=0.40225593524096387

## Nearest historical live analogues

- `2026-09-15T20:22:50.211969Z` distance=0.018 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T20:27:39.367678Z` distance=0.018 → {'next30m_imbalance_delta': -66.0, 'next30m_margin_delta': 18.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:31:50.302711Z` distance=0.061 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:36:02.892054Z` distance=0.061 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T19:40:15.609389Z` distance=0.061 → {'next30m_imbalance_delta': -5.0, 'next30m_margin_delta': -44.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
