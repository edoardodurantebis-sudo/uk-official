# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T07:10:48.323528Z`  
Memory snapshots: **479**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `imbalance` value=7314 d1=0.0 d12=124.0 z=11.502298536666666
- **CHANGE_POINT** `ind_generation` value=2.644e+04 d1=0.0 d12=124.0 z=11.502298536666666
- **ROBUST_OUTLIER** `imbalance` value=7314 d1=0.0 d12=124.0 z=11.502298536666666
- **ROBUST_OUTLIER** `ind_generation` value=2.644e+04 d1=0.0 d12=124.0 z=11.502298536666666
- **ROBUST_OUTLIER** `ind_demand` value=-1.247e+04 d1=0.0 d12=-249.0 z=-10.553780794117648
- **CHANGE_POINT** `margin` value=3.74e+04 d1=0.0 d12=-45.0 z=-5.2272955625
- **REVERSAL** `ccgt_gen` value=8321 d1=1.0 d12=-122.0 z=6.118628643655049
- **ROBUST_OUTLIER** `ccgt_gen` value=8321 d1=1.0 d12=-122.0 z=6.118628643655049
- **REVERSAL** `thermal_base` value=1.165e+04 d1=4.0 d12=-126.0 z=6.089610305160143
- **ROBUST_OUTLIER** `thermal_base` value=1.165e+04 d1=4.0 d12=-126.0 z=6.089610305160143
- **ROBUST_OUTLIER** `margin` value=3.74e+04 d1=0.0 d12=-45.0 z=-5.2272955625
- **CHANGE_POINT** `interconnector_net` value=6907 d1=806.0 d12=5984.0 z=1.7804080420574886
- **CHANGE_POINT** `ps_gen` value=222 d1=0.0 d12=4.0 z=0.4496598333333333
- **PERSISTENT_UP** `interconnector_net` value=6907 d1=806.0 d12=5984.0 z=1.7804080420574886
- **PERSISTENT_UP** `wind_gen` value=8103 d1=45.0 d12=340.0 z=-1.7667948229522186

## Nearest historical live analogues

- `2026-09-16T05:51:19.396641Z` distance=0.699 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:55:30.704372Z` distance=0.699 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -79.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:59:40.455597Z` distance=0.699 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -79.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:03:52.494424Z` distance=0.699 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -79.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T06:08:05.860458Z` distance=0.699 → {'next30m_imbalance_delta': -24.0, 'next30m_margin_delta': -79.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
