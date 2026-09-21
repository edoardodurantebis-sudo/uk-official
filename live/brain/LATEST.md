# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T08:01:20.715748Z`  
Memory snapshots: **2106**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.825e+04 d1=0.0 d12=101.0 z=21.7063065
- **ROBUST_OUTLIER** `margin` value=3.825e+04 d1=0.0 d12=101.0 z=21.7063065
- **ROBUST_OUTLIER** `ind_demand` value=-1.283e+04 d1=0.0 d12=-274.0 z=-12.64361695
- **CHANGE_POINT** `ind_generation` value=1.797e+04 d1=0.0 d12=1307.0 z=5.893354190625
- **ROBUST_OUTLIER** `ind_generation` value=1.797e+04 d1=0.0 d12=1307.0 z=5.893354190625
- **CHANGE_POINT** `imbalance` value=-3297 d1=0.0 d12=1061.0 z=1.597363026984127
- **CHANGE_POINT** `ps_gen` value=-10 d1=0.0 d12=-234.0 z=0.01143202966101695
- **PERSISTENT_UP** `wind_gen` value=4385 d1=21.0 d12=216.0 z=1.7597023086592178
- **PERSISTENT_DOWN** `nuclear_gen` value=3499 d1=-2.0 d12=-1.0 z=1.5292886410891091
- **ACCELERATION** `nuclear_gen` value=3499 d1=-2.0 d12=-1.0 z=1.5292886410891091
- **REVERSAL** `thermal_base` value=1.233e+04 d1=90.0 d12=-60.0 z=0.5828983436044428
- **ACCELERATION** `thermal_base` value=1.233e+04 d1=90.0 d12=-60.0 z=0.5828983436044428
- **REVERSAL** `ccgt_gen` value=8828 d1=92.0 d12=-59.0 z=0.5721352743190662
- **ACCELERATION** `ccgt_gen` value=8828 d1=92.0 d12=-59.0 z=0.5721352743190662
- **PERSISTENT_DOWN** `biomass_gen` value=3015 d1=-6.0 d12=-10.0 z=-0.5395918

## Nearest historical live analogues

- `2026-09-21T06:53:56.422040Z` distance=0.331 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:58:09.070698Z` distance=0.331 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:02:21.725847Z` distance=0.331 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T07:06:37.268181Z` distance=0.331 → {'next30m_imbalance_delta': 1061.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 101.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T06:49:44.005596Z` distance=0.814 → {'next30m_imbalance_delta': -491.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
