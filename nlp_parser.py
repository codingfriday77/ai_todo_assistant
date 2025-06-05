import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def parse_task_from_text(text):
    prompt = f"""Extract the task, date, and time from the following sentence:\n\n"{text}"\n\nFormat:\nTask: <task>\nDate: <YYYY-MM-DD>\nTime: <HH:MM in 24hr format or blank>"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    result = response.choices[0].message.content

    task_line = next((line for line in result.splitlines() if line.startswith("Task:")), "")
    date_line = next((line for line in result.splitlines() if line.startswith("Date:")), "")
    time_line = next((line for line in result.splitlines() if line.startswith("Time:")), "")

    task = task_line.replace("Task:", "").strip()
    date = date_line.replace("Date:", "").strip()
    time = time_line.replace("Time:", "").strip()

    return task, date, time
