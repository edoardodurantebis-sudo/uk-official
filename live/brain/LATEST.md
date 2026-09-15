# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T00:39:11.597028Z`  
Memory snapshots: **44**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2993 d1=48.0 d12=300.0 z=10.142327351851852
- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=0.0 z=8.173017130666667
- **PERSISTENT_UP** `biomass_gen` value=2993 d1=48.0 d12=300.0 z=10.142327351851852
- **ROBUST_OUTLIER** `biomass_gen` value=2993 d1=48.0 d12=300.0 z=10.142327351851852
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=0.0 z=8.173017130666667
- **CHANGE_POINT** `wind_gen` value=1.19e+04 d1=63.0 d12=-232.0 z=-0.9877882433431953
- **CHANGE_POINT** `margin` value=3.27e+04 d1=0.0 d12=216.0 z=0.7987378618421054
- **CHANGE_POINT** `ind_demand` value=-1.227e+04 d1=0.0 d12=-1.0 z=-0.67448975
- **CHANGE_POINT** `ps_gen` value=-12 d1=0.0 d12=4.0 z=None
- **PERSISTENT_UP** `interconnector_net` value=264 d1=36.0 d12=1219.0 z=1.1693302014319809
- **REVERSAL** `wind_gen` value=1.19e+04 d1=63.0 d12=-232.0 z=-0.9877882433431953
- **REVERSAL** `nuclear_gen` value=3313 d1=2.0 d12=-1.0 z=-0.22482991666666666
- **ACCELERATION** `nuclear_gen` value=3313 d1=2.0 d12=-1.0 z=-0.22482991666666666
- **PERSISTENT_UP** `ps_gen` value=-12 d1=0.0 d12=4.0 z=None

## Nearest historical live analogues

- `2026-09-14T23:32:10.678260Z` distance=0.717 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:36:23.316269Z` distance=0.717 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:40:34.642541Z` distance=0.717 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-14T23:28:00.797408Z` distance=6.795 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 4389.0}
- `2026-09-14T23:23:50.457848Z` distance=6.899 → {'next30m_imbalance_delta': 23.0, 'next30m_margin_delta': 239.0, 'next30m_residual_proxy_delta': 4457.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
