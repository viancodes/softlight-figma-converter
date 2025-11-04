import os
from figma_client import FigmaClient


def main():
    """Quick check to verify the Figma API connection and access token."""

    FIGMA_FILE_KEY = "Z47gVQ7iVt0vJ9iCgfktCt"
    FIGMA_TOKEN = os.getenv("FIGMA_TOKEN")

    if not FIGMA_TOKEN:
        print("Error: FIGMA_TOKEN not found in environment variables.")
        print('Set it using PowerShell:  setx FIGMA_TOKEN "your_personal_token_here"')
        return

    print("Connecting to Figma...")

    try:
        client = FigmaClient(FIGMA_TOKEN)
        data = client.get_file(FIGMA_FILE_KEY)

        print("Connection successful.")
        print(f"File name: {data.get('name', 'Unknown')}")
        print("Top-level frames:",
              [node.get("name") for node in data.get("document", {}).get("children", [])])

    except Exception as e:
        print("Connection failed.")
        print("Details:", e)


if __name__ == "__main__":
    main()
