# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T02:44:14.231261Z  
Source heartbeat: 2026-09-21T02:44:12.648733Z  

## Regime: **LOOSE**
Reason: margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 20610.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 1603.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 3823.0 | -16.0 | -104.0 | 33.0 | PERSISTENT_DOWN |
| Residual-load proxy | 18507.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 37546.0 | 0.0 | 1716.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Indicated imbalance | -4904.0 | 0.0 | -5.0 | 0.0 |  |
| Interconnector net | 12526.0 | 2.0 | 292.0 | -3.0 | PERSISTENT_UP |
| CCGT generation | 4875.0 | 24.0 | -576.0 | 86.0 | REVERSAL, CHANGE_POINT |
| Nuclear generation | 3336.0 | -3.0 | -6.0 | 1.0 | PERSISTENT_DOWN |
| Pumped-storage generation | -129.0 | -1.0 | -117.0 | -3.0 |  |
| Thermal base | 8211.0 | 21.0 | -582.0 | 87.0 | REVERSAL, CHANGE_POINT |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **margin / CHANGE_POINT** — value=37546.0, Δ1=0.0, Δ12=1716.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=37546.0, Δ1=0.0, Δ12=1716.0, accel=0.0
- **ccgt_gen / CHANGE_POINT** — value=4875.0, Δ1=24.0, Δ12=-576.0, accel=86.0
- **thermal_base / CHANGE_POINT** — value=8211.0, Δ1=21.0, Δ12=-582.0, accel=87.0
- **ind_demand / CHANGE_POINT** — value=-11802.0, Δ1=0.0, Δ12=26.0, accel=0.0
- **wind_gen / PERSISTENT_DOWN** — value=3823.0, Δ1=-16.0, Δ12=-104.0, accel=33.0
- **ccgt_gen / REVERSAL** — value=4875.0, Δ1=24.0, Δ12=-576.0, accel=86.0
- **thermal_base / REVERSAL** — value=8211.0, Δ1=21.0, Δ12=-582.0, accel=87.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
