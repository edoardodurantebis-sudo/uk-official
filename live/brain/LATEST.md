# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-22T22:06:53.543524Z`  
Memory snapshots: **2500**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `thermal_base` value=1.591e+04 d1=-464.0 d12=-1883.0 z=-5.617158469521045
- **CHANGE_POINT** `ccgt_gen` value=1.216e+04 d1=-468.0 d12=-1898.0 z=-5.603901871037464
- **CHANGE_POINT** `nuclear_gen` value=3746 d1=4.0 d12=15.0 z=4.0469385
- **PERSISTENT_DOWN** `thermal_base` value=1.591e+04 d1=-464.0 d12=-1883.0 z=-5.617158469521045
- **ROBUST_OUTLIER** `thermal_base` value=1.591e+04 d1=-464.0 d12=-1883.0 z=-5.617158469521045
- **PERSISTENT_DOWN** `ccgt_gen` value=1.216e+04 d1=-468.0 d12=-1898.0 z=-5.603901871037464
- **ROBUST_OUTLIER** `ccgt_gen` value=1.216e+04 d1=-468.0 d12=-1898.0 z=-5.603901871037464
- **CHANGE_POINT** `ps_gen` value=143 d1=0.0 d12=-1.0 z=-2.4510271593220336
- **CHANGE_POINT** `interconnector_net` value=5002 d1=242.0 d12=-679.0 z=-2.4126558579799107
- **PERSISTENT_UP** `nuclear_gen` value=3746 d1=4.0 d12=15.0 z=4.0469385
- **ROBUST_OUTLIER** `nuclear_gen` value=3746 d1=4.0 d12=15.0 z=4.0469385
- **CHANGE_POINT** `wind_gen` value=2500 d1=36.0 d12=192.0 z=1.6246759136500755
- **CHANGE_POINT** `ind_generation` value=1.312e+04 d1=0.0 d12=-13.0 z=-1.2625064551282053
- **CHANGE_POINT** `imbalance` value=-8054 d1=0.0 d12=-13.0 z=-1.21408155
- **REVERSAL** `interconnector_net` value=5002 d1=242.0 d12=-679.0 z=-2.4126558579799107

## Nearest historical live analogues

- `2026-09-22T20:50:58.019212Z` distance=0.001 → {'next30m_imbalance_delta': -3.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:55:13.117327Z` distance=0.002 → {'next30m_imbalance_delta': 0.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T20:59:27.826421Z` distance=0.002 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:03:40.476515Z` distance=0.002 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-22T21:07:51.999414Z` distance=0.002 → {'next30m_imbalance_delta': 22.0, 'next30m_mid_price_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
