# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T12:40:22.755654Z  
Source heartbeat: 2026-09-21T12:40:21.941940Z  

## Regime: **BALANCED**
Reason: wind falling

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 21004.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| TS demand forecast | 21504.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 8616.0 | 0.0 | -307.0 | 0.0 | PERSISTENT_DOWN |
| Wind generation | 4059.0 | 0.0 | 628.0 | -73.0 | PERSISTENT_UP, CHANGE_POINT |
| Residual-load proxy | 12388.0 | 0.0 | 307.0 | 0.0 | PERSISTENT_UP |
| Indicated margin | 36677.0 | 0.0 | 0.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -3333.0 | 0.0 | -318.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 11201.0 | 0.0 | -147.0 | -34.0 | PERSISTENT_DOWN |
| CCGT generation | 6067.0 | 0.0 | -694.0 | 134.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Nuclear generation | 3506.0 | 0.0 | -7.0 | 6.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | 228.0 | 0.0 | 180.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 9573.0 | 0.0 | -701.0 | 140.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / ROBUST_OUTLIER** — value=-12237.0, Δ1=0.0, Δ12=4.0, accel=0.0
- **demand_forecast / ROBUST_OUTLIER** — value=21004.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=228.0, Δ1=0.0, Δ12=180.0, accel=0.0
- **ps_gen / ROBUST_OUTLIER** — value=228.0, Δ1=0.0, Δ12=180.0, accel=0.0
- **thermal_base / CHANGE_POINT** — value=9573.0, Δ1=0.0, Δ12=-701.0, accel=140.0
- **ccgt_gen / CHANGE_POINT** — value=6067.0, Δ1=0.0, Δ12=-694.0, accel=134.0
- **wind_gen / CHANGE_POINT** — value=4059.0, Δ1=0.0, Δ12=628.0, accel=-73.0
- **margin / CHANGE_POINT** — value=36677.0, Δ1=0.0, Δ12=0.0, accel=0.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
