# NexusRunner — Commit & PR Guide (Codex-Optimized)

**North Star:** máximo throughput com governança mínima. Este documento é **a fonte de verdade** para gerar commits e PRs via agente (Codex/LLM).

---

## TL;DR (Diretivas para o Agente)

```yaml
commit_format:
  standard: conventional_commits
  title_max_len: 72
  body_wrap: 100
  footer_tokens:
    - "Refs:"
    - "BREAKING CHANGE:"
branching:
  pattern: "(feat|fix|chore|docs|refactor|perf|test|ci|build)/[a-z0-9._-]+"
  default_base: "main"
pr:
  title_regex: "^(feat|fix|chore|docs|refactor|perf|test|ci|build)(\\([a-z0-9-]+\\))?: .+"
  require_checks: true
  require_reviewers: 1
  size_labels:
    - {name: "size/S", max_changed_lines: 120}
    - {name: "size/M", max_changed_lines: 400}
    - {name: "size/L", max_changed_lines: 1000000}
security_guardrails:
  disallow_flags:
    - "--privileged"
    - "--net=host"
  allowed_mount_roots:
    - "/workspace"
    - "/cache"
  cap_drop_all: true
  default_limits:
    cpu: "2"
    memory: "4Gi"
required_labels:
  - "feat|fix|chore|docs|refactor|perf|test|ci|build"
  - "P0|P1|P2|P3"
  - "security" # quando alterar policies/execução
```

---

## 1) Conventional Commits (exigido)

**Formato:**
```
<type>(<scope>): <subject>
<blank line>
<body - opcional>
<blank line>
<footer - opcional>
```

**Types:** `feat|fix|chore|docs|refactor|perf|test|ci|build`  
**Scopes sugeridos por repo:**
- **control-plane:** `api`, `rbac`, `jobs`, `policies`, `artifacts`, `dsl`, `infra`
- **runner-agent:** `executor`, `docker`, `scheduler`, `uploader`, `guards`
- **playbook-spec:** `schema`, `validator`, `examples`
- **ui-console:** `runners`, `jobs`, `playbooks`, `auth`, `ux`
- **infra:** `compose`, `observability`, `k8s`, `cache`
- **examples/marketplace/meta:** `samples`, `publisher`, `scripts`, `docs`

**Exemplos válidos:**
- `feat(api): POST /jobs com constraints e prioridade`
- `fix(executor): isola mounts fora de /workspace e /cache`
- `docs(schema): adiciona exemplos GPU AMD no DSL`

---

## 2) Branching

- Crie branch a partir de `main`:
  - `feat/<slug>`, `fix/<slug>`, `chore/<slug>`, etc.  
  - **Regex:** `(feat|fix|chore|docs|refactor|perf|test|ci|build)/[a-z0-9._-]+`

---

## 3) Pull Requests (PR)

**Título do PR = mesmo do commit principal** (Conventional Commit).  
**Checklist (o agente deve preencher):**
- [ ] Tipo e escopo corretos (`feat|fix|...` + `(<scope>)`)
- [ ] *Size label* aplicada (`size/S` até 120 linhas; `size/M` até 400)
- [ ] Políticas de segurança respeitadas (sem `--privileged`, sem `--net=host`, mounts apenas `/workspace` e `/cache`)
- [ ] Testes ou *smoke* incluídos (quando aplicável)
- [ ] Documentação atualizada (`README/ADRs` quando necessário)
- [ ] **Issues/Refs** linkadas no rodapé (`Refs: #123, #124`)

**Template de corpo (o agente deve usar):**
```markdown
## Contexto
(qual problema/objetivo)

## O que foi feito
- ponto 1
- ponto 2

## Como validar
- comando A
- resultado esperado

## Segurança/Policies
- Sem `--privileged` / `--net=host`
- Mounts confinados a `/workspace` e `/cache`
- Limits padrão ou justificados

## Refs
Refs: #<issue>
```

---

## 4) Guardrails de Segurança (sempre checar)

- **PROIBIDO:** `--privileged`, `--net=host`, *capabilities* elevadas sem justificativa.
- **Mounts somente:** `/workspace`, `/cache`.  
- **`cap-drop=ALL`** por padrão.  
- **Limits default:** `cpu=2`, `memory=4Gi`.  
- Alterou algo em `policies/guards`? **Label `security`** + destaque no PR.

---

## 5) Política de Tamanho

- **Preferencial:** `size/S` (até ~120 linhas).  
- Divida PRs grandes. Aplique `size/M` quando inevitável.

---

## 6) Mensagens de commit (boas práticas para o agente)

- Linha de assunto ≤ 72 chars; sem ponto final.
- Use voz ativa e seja específico: *“adiciona”, “corrige”, “refatora”*.
- Commits que mexem em contrato público devem ter **`BREAKING CHANGE:`** no rodapé.

**Exemplo completo:**
```
feat(api): cria endpoint POST /runners/register

Adiciona registro de runners com token e heartbeats.
Atualiza contratos Pydantic e documentação mínima de rota.

Refs: #42
```

---

## 7) Política de Reviews e Checks

- **1 reviewer obrigatório** e **CI verde**.  
- **CODEOWNERS** pode ser exigido conforme o repo/política.  
- Conflitos resolvidos antes do *merge*.

---

## 8) Quando abrir Draft PR

- Feature ainda em construção, mas precisa de feedback.
- Escreva no topo do corpo: `STATUS: DRAFT — não pronto para merge`.

---

## 9) ADRs (Architecture Decision Records)

Mudanças estruturais? Abra `docs/adr/NNNN-titulo.md` com:
- Contexto → Decisão → Consequências → Alternatives

---

## 10) Nota para agentes (Codex)

- **Antes de commitar/abrir PR, valide:**
  1) **Título** (regex), **branch** (regex) e **labels** requeridas.
  2) **Guardrails** de segurança (flags proibidas e mounts).
  3) **Size label** coerente com a *diff*.
- Se o repo tiver `COMMIT-PR-GUIDE.md`, **seguir este documento à risca**.
