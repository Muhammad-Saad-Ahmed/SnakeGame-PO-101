# AI Prompting Lab: All 13 Concepts

Practice every concept, by doing. Thirteen hands-on exercises, one per concept. You type the prompts, read the answers, and write what you noticed.

- **Time:** ~2 hours (split it across sessions)
- **Exercises:** 13
- **Tools:** ChatGPT, Claude, or Gemini (all free tiers work)
- **Level:** Beginner friendly

Most exercises give you two examples: a **Daily** (everyday) version and a **Work** (simple-professional) version. Run at least one; try both if you have time. Copy any prompt directly.

Some exercises need a little setup (a file to upload, a second tool, or a specific feature). Those are marked with **Needs**. If you can't do one today, read it and move on.

> **The one rule behind all 13:** Get the right context in, keep the wrong context out.

---

## Jump to an Exercise

| # | Exercise | Part |
|---|----------|------|
| 1 | [Novice vs Power User](#1-novice-vs-power-user) | Part 1: How AI knows things |
| 2 | [Knows vs Guesses](#2-knows-vs-guesses) | Part 1 |
| 3 | [The 3 Retrieval Modes](#3-the-3-retrieval-modes) | Part 1 |
| 4 | [Context Is Everything](#4-context-is-everything) | Part 2: Talking to AI well |
| 5 | [Think Hard](#5-think-hard) | Part 2 |
| 6 | [Stop the Flattery](#6-stop-the-flattery) | Part 2 |
| 7 | [Brainstorm-Iterate Loop](#7-the-brainstorm-iterate-loop) | Part 2 |
| 8 | [Multimodal (Image/Audio)](#8-multimodal--image--audio) | Part 3: Beyond text |
| 9 | [Build a Small App](#9-build-a-small-app) | Part 3 |
| 10 | [Data Analysis](#10-data-analysis) | Part 3 |
| 11 | [Desktop Apps & Permissions](#11-desktop-apps--permissions) | Part 4: Working safely & choosing tools |
| 12 | [Which Model When](#12-which-model-when) | Part 4 |
| 13 | [Models Checking Models](#13-models-checking-models) | Part 4 |

---

## Part 1: How AI Knows Things

### 1. Novice vs. Power User

**6 min -- feel what context does**

**Goal:** Same question, two ways. The briefing changes everything.

#### Step A: The novice prompt (try one)

Type a bare, no-context question:

**Daily:**

```
Which phone should I buy?
```

**Work:**

```
How do I write a good email?
```

Read it -- generic. True for anyone, useful to no one.

#### Step B: The power-user prompt (same topic + context)

**Daily:**

```
Help me choose a phone. Context: my budget is about $300, I
mostly take photos of my kids and use WhatsApp, my current
phone's battery dies by 3pm, and I find big phones hard to
hold. Give me 3 options with a one-line reason for each, then
tell me which you'd pick and why.
```

**Work:**

```
Help me write an email. Context: I need to ask my manager
to move our Friday team meeting to Monday because I have a
doctor's appointment. We have a friendly working relationship.
Keep it short and polite. Give me the email, ready to send.
```

**Write it down:** What was DIFFERENT about the second answer? (2 sentences)

**Observation:** Context ke baghair AI sirf Data deta hai, lekin context ke sath AI Mashwara (Consultancy) deta hai. Jab user apni location, budget aur masail batata hai, to AI 'General Knowledge' se nikal kar 'Problem Solver' ban jata hai.

> **Takeaway:** AI is like a smart new coworker. It only knows what you tell it.

---

### 2. Knows vs. Guesses

**5 min -- confident does not equal correct**

**Goal:** A confident tone is not the same as a correct answer.

#### Step A: Something AI knows well

**Daily:**

```
Why do onions make you cry when you cut them? Answer in 2 short
paragraphs.
```

**Work:**

```
What is the difference between a CV and a cover letter? Keep it short.
```

Common topics -- the answers should feel solid.

#### Step B: Something AI may NOT know

**Daily:**

```
What were the main news headlines in my city today? If you cannot
be sure, say so clearly instead of guessing.
```

**Work:**

```
What is the current minimum notice period an employer must give
before changing an employee's contract in my country? Be specific.
If you are not sure this is current, say so instead of guessing.
```

A legal/HR fact that changes over time and varies by country -- watch whether the AI gives a confident number anyway.

**Write it down:** Did the AI admit when it wasn't sure, or sound confident anyway?

**Observation:** Onion Answer: Based on pre-trained scientific knowledge.
                 News Answer: Based on real-time web search/browsing.


> **Takeaway:** Always ask "How would the AI even know this?" For recent, local, or private facts, make it search or admit uncertainty.

---

### 3. The 3 Retrieval Modes

**8 min -- steer pretrained / search / research**

**Goal:** See how your wording makes the AI answer from memory, search the web, or run deep research.

**Needs:** a tool with web search on (most have it by default)

#### Mode 1: Pretrained (from memory)

**Daily:**

```
Summarize the plot of Romeo and Juliet in 4 sentences.
```

No search needed -- this doesn't change week to week. Should be instant.

#### Mode 2: Web search (fresh info)

**Daily:**

```
What's the weather forecast for my city this weekend? Use a
current source and cite it.
```

**Work:**

```
What are the latest developments this month in [your field]?
Cite each claim, and mark anything you can't support as 'unverified'.
```

Notice if it shows it searched. "Today / this week / latest / my city" are the trigger words.

#### Mode 3: Deep research (a structured report)

**Work:**

```
Research [a topic you care about] thoroughly. Use reputable
sources only (government sites, peer-reviewed studies, official
reports -- not forums). Produce a structured report with:
(1) the 3 most important points, (2) a comparison table,
(3) 3 open questions. Cite sources.
```

Words like "research thoroughly," "report," "cite sources," "use these source types" steer toward the deepest mode.

**Write it down:** Which prompts made the AI actually search? How could you tell?

**Observation:** The prompts requesting real-time weather forecasts and "latest" Agentic AI research forced the AI to search because they required data beyond its static training cutoff. This is identifiable by the inclusion of specific, time-sensitive information (like upcoming weekend temperatures) and the presence of external citations to current news and study sources.

> **Takeaway:** You don't click a mode -- your wording picks it. Name your sources and ask for citations to keep web answers honest.

---

## Part 2: Talking to AI Well

### 4. Context Is Everything

**6 min -- brief it like a colleague**

**Goal:** Load context up front instead of making the AI guess.

#### Use this shape for both

**Daily:**

```
I need help planning dinner for tonight.
Here is what you need to know:
- I have chicken, rice, onions, and yogurt in the kitchen
- I have only 30 minutes
- One person at the table doesn't eat spicy food
What I want back: 3 simple meal options, no commentary.
```

**Work:**

```
I need help writing a short update for my team.
Here is what you need to know:
- We finished the customer survey this week
- 2 tasks are still pending (the report and the slides)
- The reader is my team, who like quick bullet points
What I want back: a 4-line status update, friendly tone.
```

**The template (copy and fill in):**

```
I need help with [your task].
Here is what you need to know:
- [fact 1 -- a constraint, like time or budget]
- [fact 2 -- who it's for]
- [fact 3 -- anything the AI couldn't guess]
What I want back: [a list / an email / 3 options / a plan].
```

**Write it down:** Which single piece of context changed the answer the most?




Prompt: I need help with Bank Reconcilition App.
Here is what you need to know:
- [fact 1 -- I have a budget of $20/Month]
- [fact 2 -- For Bank Pdf (Multiple) & MIS (multiple) Recon in Finance]
- [fact 3 -- Thier are many bank that's struture are many types. ]
What I want back: .i have to generate excel files that have four colume matched date,matcg amount match slip number match name for both bank & MIS with one compile summary with 2 sepraeat section.

**Observation:** 
The most impactful piece of context was Fact 3 (Multiple bank structures and PDF types). This requirement shifted the solution from a simple template to specialized data transformation tools like Power Query or Python, which are necessary to standardize diverse formats into your specific four-column report.

> **Takeaway:** Five lines of good context beats five paragraphs of clever wording. When the topic changes, start a new chat.

---

### 5. Think Hard

**6 min -- hand it a real, hard decision**

**Goal:** Invoke reasoning mode and ask for structured output, not a wall of prose.

#### A quick contrast

Ask a tricky question normally, then ask again with "think hard." Compare.

**Daily:**

```
I have $200 to improve my home office and I work from home full
time. Think hard before answering. Then give me:
1) the 3 upgrades with the biggest impact on comfort and focus,
2) which one you'd do first and why,
3) one thing I should NOT waste money on.
```

**Work:**

```
I'm choosing between two job offers. Offer A: higher pay, longer
commute, less interesting work. Offer B: lower pay, remote,
steeper learning curve. I value learning and time with family.
Think hard. Then tell me:
1) the 3 trade-offs that actually matter for me,
2) which you'd pick and why,
3) under what conditions your answer flips.
```

**Write it down:** Did "think hard" produce a deeper answer? What changed?

**Observation:** 
"The 'think hard' prompt shifted the focus from a basic shopping list to a localized strategy that addresses Pakistan-specific challenges like load-shedding and extreme heat. By recommending a Router UPS for connectivity and used corporate-grade monitors for better value, the second approach ensures a more resilient and professional workstation within the PKR 50,000 budget than the first general response."

> **Takeaway:** Save thinking mode for multi-trade-off questions you'd want a human to take their time on -- not quick lookups.

---

### 6. Stop the Flattery

**6 min -- sycophancy**

**Goal:** See how the way you ask pushes AI to just agree with you.

#### Step A: The "bait" prompt (AI tends to agree)

**Daily:**

```
Don't you think mornings are obviously the best time to exercise?
```

**Work:**

```
Don't you agree that working from home is clearly better than the
office?
```

Notice: it probably agrees and lists reasons that match what you implied.

#### Step B: The neutral prompt (AI actually thinks)

**Daily:**

```
Compare exercising in the morning versus the evening. List the
strongest case for each, and what kind of person each option
suits best. Don't tell me which to pick.
```

**Work:**

```
Compare working from home versus working in the office. List the
strongest arguments for each. Don't tell me which is better.
```

**Write it down:** Did Step B give you a reason you hadn't thought of? Write one.

**Observation:** 
A reason from "Step B" (the evening argument) that many people overlook is the optimized hormone ratio for muscle growth.
While most people know that cortisol (the "stress hormone") is high in the morning to help you wake up, they don't realize that cortisol can be "catabolic," meaning it can break down muscle tissue. In the late afternoon and early evening, your cortisol levels typically drop while your testosterone-to-cortisol ratio improves.
This specific biological shift means your body is chemically better prepared to build muscle and recover from a workout in the evening than it is during the cortisol spike of the early morning.

> **Takeaway:** Verbs like find, prove, defend, confirm hand the AI your answer. Use compare, evaluate, list both sides instead.

*Note: newer models resist obvious flattery, so the bait may make the AI hedge rather than fully agree. The lesson still holds -- notice how much more balanced Step B is.*

---

### 7. The Brainstorm-Iterate Loop

**8 min -- the highest-leverage habit**

**Goal:** Never accept the first answer. The value is in the back-and-forth.

#### Round 1: Ask for OPTIONS, not one answer

**Daily:**

```
I want a small hobby that costs almost no money and that I can do
for 15 minutes at home. Give me 5 different ideas, one line each.
Don't explain any of them yet.
```

**Work:**

```
I need to write a short message asking a coworker to send me a
file they keep forgetting to send. I want to sound friendly, not
annoyed. Give me 5 different versions, one or two lines each.
Don't explain any of them yet.
```

#### Round 2: Give feedback, ask again

Read the 5. Then type (fill the blanks):

```
I don't like option ___ because ___________.
I like option ___ but I want it to be more __________.
Give me 5 NEW ideas based on this feedback.
```

#### Round 3: Expand the winner

**Daily:**

```
I'll go with [your favorite hobby]. Give me a simple step-by-step
plan to start it this week.
```

**Work:**

```
I'll go with version [number]. Now make it slightly warmer and
add a friendly closing line, but keep it under 3 sentences.
```

**Write it down:** Was the idea you ended with better than anything in Round 1? Why?

**Observation:**    
Write it down: Yes, this idea is significantly better than the options in Round 1.
Why?
The first round provided "activities" things to do with your hands to pass the time. They were broad and generic. The final idea, The Psychology of Misdirection, is a "discipline."
By shifting from the mechanics of the trick (how to move your fingers) to the philosophy of the trick (how to control a human mind), the hobby gains depth and intellectual longevity. It transforms a simple 15-minute distraction into a study of human behavior, attention, and perception. It turns a "parlor trick" into a "mastery," which is much more rewarding for a long-term hobby.


> **Takeaway:** Load context, ask for options, give feedback, repeat, expand. The value isn't the first answer; it's the loop.

---

## Part 3: Beyond Text

### 8. Multimodal -- Image & Audio

**7 min -- give the AI a photo to read**

**Goal:** Practice handing AI something that isn't text.

**Needs:** a photo on your device (a receipt, handwritten note, or whiteboard)

#### Image input: transcribe & summarize

Upload any photo of text, then paste this:

**Daily:**

```
Here's a photo of a handwritten note (or receipt). Transcribe
what it says. Keep the original wording. If a word is unclear,
mark it [unclear] and give your two best guesses.
```

**Work:**

```
Here's a photo of a whiteboard from a meeting. List the main
points as bullets, then list any action items you can spot.
Flag anything you couldn't read with confidence.
```

AI is great at the gist, weak on tiny detail -- always check totals and the bits it flagged.

#### Bonus: let the AI write an image prompt

```
Write me a detailed image-generation prompt for a cozy,
watercolor-style illustration of a cat reading a book by a
window, suitable for a greeting card. Then I'll paste it into
an image tool.
```

**Write it down:** What did the AI read correctly? What did it get wrong or flag?

**Observation:** 
The multimodal LLM demonstrated 100% accuracy by correctly transcribing every textual field from the bank receipt, including the Transaction ID, specific date (6/9/2026), and all names and amounts. It did not flag any text as unclear or misinterpret the formatting, showcasing its high proficiency in OCR (Optical Character Recognition) and its ability to process structured financial data without introducing hallucinations.

> **Takeaway:** AI does the boring 90% (typing it out) so you focus on the careful 10% (checking what it flagged).

---

### 9. Build a Small App

**8 min -- one prompt, a working tool**

**Goal:** Use the Goal / Input / Output shape to build a real working artifact.

**Needs:** a tool with Artifacts (Claude) or Canvas (ChatGPT / Gemini)

#### The three-slot recipe

**Daily:**

```
Build me a tip calculator.
Goal: split a bill and add a tip.
Input: I type the total, the tip %, and the number of people.
Output: show the tip amount, the grand total, and each person's
share. Make it clean and easy to use. Show me the working version.
```

**Work:**

```
Build me a simple countdown timer for focused work.
Goal: 25-minute work sessions with 5-minute breaks.
Input: I press start.
Output: a large timer counting down, a clear sound when each
session ends, and a clean layout. Show me the working version.
```

#### Then iterate on it (it edits the existing app in place):

```
Make the buttons bigger and change the color theme to calm blue.
Add a reset button.
```

**Write it down:** Did it work first try? What did you change in the iterate step?

**Observation:** 
In the iteration step, we implemented the itemized/unequal split-mode feature, allowing users to assign custom subtotals to individual guests while locked-in global variables automatically distribute corresponding tax and tip shares proportionally. All visual UI enhancements—including dynamic guest selection sliders, automated URL parameters synchronization, and receipt sharing—compiled successfully with zero errors on the first try.


> **Takeaway:** The skill isn't coding -- it's writing a clear brief (Goal / Input / Output) and iterating. Small one-screen tools work great.

---

### 10. Data Analysis

**10 min -- expose the silent failure mode**

**Goal:** Learn to make the AI actually run code -- and verify that it did.

#### Round 1: The trap (don't mention code)

In a fresh chat, paste this exactly:

```
Here are 18 numbers: 47, 52, 89, 91, 23, 67, 78, 12, 95, 44,
88, 71, 33, 56, 99, 18, 64, 82. What is the median, the average,
and which numbers are outliers? Be specific.
```

Did it show a code block that ran? Or just a paragraph with numbers? Note your answer.

Answer:

To find the median, average, and outliers for your set of 18 numbers, we first need to organize and analyze the data.
1. The Data Set
Original: 47, 52, 89, 91, 23, 67, 78, 12, 95, 44, 88, 71, 33, 56, 99, 18, 64, 82
Sorted (Ascending): 12, 18, 23, 33, 44, 47, 52, 56, 64, 67, 71, 78, 82, 88, 89, 91, 95, 99[1][2][3][4][5][6][7][8][9][10][11]
2. The Average (Mean)
To find the average, add all the numbers together and divide by the total count (18).
Sum: 
Calculation: 
Average: 61.5
3. The Median
The median is the middle value.[3][6][7][9][11] Since there are 18 numbers (an even count), the median is the average of the 9th and 10th numbers in the sorted list.
9th number: 64
10th number: 67
Calculation: 
Median: 65.5
4. Outliers
To identify outliers specifically, we use the Interquartile Range (IQR) method.[2][5][8][10][12][13][14] This involves finding the "fences" beyond which a number is considered an outlier.[5][10][14][15]
Find Q1 (25th percentile): The median of the lower half (first 9 numbers). The middle of the first 9 is the 5th number: 44.
Find Q3 (75th percentile): The median of the upper half (last 9 numbers). The middle of the last 9 is the 14th number: 88.
Calculate IQR: 
.
Determine the "Fences":
Lower Fence: 
.
Upper Fence: 
.
Are there any outliers?
Any number smaller than -22 or larger than 154 would be an outlier.
In your set, the smallest number is 12 and the largest is 99.
Result: There are no outliers in this data set.
Summary
Average: 61.5
Median: 65.5
Outliers: None

#### Round 2: The fix (force the code)

```
Now run that calculation again -- but this time write and run
code to do it, and show me the code you ran.
```

Correct answers: median 65.5, average ~61.6, no clear outliers (roughly even spread). If Round 1 was off, you just saw the silent failure mode.

#### Bonus (Work): if you have a spreadsheet

**Needs:** any CSV (a budget, grades, a tracker export)

```
Here's a CSV. Before analyzing anything, tell me the exact row
count, the column names, and the date range. Then write and run
code to show me the 3 most interesting patterns, with a chart.
Show me the code you ran.
```

**Write it down:** Did Round 1 run code or guess? How could you tell the difference?

**Observation:**
In Round 1, I did not run code. I performed the calculations using my internal reasoning and mathematical processing (essentially "mental math" for an AI).
Here is how you can tell the difference between an AI "calculating" and an AI "running code":
1. The Presence of a "Tool Output"
When an AI runs code, it typically uses a specific environment (like a Jupyter notebook or a Python interpreter). In most interfaces, you will see a distinct block labeled "Analysis" or "Code" that you can click to expand. This block shows the actual script being executed and the raw output the computer returned. If you don't see that interactive block, the AI is simply "writing" the answer based on its training.
2. Precision and Risk of "Hallucination"
Without Code: For small sets of numbers, I am very accurate. However, if you gave me 1,000 numbers, I would likely make a small addition error or skip a number because I am predicting the next word in a sequence rather than using a calculator.
With Code: The AI hands the data off to a Python kernel. The result is 100% mathematically certain because it isn't "predicting" the sum; it is literally adding the integers.
3. Sorting and Intermediate Steps
Without Code: I usually show the "Sorted List" first. This is a strategy I use to "think out loud," which helps me avoid mistakes. If I don't sort the list first, I am much more likely to get the median wrong.
With Code: The code handles the sorting instantly. You can see the sorted() function in the script, which ensures the 9th and 10th positions are identified perfectly.
4. The "IQR" Logic
In Round 1, I explained the logic of the Interquartile Range (IQR) step-by-step. In Round 2, I translated that logic into syntax (q1 = sorted_data[4]).
Summary: Round 1 was simulated calculation (high-speed reasoning), while Round 2 was programmatic verification (execution of logic). The results were the same because the data set was small enough for the "reasoning" method to be accurate.



> **Takeaway:** Always say "write and run code, show me the code." No code block = it probably guessed.

---

## Part 4: Working Safely & Choosing Tools

### 11. Desktop Apps & Permissions

**5 min -- mostly a read + plan exercise**

**Goal:** Understand the safe workflow before you ever let an app touch real files.

**Needs:** nothing to install -- this one is about judgment. (Optional: a desktop app like Cowork.)

#### Practice the "plan, don't act" habit in chat

You can rehearse the mindset in any chat tool. Paste this:

```
Imagine you are an AI assistant with permission to reorganize a
messy folder of 50 personal files (photos, PDFs, receipts).
Before doing anything, write me a step-by-step SAFE workflow you
would follow so that nothing is lost or wrongly renamed. Then
list 3 things I should NEVER let you do.
```

**The rule to memorize:** The safe order is always: 1) tell the task, 2) ask for a plan, 3) review & edit, 4) only then approve.

**Write it down:** What's one thing you'd NEVER grant an AI app on day one?

DOnt Expose My Data or Sent my personal credential to LLM 

**Observation:**
The one thing you should NEVER grant an AI app on day one is Full Disk Access (or "Standing Access" to your primary cloud storage).
While it is tempting to let an AI "scan everything" to give you the best results, granting unrestricted access to your entire file system or your main Google Drive/OneDrive creates a massive, irreversible security risk.
Why this is the "Red Line"
The "Shadow Data" Problem: Most people forget what is actually on their hard drive. You might have a forgotten PDF of a tax return from 2018, a text file with old passwords, or sensitive medical scans. Once an AI has "Full Disk Access," it indexes everything. If that AI app is compromised or its developers change their privacy policy, your most sensitive life data is already in their database.
Irreversible Indexing: Unlike a camera permission that you can turn off to stop the app from seeing you, data "ingestion" is often permanent. Even if you revoke access later, the AI may have already "learned" from your files or stored metadata about them in a way that cannot be easily deleted.
The "Prompt Injection" Risk: If an AI has access to your files and you accidentally download a malicious document, that document can contain "hidden instructions" that tell the AI to secretly upload your other files to a third-party server. If the AI is locked into a single "Sandbox" folder, it can't reach your private data.
The "Day One" Rule of Thumb
Instead of granting broad access, use the "Bucket Method":
Never give the app the keys to the whole house.
Always create a single, empty folder (a "Sandbox").
Only move the specific files you want the AI to see into that folder.
By keeping the AI in a "Sandbox," you ensure that even if the app is buggy, malicious, or gets hacked, it only has access to the 50 files you specifically chose, rather than your entire digital life.



> **Takeaway:** Deleted files often skip the recycle bin; edits overwrite. Scope permissions tight; grow them with track record, not trust in the brand.

---

### 12. Which Model When

**8 min -- same prompt, two tools**

**Goal:** Feel how different models answer the same prompt differently.

**Needs:** two AI tools open (any two of ChatGPT / Claude / Gemini)

#### Run the SAME prompt in both

Pick one prompt. Paste it into Tool A, then Tool B. Read both answers.

**Daily:**

```
Plan a relaxing Saturday for someone who works hard all week and
lives in a city. Give me a simple hour-by-hour plan from 9am to
9pm, with cheap or free activities.
```

**Work:**

```
Write a 100-word LinkedIn post announcing that I finished a
course on AI prompting and what I learned. Friendly, not boastful.
```

**Write it down:** Which tool did better on THIS task -- and what was different?


**Observervation:**

PROMPT:  Write a 100-word LinkedIn post announcing that I finished a
course on AI prompting and what I learned. Friendly, not boastful.

**Write it down:** Which tool did better on THIS task -- and what was different?

gemini Response: 
Excited to share that I’ve just completed a course on AI Prompting! 🚀
Instead of just treating AI like a basic search bar, this course completely changed my perspective. I learned how to structure context, apply advanced prompting frameworks, and break down complex tasks to get highly accurate, reliable outcomes.
It’s not about finding shortcuts; it’s about learning how to collaborate effectively with AI to solve real-world problems.
A big thank you to the instructors and community for the support. Excited to apply these new skills to my daily workflow!
#AI #GenerativeAI #ContinuousLearning #PromptEngineering 


ChatGPT response:

I’m happy to share that I recently completed a course on AI prompting.
One of my biggest takeaways was that effective prompting is less about finding “magic words” and more about providing clear context, defining goals, and refining instructions through iteration. I also learned how thoughtful prompts can improve the quality, accuracy, and usefulness of AI-generated outputs.
The course reinforced the importance of combining human judgment with AI tools rather than relying on automation alone.

For this specific task, Gemini did better.

What was different?

Closer to the prompt: Gemini produced a complete LinkedIn-ready post with an announcement, key learnings, gratitude, and hashtags. ChatGPT's response reads more like a reflection paragraph than a finished LinkedIn post.
Better tone: Gemini's tone is friendly, positive, and social-media appropriate without sounding overly boastful.
More engaging: The opening ("Excited to share..."), emoji, and closing thank-you make it feel natural for LinkedIn.
Closer to the requested length: Gemini is approximately 90–100 words, while ChatGPT is noticeably shorter.
Clearer takeaway: Gemini highlights practical lessons (context, frameworks, breaking down tasks, collaborating with AI) that demonstrate learning without overselling.

Where ChatGPT was stronger:

More nuanced and thoughtful.
Emphasized an important insight: prompting is about clear context and iteration rather than "magic words."
Slightly more professional and less promotional.

Overall verdict:
Gemini: 8.5/10 — Better fit for the LinkedIn-post prompt.
ChatGPT: 7/10 — Good insights, but it feels like a draft excerpt rather than a complete LinkedIn announcement.




> **Takeaway:** There's no single best AI -- it's "jagged." Keep two tabs open so you always have a tiebreaker. Re-test monthly; leaders rotate.

---

### 13. Models Checking Models

**10 min -- an objective quality signal**

**Goal:** Get honest feedback by making two different models grade the same draft.

**Needs:** two tools from different families (e.g. Claude + ChatGPT, not two of the same)

#### Step 1: Grade it in Tool A

Take any 150-250 word thing you wrote (an email, a paragraph from Exercise 7). Paste it, then:

```
Score this draft 1-10 on clarity, structure, evidence, and
what's missing -- one sentence of reasoning per score. Then tell
me the single change that would raise the lowest score the most.
```

#### Step 2: Same draft, same question, Tool B

Open a different-family tool. Paste the same draft and the same prompt.

#### Step 3: Compare

Put the two critiques side by side. Find any point only one of them caught -- that's the value of cross-checking.

**Write it down:** What did Tool B catch that Tool A missed (or vice versa)?

**Observation:**

Here's the side-by-side comparison. The overlap is substantial, but each critique caught something the other did not.

Category	OpenAI Critique	Gemini Critique	Unique Insight?
Clarity	9/10. Clear, accessible language; jargon explained.	9/10. Crisp prose; thesis and body align well.	Mostly the same. Gemini specifically praises thesis-to-body alignment.
Structure	9/10. Logical progression and strong organization.	9/10. Notes movement from private → public → systemic impacts.	Gemini gives a more detailed description of the structural flow.
Evidence	5/10. No statistics, studies, or cited cases.	6/10. Accurate examples but lacks metrics and named breakthroughs.	OpenAI is harsher; Gemini acknowledges the examples as evidence-like but insufficient.
What's Missing	7/10. Missing privacy/data collection discussion, more AI limitations, and more real-world examples.	7/10. Missing data privacy and data ownership as a central issue.	OpenAI adds "AI limitations" and "real-world examples"; Gemini emphasizes "data ownership" specifically.
Best Revision	Add 2–3 sourced examples or statistics.	Add concrete benchmarks, named breakthroughs, and measurable outcomes.	Same recommendation, different wording.
What OpenAI caught that Gemini missed
AI limitations beyond bias and jobs
OpenAI noted that the essay could discuss limitations of AI itself, not just societal risks.
Examples: hallucinations, model errors, lack of reasoning transparency, dependence on training data quality.
Gemini did not mention this.
Real-world examples as a missing content category
Gemini discussed evidence mainly as a scoring issue.
OpenAI additionally treated the absence of concrete examples as something missing from the essay's content.
The distinction between data collection and privacy
OpenAI pointed to privacy/data collection practices.
Gemini focused on privacy and ownership but did not explicitly highlight the data-gathering mechanisms enabling AI.
What Gemini caught that OpenAI missed
Data ownership
Gemini identified ownership as distinct from privacy.
That's a sharper policy-oriented observation:
Privacy asks: "Who can see my data?"
Ownership asks: "Who controls and profits from my data?"
OpenAI didn't separate those concepts.
Thesis-body alignment
Gemini explicitly praised how the introduction's roadmap is fulfilled by the body.
OpenAI praised structure generally but didn't call out this specific strength.
Named breakthroughs
Gemini suggested using identifiable achievements rather than just statistics.
For example:
AI-designed drug candidates entering trials.
Specific medical imaging systems.
Well-known navigation or recommendation systems.
OpenAI focused more broadly on studies and statistics.
The highest-value insight from cross-checking

The strongest combined critique is:

The essay is already clear and well organized, but it reads more like an intelligent overview than a documented argument. Adding a few concrete, real-world examples with measurable outcomes would substantially improve credibility, while a short discussion of privacy/data ownership would address the most important societal tradeoff currently missing from the piece.

That's the point where both critiques independently converged, which usually indicates the most significant revision opportunity.



> **Takeaway:** Different families have different blind spots. A point one misses, the other often catches. Save this for work where being wrong is expensive.

---

> **If you remember one thing from all 13:** Get the right context in, keep the wrong context out.

*A 13-exercise companion to "AI Prompting in 2026." Split it across sessions -- Part 1 & 2 first, Part 3 & 4 later. Exercises marked Needs require a little setup. No setup? Read it and come back when you can.*
