# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-23T10:39:20.220249Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high, wind rising.

## Active patterns

- **CHANGE_POINT** `ind_demand` value=-1.374e+04 d1=0.0 d12=-1055.0 z=-59.26516603333334
- **ROBUST_OUTLIER** `ind_demand` value=-1.374e+04 d1=0.0 d12=-1055.0 z=-59.26516603333334
- **ROBUST_OUTLIER** `ind_generation` value=1.873e+04 d1=0.0 d12=2815.0 z=8.232025503012048
- **CHANGE_POINT** `margin` value=4.078e+04 d1=0.0 d12=57.0 z=5.957497571585903
- **ROBUST_OUTLIER** `imbalance` value=-2300 d1=0.0 d12=2815.0 z=7.6274902144420125
- **ROBUST_OUTLIER** `margin` value=4.078e+04 d1=0.0 d12=57.0 z=5.957497571585903
- **CHANGE_POINT** `ps_gen` value=-861 d1=9.0 d12=-292.0 z=-3.5358344658385095
- **REVERSAL** `ps_gen` value=-861 d1=9.0 d12=-292.0 z=-3.5358344658385095
- **ROBUST_OUTLIER** `ps_gen` value=-861 d1=9.0 d12=-292.0 z=-3.5358344658385095
- **CHANGE_POINT** `nuclear_gen` value=3797 d1=-8.0 d12=186.0 z=-1.3489794999999998
- **REVERSAL** `thermal_base` value=5931 d1=6.0 d12=-144.0 z=-2.4075792166212535
- **REVERSAL** `ccgt_gen` value=2134 d1=14.0 d12=-330.0 z=-2.402818883217732
- **PERSISTENT_DOWN** `residual_proxy` value=1.31e+04 d1=0.0 d12=-182.0 z=-1.497038225609756
- **REVERSAL** `interconnector_net` value=1.147e+04 d1=-15.0 d12=98.0 z=1.4535328932912124
- **REVERSAL** `nuclear_gen` value=3797 d1=-8.0 d12=186.0 z=-1.3489794999999998

## Nearest historical live analogues

- `2026-09-22T10:20:52.187902Z` distance=0.962 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -614.0}
- `2026-09-22T10:25:04.719488Z` distance=0.962 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': -127.0}
- `2026-09-22T10:29:21.446166Z` distance=0.962 → {'next30m_imbalance_delta': -11397.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3381.0, 'next30m_residual_proxy_delta': -127.0}
- `2026-09-22T10:50:36.865474Z` distance=1.006 → {'next30m_imbalance_delta': -11397.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -3381.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-21T10:33:45.224867Z` distance=1.009 → {'next30m_imbalance_delta': -7439.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': -4517.0, 'next30m_residual_proxy_delta': 1108.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
