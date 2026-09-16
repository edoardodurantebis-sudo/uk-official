# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T01:14:05.163798Z`  
Memory snapshots: **394**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.216e+04 d1=0.0 d12=-64.0 z=-55.08332958333333
- **ROBUST_OUTLIER** `ind_demand` value=-1.216e+04 d1=0.0 d12=-64.0 z=-55.08332958333333
- **ROBUST_OUTLIER** `imbalance` value=5999 d1=0.0 d12=-36.0 z=4.80573946875
- **ROBUST_OUTLIER** `ind_generation` value=2.512e+04 d1=0.0 d12=-36.0 z=4.80573946875
- **CHANGE_POINT** `ccgt_gen` value=3246 d1=3.0 d12=17.0 z=-0.6581359419490208
- **CHANGE_POINT** `thermal_base` value=6574 d1=-1.0 d12=8.0 z=-0.6569270906695598
- **PERSISTENT_UP** `interconnector_net` value=4446 d1=121.0 d12=427.0 z=1.1123662929944693
- **PERSISTENT_DOWN** `nuclear_gen` value=3328 d1=-4.0 d12=-9.0 z=0.8993196666666666
- **ACCELERATION** `nuclear_gen` value=3328 d1=-4.0 d12=-9.0 z=0.8993196666666666
- **PERSISTENT_UP** `ccgt_gen` value=3246 d1=3.0 d12=17.0 z=-0.6581359419490208
- **REVERSAL** `thermal_base` value=6574 d1=-1.0 d12=8.0 z=-0.6569270906695598
- **PERSISTENT_DOWN** `wind_gen` value=1.041e+04 d1=-103.0 d12=-123.0 z=-0.4987020531161473
- **ACCELERATION** `wind_gen` value=1.041e+04 d1=-103.0 d12=-123.0 z=-0.4987020531161473
- **REVERSAL** `ps_gen` value=224 d1=21.0 d12=-3.0 z=0.2585220079250721
- **ACCELERATION** `ps_gen` value=224 d1=21.0 d12=-3.0 z=0.2585220079250721

## Nearest historical live analogues

- `2026-09-15T23:49:36.074086Z` distance=0.162 → {'next30m_imbalance_delta': 39.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T23:53:48.658666Z` distance=0.164 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T23:57:59.720980Z` distance=0.164 → {'next30m_imbalance_delta': 170.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T00:02:10.447040Z` distance=0.164 → {'next30m_imbalance_delta': 170.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T00:06:21.657987Z` distance=0.164 → {'next30m_imbalance_delta': 170.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
