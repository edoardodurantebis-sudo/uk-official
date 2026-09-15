# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-15T10:27:51.997276Z`  
Memory snapshots: **184**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **ROBUST_OUTLIER** `ts_demand_forecast` value=2.057e+04 d1=0.0 d12=0.0 z=56.657139
- **CHANGE_POINT** `biomass_gen` value=1556 d1=-228.0 d12=-485.0 z=-37.657105703389824
- **PERSISTENT_DOWN** `biomass_gen` value=1556 d1=-228.0 d12=-485.0 z=-37.657105703389824
- **ROBUST_OUTLIER** `biomass_gen` value=1556 d1=-228.0 d12=-485.0 z=-37.657105703389824
- **CHANGE_POINT** `margin` value=3.449e+04 d1=0.0 d12=-9.0 z=4.485892146825397
- **ROBUST_OUTLIER** `margin` value=3.449e+04 d1=0.0 d12=-9.0 z=4.485892146825397
- **CHANGE_POINT** `ccgt_gen` value=1860 d1=7.0 d12=-626.0 z=-2.407553690972222
- **CHANGE_POINT** `thermal_base` value=5182 d1=2.0 d12=-634.0 z=-2.3901070269495412
- **CHANGE_POINT** `imbalance` value=-832 d1=0.0 d12=-740.0 z=-2.354228646634615
- **CHANGE_POINT** `ind_generation` value=1.974e+04 d1=0.0 d12=-740.0 z=-1.4859059906015037
- **ROBUST_OUTLIER** `ind_demand` value=-1.227e+04 d1=0.0 d12=-16.0 z=3.4688044285714286
- **REVERSAL** `ps_gen` value=-1205 d1=1.0 d12=-41.0 z=-3.047694425925926
- **ROBUST_OUTLIER** `ps_gen` value=-1205 d1=1.0 d12=-41.0 z=-3.047694425925926
- **REVERSAL** `ccgt_gen` value=1860 d1=7.0 d12=-626.0 z=-2.407553690972222
- **REVERSAL** `thermal_base` value=5182 d1=2.0 d12=-634.0 z=-2.3901070269495412

## Nearest historical live analogues

- `2026-09-15T09:23:16.973095Z` distance=0.131 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:27:29.987536Z` distance=0.131 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:33:16.363033Z` distance=0.131 → {'next30m_imbalance_delta': -273.0, 'next30m_margin_delta': -154.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T09:19:04.462321Z` distance=1.024 → {'next30m_imbalance_delta': 43.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-15T07:21:37.326101Z` distance=1.296 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -1211.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
