# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T18:30:48.779269Z  
Source heartbeat: 2026-09-22T18:30:46.796813Z  

## Regime: **LOOSE**
Reason: residual low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13535.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 1694.0 | 40.0 | 325.0 | 24.0 | PERSISTENT_UP, CHANGE_POINT |
| Residual-load proxy | 7138.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| Indicated margin | 37157.0 | 0.0 | -19.0 | 0.0 | PERSISTENT_DOWN |
| Indicated imbalance | -8008.0 | 0.0 | -70.0 | 68.0 | PERSISTENT_DOWN, ACCELERATION, ROBUST_OUTLIER, CHANGE_POINT |
| Interconnector net | 5830.0 | -3.0 | -698.0 | 45.0 | PERSISTENT_DOWN, CHANGE_POINT |
| CCGT generation | 15134.0 | -9.0 | -1.0 | 21.0 | PERSISTENT_DOWN, ACCELERATION |
| Nuclear generation | 3740.0 | 3.0 | 8.0 | -1.0 | PERSISTENT_UP, ROBUST_OUTLIER |
| Pumped-storage generation | 1360.0 | 2.0 | -148.0 | 4.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 18874.0 | -6.0 | 7.0 | 20.0 | REVERSAL, ACCELERATION |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **residual_proxy / ROBUST_OUTLIER** — value=7138.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=1360.0, Δ1=2.0, Δ12=-148.0, accel=4.0
- **ps_gen / REVERSAL** — value=1360.0, Δ1=2.0, Δ12=-148.0, accel=4.0
- **ps_gen / ROBUST_OUTLIER** — value=1360.0, Δ1=2.0, Δ12=-148.0, accel=4.0
- **biomass_gen / CHANGE_POINT** — value=2842.0, Δ1=0.0, Δ12=-65.0, accel=-2.0
- **imbalance / CHANGE_POINT** — value=-8008.0, Δ1=0.0, Δ12=-70.0, accel=68.0
- **ind_generation / CHANGE_POINT** — value=13165.0, Δ1=0.0, Δ12=-71.0, accel=0.0
- **interconnector_net / CHANGE_POINT** — value=5830.0, Δ1=-3.0, Δ12=-698.0, accel=45.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
