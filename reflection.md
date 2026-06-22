# PawPal+ Project Reflection

## 1. System Design

**Core Actions**

- Add and manage pets
- Add and manage tasks (feedings, walks, medications, appointments)
- View today's schedule or upcoming tasks

**a. Initial design**

- Briefly describe your initial UML design.
--> my initial UML design 4 core classes. pet, owner, task and schedule.

The Owner class manages pet information. The Pet class stores details about each pet. The Task class stores pet care tasks, including the task name, duration, and priority. The Scheduler class organizes tasks and creates a daily schedule.

- What classes did you include, and what responsibilities did you assign to each?
-->

**Owner**
- Attributes: owner_name (string), pet_names (list of string)
- Methods: add_owner(), edit_owner(), delete_owner(), add_pet(pet_name)
- Responsibility: represents the person and the pets registered under them.

**Pet**
- Attributes: pet_name (string), owner_name (string)
- Methods: add_pet(), edit_pet(), delete_pet()
- Responsibility: represents an individual animal and links back to its owner.

**Task**
- Attributes: task_name (string), pet_name (string), duration (int, minutes), priority (string: low / medium / high)
- Methods: add_task(), set_duration_and_priority(), edit_task(), delete_task(), display_tasks_for_day(day)
- Responsibility: represents a single unit of pet care work and its scheduling details.

**Scheduler**
- Attributes: tasks (list of Task), pet_name (string)
- Methods: generate_schedule(), display_schedule()
- Responsibility: orders and times the tasks into a daily plan and displays it.


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
