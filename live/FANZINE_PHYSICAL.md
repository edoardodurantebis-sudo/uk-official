# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T17:42:58.006971Z  
Source heartbeat: 2026-09-21T17:42:56.619354Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20959.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21459.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 8620.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 3515.0 | 62.0 | 191.0 | 4.0 | PERSISTENT_UP |
| Residual-load proxy | 12339.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 36168.0 | 0.0 | -106.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Indicated imbalance | -3018.0 | 0.0 | 53.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 6619.0 | 1.0 | -3110.0 | 2.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| CCGT generation | 14041.0 | 49.0 | 708.0 | 62.0 | PERSISTENT_UP |
| Nuclear generation | 3504.0 | -3.0 | -3.0 | 2.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | 423.0 | -113.0 | 322.0 | 179.0 | REVERSAL, ACCELERATION, CHANGE_POINT |
| Thermal base | 17545.0 | 46.0 | 705.0 | 64.0 | PERSISTENT_UP |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **interconnector_net / CHANGE_POINT** — value=6619.0, Δ1=1.0, Δ12=-3110.0, accel=2.0
- **interconnector_net / REVERSAL** — value=6619.0, Δ1=1.0, Δ12=-3110.0, accel=2.0
- **interconnector_net / ROBUST_OUTLIER** — value=6619.0, Δ1=1.0, Δ12=-3110.0, accel=2.0
- **margin / CHANGE_POINT** — value=36168.0, Δ1=0.0, Δ12=-106.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=423.0, Δ1=-113.0, Δ12=322.0, accel=179.0
- **margin / ROBUST_OUTLIER** — value=36168.0, Δ1=0.0, Δ12=-106.0, accel=0.0
- **ind_generation / CHANGE_POINT** — value=18441.0, Δ1=0.0, Δ12=53.0, accel=0.0
- **imbalance / CHANGE_POINT** — value=-3018.0, Δ1=0.0, Δ12=53.0, accel=0.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
