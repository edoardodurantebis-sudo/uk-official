# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-20T18:38:53.895716Z  
Source heartbeat: 2026-09-20T18:38:52.723305Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 20610.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 2115.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 6053.0 | -143.0 | -918.0 | -36.0 | PERSISTENT_DOWN |
| Residual-load proxy | 17995.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 35430.0 | 0.0 | -355.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -5158.0 | 0.0 | 14.0 | 0.0 |  |
| Interconnector net | 9874.0 | 0.0 | -167.0 | 60.0 | PERSISTENT_DOWN, ACCELERATION |
| CCGT generation | 9068.0 | -47.0 | 265.0 | -52.0 | REVERSAL, ROBUST_OUTLIER |
| Nuclear generation | 3334.0 | -4.0 | -1.0 | 2.0 | PERSISTENT_DOWN, ACCELERATION |
| Pumped-storage generation | 222.0 | 0.0 | 236.0 | 0.0 |  |
| Thermal base | 12402.0 | -51.0 | 264.0 | -50.0 | REVERSAL, ROBUST_OUTLIER |
| Frequency | 49.922 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ccgt_gen / REVERSAL** — value=9068.0, Δ1=-47.0, Δ12=265.0, accel=-52.0
- **ccgt_gen / ROBUST_OUTLIER** — value=9068.0, Δ1=-47.0, Δ12=265.0, accel=-52.0
- **thermal_base / REVERSAL** — value=12402.0, Δ1=-51.0, Δ12=264.0, accel=-50.0
- **thermal_base / ROBUST_OUTLIER** — value=12402.0, Δ1=-51.0, Δ12=264.0, accel=-50.0
- **biomass_gen / CHANGE_POINT** — value=2296.0, Δ1=10.0, Δ12=37.0, accel=24.0
- **margin / CHANGE_POINT** — value=35430.0, Δ1=0.0, Δ12=-355.0, accel=0.0
- **biomass_gen / ACCELERATION** — value=2296.0, Δ1=10.0, Δ12=37.0, accel=24.0
- **wind_gen / PERSISTENT_DOWN** — value=6053.0, Δ1=-143.0, Δ12=-918.0, accel=-36.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
