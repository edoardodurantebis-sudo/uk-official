# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T09:05:28.682509Z  
Source heartbeat: 2026-09-21T09:05:27.338721Z  

## Regime: **LOOSE**
Reason: margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | -982.0 | 0.0 |  |
| TS demand forecast | 21269.0 | 0.0 | -323.0 | 0.0 |  |
| Wind forecast | 9277.0 | 0.0 | 483.0 | 0.0 |  |
| Wind generation | 3543.0 | 0.0 | -908.0 | 68.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Residual-load proxy | 10833.0 | 0.0 | -1465.0 | 0.0 |  |
| Indicated margin | 38223.0 | 0.0 | -31.0 | 0.0 | ROBUST_OUTLIER |
| Indicated imbalance | -2000.0 | 0.0 | 1297.0 | 0.0 | ROBUST_OUTLIER |
| Interconnector net | 10665.0 | 0.0 | -15.0 | -12.0 | ACCELERATION, CHANGE_POINT |
| CCGT generation | 8826.0 | 0.0 | 75.0 | 20.0 |  |
| Nuclear generation | 3491.0 | 0.0 | -8.0 | 2.0 | PERSISTENT_DOWN |
| Pumped-storage generation | 204.0 | 0.0 | 214.0 | 80.0 | ACCELERATION, CHANGE_POINT |
| Thermal base | 12317.0 | 0.0 | 67.0 | 22.0 |  |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_generation / ROBUST_OUTLIER** — value=19269.0, Δ1=0.0, Δ12=1297.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=38223.0, Δ1=0.0, Δ12=-31.0, accel=0.0
- **ind_demand / ROBUST_OUTLIER** — value=-12837.0, Δ1=0.0, Δ12=-4.0, accel=0.0
- **imbalance / ROBUST_OUTLIER** — value=-2000.0, Δ1=0.0, Δ12=1297.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=204.0, Δ1=0.0, Δ12=214.0, accel=80.0
- **wind_gen / CHANGE_POINT** — value=3543.0, Δ1=0.0, Δ12=-908.0, accel=68.0
- **interconnector_net / CHANGE_POINT** — value=10665.0, Δ1=0.0, Δ12=-15.0, accel=-12.0
- **ps_gen / ACCELERATION** — value=204.0, Δ1=0.0, Δ12=214.0, accel=80.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
