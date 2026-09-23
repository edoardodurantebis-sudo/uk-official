# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-23T02:54:40.201361Z  
Source heartbeat: 2026-09-23T02:54:38.853175Z  

## Regime: **LOOSE**
Reason: margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 13770.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 5397.0 | 41.0 | 355.0 | 41.0 | PERSISTENT_UP |
| Residual-load proxy | 6903.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 38682.0 | 0.0 | 1467.0 | -20.0 | PERSISTENT_UP, ROBUST_OUTLIER |
| Indicated imbalance | -7980.0 | -3.0 | 0.0 | -3.0 | PERSISTENT_DOWN, ACCELERATION |
| Interconnector net | -466.0 | 1.0 | -1970.0 | 1.0 | REVERSAL, CHANGE_POINT |
| CCGT generation | 9421.0 | -43.0 | -211.0 | -43.0 |  |
| Nuclear generation | 3733.0 | 6.0 | 11.0 | 6.0 | PERSISTENT_UP, ACCELERATION |
| Pumped-storage generation | 140.0 | 0.0 | -7.0 | 0.0 | ROBUST_OUTLIER |
| Thermal base | 13154.0 | -37.0 | -200.0 | -37.0 |  |
| Frequency | 50.117 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **margin / PERSISTENT_UP** — value=38682.0, Δ1=0.0, Δ12=1467.0, accel=-20.0
- **margin / ROBUST_OUTLIER** — value=38682.0, Δ1=0.0, Δ12=1467.0, accel=-20.0
- **ind_demand / CHANGE_POINT** — value=-12419.0, Δ1=1.0, Δ12=14.0, accel=1.0
- **ind_demand / PERSISTENT_UP** — value=-12419.0, Δ1=1.0, Δ12=14.0, accel=1.0
- **ind_demand / ROBUST_OUTLIER** — value=-12419.0, Δ1=1.0, Δ12=14.0, accel=1.0
- **ps_gen / ROBUST_OUTLIER** — value=140.0, Δ1=0.0, Δ12=-7.0, accel=0.0
- **interconnector_net / CHANGE_POINT** — value=-466.0, Δ1=1.0, Δ12=-1970.0, accel=1.0
- **biomass_gen / ROBUST_OUTLIER** — value=2873.0, Δ1=2.0, Δ12=14.0, accel=2.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
