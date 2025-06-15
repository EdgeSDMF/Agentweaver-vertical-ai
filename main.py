
from agents.planner import PlannerAgent
from agents.retriever import RetrieverAgent
from agents.executor import ExecutorAgent
from agents.evaluator import EvaluatorAgent

ehr_sample = "65-year-old male with history of hypertension and chronic asthma."

planner = PlannerAgent(goal="Summarize EHR and detect patient risks")
retriever = RetrieverAgent()
executor = ExecutorAgent()
evaluator = EvaluatorAgent()

steps = planner.plan()
print(f"Planning steps: {steps}")

context = retriever.retrieve(ehr_sample)
print(f"Retrieved Context: {context}")

result = executor.execute(ehr_sample)
print(f"Execution Result: {result}")

evaluation = evaluator.evaluate(result)
print(f"Evaluation: {evaluation}")
