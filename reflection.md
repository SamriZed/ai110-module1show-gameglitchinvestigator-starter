# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards"). 

The New Game button was not working properly. It was expected that clicking the New Game button would reset the game and immediately start a new round. However, after finishing all attempts, the button did not restart the game, and I had to refresh the page manually. 
Another issue was the incorrect hint direction. The game sometimes told me to go lower even when the secret number was actually higher than my guess, which gave the wrong guidance.
And the secret number was revealed early even though I still had one attempt remaining, which spoiled the game.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used GitHub Copilot, Claude, and ChatGPT as AI tools for this project.

One correct suggestion came from Copilot, which recommended using the low and high values from the difficulty settings to display the guessing range to the player. This ensured that the displayed range always matched the selected difficulty level. I verified that this suggestion worked by changing the difficulty settings and confirming that the range displayed in the sidebar updated correctly.

Incorrect or misleading AI suggestion:
An incorrect suggestion came from Claude and Copilot, which recommended moving the Developer Debug section to the bottom of the page to make the attempts left update immediately. However, this did not solve the issue because the problem was caused by Streamlit’s rerun behavior. After testing this change and seeing no improvement, I tried another suggestion from ChatGPT, which was to add st.rerun() at the end of the if submit block. This fix worked because it forced the app to refresh immediately after processing a guess, allowing the attempts and history to update correctly.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

How I verified bugs were fixed:
I verified whether a bug was fixed by rerunning the Streamlit app and manually testing the game. After making a change, I refreshed the page and played the game again to see if the behavior matched what I expected. 

For example, I tested the attempts counter by submitting several guesses and checking whether the number of attempts left decreased immediately and whether the game ended at the correct attempt limit. This helped confirm that the fixes for the hint logic and attempt counting were working correctly.

I used claude to understand what some lines of code were doing. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

For me the secret nubmer wasn't changing, but if they were changing, it would be because the streamlit app was being rerun and generating a new secret number each time.

Rerunning runs the entire script every time the user interacts with the app. And any variable created normally would reset every time the app reruns. Session state prevents values from resetting between reruns.  

In my code the secret number is generated once and stored in st.session_state.secret when the game starts. This way, it remains stable throughout the game until the player wins or loses, at which point a new game can be started to generate a new secret number.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Habit or strategy I want to reuse:
One habit I want to reuse in future projects is understanding what the code is doing before asking AI to debug it. If I do not understand the code first, the AI’s suggestions can sometimes make the code more complicated and harder to follow.

What I would do differently next time:
Next time, I would focus on writing clearer and more specific prompts when asking AI for help. I learned that better prompting strategies can make debugging faster and lead to more useful suggestions.

How this project changed the way I think about AI-generated code:
This project showed me that AI-generated code is not perfect and often requires careful debugging and testing. However, it can still be a helpful starting point when building or improving a program.
