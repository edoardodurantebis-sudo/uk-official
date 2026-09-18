# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T02:03:17.114876Z`  
Memory snapshots: **1052**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ind_demand` value=-1.122e+04 d1=0.0 d12=1.0 z=-20.571937375
- **PERSISTENT_UP** `imbalance` value=1.016e+04 d1=0.0 d12=32.0 z=10.767747080357143
- **ROBUST_OUTLIER** `imbalance` value=1.016e+04 d1=0.0 d12=32.0 z=10.767747080357143
- **PERSISTENT_UP** `ind_generation` value=2.698e+04 d1=0.0 d12=32.0 z=10.767747080357143
- **ROBUST_OUTLIER** `ind_generation` value=2.698e+04 d1=0.0 d12=32.0 z=10.767747080357143
- **CHANGE_POINT** `margin` value=3.67e+04 d1=0.0 d12=101.0 z=2.557970561320755
- **CHANGE_POINT** `wind_gen` value=1.45e+04 d1=-31.0 d12=369.0 z=-0.588068640890891
- **PERSISTENT_UP** `nuclear_gen` value=3336 d1=3.0 d12=7.0 z=2.5293365625
- **ACCELERATION** `nuclear_gen` value=3336 d1=3.0 d12=7.0 z=2.5293365625
- **CHANGE_POINT** `biomass_gen` value=1925 d1=-13.0 d12=-31.0 z=-0.12740361944444445
- **PERSISTENT_DOWN** `ccgt_gen` value=3502 d1=-173.0 d12=-290.0 z=-1.0011703277108432
- **PERSISTENT_DOWN** `thermal_base` value=6838 d1=-170.0 d12=-283.0 z=-0.9857927115384615
- **REVERSAL** `wind_gen` value=1.45e+04 d1=-31.0 d12=369.0 z=-0.588068640890891
- **ACCELERATION** `wind_gen` value=1.45e+04 d1=-31.0 d12=369.0 z=-0.588068640890891
- **PERSISTENT_DOWN** `ps_gen` value=229 d1=-140.0 d12=-242.0 z=-0.2177870518072289

## Nearest historical live analogues

- `2026-09-18T00:55:05.130155Z` distance=0.045 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:59:16.440589Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:03:26.672918Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T01:07:37.196261Z` distance=0.045 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 100.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T00:50:53.445195Z` distance=0.063 → {'next30m_imbalance_delta': 15.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
