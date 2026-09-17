# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T18:49:35.533928Z`  
Memory snapshots: **949**  
Current physical regime: **BALANCED**

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.65e+04 d1=0.0 d12=10.0 z=-80.87745275
- **ROBUST_OUTLIER** `ind_generation` value=2.65e+04 d1=0.0 d12=10.0 z=-80.87745275
- **CHANGE_POINT** `imbalance` value=9682 d1=0.0 d12=10.0 z=-4.948336077171904
- **ROBUST_OUTLIER** `ind_demand` value=-1.125e+04 d1=0.0 d12=29.0 z=5.8455778333333335
- **ROBUST_OUTLIER** `imbalance` value=9682 d1=0.0 d12=10.0 z=-4.948336077171904
- **CHANGE_POINT** `thermal_base` value=1.041e+04 d1=-10.0 d12=656.0 z=2.372161078981723
- **CHANGE_POINT** `ccgt_gen` value=7087 d1=-5.0 d12=655.0 z=2.36600193662892
- **CHANGE_POINT** `interconnector_net` value=-468 d1=-25.0 d12=-1170.0 z=-1.657865146875
- **REVERSAL** `thermal_base` value=1.041e+04 d1=-10.0 d12=656.0 z=2.372161078981723
- **REVERSAL** `ccgt_gen` value=7087 d1=-5.0 d12=655.0 z=2.36600193662892
- **REVERSAL** `nuclear_gen` value=3319 d1=-5.0 d12=1.0 z=1.686224375
- **ACCELERATION** `nuclear_gen` value=3319 d1=-5.0 d12=1.0 z=1.686224375
- **PERSISTENT_DOWN** `interconnector_net` value=-468 d1=-25.0 d12=-1170.0 z=-1.657865146875
- **PERSISTENT_UP** `wind_gen` value=1.507e+04 d1=22.0 d12=443.0 z=1.1380693038793102
- **PERSISTENT_DOWN** `ps_gen` value=280 d1=-2.0 d12=-75.0 z=0.9203067691161867

## Nearest historical live analogues

- `2026-09-17T16:51:11.529831Z` distance=0.040 → {'next30m_imbalance_delta': -25.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T17:21:14.586656Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:55:22.028914Z` distance=0.043 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:59:33.030689Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T17:04:23.689660Z` distance=0.043 → {'next30m_imbalance_delta': -1933.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
