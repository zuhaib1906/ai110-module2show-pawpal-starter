import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs")
owner_name = st.text_input("Owner name", value="Jordan")

# Create the Owner once and keep it across reruns (see st.session_state).
if "owner" not in st.session_state:
    st.session_state.owner = Owner(owner_name)
owner = st.session_state.owner
owner.owner_name = owner_name  # keep in sync with the input box

st.markdown("### Pets")
pet_name = st.text_input("Pet name", value="Mochi")

if st.button("Add pet"):
    # Add the pet only if one with that name isn't already registered.
    if any(pet.pet_name == pet_name for pet in owner.pets):
        st.warning(f"{pet_name} is already added.")
    else:
        owner.add_pet(Pet(pet_name, owner.owner_name))

if owner.pets:
    st.write("Pets:", ", ".join(pet.pet_name for pet in owner.pets))
else:
    st.info("No pets yet. Add one above.")

st.markdown("### Tasks")
st.caption("Add a few tasks to a pet. These feed into the scheduler below.")

col1, col2, col3, col4 = st.columns(4)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
with col4:
    start_time = st.text_input("Start time (HH:MM)", value="08:00")

# Pick which pet the task belongs to.
pet_choices = [pet.pet_name for pet in owner.pets]
selected_pet_name = st.selectbox("Assign to pet", pet_choices) if pet_choices else None

if st.button("Add task"):
    if selected_pet_name is None:
        st.warning("Add a pet first, then assign tasks to it.")
    else:
        # Find the chosen Pet and attach a real Task to it.
        pet = next(p for p in owner.pets if p.pet_name == selected_pet_name)
        pet.add_task(
            Task(
                task_title,
                pet.pet_name,
                int(duration),
                priority,
                start_time or None,
            )
        )

# Show every task across all pets via Owner.all_tasks().
all_tasks = owner.all_tasks()
if all_tasks:
    st.write("Current tasks:")
    st.table(
        [
            {
                "task": t.task_name,
                "pet": t.pet_name,
                "duration_minutes": t.duration,
                "priority": t.priority,
                "start_time": t.start_time or "--",
            }
            for t in all_tasks
        ]
    )
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("Generates a daily plan from all tasks, sorted by start time.")

day = st.text_input("Day", value="Monday")

if st.button("Generate schedule"):
    scheduler = Scheduler(owner)
    scheduled = scheduler.generate_schedule(day)
    if not scheduled:
        st.info("No tasks to schedule yet.")
    else:
        st.write(f"**Daily plan for {owner.owner_name} — {day}**")
        for task in scheduled:
            time_label = task.start_time if task.start_time else "--"
            st.write(
                f"{time_label} — {task.task_name} ({task.pet_name}, "
                f"{task.duration} min) [priority: {task.priority}]"
            )
        st.caption(scheduler.reasoning)
