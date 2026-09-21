# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T20:37:18.070906Z`  
Memory snapshots: **2284**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `nuclear_gen` value=3557 d1=8.0 d12=50.0 z=6.7448975
- **PERSISTENT_UP** `nuclear_gen` value=3557 d1=8.0 d12=50.0 z=6.7448975
- **ROBUST_OUTLIER** `nuclear_gen` value=3557 d1=8.0 d12=50.0 z=6.7448975
- **ROBUST_OUTLIER** `ind_demand` value=-1.226e+04 d1=0.0 d12=4.0 z=4.9462581666666665
- **ROBUST_OUTLIER** `imbalance` value=-2707 d1=0.0 d12=87.0 z=4.734154471698114
- **ROBUST_OUTLIER** `ind_generation` value=1.875e+04 d1=0.0 d12=87.0 z=4.734154471698114
- **CHANGE_POINT** `ps_gen` value=232 d1=-21.0 d12=-294.0 z=-0.37696322216274086
- **PERSISTENT_UP** `biomass_gen` value=3015 d1=1.0 d12=1.0 z=2.3045066458333334
- **ACCELERATION** `biomass_gen` value=3015 d1=1.0 d12=1.0 z=2.3045066458333334
- **REVERSAL** `interconnector_net` value=8098 d1=12.0 d12=-1407.0 z=-0.6388469055873442
- **ACCELERATION** `interconnector_net` value=8098 d1=12.0 d12=-1407.0 z=-0.6388469055873442
- **PERSISTENT_DOWN** `ps_gen` value=232 d1=-21.0 d12=-294.0 z=-0.37696322216274086
- **PERSISTENT_DOWN** `ccgt_gen` value=1.269e+04 d1=-20.0 d12=-262.0 z=-0.32779979612850085
- **ACCELERATION** `ccgt_gen` value=1.269e+04 d1=-20.0 d12=-262.0 z=-0.32779979612850085
- **PERSISTENT_DOWN** `thermal_base` value=1.625e+04 d1=-12.0 d12=-212.0 z=-0.2864889573578595

## Nearest historical live analogues

- `2026-09-21T19:33:55.455548Z` distance=0.005 → {'next30m_imbalance_delta': 15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -48.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:38:10.834672Z` distance=0.005 → {'next30m_imbalance_delta': 15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -48.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:42:26.244827Z` distance=0.005 → {'next30m_imbalance_delta': 15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -48.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:25:28.829877Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1.0}
- `2026-09-21T19:29:43.204818Z` distance=0.005 → {'next30m_imbalance_delta': 15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -48.0, 'next30m_residual_proxy_delta': -1.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
