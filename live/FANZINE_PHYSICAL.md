# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T11:37:41.064468Z  
Source heartbeat: 2026-09-22T11:37:39.590020Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20658.0 | 0.0 | 458.0 | 0.0 |  |
| TS demand forecast | 21158.0 | 0.0 | 210.0 | 0.0 |  |
| Wind forecast | 13007.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| Wind generation | 3729.0 | -96.0 | 280.0 | -34.0 | REVERSAL |
| Residual-load proxy | 7651.0 | 0.0 | 458.0 | 0.0 |  |
| Indicated margin | 37032.0 | 0.0 | -3354.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Indicated imbalance | -6224.0 | 0.0 | -11391.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Interconnector net | 10946.0 | 1.0 | 10.0 | -9.0 | PERSISTENT_UP, ACCELERATION |
| CCGT generation | 7905.0 | -241.0 | -1040.0 | -119.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Nuclear generation | 3658.0 | 3.0 | 9.0 | 0.0 | PERSISTENT_UP |
| Pumped-storage generation | -7.0 | 12.0 | 160.0 | -133.0 | PERSISTENT_UP, ACCELERATION, ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 11563.0 | -238.0 | -1031.0 | -119.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ps_gen / CHANGE_POINT** — value=-7.0, Δ1=12.0, Δ12=160.0, accel=-133.0
- **ps_gen / PERSISTENT_UP** — value=-7.0, Δ1=12.0, Δ12=160.0, accel=-133.0
- **ps_gen / ACCELERATION** — value=-7.0, Δ1=12.0, Δ12=160.0, accel=-133.0
- **ps_gen / ROBUST_OUTLIER** — value=-7.0, Δ1=12.0, Δ12=160.0, accel=-133.0
- **margin / CHANGE_POINT** — value=37032.0, Δ1=0.0, Δ12=-3354.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=37032.0, Δ1=0.0, Δ12=-3354.0, accel=0.0
- **wind_forecast / ROBUST_OUTLIER** — value=13007.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **ind_generation / CHANGE_POINT** — value=14934.0, Δ1=0.0, Δ12=-11181.0, accel=0.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
