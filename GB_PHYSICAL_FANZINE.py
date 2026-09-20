#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

VERSION = "GB_PHYSICAL_FANZINE_V1.0.0"
ORDER = ["demand_forecast","ts_demand_forecast","wind_forecast","wind_gen","residual_proxy","margin","imbalance","interconnector_net","ccgt_gen","nuclear_gen","ps_gen","thermal_base","frequency"]
LABEL = {"demand_forecast":"Demand forecast","ts_demand_forecast":"TS demand forecast","wind_forecast":"Wind forecast","wind_gen":"Wind generation","residual_proxy":"Residual-load proxy","margin":"Indicated margin","imbalance":"Indicated imbalance","interconnector_net":"Interconnector net","ccgt_gen":"CCGT generation","nuclear_gen":"Nuclear generation","ps_gen":"Pumped-storage generation","thermal_base":"Thermal base","frequency":"Frequency"}

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def latest_mid_health(state: dict) -> dict:
    ev=[x for x in state.get("events",[]) if x.get("dataset")=="MID"]
    if not ev:
        return {"status":"UNKNOWN","detail":"No MID publication event in retained window."}
    x=ev[-1]
    if x.get("error"):
        return {"status":"DEGRADED","detail":x.get("error"),"ts":x.get("ts")}
    return {"status":"OK","detail":str(x.get("rows",0))+" rows","ts":x.get("ts")}

def build(state: dict, brain: dict) -> dict:
    states=brain.get("states",{})
    physical=[]
    for key in ORDER:
        if key not in states:
            continue
        x=states[key]
        physical.append({"metric":key,"label":LABEL.get(key,key),"value":x.get("value"),"d1":x.get("d1"),"d12":x.get("d12"),"accel":x.get("accel"),"tags":x.get("tags",[])})
    patterns=[]
    seen=set()
    for p in brain.get("active_patterns",[]):
        key=(p.get("metric"),p.get("pattern"))
        if key in seen:
            continue
        seen.add(key)
        patterns.append({k:p.get(k) for k in ("metric","pattern","value","d1","d12","accel","z_mad")})
        if len(patterns)>=8:
            break
    analogues=brain.get("analogues",[])[:5]
    return {
        "schema":"UNDER_THE_BID_PHYSICAL_FANZINE_V1",
        "version":VERSION,
        "generated_at_utc":datetime.now(timezone.utc).isoformat().replace("+00:00","Z"),
        "source_heartbeat":state.get("last_heartbeat"),
        "brain_generated_at":brain.get("generated_at"),
        "regime":brain.get("regime","UNKNOWN"),
        "regime_reasons":brain.get("regime_reasons",[]),
        "physical":physical,
        "active_patterns":patterns,
        "analogues":analogues,
        "health":{"alien":"OK" if state.get("last_heartbeat") else "UNKNOWN","mid":latest_mid_health(state),"last_error":state.get("last_error")},
        "certification":{"market_observation_only":True,"trading_signal":False,"order_or_sizing_logic":False,"promotion_authority":False,"note":"Physical/context view only. No rule is admitted by this page."},
    }

def render(feed: dict) -> str:
    lines=[
        "# UNDER THE BID — Physical Fanzine","",
        "Generated UTC: "+str(feed["generated_at_utc"])+"  ",
        "Source heartbeat: "+str(feed.get("source_heartbeat"))+"  ","",
        "## Regime: **"+str(feed.get("regime","UNKNOWN"))+"**",
    ]
    reasons=feed.get("regime_reasons") or []
    lines.append("Reason: "+("; ".join(reasons) if reasons else "No regime explanation available."))
    lines += ["","## Physical snapshot","","| Metric | Value | Δ1 | Δ12 | Accel | Tags |","|---|---:|---:|---:|---:|---|"]
    for x in feed.get("physical",[]):
        tags=", ".join(x.get("tags") or [])
        lines.append("| "+str(x["label"])+" | "+str(x.get("value",""))+" | "+str(x.get("d1",""))+" | "+str(x.get("d12",""))+" | "+str(x.get("accel",""))+" | "+tags+" |")
    lines += ["","## Active live patterns",""]
    if feed.get("active_patterns"):
        for p in feed["active_patterns"]:
            lines.append("- **"+str(p.get("metric"))+" / "+str(p.get("pattern"))+"** — value="+str(p.get("value"))+", Δ1="+str(p.get("d1"))+", Δ12="+str(p.get("d12"))+", accel="+str(p.get("accel")))
    else:
        lines.append("- No active pattern in current retained state.")
    lines += ["","## Health","", "- Alien: **"+str(feed["health"]["alien"])+"**", "- MID: **"+str(feed["health"]["mid"]["status"])+"** — "+str(feed["health"]["mid"].get("detail","")), "", "## Trading layer", "", "**NO TRADING SIGNAL FROM THIS PAGE.**", "This is the physical/context layer only. Certified rules, shadow evidence and PnL will be attached downstream without duplicating trading logic.",""]
    return "\n".join(lines)

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--state",default="live/state.json")
    ap.add_argument("--brain",default="live/brain/LATEST.json")
    ap.add_argument("--json-out",default="live/FANZINE_PHYSICAL.json")
    ap.add_argument("--md-out",default="live/FANZINE_PHYSICAL.md")
    a=ap.parse_args()
    feed=build(load(Path(a.state)),load(Path(a.brain)))
    Path(a.json_out).write_text(json.dumps(feed,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    Path(a.md_out).write_text(render(feed),encoding="utf-8")
    print(json.dumps({"version":VERSION,"regime":feed["regime"],"mid":feed["health"]["mid"]["status"]}))
    return 0

if __name__=="__main__":
    raise SystemExit(main())