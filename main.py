import os
import sys
import time
from dotenv import load_dotenv
import openai
from rich.console import Console
from rich.markdown import Markdown


load_dotenv()
console = Console()


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
console.print("[bold red]Error:[/bold red] OPENAI_API_KEY not set. Please set your API key as an environment variable or in a .env file.")
console.print("See README.md for setup instructions.")
sys.exit(1)


openai.api_key = OPENAI_API_KEY


MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')


system_prompt = (
"You are a helpful assistant. Answer clearly and concisely. If the user asks for code, provide a short code snippet and an explanation."
)


def ask_openai(question: str) -> str:
try:
response = openai.ChatCompletion.create(
model=MODEL,
messages=[
{"role": "system", "content": system_prompt},
{"role": "user", "content": question},
],
max_tokens=600,
temperature=0.2,
)
return response['choices'][0]['message']['content'].strip()
except Exception as e:
return f"[Error contacting API] {e}"




def main():
console.print("[bold green]Tiny AI Q&A Bot (CLI)[/bold green]")
console.print("Type a question and press Enter. Type 'exit' to quit.\n")


try:
while True:
question = console.input("[bold blue]You:[/bold blue] ")
if not question:
continue
if question.lower().strip() in ('exit', 'quit'):
console.print("Goodbye!")
break


console.print("[yellow]Thinking...[/yellow]")
answer = ask_openai(question)
console.rule("Answer")
console.print(Markdown(answer))
console.rule()
except KeyboardInterrupt:
console.print("\nExiting — goodbye!")


if __name__ == '__main__':
main(
