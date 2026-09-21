# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T00:11:54.449218Z  
Source heartbeat: 2026-09-21T00:11:53.168385Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 20610.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 1603.0 | 0.0 | -123.0 | 0.0 |  |
| Wind generation | 5070.0 | -76.0 | -706.0 | -19.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Residual-load proxy | 18507.0 | 0.0 | 123.0 | 0.0 |  |
| Indicated margin | 35822.0 | 0.0 | 11.0 | 0.0 |  |
| Indicated imbalance | -5229.0 | 0.0 | -9.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 10226.0 | 156.0 | 908.0 | -399.0 | PERSISTENT_UP, ACCELERATION |
| CCGT generation | 5826.0 | -111.0 | -216.0 | -30.0 | PERSISTENT_DOWN |
| Nuclear generation | 3336.0 | 0.0 | -1.0 | -2.0 | ACCELERATION |
| Pumped-storage generation | -12.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER |
| Thermal base | 9162.0 | -111.0 | -217.0 | -32.0 | PERSISTENT_DOWN |
| Frequency | 50.105 | 0.0 | 0.18299999999999983 | 0.0 | PERSISTENT_UP |

## Active live patterns

- **ps_gen / ROBUST_OUTLIER** — value=-12.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **wind_gen / CHANGE_POINT** — value=5070.0, Δ1=-76.0, Δ12=-706.0, accel=-19.0
- **imbalance / CHANGE_POINT** — value=-5229.0, Δ1=0.0, Δ12=-9.0, accel=0.0
- **ind_generation / CHANGE_POINT** — value=15381.0, Δ1=0.0, Δ12=-8.0, accel=0.0
- **wind_gen / PERSISTENT_DOWN** — value=5070.0, Δ1=-76.0, Δ12=-706.0, accel=-19.0
- **biomass_gen / REVERSAL** — value=2992.0, Δ1=-13.0, Δ12=10.0, accel=6.0
- **biomass_gen / ACCELERATION** — value=2992.0, Δ1=-13.0, Δ12=10.0, accel=6.0
- **ccgt_gen / PERSISTENT_DOWN** — value=5826.0, Δ1=-111.0, Δ12=-216.0, accel=-30.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
