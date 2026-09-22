# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T06:19:45.630706Z`  
Memory snapshots: **2421**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.786e+04 d1=31.0 d12=624.0 z=4.224699879383635
- **CHANGE_POINT** `ccgt_gen` value=1.42e+04 d1=27.0 d12=622.0 z=4.193814703488372
- **PERSISTENT_UP** `thermal_base` value=1.786e+04 d1=31.0 d12=624.0 z=4.224699879383635
- **ROBUST_OUTLIER** `thermal_base` value=1.786e+04 d1=31.0 d12=624.0 z=4.224699879383635
- **PERSISTENT_UP** `ccgt_gen` value=1.42e+04 d1=27.0 d12=622.0 z=4.193814703488372
- **ROBUST_OUTLIER** `ccgt_gen` value=1.42e+04 d1=27.0 d12=622.0 z=4.193814703488372
- **CHANGE_POINT** `ps_gen` value=-172 d1=2.0 d12=-1.0 z=0.680735025462963
- **CHANGE_POINT** `imbalance` value=-3209 d1=0.0 d12=53.0 z=-0.67448975
- **CHANGE_POINT** `ind_generation` value=1.825e+04 d1=0.0 d12=53.0 z=-0.67448975
- **CHANGE_POINT** `ind_demand` value=-1.248e+04 d1=0.0 d12=-2.0 z=0.0
- **PERSISTENT_DOWN** `biomass_gen` value=3027 d1=-2.0 d12=-2.0 z=-1.0712484264705882
- **ACCELERATION** `biomass_gen` value=3027 d1=-2.0 d12=-2.0 z=-1.0712484264705882
- **REVERSAL** `interconnector_net` value=-518 d1=-77.0 d12=2560.0 z=-0.9549466464975302
- **REVERSAL** `ps_gen` value=-172 d1=2.0 d12=-1.0 z=0.680735025462963
- **ACCELERATION** `ps_gen` value=-172 d1=2.0 d12=-1.0 z=0.680735025462963

## Nearest historical live analogues

- `2026-09-22T05:24:23.506139Z` distance=0.065 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -27.0, 'next30m_residual_proxy_delta': -696.0}
- `2026-09-22T03:33:35.816390Z` distance=0.070 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:37:48.990972Z` distance=0.070 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:42:37.215255Z` distance=0.070 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T03:46:49.421565Z` distance=0.070 → {'next30m_imbalance_delta': -592.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
