# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T03:28:22.295901Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `margin` value=3.857e+04 d1=0.0 d12=-91.0 z=90.51652444999999
- **PERSISTENT_DOWN** `margin` value=3.857e+04 d1=0.0 d12=-91.0 z=90.51652444999999
- **ROBUST_OUTLIER** `margin` value=3.857e+04 d1=0.0 d12=-91.0 z=90.51652444999999
- **CHANGE_POINT** `ps_gen` value=-9 d1=1.0 d12=-149.0 z=-69.92210408333334
- **REVERSAL** `ps_gen` value=-9 d1=1.0 d12=-149.0 z=-69.92210408333334
- **ROBUST_OUTLIER** `ps_gen` value=-9 d1=1.0 d12=-149.0 z=-69.92210408333334
- **PERSISTENT_UP** `ind_demand` value=-1.242e+04 d1=0.0 d12=5.0 z=4.6464849444444445
- **ACCELERATION** `ind_demand` value=-1.242e+04 d1=0.0 d12=5.0 z=4.6464849444444445
- **ROBUST_OUTLIER** `ind_demand` value=-1.242e+04 d1=0.0 d12=5.0 z=4.6464849444444445
- **REVERSAL** `biomass_gen` value=2875 d1=4.0 d12=-6.0 z=-3.934523541666667
- **ACCELERATION** `biomass_gen` value=2875 d1=4.0 d12=-6.0 z=-3.934523541666667
- **ROBUST_OUTLIER** `biomass_gen` value=2875 d1=4.0 d12=-6.0 z=-3.934523541666667
- **CHANGE_POINT** `wind_gen` value=6314 d1=159.0 d12=965.0 z=1.4764190087070093
- **REVERSAL** `interconnector_net` value=-2234 d1=8.0 d12=-1732.0 z=-2.470812613776862
- **PERSISTENT_UP** `wind_gen` value=6314 d1=159.0 d12=965.0 z=1.4764190087070093

## Nearest historical live analogues

- `2026-09-23T02:25:13.002873Z` distance=0.051 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T02:29:24.337782Z` distance=0.051 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T02:33:36.910814Z` distance=0.051 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T02:21:01.680995Z` distance=0.055 → {'next30m_imbalance_delta': 3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T06:53:31.262818Z` distance=0.676 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
