import openai

def texto_traduzir(text, target_language):
    openai.api_key = "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"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Traduza o seguinte texto para {target_language}:\n{text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()
