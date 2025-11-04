#Softlight Engineering Take-Home Assignment

This repository contains both the Figma-to-HTML/CSS conversion system and the generated output for the provided Softlight design mock.
The goal was to reproduce the visual layout from Figma as accurately as possible, ensuring pixel-perfect fidelity in dimensions, typography, colors, spacing, and gradients.

#Project Structure
softlight-figma-converter/
│
├── src/
│   ├── figma_client.py      # Handles Figma API authentication and data fetch
│   ├── parser.py            # Parses Figma node structure (frames, text, fills, etc.)
│   ├── renderer.py          # Generates HTML/CSS from parsed layers
│   ├── main.py              # Entry point for running the full pipeline
│   └── test_connection.py   # Quick sanity check for Figma API key and file access
│
├── output/
│   ├── index.html           # Final rendered Sign-In screen
│   └── styles.css           # Matched Figma’s visual design
│
├── README.md
└── requirements.txt

#How It Works
1. Connect to the Figma API

figma_client.py authenticates using your Figma personal access token and retrieves the file’s JSON representation.

2. Parse the Design Tree

parser.py extracts relevant layer information — frames, text, fills, gradients, corner radii, and constraints.

3. Render to HTML/CSS

renderer.py converts the parsed node data into clean, human-readable HTML and CSS.
The generated output is written to output/index.html and output/styles.css.
