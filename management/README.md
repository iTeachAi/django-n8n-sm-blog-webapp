# 🏀 Full Court Press

**From a single lesson to a full-court article — no travel calls, no shot clock violations.**

Full Court Press is a Django + n8n powered basketball content platform that takes one raw coaching idea and runs it the length of the floor: from a short lesson description, through an AI-assisted automation pipeline, into a fully structured, publish-ready educational blog post. Think of it as a fast break for content — you inbound the idea, the system pushes it up the court, and it finishes at the rim with a title, summary, category, author, and full article body, ready to be stored and displayed.

---

## 🏆 The Play (What It Does)

The workflow is built like a possession — a clear sequence, each step setting up the next:

1. **Inbound the ball** — A user submits a basketball lesson description through the Django front end.
2. **Run the play through n8n** — That description is sent through an n8n webhook into an AI-assisted automation process that generates several possible article topics.
3. **Call the play** — The user picks the strongest topic from the options generated.
4. **Set the screen** — The system prompts the user with five required questions designed to surface missing details, explain cause and effect, connect the concept back to the bigger picture of the game, and sharpen the article's core message.
5. **Take the shot** — Once all five answers are in, the automation generates a complete blog: title, category, summary, author, publication date, and full article content.
6. **Box score** — Django models, views, templates, and the ORM store and display the finished piece, ready to be added to the growing library of content.

No missed shots, no forced turnovers — just a clean, guided path from idea to article.

---

## ⚙️ Under the Hood (Tech & Tools)

Full Court Press runs a full rotation of tools, each playing a specific position:

- **Python & Django** — the point guard, running the offense: models, views, templates, and the ORM handling all the ball-handling and structure.
- **n8n** — the playmaker off the bench, orchestrating the automation via webhooks and Code nodes to turn a lesson description into topics, questions, and a finished article.
- **JSON responses & Webhooks** — the passing lanes connecting Django and n8n so data moves cleanly between the two.
- **Bootstrap & Bootstrap Icons** — the uniform, giving the platform a clean, dashboard-style, responsive look.
- **Custom CSS** — the finishing touches: a chrome-inspired styling pass and Netflix-style blog cards that make browsing articles feel like scrolling a streaming library instead of a spreadsheet.
- **SQLite** — the current home court for development, keeping things light and fast while the project is built out.

---

## 🎯 Full Bench (Features)

- Guided, multi-step lesson-to-article workflow
- AI-assisted topic generation via n8n automation
- Five-question deep-dive to strengthen article substance before generation
- Automatic blog structuring — title, category, summary, author, publish date, and content
- Django-powered storage, retrieval, and display through models, views, templates, and the ORM
- Dashboard-style, responsive UI with chrome-inspired styling
- Netflix-style blog cards for browsing generated content

---

## Program Screenshots 
![App Dashboard](/screenshots/appDashboard.jpg)
![App Post Form](/screenshots/app-smpostform.jpg)
![Blog Dashboard](/screenshots/blogDashboard.jpg)
![Blog Topics](/screenshots/blogTopics.jpg)
![Blog Questions](/screenshots/blogquestions.jpg)

## 🔮 Next Season (Future Upgrades)

Every good team has an offseason plan. Here's what's on the roster for future development:

- **Secure, signed webhooks** — tightening up the connection between Django and n8n so no unauthorized passes get intercepted
- **User authentication** — knowing who's actually on the roster
- **Image uploading & cloud storage** — giving articles visuals, not just words
- **AI-generated cover images** — automatic art for every article
- **PostgreSQL migration** — trading up from SQLite for a database built for the long season
- **Blog editing** — the ability to call a timeout and revise a play after it's run
- **Search & filtering** — faster ways to find a specific article in a growing playbook
- **Analytics** — box scores for content: what's getting read, and how often
- **Generation history** — a record of every possession, not just the final score
- **Improved error handling** — fewer unforced turnovers in the workflow
- **Content expansion tools** — turning one lesson into social posts, video scripts, lesson plans, and other educational formats, so a single idea can run multiple plays

---

## 🤝 Coaching Staff (Credits)

Full Court Press was designed and directed by **MO**, who wrote the majority of the code and set the overall project vision, workflow logic, and direction from tip-off to final buzzer.

**AI** is credited as a coding partner throughout the project — assisting with debugging, workflow planning, prompt development, and contributing to roughly **90%** of the Bootstrap-based template design.

---

*Full Court Press — because every great article deserves full-court effort.*