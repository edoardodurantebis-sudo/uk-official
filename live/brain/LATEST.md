# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-16T05:17:54.209175Z`  
Memory snapshots: **452**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `ccgt_gen` value=6551 d1=247.0 d12=2827.0 z=27.842601729813666
- **CHANGE_POINT** `thermal_base` value=9881 d1=245.0 d12=2829.0 z=27.00803233885542
- **PERSISTENT_UP** `ccgt_gen` value=6551 d1=247.0 d12=2827.0 z=27.842601729813666
- **ROBUST_OUTLIER** `ccgt_gen` value=6551 d1=247.0 d12=2827.0 z=27.842601729813666
- **PERSISTENT_UP** `thermal_base` value=9881 d1=245.0 d12=2829.0 z=27.00803233885542
- **ROBUST_OUTLIER** `thermal_base` value=9881 d1=245.0 d12=2829.0 z=27.00803233885542
- **CHANGE_POINT** `imbalance` value=7203 d1=0.0 d12=56.0 z=17.163611510638297
- **CHANGE_POINT** `ind_generation` value=2.632e+04 d1=0.0 d12=56.0 z=17.163611510638297
- **ROBUST_OUTLIER** `imbalance` value=7203 d1=0.0 d12=56.0 z=17.163611510638297
- **ROBUST_OUTLIER** `ind_generation` value=2.632e+04 d1=0.0 d12=56.0 z=17.163611510638297
- **REVERSAL** `interconnector_net` value=-1209 d1=29.0 d12=-1642.0 z=-7.536658146058315
- **ROBUST_OUTLIER** `interconnector_net` value=-1209 d1=29.0 d12=-1642.0 z=-7.536658146058315
- **CHANGE_POINT** `wind_gen` value=9149 d1=-221.0 d12=-492.0 z=-1.667870912414966
- **CHANGE_POINT** `ps_gen` value=223 d1=2.0 d12=1.0 z=0.6715571858695653
- **CHANGE_POINT** `ind_demand` value=-1.218e+04 d1=0.0 d12=20.0 z=0.0

## Nearest historical live analogues

- `2026-09-16T04:23:14.638799Z` distance=0.052 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:53:53.579562Z` distance=0.060 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T03:58:05.004513Z` distance=0.060 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T04:02:15.050270Z` distance=0.060 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T04:06:27.964921Z` distance=0.060 → {'next30m_imbalance_delta': 126.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
