# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T22:02:43.314703Z  
Source heartbeat: 2026-09-22T22:02:41.905609Z  

## Regime: **LOOSE**
Reason: margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13612.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 2464.0 | 24.0 | 156.0 | 49.0 | CHANGE_POINT |
| Residual-load proxy | 7061.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 37209.0 | 0.0 | -1.0 | 0.0 |  |
| Indicated imbalance | -8054.0 | 0.0 | -13.0 | 0.0 | PERSISTENT_DOWN |
| Interconnector net | 4760.0 | -2.0 | -924.0 | -4.0 | PERSISTENT_DOWN, CHANGE_POINT |
| CCGT generation | 12633.0 | -156.0 | -1732.0 | 0.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Nuclear generation | 3742.0 | 5.0 | 10.0 | 6.0 | PERSISTENT_UP, ACCELERATION |
| Pumped-storage generation | 143.0 | 0.0 | 0.0 | 0.0 | CHANGE_POINT |
| Thermal base | 16375.0 | -151.0 | -1722.0 | 6.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **thermal_base / CHANGE_POINT** — value=16375.0, Δ1=-151.0, Δ12=-1722.0, accel=6.0
- **ccgt_gen / CHANGE_POINT** — value=12633.0, Δ1=-156.0, Δ12=-1732.0, accel=0.0
- **interconnector_net / CHANGE_POINT** — value=4760.0, Δ1=-2.0, Δ12=-924.0, accel=-4.0
- **thermal_base / PERSISTENT_DOWN** — value=16375.0, Δ1=-151.0, Δ12=-1722.0, accel=6.0
- **thermal_base / ROBUST_OUTLIER** — value=16375.0, Δ1=-151.0, Δ12=-1722.0, accel=6.0
- **ccgt_gen / PERSISTENT_DOWN** — value=12633.0, Δ1=-156.0, Δ12=-1732.0, accel=0.0
- **ccgt_gen / ROBUST_OUTLIER** — value=12633.0, Δ1=-156.0, Δ12=-1732.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=143.0, Δ1=0.0, Δ12=0.0, accel=0.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
