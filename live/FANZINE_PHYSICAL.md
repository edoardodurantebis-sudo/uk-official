# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T16:44:42.850518Z  
Source heartbeat: 2026-09-22T16:44:41.356627Z  

## Regime: **LOOSE**
Reason: residual low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13535.0 | 0.0 | 453.0 | 0.0 |  |
| Wind generation | 1311.0 | 0.0 | -88.0 | -10.0 |  |
| Residual-load proxy | 7138.0 | 0.0 | -453.0 | 0.0 | ROBUST_OUTLIER |
| Indicated margin | 37153.0 | 0.0 | -32.0 | 0.0 |  |
| Indicated imbalance | -7943.0 | 0.0 | -1.0 | 0.0 |  |
| Interconnector net | 6808.0 | 0.0 | -1806.0 | 8.0 | PERSISTENT_DOWN, ROBUST_OUTLIER, CHANGE_POINT |
| CCGT generation | 14830.0 | 0.0 | 409.0 | -108.0 | PERSISTENT_UP |
| Nuclear generation | 3728.0 | 0.0 | -5.0 | 1.0 | PERSISTENT_DOWN |
| Pumped-storage generation | 1507.0 | 0.0 | 1222.0 | -60.0 | PERSISTENT_UP, ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 18558.0 | 0.0 | 404.0 | -107.0 | PERSISTENT_UP |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **residual_proxy / ROBUST_OUTLIER** — value=7138.0, Δ1=0.0, Δ12=-453.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=1507.0, Δ1=0.0, Δ12=1222.0, accel=-60.0
- **ps_gen / PERSISTENT_UP** — value=1507.0, Δ1=0.0, Δ12=1222.0, accel=-60.0
- **ps_gen / ROBUST_OUTLIER** — value=1507.0, Δ1=0.0, Δ12=1222.0, accel=-60.0
- **interconnector_net / CHANGE_POINT** — value=6808.0, Δ1=0.0, Δ12=-1806.0, accel=8.0
- **interconnector_net / PERSISTENT_DOWN** — value=6808.0, Δ1=0.0, Δ12=-1806.0, accel=8.0
- **interconnector_net / ROBUST_OUTLIER** — value=6808.0, Δ1=0.0, Δ12=-1806.0, accel=8.0
- **thermal_base / PERSISTENT_UP** — value=18558.0, Δ1=0.0, Δ12=404.0, accel=-107.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
