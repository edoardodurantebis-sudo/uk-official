# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-21T20:41:31.558862Z`  
Memory snapshots: **2285**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `nuclear_gen` value=3563 d1=6.0 d12=56.0 z=7.5542852
- **PERSISTENT_UP** `nuclear_gen` value=3563 d1=6.0 d12=56.0 z=7.5542852
- **ROBUST_OUTLIER** `nuclear_gen` value=3563 d1=6.0 d12=56.0 z=7.5542852
- **CHANGE_POINT** `imbalance` value=-2707 d1=0.0 d12=87.0 z=4.734154471698114
- **CHANGE_POINT** `ind_generation` value=1.875e+04 d1=0.0 d12=87.0 z=4.734154471698114
- **ROBUST_OUTLIER** `ind_demand` value=-1.226e+04 d1=0.0 d12=4.0 z=4.9462581666666665
- **ROBUST_OUTLIER** `imbalance` value=-2707 d1=0.0 d12=87.0 z=4.734154471698114
- **ROBUST_OUTLIER** `ind_generation` value=1.875e+04 d1=0.0 d12=87.0 z=4.734154471698114
- **PERSISTENT_UP** `biomass_gen` value=3015 d1=0.0 d12=3.0 z=2.21232638
- **CHANGE_POINT** `ps_gen` value=289 d1=57.0 d12=-237.0 z=-0.21231261937901497
- **REVERSAL** `interconnector_net` value=8123 d1=25.0 d12=-1381.0 z=-0.6406377377964937
- **PERSISTENT_DOWN** `wind_gen` value=3422 d1=-92.0 d12=-207.0 z=-0.5153404831460674
- **REVERSAL** `ccgt_gen` value=1.277e+04 d1=78.0 d12=-280.0 z=-0.24232495985099337
- **REVERSAL** `ps_gen` value=289 d1=57.0 d12=-237.0 z=-0.21231261937901497
- **REVERSAL** `thermal_base` value=1.634e+04 d1=84.0 d12=-224.0 z=-0.19303578703703703

## Nearest historical live analogues

- `2026-09-21T19:33:55.455548Z` distance=0.005 → {'next30m_imbalance_delta': 15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -48.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:38:10.834672Z` distance=0.005 → {'next30m_imbalance_delta': 15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -48.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:42:26.244827Z` distance=0.005 → {'next30m_imbalance_delta': 15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -48.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:46:37.622492Z` distance=0.005 → {'next30m_imbalance_delta': 15.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -48.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T19:25:28.829877Z` distance=0.005 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
