# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T19:51:41.775230Z  
Source heartbeat: 2026-09-22T19:51:40.252574Z  

## Regime: **BALANCED**
Reason: residual low; margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13612.0 | 0.0 | 77.0 | 0.0 |  |
| Wind generation | 1872.0 | 36.0 | 145.0 | 11.0 | PERSISTENT_UP, CHANGE_POINT |
| Residual-load proxy | 7061.0 | 0.0 | -77.0 | 0.0 | ROBUST_OUTLIER |
| Indicated margin | 37124.0 | 2.0 | -44.0 | 2.0 | REVERSAL, CHANGE_POINT |
| Indicated imbalance | -8035.0 | 0.0 | -53.0 | 0.0 | ROBUST_OUTLIER |
| Interconnector net | 6953.0 | -1.0 | 1434.0 | -1.0 | REVERSAL |
| CCGT generation | 15339.0 | -68.0 | -33.0 | -38.0 | PERSISTENT_DOWN, ACCELERATION |
| Nuclear generation | 3736.0 | 5.0 | 10.0 | 0.0 | PERSISTENT_UP |
| Pumped-storage generation | 1128.0 | 0.0 | -384.0 | 23.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Thermal base | 19075.0 | -63.0 | -23.0 | -38.0 | PERSISTENT_DOWN, ACCELERATION |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **residual_proxy / ROBUST_OUTLIER** — value=7061.0, Δ1=0.0, Δ12=-77.0, accel=0.0
- **imbalance / ROBUST_OUTLIER** — value=-8035.0, Δ1=0.0, Δ12=-53.0, accel=0.0
- **ind_generation / PERSISTENT_DOWN** — value=13137.0, Δ1=-1.0, Δ12=-55.0, accel=-1.0
- **ind_generation / ROBUST_OUTLIER** — value=13137.0, Δ1=-1.0, Δ12=-55.0, accel=-1.0
- **margin / CHANGE_POINT** — value=37124.0, Δ1=2.0, Δ12=-44.0, accel=2.0
- **wind_gen / CHANGE_POINT** — value=1872.0, Δ1=36.0, Δ12=145.0, accel=11.0
- **biomass_gen / REVERSAL** — value=2851.0, Δ1=-3.0, Δ12=16.0, accel=-4.0
- **ps_gen / CHANGE_POINT** — value=1128.0, Δ1=0.0, Δ12=-384.0, accel=23.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
