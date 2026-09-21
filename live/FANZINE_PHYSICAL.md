# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T13:18:53.951114Z  
Source heartbeat: 2026-09-21T13:18:52.472401Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 21004.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| TS demand forecast | 21504.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 8616.0 | 0.0 | -307.0 | 0.0 |  |
| Wind generation | 4000.0 | 39.0 | 117.0 | 98.0 | ACCELERATION |
| Residual-load proxy | 12388.0 | 0.0 | 307.0 | 0.0 |  |
| Indicated margin | 36271.0 | 0.0 | -406.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -3248.0 | 0.0 | 85.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 11474.0 | 2.0 | 208.0 | -25.0 | PERSISTENT_UP, CHANGE_POINT |
| CCGT generation | 6132.0 | -12.0 | -159.0 | -33.0 |  |
| Nuclear generation | 3507.0 | -2.0 | -6.0 | -3.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | 264.0 | 6.0 | 36.0 | -24.0 | PERSISTENT_UP, ACCELERATION, ROBUST_OUTLIER |
| Thermal base | 9639.0 | -14.0 | -165.0 | -36.0 |  |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / ROBUST_OUTLIER** — value=-12240.0, Δ1=0.0, Δ12=-3.0, accel=0.0
- **ps_gen / PERSISTENT_UP** — value=264.0, Δ1=6.0, Δ12=36.0, accel=-24.0
- **ps_gen / ACCELERATION** — value=264.0, Δ1=6.0, Δ12=36.0, accel=-24.0
- **ps_gen / ROBUST_OUTLIER** — value=264.0, Δ1=6.0, Δ12=36.0, accel=-24.0
- **biomass_gen / CHANGE_POINT** — value=2938.0, Δ1=73.0, Δ12=-71.0, accel=68.0
- **demand_forecast / ROBUST_OUTLIER** — value=21004.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **biomass_gen / REVERSAL** — value=2938.0, Δ1=73.0, Δ12=-71.0, accel=68.0
- **biomass_gen / ACCELERATION** — value=2938.0, Δ1=73.0, Δ12=-71.0, accel=68.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
