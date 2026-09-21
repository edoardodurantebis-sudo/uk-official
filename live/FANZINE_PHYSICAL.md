# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T07:10:53.692574Z  
Source heartbeat: 2026-09-21T07:10:52.783726Z  

## Regime: **LOOSE**
Reason: margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21023.0 | 0.0 | 413.0 | 0.0 |  |
| Wind forecast | 8794.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 4169.0 | -37.0 | 540.0 | -78.0 | REVERSAL |
| Residual-load proxy | 11316.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 38153.0 | 0.0 | 18.0 | 0.0 | ROBUST_OUTLIER |
| Indicated imbalance | -4358.0 | 0.0 | -491.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Interconnector net | 9558.0 | 278.0 | 1830.0 | -487.0 | PERSISTENT_UP |
| CCGT generation | 8887.0 | -13.0 | -162.0 | 17.0 | PERSISTENT_DOWN |
| Nuclear generation | 3500.0 | 1.0 | 8.0 | -2.0 | PERSISTENT_UP, ROBUST_OUTLIER |
| Pumped-storage generation | 224.0 | 0.0 | -2.0 | -1.0 | ACCELERATION |
| Thermal base | 12387.0 | -12.0 | -154.0 | 15.0 | PERSISTENT_DOWN |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / ROBUST_OUTLIER** — value=-12559.0, Δ1=0.0, Δ12=-413.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=38153.0, Δ1=0.0, Δ12=18.0, accel=0.0
- **nuclear_gen / PERSISTENT_UP** — value=3500.0, Δ1=1.0, Δ12=8.0, accel=-2.0
- **nuclear_gen / ROBUST_OUTLIER** — value=3500.0, Δ1=1.0, Δ12=8.0, accel=-2.0
- **ind_generation / ROBUST_OUTLIER** — value=16665.0, Δ1=0.0, Δ12=-69.0, accel=0.0
- **imbalance / CHANGE_POINT** — value=-4358.0, Δ1=0.0, Δ12=-491.0, accel=0.0
- **imbalance / ROBUST_OUTLIER** — value=-4358.0, Δ1=0.0, Δ12=-491.0, accel=0.0
- **thermal_base / PERSISTENT_DOWN** — value=12387.0, Δ1=-12.0, Δ12=-154.0, accel=15.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
