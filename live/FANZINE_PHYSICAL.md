# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-23T10:39:21.485197Z  
Source heartbeat: 2026-09-23T10:39:20.220249Z  

## Regime: **LOOSE**
Reason: margin high; wind rising

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20282.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21028.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 7178.0 | 0.0 | 182.0 | 0.0 | PERSISTENT_UP |
| Wind generation | 9520.0 | -45.0 | -23.0 | -45.0 | PERSISTENT_DOWN, ACCELERATION |
| Residual-load proxy | 13104.0 | 0.0 | -182.0 | 0.0 | PERSISTENT_DOWN |
| Indicated margin | 40780.0 | 0.0 | 57.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Indicated imbalance | -2300.0 | 0.0 | 2815.0 | 0.0 | ROBUST_OUTLIER |
| Interconnector net | 11469.0 | -15.0 | 98.0 | -15.0 | REVERSAL |
| CCGT generation | 2134.0 | 14.0 | -330.0 | 14.0 | REVERSAL |
| Nuclear generation | 3797.0 | -8.0 | 186.0 | -8.0 | REVERSAL, CHANGE_POINT |
| Pumped-storage generation | -861.0 | 9.0 | -292.0 | 9.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 5931.0 | 6.0 | -144.0 | 6.0 | REVERSAL |
| Frequency | 50.117 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / CHANGE_POINT** — value=-13737.0, Δ1=0.0, Δ12=-1055.0, accel=0.0
- **ind_demand / ROBUST_OUTLIER** — value=-13737.0, Δ1=0.0, Δ12=-1055.0, accel=0.0
- **ind_generation / ROBUST_OUTLIER** — value=18728.0, Δ1=0.0, Δ12=2815.0, accel=0.0
- **margin / CHANGE_POINT** — value=40780.0, Δ1=0.0, Δ12=57.0, accel=0.0
- **imbalance / ROBUST_OUTLIER** — value=-2300.0, Δ1=0.0, Δ12=2815.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=40780.0, Δ1=0.0, Δ12=57.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=-861.0, Δ1=9.0, Δ12=-292.0, accel=9.0
- **ps_gen / REVERSAL** — value=-861.0, Δ1=9.0, Δ12=-292.0, accel=9.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
