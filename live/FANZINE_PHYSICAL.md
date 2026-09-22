# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T12:54:38.692613Z  
Source heartbeat: 2026-09-22T12:54:37.550737Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20658.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21158.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13082.0 | 0.0 | 75.0 | 0.0 | ROBUST_OUTLIER |
| Wind generation | 2499.0 | -50.0 | -819.0 | -50.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Residual-load proxy | 7576.0 | 0.0 | -75.0 | 0.0 |  |
| Indicated margin | 37206.0 | 141.0 | 174.0 | 141.0 | PERSISTENT_UP, ACCELERATION |
| Indicated imbalance | -7090.0 | -15.0 | -41.0 | -15.0 | PERSISTENT_DOWN, ACCELERATION, CHANGE_POINT |
| Interconnector net | 11108.0 | 18.0 | 171.0 | 18.0 | PERSISTENT_UP, CHANGE_POINT |
| CCGT generation | 8397.0 | 64.0 | 530.0 | 64.0 | PERSISTENT_UP |
| Nuclear generation | 3731.0 | 9.0 | 26.0 | 9.0 | PERSISTENT_UP, ROBUST_OUTLIER, CHANGE_POINT |
| Pumped-storage generation | -126.0 | 0.0 | -113.0 | 0.0 | PERSISTENT_DOWN, ROBUST_OUTLIER |
| Thermal base | 12128.0 | 73.0 | 556.0 | 73.0 | PERSISTENT_UP |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **nuclear_gen / CHANGE_POINT** — value=3731.0, Δ1=9.0, Δ12=26.0, accel=9.0
- **nuclear_gen / PERSISTENT_UP** — value=3731.0, Δ1=9.0, Δ12=26.0, accel=9.0
- **nuclear_gen / ROBUST_OUTLIER** — value=3731.0, Δ1=9.0, Δ12=26.0, accel=9.0
- **wind_forecast / ROBUST_OUTLIER** — value=13082.0, Δ1=0.0, Δ12=75.0, accel=0.0
- **wind_gen / CHANGE_POINT** — value=2499.0, Δ1=-50.0, Δ12=-819.0, accel=-50.0
- **ps_gen / PERSISTENT_DOWN** — value=-126.0, Δ1=0.0, Δ12=-113.0, accel=0.0
- **ps_gen / ROBUST_OUTLIER** — value=-126.0, Δ1=0.0, Δ12=-113.0, accel=0.0
- **wind_gen / PERSISTENT_DOWN** — value=2499.0, Δ1=-50.0, Δ12=-819.0, accel=-50.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
