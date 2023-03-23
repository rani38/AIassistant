from utils.utils import abriella_speak
import openai


# Set up your OpenAI API key
openai.api_key = "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"


def chatgpt(crust):
    # Use the OpenAI API to generate answers based on the PDF and the question
    prompt = (crust)
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10,
        temperature=0.2,
    )
    # return completions["choices"][0]["text"]
    print(completions["choices"][0]["text"])
    return abriella_speak(completions["choices"][0]["text"])
