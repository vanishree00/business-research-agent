import os
import time
from dotenv import load_dotenv
from google import genai
from tavily import TavilyClient


# Load API keys
load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")

if not gemini_key or not tavily_key:
    raise ValueError("API keys missing. Check your .env file.")

# Initialize clients
client = genai.Client(api_key=gemini_key)
tavily = TavilyClient(api_key=tavily_key)

print("Business Research Agent initialized successfully!")


def search_company(company_name):
    print(f"\nSearching the web for {company_name}...")

    response = tavily.search(
        query=f"{company_name} company overview products services customers growth",
        search_depth="basic",
        max_results=5
    )

    return response.get("results", [])



def generate_report(company_name, results):
    print("\nAnalyzing search results with Gemini...")

    source_text = ""

    for index, result in enumerate(results, start=1):
        source_text += f"""
Source {index}
Title: {result.get('title', 'N/A')}
URL: {result.get('url', 'N/A')}
Content: {result.get('content', 'N/A')}
"""

    prompt = f"""
You are a professional business research analyst.

Prepare a structured research report about {company_name}
using ONLY the supplied search results.

Report sections:
1. Company Overview
2. Products and Services
3. Target Customers and Industries
4. Market Position and Growth Opportunities
5. Three Strategic Business Recommendations
6. Key Findings and Conclusion

Rules:
- Do not invent facts or statistics.
- Mention when information is unavailable.
- Separate sourced facts from recommendations.
- Use references like [1], [2] for sourced claims.
- Do not cite sources that do not support a claim.

Search Results:
{source_text}
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

            return response.text

        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                print(f"Gemini is busy. Retrying ({attempt + 1}/3)...")
                time.sleep(10)
            else:
                raise

    raise RuntimeError(
        "Gemini is still unavailable after 3 attempts. Please try again later."
    )




if __name__ == "__main__":

    print("\n================================")
    print("     BUSINESS RESEARCH AGENT")
    print("================================")

    company_name = input("\nEnter company name: ").strip()

    if company_name:
        try:
            results = search_company(company_name)

            if results:
                report = generate_report(company_name, results)

                print("\n========== BUSINESS RESEARCH REPORT ==========\n")
                print(report)

                # Create reports folder
                os.makedirs("reports", exist_ok=True)

                # Save the generated report
                filename = f"reports/{company_name.lower().replace(' ', '_')}_report.md"

                with open(filename, "w", encoding="utf-8") as file:
                    file.write(f"# Business Research Report: {company_name}\n\n")
                    file.write(report)

                    file.write("\n\n## Sources and References\n\n")
                    for index, result in enumerate(results, start=1):
                       file.write(f"{index}. [{result.get('title', 'Source')}]")
                       file.write(f"({result.get('url', '')})\n")


                print(f"\nReport saved successfully at: {filename}")

            else:
                print("No search results found.")

        except Exception as e:
            print("\nError:", e)

    else:
        print("Please enter a valid company name.")

