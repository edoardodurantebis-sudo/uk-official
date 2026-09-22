# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T23:18:31.693074Z  
Source heartbeat: 2026-09-22T23:18:30.768489Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13612.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 3111.0 | 24.0 | 511.0 | -18.0 | PERSISTENT_UP, CHANGE_POINT |
| Residual-load proxy | 7061.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 37229.0 | 0.0 | 0.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -8056.0 | 0.0 | -9.0 | 0.0 |  |
| Interconnector net | 4618.0 | 24.0 | -477.0 | 153.0 | REVERSAL |
| CCGT generation | 10150.0 | 4.0 | -430.0 | -1.0 | REVERSAL, ROBUST_OUTLIER |
| Nuclear generation | 3738.0 | -5.0 | -6.0 | -8.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | 147.0 | 0.0 | 2.0 | 0.0 |  |
| Thermal base | 13888.0 | -1.0 | -436.0 | -9.0 | ROBUST_OUTLIER |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / ROBUST_OUTLIER** — value=-12493.0, Δ1=0.0, Δ12=-15.0, accel=0.0
- **thermal_base / ROBUST_OUTLIER** — value=13888.0, Δ1=-1.0, Δ12=-436.0, accel=-9.0
- **ccgt_gen / REVERSAL** — value=10150.0, Δ1=4.0, Δ12=-430.0, accel=-1.0
- **ccgt_gen / ROBUST_OUTLIER** — value=10150.0, Δ1=4.0, Δ12=-430.0, accel=-1.0
- **wind_gen / CHANGE_POINT** — value=3111.0, Δ1=24.0, Δ12=511.0, accel=-18.0
- **margin / CHANGE_POINT** — value=37229.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **wind_gen / PERSISTENT_UP** — value=3111.0, Δ1=24.0, Δ12=511.0, accel=-18.0
- **interconnector_net / REVERSAL** — value=4618.0, Δ1=24.0, Δ12=-477.0, accel=153.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
