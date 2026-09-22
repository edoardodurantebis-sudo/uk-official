# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T03:46:50.803370Z  
Source heartbeat: 2026-09-22T03:46:49.421565Z  

## Regime: **LOOSE**
Reason: margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20959.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21459.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 11644.0 | 0.0 | 2141.0 | 0.0 |  |
| Wind generation | 3786.0 | -25.0 | -323.0 | 19.0 | PERSISTENT_DOWN |
| Residual-load proxy | 9315.0 | 0.0 | -2141.0 | 0.0 |  |
| Indicated margin | 37794.0 | 0.0 | -43.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Indicated imbalance | -2644.0 | 0.0 | 15.0 | 0.0 | CHANGE_POINT |
| Interconnector net | -1451.0 | -4.0 | -4142.0 | -18.0 | ROBUST_OUTLIER, CHANGE_POINT |
| CCGT generation | 11320.0 | -34.0 | 603.0 | -84.0 | REVERSAL, CHANGE_POINT |
| Nuclear generation | 3657.0 | -1.0 | 3.0 | -2.0 | REVERSAL, ACCELERATION |
| Pumped-storage generation | -709.0 | 3.0 | -544.0 | 307.0 | REVERSAL, ACCELERATION, ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 14977.0 | -35.0 | 606.0 | -86.0 | REVERSAL, CHANGE_POINT |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **margin / CHANGE_POINT** — value=37794.0, Δ1=0.0, Δ12=-43.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=37794.0, Δ1=0.0, Δ12=-43.0, accel=0.0
- **interconnector_net / CHANGE_POINT** — value=-1451.0, Δ1=-4.0, Δ12=-4142.0, accel=-18.0
- **ps_gen / CHANGE_POINT** — value=-709.0, Δ1=3.0, Δ12=-544.0, accel=307.0
- **interconnector_net / ROBUST_OUTLIER** — value=-1451.0, Δ1=-4.0, Δ12=-4142.0, accel=-18.0
- **ind_demand / CHANGE_POINT** — value=-12500.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **ps_gen / REVERSAL** — value=-709.0, Δ1=3.0, Δ12=-544.0, accel=307.0
- **ps_gen / ACCELERATION** — value=-709.0, Δ1=3.0, Δ12=-544.0, accel=307.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
