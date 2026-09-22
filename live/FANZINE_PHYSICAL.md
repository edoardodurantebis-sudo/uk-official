# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T12:12:12.090452Z  
Source heartbeat: 2026-09-22T12:12:10.835981Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20658.0 | 0.0 | 0.0 | 0.0 | CHANGE_POINT |
| TS demand forecast | 21158.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13007.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| Wind generation | 2996.0 | -277.0 | -896.0 | -232.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Residual-load proxy | 7651.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 37032.0 | 0.0 | 0.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -7049.0 | 0.0 | -819.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 10907.0 | -5.0 | -29.0 | 20.0 | PERSISTENT_DOWN, ACCELERATION |
| CCGT generation | 8323.0 | 278.0 | -152.0 | 100.0 | REVERSAL, ACCELERATION |
| Nuclear generation | 3705.0 | -2.0 | 58.0 | -4.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| Pumped-storage generation | -125.0 | -89.0 | 39.0 | -66.0 | REVERSAL, ACCELERATION, ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 12028.0 | 276.0 | -94.0 | 96.0 | REVERSAL, ACCELERATION |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **nuclear_gen / CHANGE_POINT** — value=3705.0, Δ1=-2.0, Δ12=58.0, accel=-4.0
- **nuclear_gen / REVERSAL** — value=3705.0, Δ1=-2.0, Δ12=58.0, accel=-4.0
- **nuclear_gen / ROBUST_OUTLIER** — value=3705.0, Δ1=-2.0, Δ12=58.0, accel=-4.0
- **ps_gen / CHANGE_POINT** — value=-125.0, Δ1=-89.0, Δ12=39.0, accel=-66.0
- **ps_gen / REVERSAL** — value=-125.0, Δ1=-89.0, Δ12=39.0, accel=-66.0
- **ps_gen / ACCELERATION** — value=-125.0, Δ1=-89.0, Δ12=39.0, accel=-66.0
- **ps_gen / ROBUST_OUTLIER** — value=-125.0, Δ1=-89.0, Δ12=39.0, accel=-66.0
- **wind_forecast / ROBUST_OUTLIER** — value=13007.0, Δ1=0.0, Δ12=0.0, accel=0.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
