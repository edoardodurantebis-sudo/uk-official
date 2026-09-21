# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T03:47:18.446713Z  
Source heartbeat: 2026-09-21T03:47:17.001381Z  

## Regime: **LOOSE**
Reason: margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 20610.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 8021.0 | 0.0 | 6418.0 | 0.0 |  |
| Wind generation | 3743.0 | 27.0 | 15.0 | 81.0 | ACCELERATION |
| Residual-load proxy | 12089.0 | 0.0 | -6418.0 | 0.0 |  |
| Indicated margin | 37568.0 | 0.0 | 8.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Indicated imbalance | -4820.0 | 0.0 | 45.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 10000.0 | 12.0 | -2523.0 | 34.0 | REVERSAL, CHANGE_POINT |
| CCGT generation | 5584.0 | -94.0 | 791.0 | -20.0 | REVERSAL |
| Nuclear generation | 3334.0 | 0.0 | -7.0 | 6.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | -12.0 | 0.0 | 118.0 | 0.0 | CHANGE_POINT |
| Thermal base | 8918.0 | -94.0 | 784.0 | -14.0 | REVERSAL |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **margin / CHANGE_POINT** — value=37568.0, Δ1=0.0, Δ12=8.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=37568.0, Δ1=0.0, Δ12=8.0, accel=0.0
- **imbalance / CHANGE_POINT** — value=-4820.0, Δ1=0.0, Δ12=45.0, accel=0.0
- **ind_generation / CHANGE_POINT** — value=15790.0, Δ1=0.0, Δ12=45.0, accel=0.0
- **interconnector_net / CHANGE_POINT** — value=10000.0, Δ1=12.0, Δ12=-2523.0, accel=34.0
- **ps_gen / CHANGE_POINT** — value=-12.0, Δ1=0.0, Δ12=118.0, accel=0.0
- **wind_gen / ACCELERATION** — value=3743.0, Δ1=27.0, Δ12=15.0, accel=81.0
- **interconnector_net / REVERSAL** — value=10000.0, Δ1=12.0, Δ12=-2523.0, accel=34.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
