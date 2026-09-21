# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T12:53:01.850217Z  
Source heartbeat: 2026-09-21T12:53:00.200547Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 21004.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| TS demand forecast | 21504.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 8616.0 | 0.0 | -307.0 | 0.0 |  |
| Wind generation | 3870.0 | -73.0 | 246.0 | 44.0 | REVERSAL, CHANGE_POINT |
| Residual-load proxy | 12388.0 | 0.0 | 307.0 | 0.0 |  |
| Indicated margin | 36271.0 | -406.0 | -402.0 | -406.0 | PERSISTENT_DOWN, ACCELERATION, CHANGE_POINT |
| Indicated imbalance | -3333.0 | 0.0 | -319.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 11312.0 | 23.0 | -55.0 | -12.0 | REVERSAL |
| CCGT generation | 5930.0 | -10.0 | -616.0 | 60.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Nuclear generation | 3503.0 | -6.0 | -6.0 | -3.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | 228.0 | 0.0 | 120.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 9433.0 | -16.0 | -622.0 | 57.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / ROBUST_OUTLIER** — value=-12237.0, Δ1=0.0, Δ12=4.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=228.0, Δ1=0.0, Δ12=120.0, accel=0.0
- **ps_gen / ROBUST_OUTLIER** — value=228.0, Δ1=0.0, Δ12=120.0, accel=0.0
- **demand_forecast / ROBUST_OUTLIER** — value=21004.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **thermal_base / CHANGE_POINT** — value=9433.0, Δ1=-16.0, Δ12=-622.0, accel=57.0
- **ccgt_gen / CHANGE_POINT** — value=5930.0, Δ1=-10.0, Δ12=-616.0, accel=60.0
- **margin / CHANGE_POINT** — value=36271.0, Δ1=-406.0, Δ12=-402.0, accel=-406.0
- **wind_gen / CHANGE_POINT** — value=3870.0, Δ1=-73.0, Δ12=246.0, accel=44.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
