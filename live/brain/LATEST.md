# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T08:03:35.436277Z`  
Memory snapshots: **150**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.228e+04 d1=0.0 d12=144.0 z=3.1074706339285716
- **CHANGE_POINT** `interconnector_net` value=7019 d1=579.0 d12=3966.0 z=2.7979870020240916
- **CHANGE_POINT** `thermal_base` value=6321 d1=4.0 d12=-459.0 z=-2.185268814306358
- **CHANGE_POINT** `ccgt_gen` value=3002 d1=2.0 d12=-460.0 z=-2.1729188739067054
- **CHANGE_POINT** `wind_gen` value=1.262e+04 d1=71.0 d12=-879.0 z=-1.6927098533653846
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=0.0 d12=144.0 z=3.1074706339285716
- **PERSISTENT_UP** `interconnector_net` value=7019 d1=579.0 d12=3966.0 z=2.7979870020240916
- **CHANGE_POINT** `margin` value=3.413e+04 d1=0.0 d12=158.0 z=0.67448975
- **REVERSAL** `thermal_base` value=6321 d1=4.0 d12=-459.0 z=-2.185268814306358
- **REVERSAL** `ccgt_gen` value=3002 d1=2.0 d12=-460.0 z=-2.1729188739067054
- **CHANGE_POINT** `ps_gen` value=-264 d1=-5.0 d12=-2.0 z=-0.013225289215686274
- **REVERSAL** `wind_gen` value=1.262e+04 d1=71.0 d12=-879.0 z=-1.6927098533653846
- **REVERSAL** `biomass_gen` value=3229 d1=-18.0 d12=10.0 z=1.5738094166666667
- **ACCELERATION** `biomass_gen` value=3229 d1=-18.0 d12=10.0 z=1.5738094166666667
- **PERSISTENT_UP** `nuclear_gen` value=3319 d1=2.0 d12=1.0 z=-1.3489794999999998

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=1.114 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=1.114 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=1.114 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=1.114 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=1.114 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
