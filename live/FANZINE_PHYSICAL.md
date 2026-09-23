# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-23T09:10:30.175308Z  
Source heartbeat: 2026-09-23T09:10:29.403352Z  

## Regime: **LOOSE**
Reason: margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20282.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21028.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 6996.0 | 0.0 | -309.0 | 0.0 |  |
| Wind generation | 10386.0 | -55.0 | -92.0 | 61.0 | PERSISTENT_DOWN, ACCELERATION |
| Residual-load proxy | 13286.0 | 0.0 | 309.0 | 0.0 | CHANGE_POINT |
| Indicated margin | 39658.0 | 0.0 | 360.0 | 0.0 | ROBUST_OUTLIER |
| Indicated imbalance | -7365.0 | 0.0 | 89.0 | 0.0 | ROBUST_OUTLIER |
| Interconnector net | 10755.0 | 94.0 | 3762.0 | 8.0 | PERSISTENT_UP, ROBUST_OUTLIER |
| CCGT generation | 2972.0 | 0.0 | -3032.0 | 116.0 | PERSISTENT_DOWN, ROBUST_OUTLIER |
| Nuclear generation | 3804.0 | 5.0 | -4.0 | 5.0 | REVERSAL, ACCELERATION |
| Pumped-storage generation | -19.0 | 1.0 | 272.0 | 4.0 | CHANGE_POINT |
| Thermal base | 6776.0 | 5.0 | -3036.0 | 121.0 | REVERSAL, ROBUST_OUTLIER |
| Frequency | 50.117 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / ROBUST_OUTLIER** — value=-12660.0, Δ1=0.0, Δ12=-10.0, accel=0.0
- **ccgt_gen / PERSISTENT_DOWN** — value=2972.0, Δ1=0.0, Δ12=-3032.0, accel=116.0
- **ccgt_gen / ROBUST_OUTLIER** — value=2972.0, Δ1=0.0, Δ12=-3032.0, accel=116.0
- **thermal_base / REVERSAL** — value=6776.0, Δ1=5.0, Δ12=-3036.0, accel=121.0
- **thermal_base / ROBUST_OUTLIER** — value=6776.0, Δ1=5.0, Δ12=-3036.0, accel=121.0
- **margin / ROBUST_OUTLIER** — value=39658.0, Δ1=0.0, Δ12=360.0, accel=0.0
- **interconnector_net / PERSISTENT_UP** — value=10755.0, Δ1=94.0, Δ12=3762.0, accel=8.0
- **interconnector_net / ROBUST_OUTLIER** — value=10755.0, Δ1=94.0, Δ12=3762.0, accel=8.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
