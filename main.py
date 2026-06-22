from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Zuhaib DADA")

dog = Pet("Filo", owner.owner_name)
cat = Pet("Rimuru", owner.owner_name)

owner.add_pet(dog)
owner.add_pet(cat)

# Add tasks intentionally out of time order to show off sort_by_time().
dog.add_task(Task("Evening Walk", "Filo", 30, "high", "18:00"))
dog.add_task(Task("Morning Walk", "Filo", 30, "high", "08:00"))
dog.add_task(Task("Feed Dog", "Filo", 10, "medium", "09:00"))
cat.add_task(Task("Feed Cat", "Rimuru", 5, "medium", "07:30"))
cat.add_task(Task("Clean Litter", "Rimuru", 10, "low", "12:00"))

# Two tasks scheduled at the exact same time (08:00) to trigger a conflict.
dog.add_task(Task("Give Meds", "Filo", 5, "high", "08:00"))

# Mark one task done so the status filter has something to hide/show.
dog.tasks[0].mark_complete()  # Evening Walk is done

scheduler = Scheduler(owner)

print("All tasks sorted by time (sort_by_time)")
print("-" * 40)
for task in scheduler.sort_by_time(owner.all_tasks()):
    time_label = task.start_time if task.start_time else "  --  "
    done = " [done]" if task.completed else ""
    print(f"  {time_label} — {task.task_name} ({task.pet_name}){done}")

print("\nFilo's tasks only (filter_tasks by pet)")
print("-" * 40)
for task in scheduler.sort_by_time(scheduler.filter_tasks(owner.all_tasks(), pet_name="Filo")):
    print(f"  {task.start_time} — {task.task_name}")

print("\nPending tasks only (filter_tasks by status)")
print("-" * 40)
for task in scheduler.sort_by_time(scheduler.filter_tasks(owner.all_tasks(), status="pending")):
    print(f"  {task.start_time} — {task.task_name} ({task.pet_name})")

print("\nFull daily plan (generate_schedule)")
print("-" * 40)
scheduler.display_schedule("Monday")

print("\nConflict check (conflict_warning)")
print("-" * 40)
plan = scheduler.generate_schedule("Monday")
warning = scheduler.conflict_warning(plan)
if warning:
    print(warning)
else:
    print("No time conflicts. ✅")
