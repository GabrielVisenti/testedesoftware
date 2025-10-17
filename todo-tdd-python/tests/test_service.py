import pytest
from todo.service import TaskService
from todo.models import TaskStatus

import sys, os
# Ensure src/ is on path when running pytest locally without installing the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

@pytest.fixture
def service():
    return TaskService()

def test_add_task_should_create_with_auto_id_and_default_status_todo(service):
    t = service.add_task("Estudar TDD", "Ler sobre Red-Green-Refactor")
    assert t.id is not None
    assert t.name == "Estudar TDD"
    assert t.description == "Ler sobre Red-Green-Refactor"
    assert t.status == TaskStatus.TODO

    all_tasks = service.list_tasks()
    assert len(all_tasks) == 1
    assert all_tasks[0].id == t.id

def test_add_task_should_reject_blank_name(service):
    with pytest.raises(ValueError) as ex:
        service.add_task("   ", "desc")
    assert "nome" in str(ex.value).lower()

def test_mark_as_done_should_set_status_done(service):
    t = service.add_task("Praticar testes", "Escrever asserts")
    updated = service.mark_as_done(t.id)
    assert updated.status == TaskStatus.DONE

def test_mark_in_progress_should_set_status_in_progress(service):
    t = service.add_task("Implementar serviço", "Service + Map")
    updated = service.mark_in_progress(t.id)
    assert updated.status == TaskStatus.IN_PROGRESS

def test_edit_task_should_update_name_and_description(service):
    t = service.add_task("Antigo", "Desc antiga")
    edited = service.edit_task(t.id, "Novo", "Desc nova")
    assert edited.name == "Novo"
    assert edited.description == "Desc nova"

def test_delete_task_should_remove_task(service):
    t1 = service.add_task("A", "a")
    t2 = service.add_task("B", "b")
    service.delete_task(t1.id)

    remaining = service.list_tasks()
    assert len(remaining) == 1
    assert remaining[0].id == t2.id

def test_operations_with_missing_id_should_throw(service):
    unknown = 9999
    with pytest.raises(ValueError): service.mark_as_done(unknown)
    with pytest.raises(ValueError): service.mark_in_progress(unknown)
    with pytest.raises(ValueError): service.edit_task(unknown, "x", "y")
    with pytest.raises(ValueError): service.delete_task(unknown)

def test_list_tasks_should_return_immutable_tuple(service):
    service.add_task("X", "Y")
    tasks = service.list_tasks()
    assert isinstance(tasks, tuple)
    with pytest.raises(AttributeError):
        tasks.append("qualquer")  # tupla não possui append
