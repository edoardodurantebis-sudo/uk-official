# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T12:36:09.437186Z  
Source heartbeat: 2026-09-21T12:36:07.972635Z  

## Regime: **BALANCED**
Reason: wind falling

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 21004.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21504.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 8616.0 | 0.0 | -307.0 | 307.0 | PERSISTENT_DOWN, ACCELERATION |
| Wind generation | 4059.0 | 73.0 | 652.0 | -30.0 | PERSISTENT_UP, CHANGE_POINT |
| Residual-load proxy | 12388.0 | 0.0 | 307.0 | -307.0 | PERSISTENT_UP, ACCELERATION |
| Indicated margin | 36677.0 | 0.0 | 0.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -3333.0 | 0.0 | -318.0 | 0.0 | PERSISTENT_DOWN |
| Interconnector net | 11201.0 | 34.0 | -135.0 | 133.0 | REVERSAL, ACCELERATION |
| CCGT generation | 6067.0 | -134.0 | -938.0 | -44.0 | PERSISTENT_DOWN, ROBUST_OUTLIER |
| Nuclear generation | 3506.0 | -6.0 | -11.0 | -5.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | 228.0 | 0.0 | 236.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 9573.0 | -140.0 | -949.0 | -49.0 | PERSISTENT_DOWN, ROBUST_OUTLIER |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / CHANGE_POINT** — value=-12237.0, Δ1=0.0, Δ12=4.0, accel=0.0
- **ind_demand / PERSISTENT_UP** — value=-12237.0, Δ1=0.0, Δ12=4.0, accel=0.0
- **ind_demand / ROBUST_OUTLIER** — value=-12237.0, Δ1=0.0, Δ12=4.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=228.0, Δ1=0.0, Δ12=236.0, accel=0.0
- **ps_gen / ROBUST_OUTLIER** — value=228.0, Δ1=0.0, Δ12=236.0, accel=0.0
- **ccgt_gen / PERSISTENT_DOWN** — value=6067.0, Δ1=-134.0, Δ12=-938.0, accel=-44.0
- **ccgt_gen / ROBUST_OUTLIER** — value=6067.0, Δ1=-134.0, Δ12=-938.0, accel=-44.0
- **thermal_base / PERSISTENT_DOWN** — value=9573.0, Δ1=-140.0, Δ12=-949.0, accel=-49.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
