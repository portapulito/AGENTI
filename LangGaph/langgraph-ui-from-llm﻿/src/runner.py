import asyncio
import os
from .graph import get_graph
from .config import Config

async def main():
    print("=== Generative UI Python Demo ===")
    print("Describe the UI you want to generate (e.g., 'A personal dashboard with a task list and calendar view').")
    
    user_input = input("\n> ")
    
    if not user_input.strip():
        print("Input cannot be empty. Exiting.")
        return

    print("\nGenerating your UI... please wait.")
    
    # Run the graph
    from .graph import generate_html_from_prompt
    generated_html = await generate_html_from_prompt(user_input)
    
    if generated_html:
        os.makedirs(Config.OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(Config.OUTPUT_DIR, "generated_page.html")
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(generated_html)
            
        print(f"\nSUCCESS! Page generated at:\n{output_path}")
        print("Open this file in your browser to see the result.")
    else:
        print("\nERROR: Failed to generate HTML.")

if __name__ == "__main__":
    # Ensure we can run this module directly
    asyncio.run(main())
