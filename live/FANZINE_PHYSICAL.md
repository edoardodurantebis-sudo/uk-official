# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-20T18:51:30.209090Z  
Source heartbeat: 2026-09-20T18:51:28.916013Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 20610.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 2115.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 5703.0 | -138.0 | -906.0 | -32.0 | PERSISTENT_DOWN |
| Residual-load proxy | 17995.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 35401.0 | -29.0 | -59.0 | -29.0 | PERSISTENT_DOWN, ACCELERATION |
| Indicated imbalance | -5158.0 | 0.0 | 7.0 | 0.0 |  |
| Interconnector net | 9874.0 | 0.0 | -115.0 | 0.0 | CHANGE_POINT |
| CCGT generation | 8781.0 | 58.0 | -170.0 | 232.0 | REVERSAL, ACCELERATION, ROBUST_OUTLIER |
| Nuclear generation | 3338.0 | -3.0 | 0.0 | -10.0 | ACCELERATION |
| Pumped-storage generation | 223.0 | -1.0 | 1.0 | -3.0 | REVERSAL, ACCELERATION |
| Thermal base | 12119.0 | 55.0 | -170.0 | 222.0 | REVERSAL, ACCELERATION, ROBUST_OUTLIER |
| Frequency | 49.922 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ccgt_gen / REVERSAL** — value=8781.0, Δ1=58.0, Δ12=-170.0, accel=232.0
- **ccgt_gen / ACCELERATION** — value=8781.0, Δ1=58.0, Δ12=-170.0, accel=232.0
- **ccgt_gen / ROBUST_OUTLIER** — value=8781.0, Δ1=58.0, Δ12=-170.0, accel=232.0
- **thermal_base / REVERSAL** — value=12119.0, Δ1=55.0, Δ12=-170.0, accel=222.0
- **thermal_base / ACCELERATION** — value=12119.0, Δ1=55.0, Δ12=-170.0, accel=222.0
- **thermal_base / ROBUST_OUTLIER** — value=12119.0, Δ1=55.0, Δ12=-170.0, accel=222.0
- **biomass_gen / CHANGE_POINT** — value=2341.0, Δ1=5.0, Δ12=81.0, accel=1.0
- **interconnector_net / CHANGE_POINT** — value=9874.0, Δ1=0.0, Δ12=-115.0, accel=0.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
