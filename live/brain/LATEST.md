# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-20T16:27:14.846183Z`  
Memory snapshots: **1885**  
Current physical regime: **LOOSE**

Regime read: residual low, margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2012 d1=7.0 d12=801.0 z=480.573946875
- **PERSISTENT_UP** `biomass_gen` value=2012 d1=7.0 d12=801.0 z=480.573946875
- **ROBUST_OUTLIER** `biomass_gen` value=2012 d1=7.0 d12=801.0 z=480.573946875
- **CHANGE_POINT** `ccgt_gen` value=4691 d1=238.0 d12=1474.0 z=71.74688643023255
- **PERSISTENT_UP** `ccgt_gen` value=4691 d1=238.0 d12=1474.0 z=71.74688643023255
- **ROBUST_OUTLIER** `ccgt_gen` value=4691 d1=238.0 d12=1474.0 z=71.74688643023255
- **CHANGE_POINT** `thermal_base` value=8024 d1=236.0 d12=1479.0 z=64.23109681770833
- **PERSISTENT_UP** `thermal_base` value=8024 d1=236.0 d12=1479.0 z=64.23109681770833
- **ROBUST_OUTLIER** `thermal_base` value=8024 d1=236.0 d12=1479.0 z=64.23109681770833
- **CHANGE_POINT** `imbalance` value=-5182 d1=-16.0 d12=-22.0 z=13.956749442307693
- **PERSISTENT_DOWN** `imbalance` value=-5182 d1=-16.0 d12=-22.0 z=13.956749442307693
- **ACCELERATION** `imbalance` value=-5182 d1=-16.0 d12=-22.0 z=13.956749442307693
- **ROBUST_OUTLIER** `imbalance` value=-5182 d1=-16.0 d12=-22.0 z=13.956749442307693
- **ROBUST_OUTLIER** `interconnector_net` value=1.012e+04 d1=2.0 d12=2176.0 z=6.083977629534961
- **PERSISTENT_UP** `ps_gen` value=241 d1=168.0 d12=275.0 z=5.67071012037037

## Nearest historical live analogues

- `2026-09-20T14:54:10.136499Z` distance=0.004 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T14:58:25.329493Z` distance=0.004 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:02:37.176302Z` distance=0.004 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:06:50.185709Z` distance=0.004 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-20T15:11:00.797261Z` distance=0.004 → {'next30m_imbalance_delta': -2.0, 'next30m_margin_delta': 14.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
