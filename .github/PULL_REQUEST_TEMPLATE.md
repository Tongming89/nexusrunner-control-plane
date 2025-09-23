# Pull Request

> 🔎 **Leia antes de abrir:** consulte o [COMMIT-PR-GUIDE.md](../COMMIT-PR-GUIDE.md) para títulos, branching, labels e guardrails obrigatórios.

## Contexto
Explique o problema/objetivo que este PR resolve.

## O que foi feito
- [ ] Item 1
- [ ] Item 2

## Como validar
Passos de verificação manual e/ou comando(s):
```bash
# comandos de teste / smoke
```

## Segurança / Policies (obrigatório)
- [ ] Sem `--privileged` e sem `--net=host`
- [ ] Mounts apenas em `/workspace` e `/cache`
- [ ] Quotas razoáveis (cpu/mem) ou justificadas
- [ ] Secrets fora do repo (Actions/Envs)

## Checklist (auto-serviço do agente)
- [ ] Título segue Conventional Commits (`type(scope): subject`)
- [ ] Branch segue o padrão (`feat|fix|.../<slug>`)
- [ ] Labels aplicadas: tipo + prioridade (`P0|P1|P2|P3`) + `security` (se aplicável)
- [ ] CI verde
- [ ] Documentação atualizada (README/ADRs) quando aplicável
- [ ] Issues relacionadas linkadas no rodapé

## Refs
Refs: #<issue-id>
