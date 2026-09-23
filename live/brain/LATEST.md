# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T02:12:01.748327Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.243e+04 d1=0.0 d12=3.0 z=15.176019375
- **ROBUST_OUTLIER** `ind_demand` value=-1.243e+04 d1=0.0 d12=3.0 z=15.176019375
- **CHANGE_POINT** `biomass_gen` value=2847 d1=5.0 d12=-65.0 z=-7.082142375
- **REVERSAL** `biomass_gen` value=2847 d1=5.0 d12=-65.0 z=-7.082142375
- **ROBUST_OUTLIER** `biomass_gen` value=2847 d1=5.0 d12=-65.0 z=-7.082142375
- **CHANGE_POINT** `interconnector_net` value=561 d1=-271.0 d12=-1338.0 z=-1.817832131097561
- **PERSISTENT_UP** `wind_gen` value=5283 d1=108.0 d12=455.0 z=2.4131318876863026
- **PERSISTENT_DOWN** `ps_gen` value=144 d1=-3.0 d12=-3.0 z=-2.0234692499999998
- **ACCELERATION** `ps_gen` value=144 d1=-3.0 d12=-3.0 z=-2.0234692499999998
- **PERSISTENT_DOWN** `interconnector_net` value=561 d1=-271.0 d12=-1338.0 z=-1.817832131097561
- **PERSISTENT_DOWN** `ccgt_gen` value=9180 d1=-401.0 d12=-542.0 z=-1.0597016203501093
- **ACCELERATION** `ccgt_gen` value=9180 d1=-401.0 d12=-542.0 z=-1.0597016203501093
- **PERSISTENT_DOWN** `thermal_base` value=1.291e+04 d1=-403.0 d12=-541.0 z=-1.038560921875
- **ACCELERATION** `thermal_base` value=1.291e+04 d1=-403.0 d12=-541.0 z=-1.038560921875
- **REVERSAL** `nuclear_gen` value=3733 d1=-2.0 d12=1.0 z=-0.337244875

## Nearest historical live analogues

- `2026-09-23T00:50:49.821360Z` distance=0.012 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:55:39.096200Z` distance=0.012 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T00:59:50.808074Z` distance=0.012 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T01:04:02.744778Z` distance=0.012 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T01:08:15.509687Z` distance=0.012 → {'next30m_imbalance_delta': 12.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
