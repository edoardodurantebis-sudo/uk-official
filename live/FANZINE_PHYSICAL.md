# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-23T07:57:57.519041Z  
Source heartbeat: 2026-09-23T07:57:56.243020Z  

## Regime: **LOOSE**
Reason: residual low; margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 19504.0 | 0.0 | -1169.0 | 0.0 | PERSISTENT_DOWN |
| TS demand forecast | 20004.0 | 0.0 | -1169.0 | 0.0 | PERSISTENT_DOWN |
| Wind forecast | 7305.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 10305.0 | 43.0 | 256.0 | 12.0 | PERSISTENT_UP |
| Residual-load proxy | 12199.0 | 0.0 | -1169.0 | 0.0 | PERSISTENT_DOWN, ROBUST_OUTLIER |
| Indicated margin | 38775.0 | 0.0 | -10.0 | 0.0 |  |
| Indicated imbalance | -7454.0 | 0.0 | 14.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Interconnector net | 3794.0 | -5.0 | 4525.0 | -5.0 | REVERSAL, CHANGE_POINT |
| CCGT generation | 7353.0 | -92.0 | -2541.0 | 153.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Nuclear generation | 3804.0 | -1.0 | 0.0 | 4.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | -19.0 | 1.0 | 114.0 | 3.0 | ROBUST_OUTLIER |
| Thermal base | 11157.0 | -93.0 | -2541.0 | 157.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| Frequency | 50.117 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / CHANGE_POINT** — value=-12650.0, Δ1=0.0, Δ12=-243.0, accel=0.0
- **ind_demand / ROBUST_OUTLIER** — value=-12650.0, Δ1=0.0, Δ12=-243.0, accel=0.0
- **ps_gen / ROBUST_OUTLIER** — value=-19.0, Δ1=1.0, Δ12=114.0, accel=3.0
- **ind_generation / CHANGE_POINT** — value=13965.0, Δ1=0.0, Δ12=260.0, accel=0.0
- **ind_generation / ROBUST_OUTLIER** — value=13965.0, Δ1=0.0, Δ12=260.0, accel=0.0
- **imbalance / CHANGE_POINT** — value=-7454.0, Δ1=0.0, Δ12=14.0, accel=0.0
- **imbalance / ROBUST_OUTLIER** — value=-7454.0, Δ1=0.0, Δ12=14.0, accel=0.0
- **biomass_gen / REVERSAL** — value=2564.0, Δ1=-5.0, Δ12=5.0, accel=-19.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
