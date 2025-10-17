# To-Do List TDD (Python + pytest)

Projeto simples para praticar **Test-Driven Development (TDD)** com uma lista de tarefas em memória, agora em **Python**.

## Requisitos cobertos
- Adicionar tarefa (nome + descrição)
- Marcar como **concluída** (DONE)
- Marcar como **em andamento** (IN_PROGRESS)
- Editar **nome** e **descrição**
- Excluir tarefa
- Listar tarefas (retorna tupla imutável)

## Como rodar
> Requer Python 3.10+

```bash
# 1) (opcional) criar venv
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# 2) instalar dependências
pip install -r requirements.txt

# 3) rodar testes
pytest -q
```

## Estrutura
```
todo-tdd-python/
├─ requirements.txt
├─ README.md
├─ src/
│  └─ todo/
│     ├─ __init__.py
│     ├─ models.py
│     └─ service.py
└─ tests/
   └─ test_service.py
```
