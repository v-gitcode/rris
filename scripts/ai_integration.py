import os
import google.generativeai as genai

def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not set")
        return
    
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel("gemini-pro")
    
    # Example: Generate festival content
    response = model.generate_content(
        "Create event descriptions for a cultural festival"
    )
    
    print("Generated Festival Content:")
    print(response.text)

if __name__ == "__main__":
    main()
