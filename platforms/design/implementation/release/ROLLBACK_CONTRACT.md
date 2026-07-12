# MenQ Design Platform Preview Rollback Contract

Status: Approved — Implementing  
Decision: D-025  
Release channel: `next`

## Հայերեն

### Trigger-ներ

Rollback-ը պարտադիր candidate action է, երբ artifact checksum-ը չի համընկնում, deterministic rebuild-ը տարբեր output է տալիս, public API diff-ը չհաստատված breaking change է ցույց տալիս, package dependency graph-ը խախտված է, կամ consumer validation-ը critical regression է գրանցում։

### Procedure

1. Կանգնեցնել candidate promotion/publish գործողությունը։
2. Պահպանել failed source commit-ը, workflow run-ը, logs-ը, manifests-ը և checksums-ը։
3. Վերադառնալ վերջին verified preview artifact set-ին կամ source commit-ին՝ առանց canonical history վերագրելու։
4. Նորից գործարկել ամբողջ release validation-ը և consumer-relevant checks-ը։
5. Գրանցել defect-ը, remediation-ը և նոր evidence bundle-ը։
6. Promotion-ը շարունակել միայն GREEN technical evidence-ից և անհրաժեշտ Owner decision-ից հետո։

### Authority

AI-ն կարող է առաջարկել կամ տեխնիկապես պատրաստել rollback-ը, բայց չի կարող ինքնուրույն publish, merge, undraft կամ lock անել։ Owner-ը պահպանում է վերջնական authority-ն։

## English

### Triggers

Rollback is a mandatory candidate action when an artifact checksum mismatches, a deterministic rebuild produces different output, the public API diff reveals an unapproved breaking change, the package dependency graph is invalid, or consumer validation records a critical regression.

### Procedure

1. Stop candidate promotion or publishing.
2. Preserve the failed source commit, workflow run, logs, manifests, and checksums.
3. Return to the last verified preview artifact set or source commit without rewriting canonical history.
4. Re-run the complete release validation and consumer-relevant checks.
5. Record the defect, remediation, and new evidence bundle.
6. Resume promotion only after GREEN technical evidence and any required Owner decision.

### Authority

AI may recommend or technically prepare a rollback, but it cannot independently publish, merge, remove Draft status, or lock. The Owner retains final authority.

— End of document —
