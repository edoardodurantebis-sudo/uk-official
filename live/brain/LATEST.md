# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T04:50:38.818178Z`  
Memory snapshots: **104**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **REVERSAL** `ps_gen` value=-596 d1=8.0 d12=-277.0 z=-43.46711722222222
- **ROBUST_OUTLIER** `ps_gen` value=-596 d1=8.0 d12=-277.0 z=-43.46711722222222
- **CHANGE_POINT** `ind_generation` value=2.002e+04 d1=0.0 d12=-154.0 z=-12.194064690789473
- **CHANGE_POINT** `imbalance` value=-469 d1=0.0 d12=-154.0 z=-12.035700214285713
- **ROBUST_OUTLIER** `ind_generation` value=2.002e+04 d1=0.0 d12=-154.0 z=-12.194064690789473
- **ROBUST_OUTLIER** `imbalance` value=-469 d1=0.0 d12=-154.0 z=-12.035700214285713
- **CHANGE_POINT** `margin` value=3.406e+04 d1=-5.0 d12=-29.0 z=3.6552992903225805
- **CHANGE_POINT** `ind_demand` value=-1.244e+04 d1=0.0 d12=-28.0 z=-1.903559961111111
- **PERSISTENT_DOWN** `margin` value=3.406e+04 d1=-5.0 d12=-29.0 z=3.6552992903225805
- **ROBUST_OUTLIER** `margin` value=3.406e+04 d1=-5.0 d12=-29.0 z=3.6552992903225805
- **CHANGE_POINT** `interconnector_net` value=-7240 d1=-44.0 d12=243.0 z=-1.1944307084901484
- **REVERSAL** `wind_gen` value=1.344e+04 d1=43.0 d12=-512.0 z=2.210827513888889
- **CHANGE_POINT** `thermal_base` value=7037 d1=-75.0 d12=496.0 z=0.0715181087751371
- **CHANGE_POINT** `ccgt_gen` value=3706 d1=-68.0 d12=488.0 z=0.06142893897996357
- **REVERSAL** `interconnector_net` value=-7240 d1=-44.0 d12=243.0 z=-1.1944307084901484

## Nearest historical live analogues

- `2026-09-15T03:51:58.464857Z` distance=0.446 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:56:09.070441Z` distance=0.446 → {'next30m_imbalance_delta': -154.0, 'next30m_margin_delta': -24.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T03:22:39.940556Z` distance=0.470 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -8537.0}
- `2026-09-15T03:26:52.427763Z` distance=0.470 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': -8537.0}
- `2026-09-15T03:31:03.539054Z` distance=0.470 → {'next30m_imbalance_delta': -544.0, 'next30m_margin_delta': -16.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
