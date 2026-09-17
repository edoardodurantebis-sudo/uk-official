# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T23:52:06.399107Z`  
Memory snapshots: **1021**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.118e+04 d1=0.0 d12=-7.0 z=-7.41938725
- **ROBUST_OUTLIER** `ind_demand` value=-1.118e+04 d1=0.0 d12=-7.0 z=-7.41938725
- **CHANGE_POINT** `biomass_gen` value=1961 d1=1.0 d12=152.0 z=-2.1253016278863233
- **CHANGE_POINT** `imbalance` value=9745 d1=0.0 d12=31.0 z=1.812691203125
- **CHANGE_POINT** `ind_generation` value=2.656e+04 d1=0.0 d12=31.0 z=1.812691203125
- **CHANGE_POINT** `wind_gen` value=1.436e+04 d1=-192.0 d12=-869.0 z=-1.7716106001821494
- **CHANGE_POINT** `ps_gen` value=55 d1=1.0 d12=3.0 z=-1.1885061022304833
- **PERSISTENT_UP** `biomass_gen` value=1961 d1=1.0 d12=152.0 z=-2.1253016278863233
- **CHANGE_POINT** `margin` value=3.652e+04 d1=-57.0 d12=11.0 z=0.12365645416666667
- **PERSISTENT_DOWN** `wind_gen` value=1.436e+04 d1=-192.0 d12=-869.0 z=-1.7716106001821494
- **PERSISTENT_UP** `interconnector_net` value=-6144 d1=10.0 d12=2016.0 z=-1.2477216559633029
- **PERSISTENT_UP** `ps_gen` value=55 d1=1.0 d12=3.0 z=-1.1885061022304833
- **ACCELERATION** `ps_gen` value=55 d1=1.0 d12=3.0 z=-1.1885061022304833
- **REVERSAL** `ccgt_gen` value=3769 d1=101.0 d12=-219.0 z=-0.8788495680323722
- **ACCELERATION** `ccgt_gen` value=3769 d1=101.0 d12=-219.0 z=-0.8788495680323722

## Nearest historical live analogues

- `2026-09-17T19:23:15.447841Z` distance=0.042 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T19:27:27.221396Z` distance=0.042 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 26.0, 'next30m_residual_proxy_delta': 191.0}
- `2026-09-17T18:57:56.745109Z` distance=0.051 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:02:09.783762Z` distance=0.051 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T19:06:26.402438Z` distance=0.051 → {'next30m_imbalance_delta': -17.0, 'next30m_margin_delta': -91.0, 'next30m_residual_proxy_delta': 191.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
