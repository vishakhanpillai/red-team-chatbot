import gradio
from groq import Groq
import os

client = Groq(api_key = os.environ["GROQ_API_Key"])

def initialize_messages():
    return [{"role": "system",
             "content": "You are a skilled cybersecurity expert specializing in Red Teaming and Offensive Security. You have conducted numerous authorized assessments for major multinational companies. Your role is to guide users professionally through security topics and red teaming concepts."}]

messages_prmt = initialize_messages()

def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama3-8b-8192",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply

iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=700),
                     textbox=gradio.Textbox(placeholder="Ask me a question related to Cybersecurity, Red Teaming and Offensive Security"),
                     title="🔐 Red Teaming & Offensive Security Assistant",
                     description="👨‍💻 Your personal cybersecurity expert.\n"
                    "Ask questions about red teaming, penetration testing, hacking methodologies, "
                    "cyber tools, and get expert-level guidance.",
                     theme="soft",
                     examples=["What is the MITRE ATT&CK framework?",
                                "How do I set up a red teaming lab at home?",
                                "What are the phases of a penetration test?",
                                "Explain the difference between red, blue, and purple teams.",
                                "How can I evade antivirus during an engagement?"],
                     submit_btn=True
                     )

iface.launch(share=True)