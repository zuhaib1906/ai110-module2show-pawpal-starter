from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Zuhaib DADA")

dog = Pet("Filo", owner.owner_name)
cat = Pet("Rimuru", owner.owner_name)

owner.add_pet(dog)
owner.add_pet(cat)

dog.add_task(Task("Morning Walk", "Buddy", 30, "high", "08:00"))
dog.add_task(Task("Feed Dog", "Buddy", 10, "medium", "09:00"))
cat.add_task(Task("Feed Cat", "Milo", 5, "medium", "07:30"))

scheduler = Scheduler(owner)

print("Today's Schedule")
print("-" * 20)
scheduler.display_schedule("Monday")