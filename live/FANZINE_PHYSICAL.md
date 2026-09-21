# UNDER THE BID — Physical Fanzine

Generated UTC: 2026-09-21T18:08:25.536171Z  
Source heartbeat: 2026-09-21T18:08:24.517876Z  

## Regime: **TIGHT**
Reason: margin low

## Physical snapshot

| Metric | Value | Δ1 | Δ12 | Accel | Tags |
|---|---:|---:|---:|---:|---|
| Demand forecast | 20959.0 | 0.0 | 0.0 | 0.0 |  |
| TS demand forecast | 21459.0 | 0.0 | 0.0 | 0.0 |  |
| Wind forecast | 8620.0 | 0.0 | 0.0 | 0.0 |  |
| Wind generation | 3507.0 | 0.0 | 190.0 | 16.0 | CHANGE_POINT |
| Residual-load proxy | 12339.0 | 0.0 | 0.0 | 0.0 |  |
| Indicated margin | 36168.0 | 0.0 | -106.0 | 0.0 | ROBUST_OUTLIER, CHANGE_POINT |
| Indicated imbalance | -3042.0 | 0.0 | -16.0 | 0.0 |  |
| Interconnector net | 6791.0 | 201.0 | -1292.0 | 230.0 | REVERSAL, ROBUST_OUTLIER, CHANGE_POINT |
| CCGT generation | 13657.0 | -120.0 | 224.0 | -13.0 | REVERSAL |
| Nuclear generation | 3510.0 | 2.0 | 6.0 | 5.0 | ACCELERATION |
| Pumped-storage generation | 633.0 | 182.0 | -347.0 | 179.0 | REVERSAL, ACCELERATION |
| Thermal base | 17167.0 | -118.0 | 230.0 | -8.0 | REVERSAL |
| Frequency | 50.105 | 0.0 | 0.0 | 0.0 |  |

## Active live patterns

- **interconnector_net / CHANGE_POINT** — value=6791.0, Δ1=201.0, Δ12=-1292.0, accel=230.0
- **interconnector_net / REVERSAL** — value=6791.0, Δ1=201.0, Δ12=-1292.0, accel=230.0
- **interconnector_net / ROBUST_OUTLIER** — value=6791.0, Δ1=201.0, Δ12=-1292.0, accel=230.0
- **margin / CHANGE_POINT** — value=36168.0, Δ1=0.0, Δ12=-106.0, accel=0.0
- **margin / ROBUST_OUTLIER** — value=36168.0, Δ1=0.0, Δ12=-106.0, accel=0.0
- **ps_gen / REVERSAL** — value=633.0, Δ1=182.0, Δ12=-347.0, accel=179.0
- **ps_gen / ACCELERATION** — value=633.0, Δ1=182.0, Δ12=-347.0, accel=179.0
- **wind_gen / CHANGE_POINT** — value=3507.0, Δ1=0.0, Δ12=190.0, accel=16.0

## Health

- Alien: **OK**
- MID: **OK** — 1 rows

## Trading layer

**NO TRADING SIGNAL FROM THIS PAGE.**
This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.
