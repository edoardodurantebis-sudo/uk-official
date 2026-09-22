# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T13:37:01.506033Z  
Source heartbeat: 2026-09-22T13:37:00.013905Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20658.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21158.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13082.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| Wind generation | 2280.0 | -8.0 | -269.0 | 39.0 | PERSISTENT_DOWN, ROBUST_OUTLIER |
| Residual-load proxy | 7576.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 37210.0 | 0.0 | 145.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -7101.0 | 0.0 | -26.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 10123.0 | 24.0 | -967.0 | 538.0 | REVERSAL, ACCELERATION, CHANGE_POINT |
| CCGT generation | 9258.0 | 164.0 | 925.0 | 145.0 | PERSISTENT_UP, CHANGE_POINT |
| Nuclear generation | 3732.0 | -6.0 | 10.0 | -8.0 | REVERSAL, ACCELERATION, ROBUST_OUTLIER |
| Pumped-storage generation | -9.0 | 5.0 | 117.0 | 13.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 12990.0 | 158.0 | 935.0 | 137.0 | PERSISTENT_UP, CHANGE_POINT |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ps_gen / CHANGE_POINT** — value=-9.0, Δ1=5.0, Δ12=117.0, accel=13.0
- **ps_gen / ROBUST_OUTLIER** — value=-9.0, Δ1=5.0, Δ12=117.0, accel=13.0
- **nuclear_gen / REVERSAL** — value=3732.0, Δ1=-6.0, Δ12=10.0, accel=-8.0
- **nuclear_gen / ACCELERATION** — value=3732.0, Δ1=-6.0, Δ12=10.0, accel=-8.0
- **nuclear_gen / ROBUST_OUTLIER** — value=3732.0, Δ1=-6.0, Δ12=10.0, accel=-8.0
- **wind_forecast / ROBUST_OUTLIER** — value=13082.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **wind_gen / PERSISTENT_DOWN** — value=2280.0, Δ1=-8.0, Δ12=-269.0, accel=39.0
- **wind_gen / ROBUST_OUTLIER** — value=2280.0, Δ1=-8.0, Δ12=-269.0, accel=39.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
