# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T10:37:56.149770Z  
Source heartbeat: 2026-09-22T10:37:54.970152Z  

## Regime: **LOOSE**
Reason: margin high; wind rising

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20200.0 | 0.0 | -120.0 | 0.0 |  |
| TS demand forecast | 20948.0 | 0.0 | -120.0 | 0.0 | ROBUST_OUTLIER |
| Wind forecast | 13007.0 | 0.0 | 614.0 | -614.0 | PERSISTENT_UP, ACCELERATION, ROBUST_OUTLIER |
| Wind generation | 3525.0 | -50.0 | -193.0 | -54.0 | PERSISTENT_DOWN |
| Residual-load proxy | 7193.0 | 0.0 | -734.0 | 614.0 | PERSISTENT_DOWN, ACCELERATION |
| Indicated margin | 40386.0 | 0.0 | 52.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Indicated imbalance | 5167.0 | 0.0 | 2737.0 | 0.0 | ROBUST_OUTLIER |
| Interconnector net | 10888.0 | 16.0 | 74.0 | 24.0 |  |
| CCGT generation | 9610.0 | -64.0 | -495.0 | 70.0 | PERSISTENT_DOWN |
| Nuclear generation | 3657.0 | 2.0 | 6.0 | 1.0 | PERSISTENT_UP |
| Pumped-storage generation | -167.0 | 0.0 | 3.0 | 0.0 |  |
| Thermal base | 13267.0 | -62.0 | -489.0 | 71.0 | PERSISTENT_DOWN |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ts_demand_forecast / ROBUST_OUTLIER** — value=20948.0, Δ1=0.0, Δ12=-120.0, accel=0.0
- **margin / CHANGE_POINT** — value=40386.0, Δ1=0.0, Δ12=52.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=40386.0, Δ1=0.0, Δ12=52.0, accel=0.0
- **imbalance / ROBUST_OUTLIER** — value=5167.0, Δ1=0.0, Δ12=2737.0, accel=0.0
- **ind_generation / ROBUST_OUTLIER** — value=26115.0, Δ1=0.0, Δ12=2617.0, accel=0.0
- **ind_demand / ROBUST_OUTLIER** — value=-13862.0, Δ1=0.0, Δ12=-1061.0, accel=0.0
- **wind_forecast / PERSISTENT_UP** — value=13007.0, Δ1=0.0, Δ12=614.0, accel=-614.0
- **wind_forecast / ACCELERATION** — value=13007.0, Δ1=0.0, Δ12=614.0, accel=-614.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
