# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T17:50:43.122064Z`  
Memory snapshots: **935**  
Current physical regime: **TIGHT**

Regime read: residual high.

## Active patterns

- **CHANGE_POINT** `ind_generation` value=2.648e+04 d1=0.0 d12=-1933.0 z=-122.75713449999999
- **ROBUST_OUTLIER** `ind_generation` value=2.648e+04 d1=0.0 d12=-1933.0 z=-122.75713449999999
- **CHANGE_POINT** `imbalance` value=9664 d1=0.0 d12=-1933.0 z=-45.071785647058825
- **ROBUST_OUTLIER** `imbalance` value=9664 d1=0.0 d12=-1933.0 z=-45.071785647058825
- **CHANGE_POINT** `thermal_base` value=9754 d1=-8.0 d12=1294.0 z=3.078640031439854
- **CHANGE_POINT** `ccgt_gen` value=6435 d1=-9.0 d12=1295.0 z=3.067985879860267
- **ROBUST_OUTLIER** `residual_proxy` value=-2590 d1=0.0 d12=0.0 z=5.0514977021276595
- **CHANGE_POINT** `biomass_gen` value=2911 d1=92.0 d12=-212.0 z=1.2211607427113702
- **REVERSAL** `thermal_base` value=9754 d1=-8.0 d12=1294.0 z=3.078640031439854
- **ROBUST_OUTLIER** `thermal_base` value=9754 d1=-8.0 d12=1294.0 z=3.078640031439854
- **REVERSAL** `ccgt_gen` value=6435 d1=-9.0 d12=1295.0 z=3.067985879860267
- **ROBUST_OUTLIER** `ccgt_gen` value=6435 d1=-9.0 d12=1295.0 z=3.067985879860267
- **REVERSAL** `ps_gen` value=356 d1=1.0 d12=-23.0 z=2.775119563116371
- **CHANGE_POINT** `margin` value=3.658e+04 d1=0.0 d12=-6.0 z=0.3640551370292887
- **REVERSAL** `nuclear_gen` value=3319 d1=1.0 d12=-1.0 z=1.686224375

## Nearest historical live analogues

- `2026-09-17T16:55:22.028914Z` distance=0.004 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -6.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:51:11.529831Z` distance=0.006 → {'next30m_imbalance_delta': -25.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:34:16.300458Z` distance=0.062 → {'next30m_imbalance_delta': -25.0, 'next30m_margin_delta': -104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:38:28.589008Z` distance=0.062 → {'next30m_imbalance_delta': -25.0, 'next30m_margin_delta': -104.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T16:42:42.912542Z` distance=0.062 → {'next30m_imbalance_delta': -25.0, 'next30m_margin_delta': -104.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
