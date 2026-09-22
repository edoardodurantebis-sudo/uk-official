# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T12:16:30.294141Z  
Source heartbeat: 2026-09-22T12:16:29.191265Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20658.0 | 0.0 | 0.0 | 0.0 | CHANGE_POINT |
| TS demand forecast | 21158.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13007.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| Wind generation | 2872.0 | -124.0 | -1020.0 | 153.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Residual-load proxy | 7651.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 37032.0 | 0.0 | 0.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -7049.0 | 0.0 | -825.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 10933.0 | 26.0 | -3.0 | 31.0 | REVERSAL, ACCELERATION |
| CCGT generation | 8470.0 | 147.0 | -5.0 | -131.0 | REVERSAL, ACCELERATION |
| Nuclear generation | 3720.0 | 15.0 | 73.0 | 17.0 | PERSISTENT_UP, ROBUST_OUTLIER, CHANGE_POINT |
| Pumped-storage generation | -125.0 | 0.0 | 39.0 | 89.0 | ACCELERATION, ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 12190.0 | 162.0 | 68.0 | -114.0 | PERSISTENT_UP, ACCELERATION |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **nuclear_gen / CHANGE_POINT** — value=3720.0, Δ1=15.0, Δ12=73.0, accel=17.0
- **nuclear_gen / PERSISTENT_UP** — value=3720.0, Δ1=15.0, Δ12=73.0, accel=17.0
- **nuclear_gen / ROBUST_OUTLIER** — value=3720.0, Δ1=15.0, Δ12=73.0, accel=17.0
- **ps_gen / CHANGE_POINT** — value=-125.0, Δ1=0.0, Δ12=39.0, accel=89.0
- **ps_gen / ACCELERATION** — value=-125.0, Δ1=0.0, Δ12=39.0, accel=89.0
- **ps_gen / ROBUST_OUTLIER** — value=-125.0, Δ1=0.0, Δ12=39.0, accel=89.0
- **wind_forecast / ROBUST_OUTLIER** — value=13007.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **wind_gen / CHANGE_POINT** — value=2872.0, Δ1=-124.0, Δ12=-1020.0, accel=153.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
