# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T07:48:31.958372Z`  
Memory snapshots: **488**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.632e+04 d1=0.0 d12=-1077.0 z=-50.628886859375
- **ROBUST_OUTLIER** `margin` value=3.632e+04 d1=0.0 d12=-1077.0 z=-50.628886859375
- **ROBUST_OUTLIER** `ind_demand` value=-1.266e+04 d1=0.0 d12=-195.0 z=-22.065450392857144
- **PERSISTENT_UP** `residual_proxy` value=864 d1=1249.0 d12=1249.0 z=4.691355458598727
- **ACCELERATION** `residual_proxy` value=864 d1=1249.0 d12=1249.0 z=4.691355458598727
- **ROBUST_OUTLIER** `residual_proxy` value=864 d1=1249.0 d12=1249.0 z=4.691355458598727
- **CHANGE_POINT** `ps_gen` value=228 d1=0.0 d12=6.0 z=1.7536733500000001
- **REVERSAL** `thermal_base` value=1.16e+04 d1=24.0 d12=-264.0 z=2.8100138188787187
- **REVERSAL** `ccgt_gen` value=8272 d1=23.0 d12=-260.0 z=2.798794295350957
- **CHANGE_POINT** `ind_generation` value=2.644e+04 d1=0.0 d12=2.0 z=0.6825674715568862
- **CHANGE_POINT** `imbalance` value=6872 d1=0.0 d12=-442.0 z=-0.5207200660621761
- **PERSISTENT_UP** `interconnector_net` value=9787 d1=0.0 d12=6175.0 z=2.4374524797904193
- **PERSISTENT_DOWN** `wind_gen` value=7641 d1=-154.0 d12=-224.0 z=-1.9179540121631737
- **ACCELERATION** `wind_gen` value=7641 d1=-154.0 d12=-224.0 z=-1.9179540121631737
- **PERSISTENT_UP** `ps_gen` value=228 d1=0.0 d12=6.0 z=1.7536733500000001

## Nearest historical live analogues

- `2026-09-16T06:54:08.413156Z` distance=1.127 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -1077.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:22:04.416358Z` distance=1.499 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -157.0}
- `2026-09-16T05:26:14.079375Z` distance=1.499 → {'next30m_imbalance_delta': 41.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -157.0}
- `2026-09-16T05:30:25.684923Z` distance=1.499 → {'next30m_imbalance_delta': 41.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -157.0}
- `2026-09-16T06:49:55.430272Z` distance=1.518 → {'next30m_imbalance_delta': 124.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
