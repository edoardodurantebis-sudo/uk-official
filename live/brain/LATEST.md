# GB Alien Brain — live market memory

Engine: `GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0`  
Heartbeat: `2026-09-17T03:13:00.786961Z`  
Memory snapshots: **727**  
Current physical regime: **LOOSE**

Regime read: margin high.

## Active patterns

- **CHANGE_POINT** `biomass_gen` value=2034 d1=0.0 d12=1.0 z=-263.0510025
- **ACCELERATION** `biomass_gen` value=2034 d1=0.0 d12=1.0 z=-263.0510025
- **ROBUST_OUTLIER** `biomass_gen` value=2034 d1=0.0 d12=1.0 z=-263.0510025
- **ROBUST_OUTLIER** `ind_demand` value=-1.152e+04 d1=0.0 d12=11.0 z=33.31979365
- **CHANGE_POINT** `margin` value=3.586e+04 d1=0.0 d12=11.0 z=11.652977001572328
- **ROBUST_OUTLIER** `margin` value=3.586e+04 d1=0.0 d12=11.0 z=11.652977001572328
- **CHANGE_POINT** `interconnector_net` value=-8270 d1=-443.0 d12=-1691.0 z=-5.057285286008231
- **PERSISTENT_DOWN** `interconnector_net` value=-8270 d1=-443.0 d12=-1691.0 z=-5.057285286008231
- **ROBUST_OUTLIER** `interconnector_net` value=-8270 d1=-443.0 d12=-1691.0 z=-5.057285286008231
- **PERSISTENT_DOWN** `nuclear_gen` value=3308 d1=-4.0 d12=-7.0 z=-0.8993196666666666
- **ACCELERATION** `nuclear_gen` value=3308 d1=-4.0 d12=-7.0 z=-0.8993196666666666
- **PERSISTENT_DOWN** `thermal_base` value=6744 d1=-11.0 d12=-372.0 z=-0.8377990427031509
- **PERSISTENT_DOWN** `ccgt_gen` value=3436 d1=-7.0 d12=-365.0 z=-0.8352848860245359
- **REVERSAL** `wind_gen` value=1.332e+04 d1=43.0 d12=-195.0 z=0.7542867098428985
- **ACCELERATION** `ps_gen` value=-542 d1=-1.0 d12=-4.0 z=-0.67448975

## Nearest historical live analogues

- `2026-09-16T12:23:49.836209Z` distance=0.556 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T12:28:01.597273Z` distance=0.556 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 2.0, 'next30m_residual_proxy_delta': 199.0}
- `2026-09-16T11:54:04.473281Z` distance=0.563 → {'next30m_imbalance_delta': 0.0, 'next30m_margin_delta': 0.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T11:58:14.719154Z` distance=0.563 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}
- `2026-09-16T12:02:46.560952Z` distance=0.563 → {'next30m_imbalance_delta': 25.0, 'next30m_margin_delta': 29.0, 'next30m_residual_proxy_delta': 0.0}

Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.
