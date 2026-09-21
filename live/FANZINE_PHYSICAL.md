# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T09:13:52.827749Z  
Source heartbeat: 2026-09-21T09:13:51.664859Z  

## Regime: **LOOSE**
Reason: margin high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21269.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 9277.0 | 0.0 | 483.0 | 0.0 |  |
| Wind generation | 3469.0 | -50.0 | -858.0 | -26.0 | PERSISTENT_DOWN, CHANGE_POINT |
| Residual-load proxy | 10833.0 | 0.0 | -483.0 | 0.0 |  |
| Indicated margin | 38223.0 | 0.0 | -29.0 | 0.0 |  |
| Indicated imbalance | -2000.0 | 0.0 | 271.0 | 0.0 | ROBUST_OUTLIER |
| Interconnector net | 10650.0 | -2.0 | -31.0 | 11.0 | PERSISTENT_DOWN, ACCELERATION, CHANGE_POINT |
| CCGT generation | 8474.0 | -245.0 | -255.0 | -138.0 | PERSISTENT_DOWN, ACCELERATION |
| Nuclear generation | 3503.0 | 5.0 | 7.0 | -2.0 | PERSISTENT_UP |
| Pumped-storage generation | -11.0 | -11.0 | -1.0 | 193.0 | PERSISTENT_DOWN, ACCELERATION, CHANGE_POINT |
| Thermal base | 11977.0 | -240.0 | -248.0 | -140.0 | PERSISTENT_DOWN, ACCELERATION |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_generation / ROBUST_OUTLIER** — value=19269.0, Δ1=0.0, Δ12=271.0, accel=0.0
- **ind_demand / ROBUST_OUTLIER** — value=-12837.0, Δ1=0.0, Δ12=-2.0, accel=0.0
- **imbalance / ROBUST_OUTLIER** — value=-2000.0, Δ1=0.0, Δ12=271.0, accel=0.0
- **wind_gen / CHANGE_POINT** — value=3469.0, Δ1=-50.0, Δ12=-858.0, accel=-26.0
- **interconnector_net / CHANGE_POINT** — value=10650.0, Δ1=-2.0, Δ12=-31.0, accel=11.0
- **biomass_gen / PERSISTENT_DOWN** — value=3003.0, Δ1=-11.0, Δ12=-15.0, accel=-17.0
- **biomass_gen / ACCELERATION** — value=3003.0, Δ1=-11.0, Δ12=-15.0, accel=-17.0
- **ps_gen / CHANGE_POINT** — value=-11.0, Δ1=-11.0, Δ12=-1.0, accel=193.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
