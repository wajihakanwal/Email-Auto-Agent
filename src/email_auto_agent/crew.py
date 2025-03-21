from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from email_auto_agent.tools.emails_tool import fetch_email_tool, response_email_tool


# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class EmailAutoAgent():
	"""EmailAutoAgent crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def email_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['email_writer'],
			verbose=True,
			tools=[fetch_email_tool],
		)

	@agent
	def response_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['response_writer'],
			verbose=True,
			tools=[response_email_tool]
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def email_write_task(self) -> Task:
		return Task(
			config=self.tasks_config['email_writer_task'],
			output_file='email.md',
		)

	@task
	def email_response_task(self) -> Task:
		return Task(
			config=self.tasks_config['email_response_task'],
			output_file='respond.md',
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the EmailAutoAgent crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
