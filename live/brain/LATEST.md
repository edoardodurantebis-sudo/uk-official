# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T05:13:44.262069Z`  
Memory snapshots: **451**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=6304 d1=196.0 d12=2561.0 z=25.773049329192546
- **CHANGE_POINT** `thermal_base` value=9636 d1=199.0 d12=2570.0 z=25.172775033333334
- **PERSISTENT_UP** `ccgt_gen` value=6304 d1=196.0 d12=2561.0 z=25.773049329192546
- **ROBUST_OUTLIER** `ccgt_gen` value=6304 d1=196.0 d12=2561.0 z=25.773049329192546
- **PERSISTENT_UP** `thermal_base` value=9636 d1=199.0 d12=2570.0 z=25.172775033333334
- **ROBUST_OUTLIER** `thermal_base` value=9636 d1=199.0 d12=2570.0 z=25.172775033333334
- **CHANGE_POINT** `imbalance` value=7203 d1=0.0 d12=56.0 z=18.82296976744186
- **CHANGE_POINT** `ind_generation` value=2.632e+04 d1=0.0 d12=56.0 z=18.82296976744186
- **ROBUST_OUTLIER** `imbalance` value=7203 d1=0.0 d12=56.0 z=18.82296976744186
- **ROBUST_OUTLIER** `ind_generation` value=2.632e+04 d1=0.0 d12=56.0 z=18.82296976744186
- **PERSISTENT_DOWN** `interconnector_net` value=-1238 d1=-41.0 d12=-1670.0 z=-7.578904804265659
- **ROBUST_OUTLIER** `interconnector_net` value=-1238 d1=-41.0 d12=-1670.0 z=-7.578904804265659
- **CHANGE_POINT** `wind_gen` value=9370 d1=46.0 d12=-170.0 z=-1.3535678656462584
- **CHANGE_POINT** `ps_gen` value=221 d1=258.0 d12=-3.0 z=0.6570460495689655
- **CHANGE_POINT** `ind_demand` value=-1.218e+04 d1=0.0 d12=20.0 z=-0.18999711267605635

## Nearest historical live analogues

- `2026-09-16T03:53:53.579562Z` distance=0.058 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:58:05.004513Z` distance=0.058 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T04:02:15.050270Z` distance=0.058 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T04:06:27.964921Z` distance=0.058 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T04:10:40.377612Z` distance=0.058 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
