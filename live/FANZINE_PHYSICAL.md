# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-20T18:34:36.905329Z  
Source heartbeat: 2026-09-20T18:34:35.475130Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 20610.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 2115.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 6196.0 | -107.0 | -870.0 | -107.0 | PERSISTENT_DOWN |
| Residual-load proxy | 17995.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 35430.0 | 0.0 | -355.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -5158.0 | 0.0 | 14.0 | 0.0 | PERSISTENT_UP, CHANGE_POINT |
| Interconnector net | 9874.0 | -60.0 | -169.0 | -60.0 | PERSISTENT_DOWN, ACCELERATION |
| CCGT generation | 9115.0 | 5.0 | 436.0 | 5.0 | PERSISTENT_UP, ROBUST_OUTLIER |
| Nuclear generation | 3338.0 | -6.0 | 0.0 | -6.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | 222.0 | 0.0 | 152.0 | 0.0 |  |
| Thermal base | 12453.0 | -1.0 | 436.0 | -1.0 | REVERSAL, ROBUST_OUTLIER |
| Frequency | 49.922 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ccgt_gen / PERSISTENT_UP** — value=9115.0, Δ1=5.0, Δ12=436.0, accel=5.0
- **ccgt_gen / ROBUST_OUTLIER** — value=9115.0, Δ1=5.0, Δ12=436.0, accel=5.0
- **thermal_base / REVERSAL** — value=12453.0, Δ1=-1.0, Δ12=436.0, accel=-1.0
- **thermal_base / ROBUST_OUTLIER** — value=12453.0, Δ1=-1.0, Δ12=436.0, accel=-1.0
- **biomass_gen / CHANGE_POINT** — value=2286.0, Δ1=-14.0, Δ12=31.0, accel=-14.0
- **margin / CHANGE_POINT** — value=35430.0, Δ1=0.0, Δ12=-355.0, accel=0.0
- **biomass_gen / REVERSAL** — value=2286.0, Δ1=-14.0, Δ12=31.0, accel=-14.0
- **biomass_gen / ACCELERATION** — value=2286.0, Δ1=-14.0, Δ12=31.0, accel=-14.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
