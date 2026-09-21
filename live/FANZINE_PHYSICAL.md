# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T09:09:41.405520Z  
Source heartbeat: 2026-09-21T09:09:40.108229Z  

## Regime: **LOOSE**
Reason: margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21269.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 9277.0 | 0.0 | 483.0 | 0.0 |  |
| Wind generation | 3519.0 | -24.0 | -834.0 | -24.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Residual-load proxy | 10833.0 | 0.0 | -483.0 | 0.0 |  |
| Indicated margin | 38223.0 | 0.0 | -31.0 | 0.0 | ROBUST_OUTLIER |
| Indicated imbalance | -2000.0 | 0.0 | 1297.0 | 0.0 | ROBUST_OUTLIER |
| Interconnector net | 10652.0 | -13.0 | -28.0 | -13.0 | PERSISTENT_DOWN, ACCELERATION, CHANGE_POINT |
| CCGT generation | 8719.0 | -107.0 | -23.0 | -107.0 | PERSISTENT_DOWN, ACCELERATION |
| Nuclear generation | 3498.0 | 7.0 | 2.0 | 7.0 | PERSISTENT_UP, ACCELERATION, CHANGE_POINT |
| Pumped-storage generation | 0.0 | -204.0 | 10.0 | -204.0 | REVERSAL, ACCELERATION, CHANGE_POINT |
| Thermal base | 12217.0 | -100.0 | -21.0 | -100.0 | PERSISTENT_DOWN, ACCELERATION |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_generation / ROBUST_OUTLIER** — value=19269.0, Δ1=0.0, Δ12=1297.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=38223.0, Δ1=0.0, Δ12=-31.0, accel=0.0
- **ind_demand / ROBUST_OUTLIER** — value=-12837.0, Δ1=0.0, Δ12=-4.0, accel=0.0
- **imbalance / ROBUST_OUTLIER** — value=-2000.0, Δ1=0.0, Δ12=1297.0, accel=0.0
- **wind_gen / CHANGE_POINT** — value=3519.0, Δ1=-24.0, Δ12=-834.0, accel=-24.0
- **nuclear_gen / CHANGE_POINT** — value=3498.0, Δ1=7.0, Δ12=2.0, accel=7.0
- **interconnector_net / CHANGE_POINT** — value=10652.0, Δ1=-13.0, Δ12=-28.0, accel=-13.0
- **ps_gen / CHANGE_POINT** — value=0.0, Δ1=-204.0, Δ12=10.0, accel=-204.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
