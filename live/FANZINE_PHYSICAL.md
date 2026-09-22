# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T11:16:32.318097Z  
Source heartbeat: 2026-09-22T11:16:31.121162Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20687.0 | 0.0 | 487.0 | 0.0 |  |
| TS demand forecast | 21187.0 | 0.0 | 239.0 | 0.0 |  |
| Wind forecast | 13007.0 | 0.0 | 614.0 | 0.0 | ROBUST_OUTLIER |
| Wind generation | 3920.0 | 241.0 | 344.0 | 230.0 | PERSISTENT_UP, ACCELERATION, ROBUST_OUTLIER |
| Residual-load proxy | 7680.0 | 0.0 | -127.0 | 0.0 |  |
| Indicated margin | 37005.0 | 0.0 | -3381.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Indicated imbalance | -6230.0 | 0.0 | -11397.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Interconnector net | 10937.0 | -13.0 | 31.0 | 10.0 | REVERSAL, CHANGE_POINT |
| CCGT generation | 8690.0 | -26.0 | -1121.0 | 14.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Nuclear generation | 3645.0 | -5.0 | 0.0 | 4.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | -165.0 | -1.0 | -65.0 | -4.0 | CHANGE_POINT |
| Thermal base | 12335.0 | -31.0 | -1121.0 | 18.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **margin / CHANGE_POINT** — value=37005.0, Δ1=0.0, Δ12=-3381.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=37005.0, Δ1=0.0, Δ12=-3381.0, accel=0.0
- **wind_forecast / ROBUST_OUTLIER** — value=13007.0, Δ1=0.0, Δ12=614.0, accel=0.0
- **ind_generation / CHANGE_POINT** — value=14957.0, Δ1=0.0, Δ12=-11158.0, accel=0.0
- **ind_generation / ROBUST_OUTLIER** — value=14957.0, Δ1=0.0, Δ12=-11158.0, accel=0.0
- **thermal_base / CHANGE_POINT** — value=12335.0, Δ1=-31.0, Δ12=-1121.0, accel=18.0
- **ccgt_gen / CHANGE_POINT** — value=8690.0, Δ1=-26.0, Δ12=-1121.0, accel=14.0
- **imbalance / CHANGE_POINT** — value=-6230.0, Δ1=0.0, Δ12=-11397.0, accel=0.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
