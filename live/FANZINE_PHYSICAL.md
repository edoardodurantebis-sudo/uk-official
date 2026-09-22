# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T12:58:51.852540Z  
Source heartbeat: 2026-09-22T12:58:50.504318Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20658.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21158.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13082.0 | 0.0 | 75.0 | 0.0 | ROBUST_OUTLIER |
| Wind generation | 2471.0 | -28.0 | -802.0 | 22.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Residual-load proxy | 7576.0 | 0.0 | -75.0 | 0.0 |  |
| Indicated margin | 37206.0 | 0.0 | 174.0 | -141.0 | PERSISTENT_UP, ACCELERATION |
| Indicated imbalance | -7090.0 | 0.0 | -41.0 | 15.0 | PERSISTENT_DOWN, ACCELERATION, CHANGE_POINT |
| Interconnector net | 11107.0 | -1.0 | 195.0 | -19.0 | REVERSAL, CHANGE_POINT |
| CCGT generation | 8561.0 | 164.0 | 516.0 | 100.0 | PERSISTENT_UP |
| Nuclear generation | 3732.0 | 1.0 | 25.0 | -8.0 | PERSISTENT_UP, ROBUST_OUTLIER |
| Pumped-storage generation | -125.0 | 1.0 | -89.0 | 1.0 | REVERSAL, ROBUST_OUTLIER |
| Thermal base | 12293.0 | 165.0 | 541.0 | 92.0 | PERSISTENT_UP |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **nuclear_gen / PERSISTENT_UP** — value=3732.0, Δ1=1.0, Δ12=25.0, accel=-8.0
- **nuclear_gen / ROBUST_OUTLIER** — value=3732.0, Δ1=1.0, Δ12=25.0, accel=-8.0
- **wind_forecast / ROBUST_OUTLIER** — value=13082.0, Δ1=0.0, Δ12=75.0, accel=0.0
- **wind_gen / CHANGE_POINT** — value=2471.0, Δ1=-28.0, Δ12=-802.0, accel=22.0
- **ps_gen / REVERSAL** — value=-125.0, Δ1=1.0, Δ12=-89.0, accel=1.0
- **ps_gen / ROBUST_OUTLIER** — value=-125.0, Δ1=1.0, Δ12=-89.0, accel=1.0
- **wind_gen / PERSISTENT_DOWN** — value=2471.0, Δ1=-28.0, Δ12=-802.0, accel=22.0
- **wind_gen / ROBUST_OUTLIER** — value=2471.0, Δ1=-28.0, Δ12=-802.0, accel=22.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
