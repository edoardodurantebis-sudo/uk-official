# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T12:10:43.206593Z  
Source heartbeat: 2026-09-21T12:10:42.110075Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 21004.0 | 0.0 | -104.0 | 0.0 | CHANGE_POINT |
| TS demand forecast | 21504.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 8923.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 3724.0 | 49.0 | 403.0 | -2.0 | PERSISTENT_UP, CHANGE_POINT |
| Residual-load proxy | 12081.0 | 0.0 | -104.0 | 0.0 | CHANGE_POINT |
| Indicated margin | 36673.0 | 0.0 | 178.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -3014.0 | 0.0 | 857.0 | 0.0 |  |
| Interconnector net | 11303.0 | -29.0 | 68.0 | 6.0 | REVERSAL |
| CCGT generation | 6648.0 | -9.0 | -74.0 | -120.0 | ACCELERATION, ROBUST_OUTLIER |
| Nuclear generation | 3513.0 | 4.0 | -3.0 | 4.0 | REVERSAL, ACCELERATION |
| Pumped-storage generation | 228.0 | 66.0 | 237.0 | 12.0 | PERSISTENT_UP, ROBUST_OUTLIER, CHANGE_POINT |
| Thermal base | 10161.0 | -5.0 | -77.0 | -116.0 | ACCELERATION |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ps_gen / CHANGE_POINT** — value=228.0, Δ1=66.0, Δ12=237.0, accel=12.0
- **ps_gen / PERSISTENT_UP** — value=228.0, Δ1=66.0, Δ12=237.0, accel=12.0
- **ps_gen / ROBUST_OUTLIER** — value=228.0, Δ1=66.0, Δ12=237.0, accel=12.0
- **ind_demand / CHANGE_POINT** — value=-12241.0, Δ1=0.0, Δ12=2.0, accel=0.0
- **ind_demand / ROBUST_OUTLIER** — value=-12241.0, Δ1=0.0, Δ12=2.0, accel=0.0
- **margin / CHANGE_POINT** — value=36673.0, Δ1=0.0, Δ12=178.0, accel=0.0
- **ccgt_gen / ACCELERATION** — value=6648.0, Δ1=-9.0, Δ12=-74.0, accel=-120.0
- **ccgt_gen / ROBUST_OUTLIER** — value=6648.0, Δ1=-9.0, Δ12=-74.0, accel=-120.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
