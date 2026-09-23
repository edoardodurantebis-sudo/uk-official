# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-23T00:13:08.961898Z  
Source heartbeat: 2026-09-23T00:13:08.250701Z  

## Regime: **BALANCED**
Reason: No regime explanation available.

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13770.0 | 0.0 | 158.0 | 0.0 |  |
| Wind generation | 3910.0 | 46.0 | 774.0 | -18.0 | PERSISTENT_UP, CHANGE_POINT |
| Residual-load proxy | 6903.0 | 0.0 | -158.0 | 0.0 |  |
| Indicated margin | 37219.0 | 0.0 | -10.0 | 0.0 |  |
| Indicated imbalance | -7998.0 | 0.0 | 51.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 3203.0 | -178.0 | -1442.0 | 460.0 | PERSISTENT_DOWN, CHANGE_POINT |
| CCGT generation | 10024.0 | 4.0 | -27.0 | -13.0 | REVERSAL, ACCELERATION, ROBUST_OUTLIER |
| Nuclear generation | 3733.0 | -4.0 | 3.0 | -4.0 | REVERSAL, ACCELERATION |
| Pumped-storage generation | 147.0 | 0.0 | 0.0 | 0.0 |  |
| Thermal base | 13757.0 | 0.0 | -24.0 | -17.0 | ACCELERATION, ROBUST_OUTLIER |
| Frequency | 50.117 | 0.0 | 0.027999999999998693 | 0.0 | PERSISTENT_UP |

## Active live patterns

- **ind_demand / ROBUST_OUTLIER** — value=-12486.0, Δ1=0.0, Δ12=-2.0, accel=0.0
- **thermal_base / ACCELERATION** — value=13757.0, Δ1=0.0, Δ12=-24.0, accel=-17.0
- **thermal_base / ROBUST_OUTLIER** — value=13757.0, Δ1=0.0, Δ12=-24.0, accel=-17.0
- **ccgt_gen / REVERSAL** — value=10024.0, Δ1=4.0, Δ12=-27.0, accel=-13.0
- **ccgt_gen / ACCELERATION** — value=10024.0, Δ1=4.0, Δ12=-27.0, accel=-13.0
- **ccgt_gen / ROBUST_OUTLIER** — value=10024.0, Δ1=4.0, Δ12=-27.0, accel=-13.0
- **wind_gen / CHANGE_POINT** — value=3910.0, Δ1=46.0, Δ12=774.0, accel=-18.0
- **interconnector_net / CHANGE_POINT** — value=3203.0, Δ1=-178.0, Δ12=-1442.0, accel=460.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
