# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T16:53:17.287611Z  
Source heartbeat: 2026-09-22T16:53:15.798478Z  

## Regime: **LOOSE**
Reason: residual low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13535.0 | 0.0 | 453.0 | 0.0 |  |
| Wind generation | 1347.0 | 13.0 | 5.0 | -10.0 | PERSISTENT_UP, ACCELERATION |
| Residual-load proxy | 7138.0 | 0.0 | -453.0 | 0.0 | ROBUST_OUTLIER |
| Indicated margin | 37151.0 | -2.0 | -34.0 | -2.0 | PERSISTENT_DOWN |
| Indicated imbalance | -7943.0 | 0.0 | -1.0 | 0.0 |  |
| Interconnector net | 6858.0 | 24.0 | -1441.0 | -2.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| CCGT generation | 15099.0 | 147.0 | 500.0 | 25.0 | PERSISTENT_UP |
| Nuclear generation | 3734.0 | 5.0 | 9.0 | 4.0 | PERSISTENT_UP, ACCELERATION |
| Pumped-storage generation | 1507.0 | -2.0 | 1049.0 | -4.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 18833.0 | 152.0 | 509.0 | 29.0 | PERSISTENT_UP |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **residual_proxy / ROBUST_OUTLIER** — value=7138.0, Δ1=0.0, Δ12=-453.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=1507.0, Δ1=-2.0, Δ12=1049.0, accel=-4.0
- **ps_gen / REVERSAL** — value=1507.0, Δ1=-2.0, Δ12=1049.0, accel=-4.0
- **ps_gen / ROBUST_OUTLIER** — value=1507.0, Δ1=-2.0, Δ12=1049.0, accel=-4.0
- **interconnector_net / CHANGE_POINT** — value=6858.0, Δ1=24.0, Δ12=-1441.0, accel=-2.0
- **interconnector_net / REVERSAL** — value=6858.0, Δ1=24.0, Δ12=-1441.0, accel=-2.0
- **interconnector_net / ROBUST_OUTLIER** — value=6858.0, Δ1=24.0, Δ12=-1441.0, accel=-2.0
- **thermal_base / PERSISTENT_UP** — value=18833.0, Δ1=152.0, Δ12=509.0, accel=29.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
