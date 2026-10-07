# Chaos demo order service

Minimal sample application for local Chaos / resilience agent runs. The code deliberately
contains outbound HTTP, database, and queue calls with missing timeouts, weak error
handling, or unbounded retries so the SonarQube Hunter `chaos/0.0.1` playbook can
surface reliability findings.

## Intentional gaps

| Area | File | Issue |
|---|---|---|
| HTTP catalog lookup | `clients/catalog_client.py` | No request timeout |
| HTTP payment authorization | `clients/payment_client.py` | No timeout; errors swallowed as success |
| PostgreSQL persistence | `repositories/order_repository.py` | No connect or statement timeout |
| Redis notifications | `workers/notification_worker.py` | Unbounded retry loop without backoff |

## Scan with the detection agent

Clone this repository, then from a local `detection-agent-app` checkout:

```bash
git clone https://github.com/damien-urruty-sonarsource/chaos-demo-order-service.git
cd detection-agent-app

uv sync
uv run python -m analysis_agent.prompt_protection --generated-dir playbooks/chaos/generated

export LLM_PROVIDER=anthropic
export LLM_KEY=<your-key>
export LLM_MODEL=claude-opus-4-8
export LLM_SECONDARY_MODEL=claude-sonnet-4-6

PLAYBOOK_KEY=chaos PLAYBOOK_VERSION=0.0.1 \
  uv run detection-agent /path/to/chaos-demo-order-service
```

Findings are printed to stdout as JSON.

This project is sample data only. It is not deployed and does not need its Python
dependencies installed for a source scan.
