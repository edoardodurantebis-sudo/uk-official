# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T19:50:48.272398Z`  
Memory snapshots: **2273**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=3012 d1=-2.0 d12=42.0 z=3.174069411764706
- **CHANGE_POINT** `ind_generation` value=1.866e+04 d1=0.0 d12=290.0 z=3.104712360687023
- **CHANGE_POINT** `imbalance` value=-2794 d1=0.0 d12=290.0 z=2.926023879496403
- **ROBUST_OUTLIER** `ind_demand` value=-1.226e+04 d1=0.0 d12=18.0 z=4.0469385
- **ROBUST_OUTLIER** `margin` value=3.609e+04 d1=0.0 d12=-45.0 z=-3.437721951612903
- **REVERSAL** `biomass_gen` value=3012 d1=-2.0 d12=42.0 z=3.174069411764706
- **ROBUST_OUTLIER** `biomass_gen` value=3012 d1=-2.0 d12=42.0 z=3.174069411764706
- **ROBUST_OUTLIER** `ind_generation` value=1.866e+04 d1=0.0 d12=290.0 z=3.104712360687023
- **CHANGE_POINT** `interconnector_net` value=9504 d1=-1.0 d12=2342.0 z=-0.37152745094562645
- **CHANGE_POINT** `thermal_base` value=1.656e+04 d1=96.0 d12=-512.0 z=0.18318432509386734
- **CHANGE_POINT** `ccgt_gen` value=1.305e+04 d1=96.0 d12=-509.0 z=0.1823557510495382
- **REVERSAL** `interconnector_net` value=9504 d1=-1.0 d12=2342.0 z=-0.37152745094562645
- **REVERSAL** `thermal_base` value=1.656e+04 d1=96.0 d12=-512.0 z=0.18318432509386734
- **REVERSAL** `ccgt_gen` value=1.305e+04 d1=96.0 d12=-509.0 z=0.1823557510495382
- **PERSISTENT_DOWN** `nuclear_gen` value=3507 d1=0.0 d12=-3.0 z=0.0

## Nearest historical live analogues

- `2026-09-21T18:51:48.360935Z` distance=0.032 → {'next30m_imbalance_delta': 40.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T18:56:00.829155Z` distance=0.032 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -45.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:21:51.078919Z` distance=0.046 → {'next30m_imbalance_delta': 8.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:26:03.425273Z` distance=0.047 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T17:30:18.299231Z` distance=0.047 → {'next30m_imbalance_delta': -24.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
