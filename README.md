# UNDER THE BID — Power UK runner

Questo bundle mette in esecuzione i prototipi già presenti nei ledger senza
creare un secondo motore di discovery. `GB_NIGHTLY_DISCOVERY_V1.py` resta il
motore scientifico; `gb_power_runner.py` aggiunge il contratto operativo:

- lettura reale e fingerprint di master, ex-ante e Feature Availability Registry;
- identità fisica GB esplicita (`gb_start_utc`/`gb_sp`), separata da MATS/EPEX;
- controllo DST e conteggi giornalieri 46/48/50, mai un 48 fisso;
- fallimento chiuso su lineage/PIT incompleta;
- gate canonici Europe/London: DA 10:20 D-1, IDA1 18:30 D-1, IDA2 09:00 D0;
- NIV con lineage esplicita: master storico raw invertito (`MASTER_INTERNAL_INVERTED`), feed Elexon ufficiale non invertito (`ELEXON_OFFICIAL`);
- run atomico con manifest, hash, log, coda candidati e heartbeat append-only;
- fallback automatico a schema/lineage/time audit quando il test primario è bloccato;
- nessuna promozione, size, ordine o modifica del rulebook.

I dati proprietari non devono essere committati nel repository. Il workflow
GitHub è pensato per un runner self-hosted che vede una directory dati locale.

## Avvio locale

```bash
python gb_power_runner.py --self-test
python gb_power_runner.py --data-dir /opt/under-the-bid/data
```

Il runner cerca i nomi canonici `master_wide.parquet|csv`,
`exante_wide.parquet|csv` e `FEATURE_AVAILABILITY_REGISTRY.csv`. Per un join
ex-ante bisogna dichiarare esplicitamente le chiavi, ad esempio:

```bash
python gb_power_runner.py \
  --data-dir /opt/under-the-bid/data \
  --join-keys gb_start_utc
```

Se mancano dati, registry o chiavi PIT, il comando non inventa un risultato:
salva `SCHEMA_LINEAGE_AUDIT.json`, pubblica `BLOCKED_PRIMARY_WITH_FALLBACK` e
lascia comunque un heartbeat.

## Output

Ogni esecuzione finita correttamente viene committata in modo atomico in
`runs/UKPOWER_<timestamp>_<hash>/`. Gli artefatti principali sono:

- `RUN_MANIFEST.json` — configurazione, runtime, input hash e verdict;
- `INPUT_MANIFEST.json` — schema, periodo e conteggi SP osservati;
- `engine_output/` — `candidate_queue`, evidence, counterexamples, controls e
  manifest del motore V1;
- `REPORT.txt` — report visibile minimale;
- `ARTIFACT_INDEX.json` — hash di ogni file prodotto;
- `state/heartbeat.jsonl` — append-only heartbeat locale.

I risultati machine-generated sono sempre `REVIEW_READY` al massimo: la
promozione rimane umana e fuori dal runner.

## Sicurezza del repository pubblico

Questo repository è pubblico. Per questo motivo **non contiene** dataset
proprietari, endpoint/reti interne, credenziali o bundle Alien privati.
`under_the_bid_data.py` usa variabili d'ambiente per la configurazione
specifica dell'ambiente operativo.

Il motore accetta sia Parquet sia CSV per master/ex-ante attraverso il loader
tabellare comune; la validazione PIT/time resta fail-closed.
