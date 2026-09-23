# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-23T05:13:27.320149Z  
Source heartbeat: 2026-09-23T05:13:25.813738Z  

## Regime: **LOOSE**
Reason: margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20673.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21173.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 7477.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 9146.0 | -203.0 | 529.0 | -191.0 | REVERSAL, ACCELERATION |
| Residual-load proxy | 13196.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 38542.0 | 0.0 | 15.0 | 0.0 | ROBUST_OUTLIER |
| Indicated imbalance | -8014.0 | 0.0 | 23.0 | 0.0 |  |
| Interconnector net | -4873.0 | 180.0 | -246.0 | -377.0 | REVERSAL, ACCELERATION |
| CCGT generation | 8171.0 | 55.0 | -124.0 | 13.0 | REVERSAL |
| Nuclear generation | 3801.0 | -2.0 | 45.0 | -2.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| Pumped-storage generation | -8.0 | -103.0 | -152.0 | -54.0 | PERSISTENT_DOWN, ACCELERATION, ROBUST_OUTLIER |
| Thermal base | 11972.0 | 53.0 | -79.0 | 11.0 | REVERSAL |
| Frequency | 50.117 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ps_gen / PERSISTENT_DOWN** — value=-8.0, Δ1=-103.0, Δ12=-152.0, accel=-54.0
- **ps_gen / ACCELERATION** — value=-8.0, Δ1=-103.0, Δ12=-152.0, accel=-54.0
- **ps_gen / ROBUST_OUTLIER** — value=-8.0, Δ1=-103.0, Δ12=-152.0, accel=-54.0
- **margin / ROBUST_OUTLIER** — value=38542.0, Δ1=0.0, Δ12=15.0, accel=0.0
- **nuclear_gen / CHANGE_POINT** — value=3801.0, Δ1=-2.0, Δ12=45.0, accel=-2.0
- **biomass_gen / CHANGE_POINT** — value=2640.0, Δ1=-73.0, Δ12=-231.0, accel=34.0
- **nuclear_gen / REVERSAL** — value=3801.0, Δ1=-2.0, Δ12=45.0, accel=-2.0
- **nuclear_gen / ROBUST_OUTLIER** — value=3801.0, Δ1=-2.0, Δ12=45.0, accel=-2.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
