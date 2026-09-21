# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T18:47:36.241778Z  
Source heartbeat: 2026-09-21T18:47:34.928120Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20959.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21459.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 8620.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 3716.0 | -87.0 | 193.0 | -103.0 | REVERSAL, ACCELERATION, CHANGE_POINT |
| Residual-load proxy | 12339.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 36192.0 | 0.0 | 24.0 | 0.0 | ROBUST_OUTLIER |
| Indicated imbalance | -3124.0 | 0.0 | -82.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 7162.0 | 1.0 | 543.0 | 1.0 | ROBUST_OUTLIER |
| CCGT generation | 13571.0 | 22.0 | -313.0 | 53.0 | REVERSAL |
| Nuclear generation | 3506.0 | -6.0 | -5.0 | -11.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | 601.0 | 0.0 | 153.0 | -1.0 | PERSISTENT_UP |
| Thermal base | 17077.0 | 16.0 | -318.0 | 42.0 | REVERSAL |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **interconnector_net / ROBUST_OUTLIER** — value=7162.0, Δ1=1.0, Δ12=543.0, accel=1.0
- **margin / ROBUST_OUTLIER** — value=36192.0, Δ1=0.0, Δ12=24.0, accel=0.0
- **wind_gen / CHANGE_POINT** — value=3716.0, Δ1=-87.0, Δ12=193.0, accel=-103.0
- **ind_generation / CHANGE_POINT** — value=18335.0, Δ1=0.0, Δ12=-82.0, accel=0.0
- **imbalance / CHANGE_POINT** — value=-3124.0, Δ1=0.0, Δ12=-82.0, accel=0.0
- **ps_gen / PERSISTENT_UP** — value=601.0, Δ1=0.0, Δ12=153.0, accel=-1.0
- **thermal_base / REVERSAL** — value=17077.0, Δ1=16.0, Δ12=-318.0, accel=42.0
- **ccgt_gen / REVERSAL** — value=13571.0, Δ1=22.0, Δ12=-313.0, accel=53.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
