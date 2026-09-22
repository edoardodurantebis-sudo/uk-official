# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T18:05:22.439405Z  
Source heartbeat: 2026-09-22T18:05:21.433510Z  

## Regime: **LOOSE**
Reason: residual low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13535.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 1372.0 | 0.0 | 30.0 | -1.0 | CHANGE_POINT |
| Residual-load proxy | 7138.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| Indicated margin | 37173.0 | 0.0 | 22.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -7940.0 | 0.0 | 14.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 6400.0 | 0.0 | -210.0 | 66.0 | PERSISTENT_DOWN |
| CCGT generation | 15128.0 | 0.0 | -265.0 | -54.0 |  |
| Nuclear generation | 3729.0 | 0.0 | -2.0 | 2.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | 1509.0 | 0.0 | 1.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 18857.0 | 0.0 | -267.0 | -52.0 |  |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **residual_proxy / ROBUST_OUTLIER** — value=7138.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=1509.0, Δ1=0.0, Δ12=1.0, accel=0.0
- **ps_gen / ROBUST_OUTLIER** — value=1509.0, Δ1=0.0, Δ12=1.0, accel=0.0
- **biomass_gen / CHANGE_POINT** — value=2802.0, Δ1=0.0, Δ12=-113.0, accel=45.0
- **biomass_gen / PERSISTENT_DOWN** — value=2802.0, Δ1=0.0, Δ12=-113.0, accel=45.0
- **biomass_gen / ACCELERATION** — value=2802.0, Δ1=0.0, Δ12=-113.0, accel=45.0
- **biomass_gen / ROBUST_OUTLIER** — value=2802.0, Δ1=0.0, Δ12=-113.0, accel=45.0
- **wind_gen / CHANGE_POINT** — value=1372.0, Δ1=0.0, Δ12=30.0, accel=-1.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
