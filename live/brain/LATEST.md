# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T23:42:15.181563Z`  
Memory snapshots: **677**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high, wind rising.

## Active patterns

- **PERSISTENT_DOWN** `residual_proxy` value=-1481 d1=0.0 d12=-657.0 z=-10.40400439375
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=-657.0 z=-10.40400439375
- **PERSISTENT_UP** `wind_forecast` value=2.01e+04 d1=0.0 d12=657.0 z=10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=657.0 z=10.40400439375
- **CHANGE_POINT** `interconnector_net` value=-6436 d1=1.0 d12=-10840.0 z=-4.892401327453769
- **REVERSAL** `interconnector_net` value=-6436 d1=1.0 d12=-10840.0 z=-4.892401327453769
- **ROBUST_OUTLIER** `interconnector_net` value=-6436 d1=1.0 d12=-10840.0 z=-4.892401327453769
- **CHANGE_POINT** `ccgt_gen` value=5395 d1=7.0 d12=-3040.0 z=-2.8866005396689496
- **CHANGE_POINT** `thermal_base` value=8710 d1=6.0 d12=-3028.0 z=-2.8723430242027335
- **CHANGE_POINT** `wind_gen` value=1.149e+04 d1=83.0 d12=1322.0 z=1.606546690651558
- **CHANGE_POINT** `ind_generation` value=2.572e+04 d1=0.0 d12=-37.0 z=1.2069816578947368
- **CHANGE_POINT** `ps_gen` value=-247 d1=2.0 d12=-607.0 z=-1.1957293744740531
- **REVERSAL** `ccgt_gen` value=5395 d1=7.0 d12=-3040.0 z=-2.8866005396689496
- **REVERSAL** `thermal_base` value=8710 d1=6.0 d12=-3028.0 z=-2.8723430242027335
- **CHANGE_POINT** `imbalance` value=6603 d1=0.0 d12=-37.0 z=0.3118608521505376

## Nearest historical live analogues

- `2026-09-16T14:21:30.462993Z` distance=0.278 → {'next30m_imbalance_delta': 37.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:25:41.401432Z` distance=0.280 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:29:54.321922Z` distance=0.280 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:34:06.314775Z` distance=0.280 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T14:38:16.233128Z` distance=0.280 → {'next30m_imbalance_delta': 61.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
