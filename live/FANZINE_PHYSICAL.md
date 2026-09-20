# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-20T23:38:14.652714Z  
Source heartbeat: 2026-09-20T23:38:13.879631Z  

## Regime: **BALANCED**
Reason: wind falling

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 20610.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 1603.0 | 0.0 | -123.0 | 123.0 | PERSISTENT_DOWN, ACCELERATION |
| Wind generation | 5556.0 | -122.0 | -621.0 | -54.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Residual-load proxy | 18507.0 | 0.0 | 123.0 | -123.0 | PERSISTENT_UP, ACCELERATION |
| Indicated margin | 35811.0 | 0.0 | 35.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -5221.0 | 0.0 | -27.0 | 0.0 |  |
| Interconnector net | 9414.0 | 5.0 | 165.0 | -83.0 | PERSISTENT_UP, ACCELERATION |
| CCGT generation | 6043.0 | 3.0 | 507.0 | 9.0 | PERSISTENT_UP |
| Nuclear generation | 3337.0 | 7.0 | 4.0 | 8.0 | PERSISTENT_UP, ACCELERATION |
| Pumped-storage generation | -12.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| Thermal base | 9380.0 | 10.0 | 511.0 | 17.0 | PERSISTENT_UP |
| Frequency | 49.922 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ps_gen / ROBUST_OUTLIER** — value=-12.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **biomass_gen / CHANGE_POINT** — value=3004.0, Δ1=7.0, Δ12=53.0, accel=1.0
- **wind_gen / CHANGE_POINT** — value=5556.0, Δ1=-122.0, Δ12=-621.0, accel=-54.0
- **margin / CHANGE_POINT** — value=35811.0, Δ1=0.0, Δ12=35.0, accel=0.0
- **biomass_gen / PERSISTENT_UP** — value=3004.0, Δ1=7.0, Δ12=53.0, accel=1.0
- **wind_gen / PERSISTENT_DOWN** — value=5556.0, Δ1=-122.0, Δ12=-621.0, accel=-54.0
- **interconnector_net / PERSISTENT_UP** — value=9414.0, Δ1=5.0, Δ12=165.0, accel=-83.0
- **interconnector_net / ACCELERATION** — value=9414.0, Δ1=5.0, Δ12=165.0, accel=-83.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
