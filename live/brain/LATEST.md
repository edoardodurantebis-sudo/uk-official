# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-14T23:48:58.458997Z`  
Memory snapshots: **32**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=4538.0 z=10.70986675954861
- **ROBUST_OUTLIER** `residual_proxy` value=1.208e+04 d1=0.0 d12=4538.0 z=10.70986675954861
- **CHANGE_POINT** `biomass_gen` value=2693 d1=3.0 d12=133.0 z=8.318706916666667
- **PERSISTENT_UP** `biomass_gen` value=2693 d1=3.0 d12=133.0 z=8.318706916666667
- **ROBUST_OUTLIER** `biomass_gen` value=2693 d1=3.0 d12=133.0 z=8.318706916666667
- **CHANGE_POINT** `imbalance` value=187 d1=0.0 d12=250.0 z=4.284993705882353
- **CHANGE_POINT** `ind_generation` value=2.067e+04 d1=0.0 d12=251.0 z=4.162565314285715
- **CHANGE_POINT** `interconnector_net` value=-955 d1=27.0 d12=3663.0 z=2.6634435330490405
- **ROBUST_OUTLIER** `imbalance` value=187 d1=0.0 d12=250.0 z=4.284993705882353
- **ROBUST_OUTLIER** `ind_generation` value=2.067e+04 d1=0.0 d12=251.0 z=4.162565314285715
- **PERSISTENT_UP** `interconnector_net` value=-955 d1=27.0 d12=3663.0 z=2.6634435330490405
- **PERSISTENT_DOWN** `wind_gen` value=1.213e+04 d1=-103.0 d12=-257.0 z=-1.0420688201058201
- **ACCELERATION** `wind_gen` value=1.213e+04 d1=-103.0 d12=-257.0 z=-1.0420688201058201
- **PERSISTENT_UP** `nuclear_gen` value=3314 d1=4.0 d12=2.0 z=0.0
- **ACCELERATION** `nuclear_gen` value=3314 d1=4.0 d12=2.0 z=0.0

## Nearest historical live analogues

- `2026-09-14T22:50:17.291209Z` distance=11.133 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -10.0}
- `2026-09-14T22:46:06.193811Z` distance=11.154 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': -10.0}
- `2026-09-14T20:16:04.225288Z` distance=11.230 → {'next30m_imbalance_delta': 262.0, 'next30m_margin_delta': 8.0, 'next30m_residual_proxy_delta': -517.0}
- `2026-09-14T22:41:53.412159Z` distance=11.245 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 5.0}
- `2026-09-14T22:37:42.328398Z` distance=11.547 → {'next30m_imbalance_delta': 21.0, 'next30m_margin_delta': 50.0, 'next30m_residual_proxy_delta': 147.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
