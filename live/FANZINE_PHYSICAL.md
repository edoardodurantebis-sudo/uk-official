# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T15:43:38.219373Z  
Source heartbeat: 2026-09-21T15:43:37.340431Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20959.0 | 0.0 | -45.0 | 0.0 |  |
| TS demand forecast | 21459.0 | 0.0 | -45.0 | 0.0 |  |
| Wind forecast | 8616.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 3386.0 | -4.0 | -224.0 | -46.0 | CHANGE_POINT |
| Residual-load proxy | 12343.0 | 0.0 | -45.0 | 0.0 |  |
| Indicated margin | 36257.0 | 0.0 | 4.0 | 0.0 |  |
| Indicated imbalance | -3107.0 | 0.0 | 99.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 10947.0 | -24.0 | -427.0 | 15.0 | PERSISTENT_DOWN, CHANGE_POINT |
| CCGT generation | 10644.0 | 101.0 | 1585.0 | -22.0 | PERSISTENT_UP, ROBUST_OUTLIER |
| Nuclear generation | 3499.0 | 5.0 | -1.0 | 4.0 | REVERSAL, ACCELERATION |
| Pumped-storage generation | -75.0 | -54.0 | -204.0 | -54.0 | PERSISTENT_DOWN |
| Thermal base | 14143.0 | 106.0 | 1584.0 | -18.0 | PERSISTENT_UP, ROBUST_OUTLIER |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **thermal_base / PERSISTENT_UP** — value=14143.0, Δ1=106.0, Δ12=1584.0, accel=-18.0
- **thermal_base / ROBUST_OUTLIER** — value=14143.0, Δ1=106.0, Δ12=1584.0, accel=-18.0
- **ccgt_gen / PERSISTENT_UP** — value=10644.0, Δ1=101.0, Δ12=1585.0, accel=-22.0
- **ccgt_gen / ROBUST_OUTLIER** — value=10644.0, Δ1=101.0, Δ12=1585.0, accel=-22.0
- **interconnector_net / CHANGE_POINT** — value=10947.0, Δ1=-24.0, Δ12=-427.0, accel=15.0
- **wind_gen / CHANGE_POINT** — value=3386.0, Δ1=-4.0, Δ12=-224.0, accel=-46.0
- **imbalance / CHANGE_POINT** — value=-3107.0, Δ1=0.0, Δ12=99.0, accel=0.0
- **ind_generation / CHANGE_POINT** — value=18352.0, Δ1=0.0, Δ12=54.0, accel=0.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
