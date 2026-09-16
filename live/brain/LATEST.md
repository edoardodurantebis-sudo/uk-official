# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T06:33:09.371452Z`  
Memory snapshots: **470**  
Current physical regime: **TIGHT**

Regime read: margin low.

## Active patterns

- **ROBUST_OUTLIER** `imbalance` value=7190 d1=0.0 d12=17.0 z=11.707934018656717
- **ROBUST_OUTLIER** `ind_generation` value=2.631e+04 d1=0.0 d12=17.0 z=11.707934018656717
- **REVERSAL** `ccgt_gen` value=8438 d1=-6.0 d12=591.0 z=7.391639253955696
- **ROBUST_OUTLIER** `ccgt_gen` value=8438 d1=-6.0 d12=591.0 z=7.391639253955696
- **REVERSAL** `thermal_base` value=1.177e+04 d1=-2.0 d12=594.0 z=7.382467811052631
- **ROBUST_OUTLIER** `thermal_base` value=1.177e+04 d1=-2.0 d12=594.0 z=7.382467811052631
- **CHANGE_POINT** `margin` value=3.745e+04 d1=0.0 d12=-100.0 z=-3.330293140625
- **CHANGE_POINT** `wind_gen` value=7650 d1=-57.0 d12=-853.0 z=-2.89629905519802
- **ROBUST_OUTLIER** `margin` value=3.745e+04 d1=0.0 d12=-100.0 z=-3.330293140625
- **PERSISTENT_DOWN** `wind_gen` value=7650 d1=-57.0 d12=-853.0 z=-2.89629905519802
- **CHANGE_POINT** `interconnector_net` value=3586 d1=2682.0 d12=5394.0 z=0.4304989759350092
- **PERSISTENT_UP** `nuclear_gen` value=3333 d1=4.0 d12=3.0 z=1.3489795
- **ACCELERATION** `nuclear_gen` value=3333 d1=4.0 d12=3.0 z=1.3489795
- **PERSISTENT_UP** `interconnector_net` value=3586 d1=2682.0 d12=5394.0 z=0.4304989759350092
- **ACCELERATION** `interconnector_net` value=3586 d1=2682.0 d12=5394.0 z=0.4304989759350092

## Nearest historical live analogues

- `2026-09-16T05:34:36.913190Z` distance=0.060 → {'next30m_imbalance_delta': 41.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:38:46.661269Z` distance=0.060 → {'next30m_imbalance_delta': 41.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T05:22:04.416358Z` distance=0.289 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -157.0}
- `2026-09-16T05:26:14.079375Z` distance=0.289 → {'next30m_imbalance_delta': 41.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -157.0}
- `2026-09-16T05:30:25.684923Z` distance=0.289 → {'next30m_imbalance_delta': 41.0, 'next30m_margin_delta': -21.0, 'next30m_residual_proxy_delta': -157.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
