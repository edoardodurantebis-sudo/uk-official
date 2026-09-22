# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-22T02:46:17.699143Z  
Source heartbeat: 2026-09-22T02:46:16.901688Z  

## Regime: **LOOSE**
Reason: margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20959.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21459.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 9503.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 4153.0 | 22.0 | 509.0 | 7.0 | PERSISTENT_UP, ROBUST_OUTLIER, CHANGE_POINT |
| Residual-load proxy | 11456.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 37822.0 | 0.0 | 1654.0 | 0.0 | ROBUST_OUTLIER |
| Indicated imbalance | -2655.0 | 0.0 | 52.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 2666.0 | 26.0 | -2368.0 | 16.0 | REVERSAL |
| CCGT generation | 10672.0 | -17.0 | 139.0 | 38.0 | REVERSAL |
| Nuclear generation | 3653.0 | 0.0 | -5.0 | 0.0 | PERSISTENT_DOWN |
| Pumped-storage generation | -165.0 | 0.0 | 118.0 | -2.0 | CHANGE_POINT |
| Thermal base | 14325.0 | -17.0 | 134.0 | 38.0 | REVERSAL |
| Frequency | 50.089 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **margin / ROBUST_OUTLIER** — value=37822.0, Δ1=0.0, Δ12=1654.0, accel=0.0
- **wind_gen / CHANGE_POINT** — value=4153.0, Δ1=22.0, Δ12=509.0, accel=7.0
- **ind_demand / CHANGE_POINT** — value=-12497.0, Δ1=0.0, Δ12=-80.0, accel=0.0
- **wind_gen / PERSISTENT_UP** — value=4153.0, Δ1=22.0, Δ12=509.0, accel=7.0
- **wind_gen / ROBUST_OUTLIER** — value=4153.0, Δ1=22.0, Δ12=509.0, accel=7.0
- **imbalance / CHANGE_POINT** — value=-2655.0, Δ1=0.0, Δ12=52.0, accel=0.0
- **ind_generation / CHANGE_POINT** — value=18804.0, Δ1=0.0, Δ12=52.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=-165.0, Δ1=0.0, Δ12=118.0, accel=-2.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
