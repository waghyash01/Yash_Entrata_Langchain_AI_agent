import wikipedia

def get_context(topic: str) -> str:

    wikipedia.set_lang("en")

    try:
        results = wikipedia.search(topic)

        if not results:
            return ""

        page = results[0]

        try:
            return wikipedia.summary(page, sentences=5)

        except wikipedia.DisambiguationError as e:
    
            return wikipedia.summary(e.options[0], sentences=5)

        except wikipedia.PageError:
            return ""

    except Exception as e:
        print("Wikipedia Error:", e)
        return ""
