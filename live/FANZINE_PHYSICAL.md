# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-20T18:47:17.917317Z  
Source heartbeat: 2026-09-20T18:47:16.363272Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 20610.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 2115.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 5841.0 | -106.0 | -970.0 | 0.0 | PERSISTENT_DOWN |
| Residual-load proxy | 17995.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 35430.0 | 0.0 | -30.0 | 0.0 |  |
| Indicated imbalance | -5158.0 | 0.0 | 7.0 | 0.0 |  |
| Interconnector net | 9874.0 | 0.0 | -169.0 | 0.0 | CHANGE_POINT |
| CCGT generation | 8723.0 | -174.0 | -175.0 | -3.0 | PERSISTENT_DOWN, ROBUST_OUTLIER |
| Nuclear generation | 3341.0 | 7.0 | 3.0 | 7.0 | PERSISTENT_UP, ACCELERATION |
| Pumped-storage generation | 224.0 | 2.0 | -64.0 | 2.0 | REVERSAL |
| Thermal base | 12064.0 | -167.0 | -172.0 | 4.0 | PERSISTENT_DOWN, ROBUST_OUTLIER |
| Frequency | 49.922 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ccgt_gen / PERSISTENT_DOWN** — value=8723.0, Δ1=-174.0, Δ12=-175.0, accel=-3.0
- **ccgt_gen / ROBUST_OUTLIER** — value=8723.0, Δ1=-174.0, Δ12=-175.0, accel=-3.0
- **thermal_base / PERSISTENT_DOWN** — value=12064.0, Δ1=-167.0, Δ12=-172.0, accel=4.0
- **thermal_base / ROBUST_OUTLIER** — value=12064.0, Δ1=-167.0, Δ12=-172.0, accel=4.0
- **biomass_gen / CHANGE_POINT** — value=2336.0, Δ1=4.0, Δ12=77.0, accel=-32.0
- **interconnector_net / CHANGE_POINT** — value=9874.0, Δ1=0.0, Δ12=-169.0, accel=0.0
- **biomass_gen / PERSISTENT_UP** — value=2336.0, Δ1=4.0, Δ12=77.0, accel=-32.0
- **biomass_gen / ACCELERATION** — value=2336.0, Δ1=4.0, Δ12=77.0, accel=-32.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
