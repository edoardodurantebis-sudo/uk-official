# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T23:26:49.295145Z  
Source heartbeat: 2026-09-21T23:26:48.019551Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20959.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21459.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 8621.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 3521.0 | -5.0 | -216.0 | 60.0 | PERSISTENT_DOWN |
| Residual-load proxy | 12338.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 36167.0 | 0.0 | -65.0 | 67.0 | PERSISTENT_DOWN, ACCELERATION |
| Indicated imbalance | -2016.0 | 0.0 | 483.0 | -477.0 | PERSISTENT_UP, ACCELERATION, CHANGE_POINT |
| Interconnector net | 3147.0 | 19.0 | 249.0 | 21.0 |  |
| CCGT generation | 11162.0 | 74.0 | -173.0 | 39.0 | REVERSAL |
| Nuclear generation | 3650.0 | 5.0 | 14.0 | 3.0 | PERSISTENT_UP, ROBUST_OUTLIER |
| Pumped-storage generation | -282.0 | -53.0 | -275.0 | 38.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Thermal base | 14812.0 | 79.0 | -159.0 | 42.0 | REVERSAL |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / PERSISTENT_DOWN** — value=-12381.0, Δ1=0.0, Δ12=-123.0, accel=2.0
- **ind_demand / ROBUST_OUTLIER** — value=-12381.0, Δ1=0.0, Δ12=-123.0, accel=2.0
- **nuclear_gen / PERSISTENT_UP** — value=3650.0, Δ1=5.0, Δ12=14.0, accel=3.0
- **nuclear_gen / ROBUST_OUTLIER** — value=3650.0, Δ1=5.0, Δ12=14.0, accel=3.0
- **imbalance / CHANGE_POINT** — value=-2016.0, Δ1=0.0, Δ12=483.0, accel=-477.0
- **ind_generation / CHANGE_POINT** — value=19443.0, Δ1=0.0, Δ12=483.0, accel=-477.0
- **ps_gen / CHANGE_POINT** — value=-282.0, Δ1=-53.0, Δ12=-275.0, accel=38.0
- **biomass_gen / CHANGE_POINT** — value=3005.0, Δ1=2.0, Δ12=-32.0, accel=3.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
