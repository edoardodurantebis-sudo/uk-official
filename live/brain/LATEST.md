# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-19T23:07:08.414288Z`  
Memory snapshots: **1639**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **CHANGE_POINT** `ps_gen` value=-133 d1=1.0 d12=-125.0 z=-86.0648921
- **REVERSAL** `ps_gen` value=-133 d1=1.0 d12=-125.0 z=-86.0648921
- **ROBUST_OUTLIER** `ps_gen` value=-133 d1=1.0 d12=-125.0 z=-86.0648921
- **CHANGE_POINT** `thermal_base` value=6898 d1=157.0 d12=-1629.0 z=-3.3259561437757204
- **CHANGE_POINT** `ccgt_gen` value=3562 d1=155.0 d12=-1624.0 z=-3.3103791411042947
- **CHANGE_POINT** `margin` value=3.606e+04 d1=0.0 d12=-8.0 z=-1.9821739591836736
- **PERSISTENT_UP** `wind_gen` value=1.57e+04 d1=125.0 d12=652.0 z=3.4213429883828996
- **ROBUST_OUTLIER** `wind_gen` value=1.57e+04 d1=125.0 d12=652.0 z=3.4213429883828996
- **REVERSAL** `thermal_base` value=6898 d1=157.0 d12=-1629.0 z=-3.3259561437757204
- **ROBUST_OUTLIER** `thermal_base` value=6898 d1=157.0 d12=-1629.0 z=-3.3259561437757204
- **REVERSAL** `ccgt_gen` value=3562 d1=155.0 d12=-1624.0 z=-3.3103791411042947
- **ROBUST_OUTLIER** `ccgt_gen` value=3562 d1=155.0 d12=-1624.0 z=-3.3103791411042947
- **CHANGE_POINT** `imbalance` value=-3939 d1=0.0 d12=-46.0 z=-0.8977021852517986
- **CHANGE_POINT** `ind_generation` value=1.601e+04 d1=0.0 d12=-46.0 z=-0.8977021852517986
- **PERSISTENT_DOWN** `interconnector_net` value=-8031 d1=-399.0 d12=-909.0 z=-1.7411178493008521

## Nearest historical live analogues

- `2026-09-19T21:22:12.336443Z` distance=0.013 → {'next30m_imbalance_delta': -48.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:26:23.241124Z` distance=0.013 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:30:37.100220Z` distance=0.013 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:34:48.991316Z` distance=0.013 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-19T21:38:58.734712Z` distance=0.013 → {'next30m_imbalance_delta': 6.0, 'next30m_margin_delta': 5.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
