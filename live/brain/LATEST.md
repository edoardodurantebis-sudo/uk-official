# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T03:24:09.323258Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

Regime read: margin high, frequency stress.

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-10 d1=1.0 d12=-147.0 z=-105.89489075
- **REVERSAL** `ps_gen` value=-10 d1=1.0 d12=-147.0 z=-105.89489075
- **ROBUST_OUTLIER** `ps_gen` value=-10 d1=1.0 d12=-147.0 z=-105.89489075
- **CHANGE_POINT** `margin` value=3.857e+04 d1=0.0 d12=-91.0 z=90.51652444999999
- **PERSISTENT_DOWN** `margin` value=3.857e+04 d1=0.0 d12=-91.0 z=90.51652444999999
- **ACCELERATION** `margin` value=3.857e+04 d1=0.0 d12=-91.0 z=90.51652444999999
- **ROBUST_OUTLIER** `margin` value=3.857e+04 d1=0.0 d12=-91.0 z=90.51652444999999
- **PERSISTENT_UP** `ind_demand` value=-1.242e+04 d1=4.0 d12=5.0 z=4.6464849444444445
- **ACCELERATION** `ind_demand` value=-1.242e+04 d1=4.0 d12=5.0 z=4.6464849444444445
- **ROBUST_OUTLIER** `ind_demand` value=-1.242e+04 d1=4.0 d12=5.0 z=4.6464849444444445
- **REVERSAL** `biomass_gen` value=2871 d1=-10.0 d12=4.0 z=-4.384183375
- **ACCELERATION** `biomass_gen` value=2871 d1=-10.0 d12=4.0 z=-4.384183375
- **ROBUST_OUTLIER** `biomass_gen` value=2871 d1=-10.0 d12=4.0 z=-4.384183375
- **CHANGE_POINT** `wind_gen` value=6155 d1=315.0 d12=852.0 z=1.3822412158018866
- **REVERSAL** `interconnector_net` value=-2242 d1=2.0 d12=-1738.0 z=-2.509872488442285

## Nearest historical live analogues

- `2026-09-23T02:25:13.002873Z` distance=0.051 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T02:29:24.337782Z` distance=0.051 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 20.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-23T02:21:01.680995Z` distance=0.055 → {'next30m_imbalance_delta': 3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T06:53:31.262818Z` distance=0.677 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T06:57:43.435702Z` distance=0.677 → {'next30m_imbalance_delta': -691.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
