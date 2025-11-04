import os
from figma_client import FigmaClient
from parser import FigmaParser
from renderer import HTMLRenderer


def main():
    """Main entry point for the Figma-to-HTML/CSS converter."""
    FIGMA_FILE_KEY = "Z47gVQ7iVt0vJ9iCgfktCt"
    FIGMA_TOKEN = os.getenv("FIGMA_TOKEN")

    if not FIGMA_TOKEN:
        print("Error: FIGMA_TOKEN not found. Set it as an environment variable and try again.")
        return

    # Step 1: Fetch Figma file data
    client = FigmaClient(FIGMA_TOKEN)
    data = client.get_file(FIGMA_FILE_KEY)
    print("Figma file retrieved successfully.")

    # Step 2: Parse design elements
    parser = FigmaParser(data)
    elements = parser.parse()
    print(f"Parsed {len(elements)} design elements from Figma.")

    # Step 3: Generate HTML and CSS
    renderer = HTMLRenderer(elements)
    renderer.render("output")
    print("HTML and CSS files generated in the 'output' folder.")


if __name__ == "__main__":
    main()
