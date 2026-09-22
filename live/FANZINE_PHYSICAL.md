# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T17:06:01.322423Z  
Source heartbeat: 2026-09-22T17:05:59.746986Z  

## Regime: **LOOSE**
Reason: residual low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13535.0 | 0.0 | 453.0 | 0.0 |  |
| Wind generation | 1355.0 | 6.0 | 19.0 | -1.0 | PERSISTENT_UP |
| Residual-load proxy | 7138.0 | 0.0 | -453.0 | 0.0 | ROBUST_OUTLIER |
| Indicated margin | 37151.0 | 0.0 | -34.0 | 0.0 |  |
| Indicated imbalance | -7954.0 | 0.0 | -12.0 | 0.0 | PERSISTENT_DOWN |
| Interconnector net | 6912.0 | -122.0 | -683.0 | -274.0 | ACCELERATION |
| CCGT generation | 15272.0 | 13.0 | 829.0 | -60.0 | PERSISTENT_UP |
| Nuclear generation | 3728.0 | 1.0 | -2.0 | 6.0 | REVERSAL, ACCELERATION |
| Pumped-storage generation | 1508.0 | -1.0 | 263.0 | -4.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 19000.0 | 14.0 | 827.0 | -54.0 | PERSISTENT_UP |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **residual_proxy / ROBUST_OUTLIER** — value=7138.0, Δ1=0.0, Δ12=-453.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=1508.0, Δ1=-1.0, Δ12=263.0, accel=-4.0
- **ps_gen / REVERSAL** — value=1508.0, Δ1=-1.0, Δ12=263.0, accel=-4.0
- **ps_gen / ROBUST_OUTLIER** — value=1508.0, Δ1=-1.0, Δ12=263.0, accel=-4.0
- **interconnector_net / ACCELERATION** — value=6912.0, Δ1=-122.0, Δ12=-683.0, accel=-274.0
- **thermal_base / PERSISTENT_UP** — value=19000.0, Δ1=14.0, Δ12=827.0, accel=-54.0
- **ccgt_gen / PERSISTENT_UP** — value=15272.0, Δ1=13.0, Δ12=829.0, accel=-60.0
- **biomass_gen / PERSISTENT_DOWN** — value=2899.0, Δ1=-8.0, Δ12=-6.0, accel=-3.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
