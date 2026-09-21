# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T23:35:24.800013Z  
Source heartbeat: 2026-09-21T23:35:23.461931Z  

## Regime: **BALANCED**
Reason: wind rising

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20959.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21459.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 9503.0 | 0.0 | 882.0 | -882.0 | PERSISTENT_UP, ACCELERATION |
| Wind generation | 3530.0 | 0.0 | -143.0 | -9.0 |  |
| Residual-load proxy | 11456.0 | 0.0 | -882.0 | 882.0 | PERSISTENT_DOWN, ACCELERATION |
| Indicated margin | 36167.0 | 0.0 | -65.0 | 0.0 |  |
| Indicated imbalance | -2016.0 | 0.0 | 483.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 3322.0 | 0.0 | 413.0 | -175.0 | PERSISTENT_UP, ACCELERATION |
| CCGT generation | 11261.0 | 0.0 | -70.0 | -99.0 | ACCELERATION |
| Nuclear generation | 3653.0 | 0.0 | 13.0 | -3.0 | PERSISTENT_UP, ROBUST_OUTLIER |
| Pumped-storage generation | -285.0 | 0.0 | -277.0 | 3.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Thermal base | 14914.0 | 0.0 | -57.0 | -102.0 | ACCELERATION |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / ROBUST_OUTLIER** — value=-12381.0, Δ1=0.0, Δ12=-123.0, accel=0.0
- **nuclear_gen / PERSISTENT_UP** — value=3653.0, Δ1=0.0, Δ12=13.0, accel=-3.0
- **nuclear_gen / ROBUST_OUTLIER** — value=3653.0, Δ1=0.0, Δ12=13.0, accel=-3.0
- **imbalance / CHANGE_POINT** — value=-2016.0, Δ1=0.0, Δ12=483.0, accel=0.0
- **ind_generation / CHANGE_POINT** — value=19443.0, Δ1=0.0, Δ12=483.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=-285.0, Δ1=0.0, Δ12=-277.0, accel=3.0
- **ccgt_gen / ACCELERATION** — value=11261.0, Δ1=0.0, Δ12=-70.0, accel=-99.0
- **thermal_base / ACCELERATION** — value=14914.0, Δ1=0.0, Δ12=-57.0, accel=-102.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
