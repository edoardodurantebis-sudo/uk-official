# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T11:12:19.298114Z  
Source heartbeat: 2026-09-22T11:12:17.771758Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20687.0 | 0.0 | 487.0 | 0.0 |  |
| TS demand forecast | 21187.0 | 0.0 | 239.0 | 0.0 |  |
| Wind forecast | 13007.0 | 0.0 | 614.0 | 0.0 | ROBUST_OUTLIER |
| Wind generation | 3679.0 | 11.0 | 103.0 | 8.0 | PERSISTENT_UP |
| Residual-load proxy | 7680.0 | 0.0 | -127.0 | 0.0 |  |
| Indicated margin | 37005.0 | 0.0 | -3381.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Indicated imbalance | -6230.0 | 0.0 | -11397.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Interconnector net | 10950.0 | -23.0 | 44.0 | -10.0 | REVERSAL, CHANGE_POINT |
| CCGT generation | 8716.0 | -40.0 | -1095.0 | -51.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Nuclear generation | 3650.0 | -9.0 | 5.0 | -9.0 | REVERSAL, ACCELERATION |
| Pumped-storage generation | -164.0 | 3.0 | -64.0 | 3.0 | REVERSAL, CHANGE_POINT |
| Thermal base | 12366.0 | -49.0 | -1090.0 | -60.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **margin / CHANGE_POINT** — value=37005.0, Δ1=0.0, Δ12=-3381.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=37005.0, Δ1=0.0, Δ12=-3381.0, accel=0.0
- **wind_forecast / ROBUST_OUTLIER** — value=13007.0, Δ1=0.0, Δ12=614.0, accel=0.0
- **ind_generation / CHANGE_POINT** — value=14957.0, Δ1=0.0, Δ12=-11158.0, accel=0.0
- **ind_generation / ROBUST_OUTLIER** — value=14957.0, Δ1=0.0, Δ12=-11158.0, accel=0.0
- **thermal_base / CHANGE_POINT** — value=12366.0, Δ1=-49.0, Δ12=-1090.0, accel=-60.0
- **ccgt_gen / CHANGE_POINT** — value=8716.0, Δ1=-40.0, Δ12=-1095.0, accel=-51.0
- **imbalance / CHANGE_POINT** — value=-6230.0, Δ1=0.0, Δ12=-11397.0, accel=0.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
