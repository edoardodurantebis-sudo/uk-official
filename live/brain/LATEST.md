# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-18T17:51:12.400587Z`  
Memory snapshots: **1248**  
Current physical regime: **TIGHT**

Regime read: residual high, margin low.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=5127 d1=-76.0 d12=2601.0 z=30.12339815677966
- **CHANGE_POINT** `thermal_base` value=8467 d1=-75.0 d12=2604.0 z=29.875928338235294
- **REVERSAL** `ccgt_gen` value=5127 d1=-76.0 d12=2601.0 z=30.12339815677966
- **ROBUST_OUTLIER** `ccgt_gen` value=5127 d1=-76.0 d12=2601.0 z=30.12339815677966
- **REVERSAL** `thermal_base` value=8467 d1=-75.0 d12=2604.0 z=29.875928338235294
- **ROBUST_OUTLIER** `thermal_base` value=8467 d1=-75.0 d12=2604.0 z=29.875928338235294
- **ROBUST_OUTLIER** `ind_demand` value=-1.077e+04 d1=0.0 d12=0.0 z=-14.8387745
- **CHANGE_POINT** `interconnector_net` value=-1542 d1=1.0 d12=-6626.0 z=-11.98820013394018
- **REVERSAL** `interconnector_net` value=-1542 d1=1.0 d12=-6626.0 z=-11.98820013394018
- **ROBUST_OUTLIER** `interconnector_net` value=-1542 d1=1.0 d12=-6626.0 z=-11.98820013394018
- **CHANGE_POINT** `ps_gen` value=678 d1=0.0 d12=1124.0 z=8.964519381377551
- **PERSISTENT_UP** `ps_gen` value=678 d1=0.0 d12=1124.0 z=8.964519381377551
- **ROBUST_OUTLIER** `ps_gen` value=678 d1=0.0 d12=1124.0 z=8.964519381377551
- **CHANGE_POINT** `biomass_gen` value=1706 d1=-23.0 d12=225.0 z=4.982793028125
- **ROBUST_OUTLIER** `wind_forecast` value=6802 d1=0.0 d12=0.0 z=-6.528097223214285

## Nearest historical live analogues

- `2026-09-18T14:21:00.093276Z` distance=0.225 → {'next30m_imbalance_delta': -378.0, 'next30m_margin_delta': 104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T12:57:04.108111Z` distance=0.232 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:01:14.855580Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:05:25.405882Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-18T13:09:36.028376Z` distance=0.232 → {'next30m_imbalance_delta': -4.0, 'next30m_margin_delta': 70.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
