# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T11:57:57.364019Z  
Source heartbeat: 2026-09-21T11:57:55.882170Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 21004.0 | 0.0 | -104.0 | 0.0 |  |
| TS demand forecast | 21504.0 | 0.0 | -104.0 | 0.0 |  |
| Wind forecast | 8923.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 3630.0 | 126.0 | 306.0 | 53.0 | PERSISTENT_UP, CHANGE_POINT |
| Residual-load proxy | 12081.0 | 0.0 | -104.0 | 0.0 |  |
| Indicated margin | 36673.0 | 0.0 | 178.0 | 4.0 |  |
| Indicated imbalance | -3014.0 | 0.0 | 857.0 | -1.0 | PERSISTENT_UP |
| Interconnector net | 11299.0 | -24.0 | 35.0 | 1.0 | REVERSAL |
| CCGT generation | 6490.0 | -107.0 | -193.0 | 57.0 | PERSISTENT_DOWN, ROBUST_OUTLIER |
| Nuclear generation | 3506.0 | -6.0 | -13.0 | -5.0 | PERSISTENT_DOWN, ACCELERATION, CHANGE_POINT |
| Pumped-storage generation | 108.0 | 1.0 | 8.0 | -58.0 | PERSISTENT_UP, ACCELERATION, ROBUST_OUTLIER |
| Thermal base | 9996.0 | -113.0 | -206.0 | 52.0 | PERSISTENT_DOWN, ROBUST_OUTLIER |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ps_gen / PERSISTENT_UP** — value=108.0, Δ1=1.0, Δ12=8.0, accel=-58.0
- **ps_gen / ACCELERATION** — value=108.0, Δ1=1.0, Δ12=8.0, accel=-58.0
- **ps_gen / ROBUST_OUTLIER** — value=108.0, Δ1=1.0, Δ12=8.0, accel=-58.0
- **ind_demand / CHANGE_POINT** — value=-12241.0, Δ1=0.0, Δ12=2.0, accel=0.0
- **ind_demand / ROBUST_OUTLIER** — value=-12241.0, Δ1=0.0, Δ12=2.0, accel=0.0
- **ccgt_gen / PERSISTENT_DOWN** — value=6490.0, Δ1=-107.0, Δ12=-193.0, accel=57.0
- **ccgt_gen / ROBUST_OUTLIER** — value=6490.0, Δ1=-107.0, Δ12=-193.0, accel=57.0
- **thermal_base / PERSISTENT_DOWN** — value=9996.0, Δ1=-113.0, Δ12=-206.0, accel=52.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
