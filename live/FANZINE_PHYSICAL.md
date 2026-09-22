# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T18:56:25.863546Z  
Source heartbeat: 2026-09-22T18:56:24.650301Z  

## Regime: **LOOSE**
Reason: residual low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13535.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 1709.0 | 15.0 | 337.0 | 32.0 | CHANGE_POINT |
| Residual-load proxy | 7138.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| Indicated margin | 37168.0 | 0.0 | -5.0 | -11.0 | ACCELERATION |
| Indicated imbalance | -7982.0 | 0.0 | -42.0 | -26.0 | ACCELERATION, CHANGE_POINT |
| Interconnector net | 5205.0 | -37.0 | -1195.0 | 7.0 | PERSISTENT_DOWN, CHANGE_POINT |
| CCGT generation | 15401.0 | 52.0 | 273.0 | 9.0 | PERSISTENT_UP |
| Nuclear generation | 3729.0 | 0.0 | 0.0 | 0.0 |  |
| Pumped-storage generation | 1509.0 | -1.0 | 0.0 | -1.0 | PERSISTENT_DOWN, ACCELERATION, ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 19130.0 | 52.0 | 273.0 | 9.0 | PERSISTENT_UP |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **residual_proxy / ROBUST_OUTLIER** — value=7138.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=1509.0, Δ1=-1.0, Δ12=0.0, accel=-1.0
- **ps_gen / PERSISTENT_DOWN** — value=1509.0, Δ1=-1.0, Δ12=0.0, accel=-1.0
- **ps_gen / ACCELERATION** — value=1509.0, Δ1=-1.0, Δ12=0.0, accel=-1.0
- **ps_gen / ROBUST_OUTLIER** — value=1509.0, Δ1=-1.0, Δ12=0.0, accel=-1.0
- **imbalance / CHANGE_POINT** — value=-7982.0, Δ1=0.0, Δ12=-42.0, accel=-26.0
- **ind_generation / CHANGE_POINT** — value=13192.0, Δ1=0.0, Δ12=-41.0, accel=-27.0
- **interconnector_net / CHANGE_POINT** — value=5205.0, Δ1=-37.0, Δ12=-1195.0, accel=7.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
