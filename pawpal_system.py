"""PawPal+ — pet care management app.

Core functionality for Owner, Pet, Task, and Scheduler.
Beginner-friendly implementation; no Streamlit code yet.
"""

from dataclasses import dataclass, field


@dataclass
class Task:
    """Represents a single unit of pet care work and its scheduling details."""

    task_name: str
    pet_name: str
    duration: int  # minutes
    priority: str  # "low" / "medium" / "high"
    start_time: str | None = None  # "HH:MM"; None lets the scheduler place it last
    recurrence: str = "once"  # "once" / "daily" / "weekly"
    completed: bool = False  # whether the task has been done

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def set_duration_and_priority(self, duration: int, priority: str) -> None:
        """Set this task's duration and priority."""
        self.duration = duration
        self.priority = priority

    def edit_task(self, **changes) -> None:
        """Update one or more of this task's fields."""
        for field_name, value in changes.items():
            if hasattr(self, field_name):
                setattr(self, field_name, value)

    def occurs_on(self, day: str) -> bool:
        """Return whether this task should run on the given day."""
        return self.recurrence in ("once", "daily", "weekly")


@dataclass
class Pet:
    """Represents an individual animal and the tasks scheduled for it."""

    pet_name: str
    owner_name: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Attach a task to this pet."""
        self.tasks.append(task)

    def edit_task(self, task_name: str, **changes) -> None:
        """Update a task belonging to this pet (matched by name)."""
        for task in self.tasks:
            if task.task_name == task_name:
                task.edit_task(**changes)
                return

    def delete_task(self, task_name: str) -> None:
        """Remove a task from this pet (matched by name)."""
        self.tasks = [task for task in self.tasks if task.task_name != task_name]


@dataclass
class Owner:
    """Represents the person, their pets, and the scheduling constraints."""

    owner_name: str
    pets: list[Pet] = field(default_factory=list)
    available_minutes: int = 0  # daily time budget the plan should fit within
    preferences: dict = field(default_factory=dict)  # e.g. {"walk_before": "09:00"}

    def add_pet(self, pet: Pet) -> None:
        """Register a pet under this owner."""
        self.pets.append(pet)

    def edit_pet(self, pet_name: str, **changes) -> None:
        """Update a pet belonging to this owner (matched by name)."""
        for pet in self.pets:
            if pet.pet_name == pet_name:
                for field_name, value in changes.items():
                    if hasattr(pet, field_name):
                        setattr(pet, field_name, value)
                return

    def delete_pet(self, pet_name: str) -> None:
        """Remove a pet from this owner (matched by name)."""
        self.pets = [pet for pet in self.pets if pet.pet_name != pet_name]

    def all_tasks(self) -> list[Task]:
        """Return every task across all of this owner's pets."""
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks


class Scheduler:
    """Builds a daily plan from all of an owner's tasks, sorted by time."""

    def __init__(self, owner: Owner) -> None:
        """Initialize a scheduler for a given owner."""
        self.owner = owner
        self.reasoning: str = ""  # explanation of the choices made for the last plan

    def generate_schedule(self, day: str) -> list[Task]:
        """Collect the owner's tasks for the day and sort them by start time."""
        # Keep only the tasks that should run on this day.
        tasks = [task for task in self.owner.all_tasks() if task.occurs_on(day)]

        # Sort by start_time; tasks without a time ("HH:MM" is None) go last.
        scheduled = sorted(tasks, key=lambda task: task.start_time or "99:99")

        self.reasoning = (
            f"Scheduled {len(scheduled)} task(s) for {day}, "
            f"ordered by start time (untimed tasks placed last)."
        )
        return scheduled

    def display_schedule(self, day: str) -> None:
        """Print the generated daily plan and the reasoning behind it."""
        scheduled = self.generate_schedule(day)
        print(f"Daily plan for {self.owner.owner_name} — {day}")
        if not scheduled:
            print("  (no tasks)")
        for task in scheduled:
            time_label = task.start_time if task.start_time else "  --  "
            print(
                f"  {time_label} — {task.task_name} ({task.pet_name}, "
                f"{task.duration} min) [priority: {task.priority}]"
            )
        print(self.reasoning)
