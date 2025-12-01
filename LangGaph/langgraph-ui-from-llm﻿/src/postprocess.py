import re

def fix_html(html_content: str) -> str:
    """
    Applies simple post-processing to ensure the HTML is valid and clean.
    """
    cleaned_html = html_content.strip()
    
    # Remove markdown code blocks if present (common LLM artifact)
    # e.g., ```html ... ```
    cleaned_html = re.sub(r"^```html\s*", "", cleaned_html, flags=re.IGNORECASE)
    cleaned_html = re.sub(r"^```\s*", "", cleaned_html, flags=re.IGNORECASE)
    cleaned_html = re.sub(r"\s*```$", "", cleaned_html)
    
    # Ensure <!DOCTYPE html> is present
    if not cleaned_html.lower().startswith("<!doctype html>"):
        cleaned_html = "<!DOCTYPE html>\n" + cleaned_html
        
    # Basic check for closing html tag
    if "</html>" not in cleaned_html.lower():
        cleaned_html += "\n</html>"
        
    return cleaned_html
