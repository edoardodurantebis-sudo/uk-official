# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T08:09:45.783199Z`  
Memory snapshots: **2108**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.825e+04 d1=0.0 d12=0.0 z=21.7063065
- **ROBUST_OUTLIER** `margin` value=3.825e+04 d1=0.0 d12=0.0 z=21.7063065
- **ROBUST_OUTLIER** `ind_demand` value=-1.283e+04 d1=0.0 d12=-274.0 z=-12.64361695
- **CHANGE_POINT** `ind_generation` value=1.797e+04 d1=0.0 d12=1307.0 z=5.893354190625
- **ROBUST_OUTLIER** `ind_generation` value=1.797e+04 d1=0.0 d12=1307.0 z=5.893354190625
- **CHANGE_POINT** `ps_gen` value=-10 d1=0.0 d12=-234.0 z=0.01143202966101695
- **PERSISTENT_UP** `wind_gen` value=4451 d1=66.0 d12=299.0 z=2.008396853351955
- **PERSISTENT_DOWN** `nuclear_gen` value=3499 d1=0.0 d12=-2.0 z=1.2610025760869565
- **PERSISTENT_UP** `biomass_gen` value=3027 d1=12.0 d12=0.0 z=1.21408155
- **ACCELERATION** `biomass_gen` value=3027 d1=12.0 d12=0.0 z=1.21408155
- **ACCELERATION** `thermal_base` value=1.231e+04 d1=-20.0 d12=-47.0 z=0.5824519883932177
- **ACCELERATION** `ccgt_gen` value=8808 d1=-20.0 d12=-45.0 z=0.5686646340517241
- **REVERSAL** `interconnector_net` value=1.068e+04 d1=-15.0 d12=1122.0 z=0.3265398444180522

## Nearest historical live analogues

- `2026-09-21T06:53:56.422040Z` distance=0.331 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.331 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.331 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:06:37.268181Z` distance=0.331 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:10:52.783726Z` distance=0.331 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
