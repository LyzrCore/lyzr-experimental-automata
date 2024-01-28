import asyncio
import openai

class Agent:
    def __init__(self, persona):
        self.persona = persona

class Task:
    def __init__(self, instructions, desired_output, agent, display_output='no', dependencies=None,
                 model="gpt-4-turbo-preview", temperature=1, max_tokens=1000, top_p=1,
                 frequency_penalty=0, presence_penalty=0):
        self.instructions = instructions
        self.desired_output = desired_output
        self.agent = agent
        self.display_output = display_output.lower() == 'yes'
        self.dependencies = dependencies if dependencies else []
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    async def execute(self, input_from_previous_task=""):
        persona_with_prefix = f"Your role is a {self.agent.persona}"
        prompt = (f"Instructions {self.instructions} Desired outcome: {self.desired_output} Input: {input_from_previous_task}")

        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, lambda: client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": persona_with_prefix},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty
        ))
        return response.choices[0].message.content

async def _execute_task(task, task_to_future, outputs):
    for dependency in task.dependencies:
        await task_to_future[dependency]

    input_from_previous_task = " ".join(outputs.get(dep, "") for dep in task.dependencies)
    output = await task.execute(input_from_previous_task)

    outputs[task] = output
    if task.display_output:
        print("Task Output:", output)

async def _run_tasks(tasks):
    outputs = {}
    task_to_future = {}

    for task in tasks:
        task_to_future[task] = asyncio.create_task(_execute_task(task, task_to_future, outputs))

    await asyncio.gather(*task_to_future.values())

    return " ".join(outputs[task] for task in tasks)

def State(tasks):
    return asyncio.run(_run_tasks(tasks))
