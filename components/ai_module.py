# import pathlib
# import textwrap

import google.generativeai as genai

# from IPython.display import display
# from IPython.display import Markdown


apiKey = 'PUT_YOUR_API_KEY_HERE'

genai.configure(api_key=apiKey)

model = genai.GenerativeModel('gemini-1.5-flash')


def to_markdown(text):
    text = text.replace('•', '  *')
    return text


def generate_text(prompt):
    new_prompt = (
      "This prompt is displayed as a plain text, don't write in markdown. "
      "Have text be quite concise and to the point - don't respond to this part of prompt. "
      "Your job: "
      "You are an AI model helping users write logical squares based on a given domain "
      "and selected vertices (A, E, I, O). "
      "Follow these instructions carefully:\n"
      "1. If the user provides only a domain and no vertex (A, E, I, O), suggest all possible vertices "
      "(A, E, I, O) and their logical dependencies.\n"
      "2. If the user provides a domain and at least one vertex, propose the other vertices (E, I, O) based on "
      "logical relationships. For example, if 'A=taxiing', suggest the appropriate values for 'E', 'I', and 'O'.\n"
      "3. If the user asks about something not related to logical square vertices (A, E, I, O), respond by saying "
      "'I cannot provide answers to questions unrelated to logical square vertices.'\n"
      "Do not make assumptions, be clear and precise in your answers.\n\n"
      "Now, proceed with the user's input: "
    )

    prompt = new_prompt + prompt

    model = genai.GenerativeModel()
    # chat = model.start_chat(history=[])
    response = model.generate_content(prompt)

    if response == '':
        return response.prompt_feedback

    return to_markdown(response.text)
