
![Lyzr Automata Logo](https://github.com/LyzrCore/lyzr-experimental-automata/assets/136654928/f16a9cc6-4648-45ef-91b6-f117183d5079)

# lyzr-experimental-automata
The version 0.2 is a prompt-based agent workflow capable of executing tasks parallelly and in a stateful manner. 

## Lyzr Automata - Autonomous Multi-Agent Framework for Process Automation

Lyzr Automata is a sophisticated multi-agent automation framework designed to keep things simple, with a focus on workflow efficiency and effectiveness. It enables the creation of multiple agents that are coupled with specific tasks. The agents and tasks can run independently and complete the provided instructions, thus entering a stable state.

## How to Install

Get started with Lyzr Automata by installing the experimental package using pip:

pip install lyzr-experimental-automata

import os
import nest_asyncio
from lyzr_experimental_automata import Agent, Task, State
nest_asyncio.apply()

Note: Use nest_asyncio if you are running it on notebooks like Jupyter or Google Colab.

## Configuring Agents

Begin by configuring your agents and assigning them unique personas:

```python
agent1 = Agent(persona="enter the persona of agent1")
agent2 = Agent(persona="enter the persona of agent2")
agent3 = Agent(persona="enter the persona of agent3")
```

### Example Configuration

agent1 = Agent(persona="Marketing Consultant")
agent2 = Agent(persona="Tweet Generator")
agent3 = Agent(persona="Linkedin Post Creator")

### Creating Tasks

Create tasks by providing specific instructions and desired outcomes. Assign these tasks to your pre-defined agents:

task1 = Task("enter the instructions", "enter the desired outcome", agent1, display_output='no')

Task 1 is the initial task in the workflow. You can control the visibility of its output by setting display_output to either 'yes' or 'no'.

### Example Task 1

task1 = Task(instructions="Do a detailed research and pull out interesting marketing tips for SaaS companies. The research articles should not be more than 1500 words.",
desired_output="Ensure that you bring the best content from the likes of HBS and Saastr",
agent=agent1,max_tokens=1500,
display_output='yes')

Setting Up Dependencies

Leverage the multi-thread, parallel-processing capabilities of Lyzr Automata by specifying task dependencies. Here, 'task2' will wait for 'task1' to complete as the output of 'task2' is used as the input for 'task1'.

task2 = Task("enter the instructions", "enter the desired outcome", agent1, display_output='yes', dependencies=[task1])

### Example Task 2

task2 = Task(instructions="Use the research material provided and write five engaging tweets. Display only the tweets. No explanation or additional comments required.",
desired_output="Ensure that the tweets are as engaging as if the best influencer in the world wrote it",
agent=agent2, display_output="yes",
dependencies=[task1],
)

Continue adding tasks as required, defining their dependencies to optimize parallel processing.

task3 = Task("enter the instructions", "enter the desired outcome", agent1, display_output='yes', dependencies=[task1])

### Example Task 3

task3 = Task("Use the research material provided and write 1 short form LinkedIn post. Display only the LinkedIn post. No explanation or additional comments required.", "Ensure that the post is as if it was written by the best influencer in the world", agent3, display_output='yes', dependencies=[task1])

## How is Lyzr Automata different from other agent frameworks like LangGraph, Autogen, ChatDev?

Lyzr Automata follows a unique prompting structure (in the 'Prompt Agents') by combining Agent Persona and Task Instructions. While Agents and Tasks can exist independently, combining them allows the task to enter a steady state post-completion.

Lyzr Automata also focuses on multi-threading from the word go without compromising the 'low-code' focus of Lyzr's framework.

## Upcoming Features

1. Advanced prompt restructuring powered by Lyzr's MagicPrompts (https://magicprompts.lyzr.ai/)
2. More non-prompt agents to be added (this is where Lyzr's Multi-Agent Framework stands apart as we are taking a completely different approach towards process automation)
3. An easy-to-use UI to create workflows and debug issues
4. Even more simpler syntax to stitch together tasks to form a workflow
5. Integrations with pre-built and SOTA architecture-powered Lyzr Agent SDKs - Chat Agents, RAG Agents, Search Agents, Data Agents, Generator Agents, Summarizer Agents
6. AWS Native Agent Framework with agents running on AWS Lambda

## Contribution

Lyzr Automata is in the experimental phase, and it is open-source. Welcoming contributions.

- Fork the repository.
- Create a new branch for your feature.
- Add your feature or improvement.
- Send a pull request.

- 
