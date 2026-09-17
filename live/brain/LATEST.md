# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T02:14:21.637424Z`  
Memory snapshots: **713**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2031 d1=9.0 d12=-958.0 z=-316.7403866
- **REVERSAL** `biomass_gen` value=2031 d1=9.0 d12=-958.0 z=-316.7403866
- **ROBUST_OUTLIER** `biomass_gen` value=2031 d1=9.0 d12=-958.0 z=-316.7403866
- **CHANGE_POINT** `ind_demand` value=-1.153e+04 d1=0.0 d12=120.0 z=31.835916200000003
- **ROBUST_OUTLIER** `ind_demand` value=-1.153e+04 d1=0.0 d12=120.0 z=31.835916200000003
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `ccgt_gen` value=3983 d1=-106.0 d12=-460.0 z=-1.7977061525348355
- **CHANGE_POINT** `thermal_base` value=7296 d1=-107.0 d12=-467.0 z=-1.785437458616111
- **CHANGE_POINT** `ps_gen` value=-537 d1=44.0 d12=-222.0 z=-0.9781699691943128
- **CHANGE_POINT** `margin` value=3.456e+04 d1=0.0 d12=69.0 z=0.7832784193548387
- **PERSISTENT_UP** `interconnector_net` value=-6555 d1=29.0 d12=114.0 z=-2.7178187018562543
- **PERSISTENT_DOWN** `ccgt_gen` value=3983 d1=-106.0 d12=-460.0 z=-1.7977061525348355
- **PERSISTENT_DOWN** `thermal_base` value=7296 d1=-107.0 d12=-467.0 z=-1.785437458616111
- **PERSISTENT_UP** `wind_gen` value=1.352e+04 d1=29.0 d12=757.0 z=1.2873325873655914

## Nearest historical live analogues

- `2026-09-17T00:54:40.714610Z` distance=0.482 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:58:51.888099Z` distance=0.482 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:03:09.320399Z` distance=0.482 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:07:19.944210Z` distance=0.482 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:11:31.123687Z` distance=0.482 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
