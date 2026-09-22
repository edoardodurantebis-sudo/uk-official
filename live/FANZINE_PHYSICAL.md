# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T11:29:16.022511Z  
Source heartbeat: 2026-09-22T11:29:14.531873Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20658.0 | 0.0 | 458.0 | 0.0 |  |
| TS demand forecast | 21158.0 | 0.0 | 210.0 | 0.0 |  |
| Wind forecast | 13007.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| Wind generation | 3887.0 | -5.0 | 362.0 | -5.0 | REVERSAL, ROBUST_OUTLIER |
| Residual-load proxy | 7651.0 | 0.0 | 458.0 | 0.0 |  |
| Indicated margin | 37032.0 | 0.0 | -3354.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Indicated imbalance | -6224.0 | 0.0 | -11391.0 | -6.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Interconnector net | 10935.0 | -1.0 | 47.0 | -1.0 | REVERSAL |
| CCGT generation | 8268.0 | -207.0 | -1342.0 | -207.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Nuclear generation | 3652.0 | 5.0 | -5.0 | 5.0 | REVERSAL, ACCELERATION |
| Pumped-storage generation | -164.0 | 0.0 | 3.0 | 0.0 | PERSISTENT_UP |
| Thermal base | 11920.0 | -202.0 | -1347.0 | -202.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **margin / CHANGE_POINT** — value=37032.0, Δ1=0.0, Δ12=-3354.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=37032.0, Δ1=0.0, Δ12=-3354.0, accel=0.0
- **wind_forecast / ROBUST_OUTLIER** — value=13007.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **ind_generation / CHANGE_POINT** — value=14934.0, Δ1=0.0, Δ12=-11181.0, accel=23.0
- **thermal_base / CHANGE_POINT** — value=11920.0, Δ1=-202.0, Δ12=-1347.0, accel=-202.0
- **ccgt_gen / CHANGE_POINT** — value=8268.0, Δ1=-207.0, Δ12=-1342.0, accel=-207.0
- **ind_generation / PERSISTENT_DOWN** — value=14934.0, Δ1=0.0, Δ12=-11181.0, accel=23.0
- **ind_generation / ROBUST_OUTLIER** — value=14934.0, Δ1=0.0, Δ12=-11181.0, accel=23.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
