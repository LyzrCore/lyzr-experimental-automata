import os
import nest_asyncio
from lyzr_experimental_automata import Agent, Task, State

os.environ["OPENAI_API_KEY"] = "sk-"

nest_asyncio.apply()

agent1 = Agent(persona="Marketing Consultant")
agent2 = Agent(persona="Tweet Generator")
agent3 = Agent(persona="Linkedin Post Creator")

task1 = Task(
    instructions="Do research and pull out interesting marketing tips for SaaS companies. The research articles should not be more than 500 words.",
    desired_output="Ensure that you bring the best content from the likes of HBS, YCombinator",
    agent=agent1,
    display_output="yes",
)

task2 = Task(
    instructions="Use the research material provided and write 5 engaging tweets. Display only the tweets. No explanation or additional comments required.",
    desired_output="Ensure that the tweets are as engaging as if it was written by the best influencer in the world",
    agent=agent2,
    display_output="yes",
    dependencies=[task1],
)

task3 = Task(
    instructions="Use the research material provided and write 1 short form LinkedIn post. Display only the LinkedIn post. No explanation or additional comments required.",
    desired_output="Ensure that the post is as if it was written by the best influencer in the world",
    agent=agent3,
    display_output="yes",
    dependencies=[task1],
)

output = State([task1, task2, task3])

print(output)
