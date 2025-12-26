from ddgs import DDGS

def web_search(query: str, max_results: int = 5) -> str:
    print("🔍 Web search query:", query)

    results_text = []

    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=max_results)

            for r in results:
                print("RAW RESULT:", r)  # 👈 DEBUG
                title = r.get("title")
                snippet = r.get("body")
                link = r.get("href")

                results_text.append(
                    f"- {title}\n  {snippet}\n  Source: {link}"
                )

        if not results_text:
            return "No relevant web results found."

        return "\n\n".join(results_text)

    except Exception as e:
        return f"Web search failed: {str(e)}"