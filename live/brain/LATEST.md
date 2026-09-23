# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T00:29:55.135999Z`  
Memory snapshots: **2500**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `wind_gen` value=4143 d1=73.0 d12=961.0 z=2.2482991666666665
- **CHANGE_POINT** `interconnector_net` value=3201 d1=-1.0 d12=-971.0 z=-2.057080187037037
- **ROBUST_OUTLIER** `ind_demand` value=-1.248e+04 d1=0.0 d12=0.0 z=-4.0469384999999996
- **REVERSAL** `thermal_base` value=1.374e+04 d1=-24.0 d12=203.0 z=-3.679035
- **ROBUST_OUTLIER** `thermal_base` value=1.374e+04 d1=-24.0 d12=203.0 z=-3.679035
- **REVERSAL** `ccgt_gen` value=1e+04 d1=-23.0 d12=209.0 z=-3.6435240614997038
- **ROBUST_OUTLIER** `ccgt_gen` value=1e+04 d1=-23.0 d12=209.0 z=-3.6435240614997038
- **CHANGE_POINT** `imbalance` value=-8007 d1=0.0 d12=42.0 z=1.1506001617647057
- **CHANGE_POINT** `ind_generation` value=1.317e+04 d1=0.0 d12=42.0 z=1.1506001617647057
- **PERSISTENT_UP** `wind_gen` value=4143 d1=73.0 d12=961.0 z=2.2482991666666665
- **PERSISTENT_DOWN** `interconnector_net` value=3201 d1=-1.0 d12=-971.0 z=-2.057080187037037
- **PERSISTENT_UP** `margin` value=3.723e+04 d1=0.0 d12=1.0 z=0.7082142375
- **PERSISTENT_DOWN** `biomass_gen` value=2905 d1=-1.0 d12=-12.0 z=-0.17749730263157895
- **PERSISTENT_DOWN** `nuclear_gen` value=3734 d1=-1.0 d12=-6.0 z=-0.1686224375

## Nearest historical live analogues

- `2026-09-22T23:31:03.889259Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:35:16.889434Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T23:22:42.187473Z` distance=0.464 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -158.0}
- `2026-09-22T23:26:53.201699Z` distance=0.464 → {'next30m_imbalance_delta': 51.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -10.0, 'next30m_residual_proxy_delta': -158.0}
- `2026-09-22T22:19:30.437012Z` distance=0.464 → {'next30m_imbalance_delta': 7.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
