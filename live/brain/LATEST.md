# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T07:52:42.625642Z`  
Memory snapshots: **489**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.632e+04 d1=0.0 d12=-1077.0 z=-50.628886859375
- **ROBUST_OUTLIER** `margin` value=3.632e+04 d1=0.0 d12=-1077.0 z=-50.628886859375
- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-195.0 z=-22.065450392857144
- **PERSISTENT_UP** `residual_proxy` value=864 d1=0.0 d12=1249.0 z=4.691355458598727
- **ACCELERATION** `residual_proxy` value=864 d1=0.0 d12=1249.0 z=4.691355458598727
- **ROBUST_OUTLIER** `residual_proxy` value=864 d1=0.0 d12=1249.0 z=4.691355458598727
- **CHANGE_POINT** `ps_gen` value=229 d1=1.0 d12=7.0 z=1.8885713
- **REVERSAL** `thermal_base` value=1.168e+04 d1=80.0 d12=-4.0 z=2.803499662320144
- **ACCELERATION** `thermal_base` value=1.168e+04 d1=80.0 d12=-4.0 z=2.803499662320144
- **REVERSAL** `ccgt_gen` value=8355 d1=83.0 d12=-2.0 z=2.7869060166517654
- **ACCELERATION** `ccgt_gen` value=8355 d1=83.0 d12=-2.0 z=2.7869060166517654
- **CHANGE_POINT** `ind_generation` value=2.644e+04 d1=0.0 d12=2.0 z=0.6825674715568862
- **CHANGE_POINT** `imbalance` value=6872 d1=0.0 d12=-442.0 z=-0.5207200660621761
- **PERSISTENT_UP** `interconnector_net` value=9787 d1=0.0 d12=5207.0 z=2.4109845851431393
- **PERSISTENT_DOWN** `biomass_gen` value=3225 d1=-4.0 d12=-1.0 z=-2.360714125

## Nearest historical live analogues

- `2026-09-16T06:54:08.413156Z` distance=1.127 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:58:18.248300Z` distance=1.127 → {'next30m_imbalance_delta': -442.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:22:04.416358Z` distance=1.499 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -157.0}
- `2026-09-16T05:26:14.079375Z` distance=1.499 → {'next30m_imbalance_delta': 41.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -157.0}
- `2026-09-16T05:30:25.684923Z` distance=1.499 → {'next30m_imbalance_delta': 41.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -157.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
