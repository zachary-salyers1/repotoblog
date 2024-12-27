import os
from crewai import Agent, Task, Crew, Process
from crewai.utils import load_yaml_file

# Set environment variables for API keys (replace with your own keys)
os.environ["SERPER_API_KEY"] = "your-serper-api-key"
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# Load agents and tasks from YAML files
agents_config = load_yaml_file('config/agents.yaml')
tasks_config = load_yaml_file('config/tasks.yaml')

# Create Agents
idea_refiner = Agent(**agents_config['idea_refiner'])
prd_specialist = Agent(**agents_config['prd_specialist'])
tech_architect = Agent(**agents_config['tech_architect'])
file_structure_planner = Agent(**agents_config['file_structure_planner'])
rules_engineer = Agent(**agents_config['rules_engineer'])
prompt_engineer = Agent(**agents_config['prompt_engineer'])
flow_designer = Agent(**agents_config['flow_designer'])

# Create Tasks
idea_refinement_task = Task(**tasks_config['idea_refinement_task'], agent=idea_refiner)
prd_creation_task = Task(**tasks_config['prd_creation_task'], agent=prd_specialist)
tech_stack_task = Task(**tasks_config['tech_stack_task'], agent=tech_architect)
file_structure_task = Task(**tasks_config['file_structure_task'], agent=file_structure_planner)
rules_file_task = Task(**tasks_config['rules_file_task'], agent=rules_engineer)
system_prompt_task = Task(**tasks_config['system_prompt_task'], agent=prompt_engineer)
application_flow_task = Task(**tasks_config['application_flow_task'], agent=flow_designer)

# Create Crew
crew = Crew(
    agents=[
        idea_refiner,
        prd_specialist,
        tech_architect,
        file_structure_planner,
        rules_engineer,
        prompt_engineer,
        flow_designer,
    ],
    tasks=[
        idea_refinement_task,
        prd_creation_task,
        tech_stack_task,
        file_structure_task,
        rules_file_task,
        system_prompt_task,
        application_flow_task,
    ],
    process=Process.sequential  # Tasks execute sequentially
)
