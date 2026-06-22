# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
Daily plan for Zuhaib DADA — Monday
  07:30 — Feed Cat (Milo, 5 min) [priority: medium]
  08:00 — Morning Walk (Buddy, 30 min) [priority: high]
  09:00 — Feed Dog (Buddy, 10 min) [priority: medium]
Scheduled 3 task(s) for Monday, ordered by start time (untimed tasks placed last).
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

Daily plan for Zuhaib DADA — Monday
  07:30 — Feed Cat (Milo, 5 min) [priority: medium]
  08:00 — Morning Walk (Buddy, 30 min) [priority: high]
  09:00 — Feed Dog (Buddy, 10 min) [priority: medium]
Scheduled 3 task(s) for Monday, ordered by start time (untimed tasks placed last).

```
# Paste your pytest output here

======================================== test session starts =========================================
platform darwin -- Python 3.13.13, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/zuhaibv/Documents/gits/ai110-module2show-pawpal-starter
plugins: anyio-4.14.0
collected 17 items                                                                                                 

tests/test_pawpal.py .................                                                       [100%]

========================================= 17 passed in 0.02s =========================================

Confidence Level: ⭐⭐⭐⭐⭐ (5/5 Stars)

```

## 📐 Smarter Scheduling

PawPal+ does more than list your tasks — it organizes the day for you:

| Feature | What it does for you |
|---------|----------------------|
| **Time Sorting** | Arranges tasks earliest to latest. Untimed tasks go to the bottom; tasks at the same time are ordered by priority (high first). |
| **Pet Filtering** | Show just one pet's tasks, or hide the ones you've already finished. |
| **Time Budget** | Set how many minutes you have, and PawPal+ keeps your most important tasks first, setting the rest aside. |
| **Conflict Alerts** | Warns you when two tasks overlap or start at the same time, and whether it's the same pet or different pets. |
| **Recurring Tasks** | Mark a task daily or weekly. Finish one and the next is scheduled automatically — tomorrow for daily, next week for weekly. |
| **Plan Explanation** | Every schedule comes with a short summary of what was planned, what got deferred, and any conflicts found. |
| **Task Management** | Add tasks, edit their time/duration/priority, mark them done, or delete them. |
| **Pet Management** | Add pets, update their details, or remove them — each pet keeps its own task list. |

## 📸 Demo Walkthrough

1. Enter the owner name (e.g. "Jordan").
2. Type a pet name ("Mochi") and click Add pet.
3. Fill in a task ("Morning walk", 20 min, high, 08:00), select Mochi, and click Add task.
4. Add a few more tasks — they appear in the Current tasks table, already sorted by time.
5. Use the pet/status filters to narrow the view (e.g. just Mochi's pending tasks).
6. Set the day to "Monday" and click Generate schedule to see today's ordered plan, conflict check, and reasoning.


![Project 2 Demo](Project%202%20Demo.png)
