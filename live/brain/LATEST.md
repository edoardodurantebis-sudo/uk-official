# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T02:18:31.336271Z`  
Memory snapshots: **714**  
Current physical regime: **LOOSE**

Regime read: residual low.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2033 d1=2.0 d12=-933.0 z=-316.2007948
- **REVERSAL** `biomass_gen` value=2033 d1=2.0 d12=-933.0 z=-316.2007948
- **ROBUST_OUTLIER** `biomass_gen` value=2033 d1=2.0 d12=-933.0 z=-316.2007948
- **CHANGE_POINT** `ind_demand` value=-1.153e+04 d1=0.0 d12=120.0 z=31.835916200000003
- **ROBUST_OUTLIER** `ind_demand` value=-1.153e+04 d1=0.0 d12=120.0 z=31.835916200000003
- **ROBUST_OUTLIER** `residual_proxy` value=-1481 d1=0.0 d12=0.0 z=-10.40400439375
- **ROBUST_OUTLIER** `wind_forecast` value=2.01e+04 d1=0.0 d12=0.0 z=10.40400439375
- **CHANGE_POINT** `ccgt_gen` value=3817 d1=-166.0 d12=-472.0 z=-1.7789377426975943
- **CHANGE_POINT** `thermal_base` value=7129 d1=-167.0 d12=-480.0 z=-1.767436093260188
- **CHANGE_POINT** `ps_gen` value=-540 d1=-3.0 d12=-223.0 z=-0.9807272763033176
- **CHANGE_POINT** `margin` value=3.456e+04 d1=0.0 d12=69.0 z=0.6767157887788778
- **REVERSAL** `interconnector_net` value=-6579 d1=-24.0 d12=89.0 z=-2.6466037482573728
- **ACCELERATION** `interconnector_net` value=-6579 d1=-24.0 d12=89.0 z=-2.6466037482573728
- **PERSISTENT_DOWN** `ccgt_gen` value=3817 d1=-166.0 d12=-472.0 z=-1.7789377426975943
- **PERSISTENT_DOWN** `thermal_base` value=7129 d1=-167.0 d12=-480.0 z=-1.767436093260188

## Nearest historical live analogues

- `2026-09-17T01:24:02.525802Z` distance=0.265 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 69.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:54:40.714610Z` distance=0.481 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T00:58:51.888099Z` distance=0.481 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:03:09.320399Z` distance=0.481 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-17T01:07:19.944210Z` distance=0.481 → {'next30m_imbalance_delta': -10.0, 'next30m_margin_delta': -19.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
