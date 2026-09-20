# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-20T18:59:50.922420Z  
Source heartbeat: 2026-09-20T18:59:49.511883Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 20610.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 2115.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 5556.0 | 0.0 | -986.0 | 147.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Residual-load proxy | 17995.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 35401.0 | 0.0 | -59.0 | 0.0 | PERSISTENT_DOWN |
| Indicated imbalance | -5141.0 | 0.0 | 24.0 | -17.0 | PERSISTENT_UP, ACCELERATION |
| Interconnector net | 9874.0 | 0.0 | -72.0 | 0.0 | CHANGE_POINT |
| CCGT generation | 8741.0 | 0.0 | -259.0 | 40.0 | ROBUST_OUTLIER |
| Nuclear generation | 3333.0 | 0.0 | -2.0 | 5.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | 223.0 | 0.0 | -307.0 | 0.0 | PERSISTENT_DOWN |
| Thermal base | 12074.0 | 0.0 | -261.0 | 45.0 | ROBUST_OUTLIER |
| Frequency | 49.922 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **thermal_base / ROBUST_OUTLIER** — value=12074.0, Δ1=0.0, Δ12=-261.0, accel=45.0
- **ccgt_gen / ROBUST_OUTLIER** — value=8741.0, Δ1=0.0, Δ12=-259.0, accel=40.0
- **wind_gen / CHANGE_POINT** — value=5556.0, Δ1=0.0, Δ12=-986.0, accel=147.0
- **biomass_gen / CHANGE_POINT** — value=2344.0, Δ1=0.0, Δ12=86.0, accel=-3.0
- **interconnector_net / CHANGE_POINT** — value=9874.0, Δ1=0.0, Δ12=-72.0, accel=0.0
- **margin / PERSISTENT_DOWN** — value=35401.0, Δ1=0.0, Δ12=-59.0, accel=0.0
- **ind_generation / PERSISTENT_UP** — value=15469.0, Δ1=0.0, Δ12=24.0, accel=-17.0
- **ind_generation / ACCELERATION** — value=15469.0, Δ1=0.0, Δ12=24.0, accel=-17.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
