# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-23T08:02:13.063245Z  
Source heartbeat: 2026-09-23T08:02:12.092833Z  

## Regime: **LOOSE**
Reason: residual low; margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 19504.0 | 0.0 | -1169.0 | 0.0 |  |
| TS demand forecast | 20004.0 | 0.0 | -1169.0 | 0.0 |  |
| Wind forecast | 7305.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 10389.0 | 84.0 | 197.0 | 41.0 | PERSISTENT_UP |
| Residual-load proxy | 12199.0 | 0.0 | -1169.0 | 0.0 | ROBUST_OUTLIER |
| Indicated margin | 38775.0 | 0.0 | -10.0 | 0.0 |  |
| Indicated imbalance | -7454.0 | 0.0 | 14.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Interconnector net | 4554.0 | 760.0 | 4247.0 | 765.0 | PERSISTENT_UP, CHANGE_POINT |
| CCGT generation | 7389.0 | 36.0 | -2247.0 | 128.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| Nuclear generation | 3798.0 | -6.0 | -8.0 | -5.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | -19.0 | 0.0 | 270.0 | -1.0 | ROBUST_OUTLIER |
| Thermal base | 11187.0 | 30.0 | -2255.0 | 123.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| Frequency | 50.117 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / CHANGE_POINT** — value=-12650.0, Δ1=0.0, Δ12=-243.0, accel=0.0
- **ind_demand / ROBUST_OUTLIER** — value=-12650.0, Δ1=0.0, Δ12=-243.0, accel=0.0
- **ps_gen / ROBUST_OUTLIER** — value=-19.0, Δ1=0.0, Δ12=270.0, accel=-1.0
- **ind_generation / ROBUST_OUTLIER** — value=13965.0, Δ1=0.0, Δ12=260.0, accel=0.0
- **imbalance / CHANGE_POINT** — value=-7454.0, Δ1=0.0, Δ12=14.0, accel=0.0
- **biomass_gen / CHANGE_POINT** — value=2477.0, Δ1=-87.0, Δ12=-80.0, accel=-82.0
- **imbalance / ROBUST_OUTLIER** — value=-7454.0, Δ1=0.0, Δ12=14.0, accel=0.0
- **biomass_gen / PERSISTENT_DOWN** — value=2477.0, Δ1=-87.0, Δ12=-80.0, accel=-82.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
