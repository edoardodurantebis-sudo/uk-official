# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T17:18:43.373329Z  
Source heartbeat: 2026-09-22T17:18:42.076917Z  

## Regime: **LOOSE**
Reason: residual low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13535.0 | 0.0 | 453.0 | 0.0 |  |
| Wind generation | 1345.0 | 3.0 | 40.0 | 16.0 | ACCELERATION |
| Residual-load proxy | 7138.0 | 0.0 | -453.0 | 0.0 | ROBUST_OUTLIER |
| Indicated margin | 37151.0 | 0.0 | -2.0 | 0.0 |  |
| Indicated imbalance | -7954.0 | 0.0 | -11.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 6584.0 | -26.0 | -1114.0 | 276.0 | PERSISTENT_DOWN |
| CCGT generation | 15400.0 | 7.0 | 775.0 | -114.0 | PERSISTENT_UP, CHANGE_POINT |
| Nuclear generation | 3730.0 | -1.0 | 0.0 | -4.0 | ACCELERATION |
| Pumped-storage generation | 1508.0 | 0.0 | 151.0 | 0.0 | ROBUST_OUTLIER |
| Thermal base | 19130.0 | 6.0 | 775.0 | -118.0 | PERSISTENT_UP, CHANGE_POINT |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **residual_proxy / ROBUST_OUTLIER** — value=7138.0, Δ1=0.0, Δ12=-453.0, accel=0.0
- **ps_gen / ROBUST_OUTLIER** — value=1508.0, Δ1=0.0, Δ12=151.0, accel=0.0
- **ccgt_gen / CHANGE_POINT** — value=15400.0, Δ1=7.0, Δ12=775.0, accel=-114.0
- **thermal_base / CHANGE_POINT** — value=19130.0, Δ1=6.0, Δ12=775.0, accel=-118.0
- **interconnector_net / PERSISTENT_DOWN** — value=6584.0, Δ1=-26.0, Δ12=-1114.0, accel=276.0
- **ind_generation / CHANGE_POINT** — value=13219.0, Δ1=0.0, Δ12=-11.0, accel=0.0
- **imbalance / CHANGE_POINT** — value=-7954.0, Δ1=0.0, Δ12=-11.0, accel=0.0
- **ccgt_gen / PERSISTENT_UP** — value=15400.0, Δ1=7.0, Δ12=775.0, accel=-114.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
