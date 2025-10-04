---


## `docs_steps.md` (documentation of steps and trial-and-error)
Documentation of steps taken while building this app (what I tried, what failed, and how I fixed it):

Decided to use OpenAI ChatCompletion for simplicity and clarity of answers.

Created a minimal CLI app using rich for nicer terminal output.

Tested locally with a real API key; common issues:

openai library not installed: solved with pip install openai.

API key errors: verify OPENAI_API_KEY and network access.

Optional: tried to use transformers locally — resource-heavy and slower on CPU, so kept it
optional.

To deploy Streamlit on Hugging Face Spaces, add requirements.txt and set the entrypoint to streamlit run streamlit_app.py.

