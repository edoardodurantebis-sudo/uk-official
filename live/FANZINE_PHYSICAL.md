# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T12:20:45.899584Z  
Source heartbeat: 2026-09-22T12:20:45.067431Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20658.0 | 0.0 | 0.0 | 0.0 | CHANGE_POINT |
| TS demand forecast | 21158.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13007.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| Wind generation | 2816.0 | -56.0 | -1071.0 | 68.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Residual-load proxy | 7651.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 37065.0 | 33.0 | 33.0 | 33.0 | PERSISTENT_UP, ACCELERATION, CHANGE_POINT |
| Indicated imbalance | -7049.0 | 0.0 | -825.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 10958.0 | 25.0 | 23.0 | -1.0 | PERSISTENT_UP |
| CCGT generation | 8509.0 | 39.0 | 241.0 | -108.0 | PERSISTENT_UP, ACCELERATION |
| Nuclear generation | 3730.0 | 10.0 | 78.0 | -5.0 | PERSISTENT_UP, ROBUST_OUTLIER, CHANGE_POINT |
| Pumped-storage generation | -125.0 | 0.0 | 39.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 12239.0 | 49.0 | 319.0 | -113.0 | PERSISTENT_UP, ACCELERATION |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **nuclear_gen / CHANGE_POINT** — value=3730.0, Δ1=10.0, Δ12=78.0, accel=-5.0
- **nuclear_gen / PERSISTENT_UP** — value=3730.0, Δ1=10.0, Δ12=78.0, accel=-5.0
- **nuclear_gen / ROBUST_OUTLIER** — value=3730.0, Δ1=10.0, Δ12=78.0, accel=-5.0
- **ps_gen / CHANGE_POINT** — value=-125.0, Δ1=0.0, Δ12=39.0, accel=0.0
- **ps_gen / ROBUST_OUTLIER** — value=-125.0, Δ1=0.0, Δ12=39.0, accel=0.0
- **wind_forecast / ROBUST_OUTLIER** — value=13007.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **wind_gen / CHANGE_POINT** — value=2816.0, Δ1=-56.0, Δ12=-1071.0, accel=68.0
- **wind_gen / PERSISTENT_DOWN** — value=2816.0, Δ1=-56.0, Δ12=-1071.0, accel=68.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
