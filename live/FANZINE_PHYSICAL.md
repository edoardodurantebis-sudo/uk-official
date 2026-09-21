# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T11:03:14.439812Z  
Source heartbeat: 2026-09-21T11:03:12.814990Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 21108.0 | 0.0 | 1108.0 | 0.0 | PERSISTENT_UP |
| TS demand forecast | 21608.0 | 0.0 | 449.0 | 0.0 | PERSISTENT_UP |
| Wind forecast | 8923.0 | 0.0 | -354.0 | 0.0 |  |
| Wind generation | 3304.0 | 7.0 | 20.0 | 1.0 |  |
| Residual-load proxy | 12185.0 | 0.0 | 1462.0 | 0.0 | PERSISTENT_UP, CHANGE_POINT |
| Indicated margin | 36495.0 | 0.0 | -3324.0 | 0.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Indicated imbalance | -3871.0 | 0.0 | -4440.0 | 0.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Interconnector net | 11285.0 | 150.0 | 526.0 | 123.0 | PERSISTENT_UP, CHANGE_POINT |
| CCGT generation | 6651.0 | 33.0 | -545.0 | 18.0 | REVERSAL, ROBUST_OUTLIER |
| Nuclear generation | 3509.0 | 6.0 | 12.0 | 8.0 | PERSISTENT_UP, ACCELERATION |
| Pumped-storage generation | 102.0 | 110.0 | 113.0 | 110.0 | PERSISTENT_UP, ACCELERATION |
| Thermal base | 10160.0 | 39.0 | -533.0 | 26.0 | REVERSAL, ROBUST_OUTLIER |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_demand / CHANGE_POINT** — value=-12243.0, Δ1=0.0, Δ12=568.0, accel=0.0
- **ind_demand / PERSISTENT_UP** — value=-12243.0, Δ1=0.0, Δ12=568.0, accel=0.0
- **ind_demand / ROBUST_OUTLIER** — value=-12243.0, Δ1=0.0, Δ12=568.0, accel=0.0
- **ccgt_gen / REVERSAL** — value=6651.0, Δ1=33.0, Δ12=-545.0, accel=18.0
- **ccgt_gen / ROBUST_OUTLIER** — value=6651.0, Δ1=33.0, Δ12=-545.0, accel=18.0
- **margin / CHANGE_POINT** — value=36495.0, Δ1=0.0, Δ12=-3324.0, accel=0.0
- **thermal_base / REVERSAL** — value=10160.0, Δ1=39.0, Δ12=-533.0, accel=26.0
- **thermal_base / ROBUST_OUTLIER** — value=10160.0, Δ1=39.0, Δ12=-533.0, accel=26.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
