# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T07:42:35.927452Z`  
Memory snapshots: **145**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3254 d1=19.0 d12=20.0 z=3.848559161764706
- **CHANGE_POINT** `interconnector_net` value=6465 d1=45.0 d12=7142.0 z=2.6504090709419432
- **CHANGE_POINT** `wind_gen` value=1.254e+04 d1=43.0 d12=-1057.0 z=-1.8613322908653847
- **PERSISTENT_UP** `biomass_gen` value=3254 d1=19.0 d12=20.0 z=3.848559161764706
- **ACCELERATION** `biomass_gen` value=3254 d1=19.0 d12=20.0 z=3.848559161764706
- **ROBUST_OUTLIER** `biomass_gen` value=3254 d1=19.0 d12=20.0 z=3.848559161764706
- **CHANGE_POINT** `thermal_base` value=6426 d1=-82.0 d12=-870.0 z=-1.6828853168316833
- **CHANGE_POINT** `ccgt_gen` value=3108 d1=-87.0 d12=-868.0 z=-1.6593790118159204
- **ROBUST_OUTLIER** `ind_demand` value=-1.228e+04 d1=0.0 d12=144.0 z=3.1074706339285716
- **CHANGE_POINT** `margin` value=3.413e+04 d1=0.0 d12=158.0 z=0.9335652831125828
- **PERSISTENT_UP** `interconnector_net` value=6465 d1=45.0 d12=7142.0 z=2.6504090709419432
- **CHANGE_POINT** `ind_generation` value=2.003e+04 d1=0.0 d12=249.0 z=-0.17986393333333334
- **CHANGE_POINT** `imbalance` value=-454 d1=0.0 d12=249.0 z=-0.17891999093511451
- **REVERSAL** `wind_gen` value=1.254e+04 d1=43.0 d12=-1057.0 z=-1.8613322908653847
- **PERSISTENT_DOWN** `thermal_base` value=6426 d1=-82.0 d12=-870.0 z=-1.6828853168316833

## Nearest historical live analogues

- `2026-09-15T03:31:03.539054Z` distance=1.046 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:35:14.775267Z` distance=1.046 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:39:27.190792Z` distance=1.046 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:43:38.131186Z` distance=1.046 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:47:47.828928Z` distance=1.046 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
