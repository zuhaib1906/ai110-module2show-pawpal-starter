"""Simple pytest tests for PawPal+."""

import os
import sys

# Make the project root importable when running pytest from anywhere.
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pawpal_system import Pet, Task


def test_task_completion():
    """A task starts incomplete and becomes complete after mark_complete()."""
    task = Task("Morning walk", "Biscuit", duration=30, priority="high")

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_task_addition():
    """Adding a task to a pet increases its task count by one."""
    pet = Pet("Biscuit", "Sam")

    initial_count = len(pet.tasks)

    pet.add_task(Task("Feeding", "Biscuit", duration=10, priority="high"))

    assert len(pet.tasks) == initial_count + 1
