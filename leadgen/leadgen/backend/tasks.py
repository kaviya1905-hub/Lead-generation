from celery import Celery
from llm import generate_icp_questions

celery_app = Celery("tasks", broker="redis://redis:6379/0", backend="redis://redis:6379/0")

@celery_app.task(bind=True, soft_time_limit=30, time_limit=40)  # <--- add timeout
def generate_questions_async(self, persona, industry):
    try:
        questions = generate_icp_questions(persona, industry)
        if not questions:
            return ["Question generation failed"]
        return questions
    except Exception as e:
        return [f"Error: {str(e)}"]
