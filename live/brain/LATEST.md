# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T12:10:42.110075Z`  
Memory snapshots: **2165**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ps_gen` value=228 d1=66.0 d12=237.0 z=39.79489525
- **PERSISTENT_UP** `ps_gen` value=228 d1=66.0 d12=237.0 z=39.79489525
- **ROBUST_OUTLIER** `ps_gen` value=228 d1=66.0 d12=237.0 z=39.79489525
- **CHANGE_POINT** `ind_demand` value=-1.224e+04 d1=0.0 d12=2.0 z=14.786890673076924
- **ROBUST_OUTLIER** `ind_demand` value=-1.224e+04 d1=0.0 d12=2.0 z=14.786890673076924
- **CHANGE_POINT** `margin` value=3.667e+04 d1=0.0 d12=178.0 z=-1.515158134057971
- **ACCELERATION** `ccgt_gen` value=6648 d1=-9.0 d12=-74.0 z=-3.10806787987013
- **ROBUST_OUTLIER** `ccgt_gen` value=6648 d1=-9.0 d12=-74.0 z=-3.10806787987013
- **CHANGE_POINT** `residual_proxy` value=1.208e+04 d1=0.0 d12=-104.0 z=1.0682912189440994
- **ACCELERATION** `thermal_base` value=1.016e+04 d1=-5.0 d12=-77.0 z=-2.8443598759689923
- **CHANGE_POINT** `wind_gen` value=3724 d1=49.0 d12=403.0 z=0.5101543236228814
- **REVERSAL** `nuclear_gen` value=3513 d1=4.0 d12=-3.0 z=2.29326515
- **ACCELERATION** `nuclear_gen` value=3513 d1=4.0 d12=-3.0 z=2.29326515
- **CHANGE_POINT** `biomass_gen` value=3013 d1=0.0 d12=-2.0 z=-0.11241495833333331
- **CHANGE_POINT** `demand_forecast` value=2.1e+04 d1=0.0 d12=-104.0 z=None

## Nearest historical live analogues

- `2026-09-21T10:54:44.355248Z` distance=0.079 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:58:55.909932Z` distance=0.079 → {'next30m_imbalance_delta': 856.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T11:03:12.814990Z` distance=0.079 → {'next30m_imbalance_delta': 856.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T11:07:25.674417Z` distance=0.079 → {'next30m_imbalance_delta': 856.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 182.0, 'next30m_residual_proxy_delta': -104.0}
- `2026-09-21T11:11:37.732087Z` distance=0.079 → {'next30m_imbalance_delta': 856.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 182.0, 'next30m_residual_proxy_delta': -104.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
