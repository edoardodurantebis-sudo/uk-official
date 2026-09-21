# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T19:46:37.622492Z`  
Memory snapshots: **2272**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `margin` value=3.609e+04 d1=0.0 d12=-45.0 z=-4.202589980769231
- **CHANGE_POINT** `ind_generation` value=1.866e+04 d1=0.0 d12=290.0 z=3.83845985
- **CHANGE_POINT** `biomass_gen` value=3014 d1=-2.0 d12=44.0 z=3.3327728823529412
- **CHANGE_POINT** `imbalance` value=-2794 d1=0.0 d12=290.0 z=2.60636162654321
- **ROBUST_OUTLIER** `margin` value=3.609e+04 d1=0.0 d12=-45.0 z=-4.202589980769231
- **ROBUST_OUTLIER** `ind_demand` value=-1.226e+04 d1=0.0 d12=18.0 z=4.0469385
- **ROBUST_OUTLIER** `ind_generation` value=1.866e+04 d1=0.0 d12=290.0 z=3.83845985
- **REVERSAL** `biomass_gen` value=3014 d1=-2.0 d12=44.0 z=3.3327728823529412
- **ROBUST_OUTLIER** `biomass_gen` value=3014 d1=-2.0 d12=44.0 z=3.3327728823529412
- **CHANGE_POINT** `interconnector_net` value=9505 d1=0.0 d12=2343.0 z=-0.37099593814026793
- **CHANGE_POINT** `ccgt_gen` value=1.296e+04 d1=63.0 d12=-605.0 z=0.18473609405568098
- **CHANGE_POINT** `thermal_base` value=1.646e+04 d1=55.0 d12=-608.0 z=0.18454929441529236
- **REVERSAL** `ccgt_gen` value=1.296e+04 d1=63.0 d12=-605.0 z=0.18473609405568098
- **REVERSAL** `thermal_base` value=1.646e+04 d1=55.0 d12=-608.0 z=0.18454929441529236
- **ACCELERATION** `wind_gen` value=3639 d1=-8.0 d12=-23.0 z=0.1346203822016461

## Nearest historical live analogues

- `2026-09-21T18:51:48.360935Z` distance=0.031 → {'next30m_imbalance_delta': 40.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:21:51.078919Z` distance=0.045 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:26:03.425273Z` distance=0.046 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:30:18.299231Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:34:31.100527Z` distance=0.046 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
