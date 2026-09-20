# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-20T20:04:00.445089Z  
Source heartbeat: 2026-09-20T20:03:58.980663Z  

## Regime: **TIGHT**
Reason: residual high

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20110.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 20610.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 1726.0 | 0.0 | -389.0 | 0.0 |  |
| Wind generation | 5707.0 | 14.0 | 291.0 | 53.0 |  |
| Residual-load proxy | 18384.0 | 0.0 | 389.0 | 0.0 |  |
| Indicated margin | 35546.0 | 0.0 | 145.0 | 0.0 | CHANGE_POINT |
| Indicated imbalance | -5337.0 | 0.0 | -196.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Interconnector net | 10898.0 | -20.0 | 494.0 | -22.0 | REVERSAL, CHANGE_POINT |
| CCGT generation | 8240.0 | -1.0 | -454.0 | 25.0 | PERSISTENT_DOWN |
| Nuclear generation | 3338.0 | 1.0 | -3.0 | -2.0 | REVERSAL, ACCELERATION |
| Pumped-storage generation | 227.0 | 0.0 | 1.0 | 0.0 | CHANGE_POINT |
| Thermal base | 11578.0 | 0.0 | -457.0 | 23.0 | PERSISTENT_DOWN |
| Frequency | 49.922 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **ind_generation / CHANGE_POINT** — value=15273.0, Δ1=0.0, Δ12=-196.0, accel=0.0
- **ind_generation / ROBUST_OUTLIER** — value=15273.0, Δ1=0.0, Δ12=-196.0, accel=0.0
- **imbalance / CHANGE_POINT** — value=-5337.0, Δ1=0.0, Δ12=-196.0, accel=0.0
- **imbalance / ROBUST_OUTLIER** — value=-5337.0, Δ1=0.0, Δ12=-196.0, accel=0.0
- **margin / CHANGE_POINT** — value=35546.0, Δ1=0.0, Δ12=145.0, accel=0.0
- **ps_gen / CHANGE_POINT** — value=227.0, Δ1=0.0, Δ12=1.0, accel=0.0
- **interconnector_net / CHANGE_POINT** — value=10898.0, Δ1=-20.0, Δ12=494.0, accel=-22.0
- **nuclear_gen / REVERSAL** — value=3338.0, Δ1=1.0, Δ12=-3.0, accel=-2.0

## Health

- Alien: **OK**
- MID: **OK** — 2 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
