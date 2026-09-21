# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T18:12:39.173412Z  
Source heartbeat: 2026-09-21T18:12:37.940711Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20959.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21459.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 8620.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 3508.0 | 1.0 | 178.0 | 1.0 | CHANGE_POINT |
| Residual-load proxy | 12339.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 36168.0 | 0.0 | 0.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Indicated imbalance | -3042.0 | 0.0 | -16.0 | 0.0 |  |
| Interconnector net | 6873.0 | 82.0 | -1210.0 | -119.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| CCGT generation | 13617.0 | -40.0 | -42.0 | 80.0 | PERSISTENT_DOWN, ACCELERATION |
| Nuclear generation | 3514.0 | 4.0 | 6.0 | 2.0 | PERSISTENT_UP |
| Pumped-storage generation | 631.0 | -2.0 | -224.0 | -184.0 | ACCELERATION |
| Thermal base | 17131.0 | -36.0 | -36.0 | 82.0 | PERSISTENT_DOWN, ACCELERATION |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **interconnector_net / CHANGE_POINT** — value=6873.0, Δ1=82.0, Δ12=-1210.0, accel=-119.0
- **interconnector_net / REVERSAL** — value=6873.0, Δ1=82.0, Δ12=-1210.0, accel=-119.0
- **interconnector_net / ROBUST_OUTLIER** — value=6873.0, Δ1=82.0, Δ12=-1210.0, accel=-119.0
- **margin / CHANGE_POINT** — value=36168.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=36168.0, Δ1=0.0, Δ12=0.0, accel=0.0
- **ps_gen / ACCELERATION** — value=631.0, Δ1=-2.0, Δ12=-224.0, accel=-184.0
- **wind_gen / CHANGE_POINT** — value=3508.0, Δ1=1.0, Δ12=178.0, accel=1.0
- **thermal_base / PERSISTENT_DOWN** — value=17131.0, Δ1=-36.0, Δ12=-36.0, accel=82.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
