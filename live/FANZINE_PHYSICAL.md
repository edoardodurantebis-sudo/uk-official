# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T12:46:12.219557Z  
Source heartbeat: 2026-09-22T12:46:10.767548Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20658.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21158.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13082.0 | 0.0 | 75.0 | 0.0 | ROBUST_OUTLIER |
| Wind generation | 2549.0 | -38.0 | -933.0 | 18.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Residual-load proxy | 7576.0 | 0.0 | -75.0 | 0.0 |  |
| Indicated margin | 37065.0 | 0.0 | 33.0 | 0.0 |  |
| Indicated imbalance | -7075.0 | 0.0 | -26.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 11090.0 | 24.0 | 146.0 | 0.0 | PERSISTENT_UP, CHANGE_POINT |
| CCGT generation | 8333.0 | 16.0 | 626.0 | 56.0 |  |
| Nuclear generation | 3722.0 | -6.0 | 41.0 | 3.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| Pumped-storage generation | -126.0 | -1.0 | -116.0 | -2.0 | PERSISTENT_DOWN, ROBUST_OUTLIER |
| Thermal base | 12055.0 | 10.0 | 667.0 | 59.0 |  |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **nuclear_gen / CHANGE_POINT** — value=3722.0, Δ1=-6.0, Δ12=41.0, accel=3.0
- **nuclear_gen / REVERSAL** — value=3722.0, Δ1=-6.0, Δ12=41.0, accel=3.0
- **nuclear_gen / ROBUST_OUTLIER** — value=3722.0, Δ1=-6.0, Δ12=41.0, accel=3.0
- **ps_gen / PERSISTENT_DOWN** — value=-126.0, Δ1=-1.0, Δ12=-116.0, accel=-2.0
- **ps_gen / ROBUST_OUTLIER** — value=-126.0, Δ1=-1.0, Δ12=-116.0, accel=-2.0
- **wind_forecast / ROBUST_OUTLIER** — value=13082.0, Δ1=0.0, Δ12=75.0, accel=0.0
- **wind_gen / CHANGE_POINT** — value=2549.0, Δ1=-38.0, Δ12=-933.0, accel=18.0
- **wind_gen / PERSISTENT_DOWN** — value=2549.0, Δ1=-38.0, Δ12=-933.0, accel=18.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
