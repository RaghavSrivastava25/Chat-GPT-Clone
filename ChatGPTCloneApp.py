#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import openai
import gradio as gr

#openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = "xxxxx"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "This is Raghav's Chat GPT Clone."

def openai_create(prompt):

    response = openai.Completion.create(
    model="code-davinci-002",
    prompt=prompt,
    temperature=0.9,
    max_tokens=8000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Raghav's ChatGPT Clone using OpenAI API hosted with Gradio</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True, share=True)


# In[3]:


pip install openai


# In[4]:


pip install gradio


# In[ ]:




