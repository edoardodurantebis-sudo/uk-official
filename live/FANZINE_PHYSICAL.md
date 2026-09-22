# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T12:41:53.842108Z  
Source heartbeat: 2026-09-22T12:41:52.346468Z  

## Regime: **BALANCED**
Reason: wind rising

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20658.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21158.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13082.0 | 0.0 | 75.0 | 0.0 | PERSISTENT_UP, ROBUST_OUTLIER |
| Wind generation | 2587.0 | -56.0 | -964.0 | 7.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Residual-load proxy | 7576.0 | 0.0 | -75.0 | 0.0 | PERSISTENT_DOWN |
| Indicated margin | 37065.0 | 0.0 | 33.0 | 0.0 |  |
| Indicated imbalance | -7075.0 | 0.0 | -851.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 11066.0 | 24.0 | 123.0 | 0.0 | PERSISTENT_UP, CHANGE_POINT |
| CCGT generation | 8317.0 | -40.0 | 511.0 | 2.0 | REVERSAL |
| Nuclear generation | 3728.0 | -9.0 | 50.0 | -9.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| Pumped-storage generation | -125.0 | 1.0 | -118.0 | 1.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 12045.0 | -49.0 | 561.0 | -7.0 | REVERSAL |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **nuclear_gen / CHANGE_POINT** — value=3728.0, Δ1=-9.0, Δ12=50.0, accel=-9.0
- **nuclear_gen / REVERSAL** — value=3728.0, Δ1=-9.0, Δ12=50.0, accel=-9.0
- **nuclear_gen / ROBUST_OUTLIER** — value=3728.0, Δ1=-9.0, Δ12=50.0, accel=-9.0
- **ps_gen / CHANGE_POINT** — value=-125.0, Δ1=1.0, Δ12=-118.0, accel=1.0
- **ps_gen / REVERSAL** — value=-125.0, Δ1=1.0, Δ12=-118.0, accel=1.0
- **ps_gen / ROBUST_OUTLIER** — value=-125.0, Δ1=1.0, Δ12=-118.0, accel=1.0
- **wind_forecast / PERSISTENT_UP** — value=13082.0, Δ1=0.0, Δ12=75.0, accel=0.0
- **wind_forecast / ROBUST_OUTLIER** — value=13082.0, Δ1=0.0, Δ12=75.0, accel=0.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
