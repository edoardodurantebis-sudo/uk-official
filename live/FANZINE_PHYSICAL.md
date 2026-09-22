# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T12:29:10.837407Z  
Source heartbeat: 2026-09-22T12:29:09.664290Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20658.0 | 0.0 | 0.0 | 0.0 | CHANGE_POINT |
| TS demand forecast | 21158.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13007.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| Wind generation | 2750.0 | -66.0 | -979.0 | -66.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Residual-load proxy | 7651.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 37065.0 | 0.0 | 33.0 | 0.0 | PERSISTENT_UP, CHANGE_POINT |
| Indicated imbalance | -7075.0 | 0.0 | -851.0 | 26.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Interconnector net | 10983.0 | 25.0 | 37.0 | 25.0 | PERSISTENT_UP, ACCELERATION |
| CCGT generation | 8500.0 | -9.0 | 595.0 | -9.0 | REVERSAL |
| Nuclear generation | 3733.0 | 3.0 | 75.0 | 3.0 | PERSISTENT_UP, ROBUST_OUTLIER, CHANGE_POINT |
| Pumped-storage generation | -126.0 | -1.0 | -119.0 | -1.0 | PERSISTENT_DOWN, ROBUST_OUTLIER |
| Thermal base | 12233.0 | -6.0 | 670.0 | -6.0 | REVERSAL |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **nuclear_gen / CHANGE_POINT** — value=3733.0, Δ1=3.0, Δ12=75.0, accel=3.0
- **nuclear_gen / PERSISTENT_UP** — value=3733.0, Δ1=3.0, Δ12=75.0, accel=3.0
- **nuclear_gen / ROBUST_OUTLIER** — value=3733.0, Δ1=3.0, Δ12=75.0, accel=3.0
- **ps_gen / PERSISTENT_DOWN** — value=-126.0, Δ1=-1.0, Δ12=-119.0, accel=-1.0
- **ps_gen / ROBUST_OUTLIER** — value=-126.0, Δ1=-1.0, Δ12=-119.0, accel=-1.0
- **wind_gen / CHANGE_POINT** — value=2750.0, Δ1=-66.0, Δ12=-979.0, accel=-66.0
- **wind_forecast / ROBUST_OUTLIER** — value=13007.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **wind_gen / PERSISTENT_DOWN** — value=2750.0, Δ1=-66.0, Δ12=-979.0, accel=-66.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
