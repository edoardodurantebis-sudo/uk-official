# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T15:02:09.156481Z  
Source heartbeat: 2026-09-22T15:02:07.633905Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 15.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 15.0 | 0.0 |  |
| Wind forecast | 13082.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 1620.0 | -30.0 | -355.0 | -19.0 | PERSISTENT_DOWN, ROBUST_OUTLIER |
| Residual-load proxy | 7591.0 | 0.0 | 15.0 | 0.0 |  |
| Indicated margin | 37097.0 | 0.0 | -134.0 | 0.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Indicated imbalance | -7961.0 | 0.0 | -858.0 | 0.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Interconnector net | 9764.0 | -179.0 | -353.0 | -233.0 | PERSISTENT_DOWN, ACCELERATION, ROBUST_OUTLIER, CHANGE_POINT |
| CCGT generation | 12821.0 | 282.0 | 2532.0 | -180.0 | PERSISTENT_UP, CHANGE_POINT |
| Nuclear generation | 3730.0 | 10.0 | -1.0 | 18.0 | REVERSAL, ACCELERATION |
| Pumped-storage generation | 19.0 | -118.0 | 36.0 | -251.0 | REVERSAL, ACCELERATION, CHANGE_POINT |
| Thermal base | 16551.0 | 292.0 | 2531.0 | -162.0 | PERSISTENT_UP, CHANGE_POINT |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **interconnector_net / CHANGE_POINT** — value=9764.0, Δ1=-179.0, Δ12=-353.0, accel=-233.0
- **wind_gen / PERSISTENT_DOWN** — value=1620.0, Δ1=-30.0, Δ12=-355.0, accel=-19.0
- **wind_gen / ROBUST_OUTLIER** — value=1620.0, Δ1=-30.0, Δ12=-355.0, accel=-19.0
- **ps_gen / CHANGE_POINT** — value=19.0, Δ1=-118.0, Δ12=36.0, accel=-251.0
- **thermal_base / CHANGE_POINT** — value=16551.0, Δ1=292.0, Δ12=2531.0, accel=-162.0
- **ccgt_gen / CHANGE_POINT** — value=12821.0, Δ1=282.0, Δ12=2532.0, accel=-180.0
- **imbalance / CHANGE_POINT** — value=-7961.0, Δ1=0.0, Δ12=-858.0, accel=0.0
- **ind_generation / CHANGE_POINT** — value=13212.0, Δ1=0.0, Δ12=-843.0, accel=0.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
