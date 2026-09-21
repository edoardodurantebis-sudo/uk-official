# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T11:07:26.846157Z  
Source heartbeat: 2026-09-21T11:07:25.674417Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 21108.0 | 0.0 | 1108.0 | 0.0 |  |
| TS demand forecast | 21608.0 | 0.0 | 449.0 | 0.0 |  |
| Wind forecast | 8923.0 | 0.0 | -354.0 | 0.0 |  |
| Wind generation | 3324.0 | 20.0 | 34.0 | 13.0 | PERSISTENT_UP, ACCELERATION |
| Residual-load proxy | 12185.0 | 0.0 | 1462.0 | 0.0 | CHANGE_POINT |
| Indicated margin | 36495.0 | 0.0 | -3324.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -3871.0 | 0.0 | -4440.0 | 0.0 | CHANGE_POINT |
| Interconnector net | 11264.0 | -21.0 | 481.0 | -171.0 | REVERSAL, ACCELERATION, CHANGE_POINT |
| CCGT generation | 6683.0 | 32.0 | -435.0 | -1.0 | REVERSAL, ROBUST_OUTLIER |
| Nuclear generation | 3519.0 | 10.0 | 23.0 | 4.0 | PERSISTENT_UP, ROBUST_OUTLIER, CHANGE_POINT |
| Pumped-storage generation | 100.0 | -2.0 | 111.0 | -112.0 | REVERSAL, ACCELERATION |
| Thermal base | 10202.0 | 42.0 | -412.0 | 3.0 | REVERSAL, ROBUST_OUTLIER |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / CHANGE_POINT** — value=-12243.0, Δ1=0.0, Δ12=568.0, accel=0.0
- **ind_demand / ROBUST_OUTLIER** — value=-12243.0, Δ1=0.0, Δ12=568.0, accel=0.0
- **nuclear_gen / CHANGE_POINT** — value=3519.0, Δ1=10.0, Δ12=23.0, accel=4.0
- **margin / CHANGE_POINT** — value=36495.0, Δ1=0.0, Δ12=-3324.0, accel=0.0
- **ccgt_gen / REVERSAL** — value=6683.0, Δ1=32.0, Δ12=-435.0, accel=-1.0
- **ccgt_gen / ROBUST_OUTLIER** — value=6683.0, Δ1=32.0, Δ12=-435.0, accel=-1.0
- **thermal_base / REVERSAL** — value=10202.0, Δ1=42.0, Δ12=-412.0, accel=3.0
- **thermal_base / ROBUST_OUTLIER** — value=10202.0, Δ1=42.0, Δ12=-412.0, accel=3.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
