"""PawPal+ — pet care management app.

Class skeleton generated from diagrams/uml.mmd.
Attributes and method stubs only; logic is not implemented yet.
"""

from dataclasses import dataclass


class Owner:
    """Represents the person and the pets registered under them."""

    def __init__(self, owner_name: str, pet_names: list[str] | None = None) -> None:
        """Initialize an owner with a name and an optional list of pet names."""
        self.owner_name: str = owner_name
        self.pet_names: list[str] = pet_names if pet_names is not None else []

    def add_owner(self) -> None:
        """Register a new owner."""
        ...

    def edit_owner(self) -> None:
        """Update this owner's details."""
        ...

    def delete_owner(self) -> None:
        """Remove this owner."""
        ...

    def add_pet(self, pet_name: str) -> None:
        """Register a pet under this owner."""
        ...


@dataclass
class Pet:
    """Represents an individual animal and links back to its owner."""

    pet_name: str
    owner_name: str

    def add_pet(self) -> None:
        """Register a new pet."""
        ...

    def edit_pet(self) -> None:
        """Update this pet's details."""
        ...

    def delete_pet(self) -> None:
        """Remove this pet."""
        ...


@dataclass
class Task:
    """Represents a single unit of pet care work and its scheduling details."""

    task_name: str
    pet_name: str
    duration: int  # minutes
    priority: str  # "low" / "medium" / "high"

    def add_task(self) -> None:
        """Create a new task."""
        ...

    def set_duration_and_priority(self) -> None:
        """Set this task's duration and priority."""
        ...

    def edit_task(self) -> None:
        """Update this task's details."""
        ...

    def delete_task(self) -> None:
        """Remove this task."""
        ...

    def display_tasks_for_day(self, day) -> None:
        """Show the tasks scheduled for the given day."""
        ...


class Scheduler:
    """Orders and times the tasks into a daily plan and displays it."""

    def __init__(self, pet_name: str, tasks: list["Task"] | None = None) -> None:
        """Initialize a scheduler for a pet with an optional list of tasks."""
        self.pet_name: str = pet_name
        self.tasks: list[Task] = tasks if tasks is not None else []

    def generate_schedule(self) -> None:
        """Order and time the tasks into a daily plan."""
        ...

    def display_schedule(self) -> None:
        """Display the generated daily schedule."""
        ...
