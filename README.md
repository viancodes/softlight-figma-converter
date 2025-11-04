Softlight Engineering Take-Home Assignment
Overview

This repository contains both the Figma-to-HTML/CSS conversion system and the generated output for the provided Softlight design mock.
The goal was to reproduce the visual layout from Figma as accurately as possible, ensuring pixel-perfect fidelity in dimensions, typography, colors, spacing, and gradients.

Project Structure
softlight-figma-converter/
│
├── src/
│   ├── figma_client.py      → Handles Figma API authentication and data fetch
│   ├── parser.py            → Parses Figma node structure (frames, text, fills, etc.)
│   ├── renderer.py          → Generates HTML/CSS from parsed layers
│   ├── main.py              → Entry point for running the full pipeline
│   └── test_connection.py   → Quick sanity check for Figma API key and file access
│
├── output/
│   ├── index.html           → Final rendered **Sign-In** screen
│   └── styles.css           → Matched Figma’s visual design
│
├── README.md
└── requirements.txt

How It Works

Connect to Figma API
figma_client.py authenticates using your Figma personal access token and retrieves the file’s JSON representation.

Parse the Design Tree
parser.py extracts relevant layer information — frames, text, fills, gradients, corner radii, and constraints.

Render to HTML/CSS
renderer.py converts the parsed node data into clean, human-readable HTML and CSS.
The generated output is written to:
output/index.html and output/styles.css.

Verification
The design was manually compared side-by-side against the Figma mock using Chrome DevTools (100% zoom)
with dimensions set to iPhone 14 Pro Max – 393×852.
Layout, text spacing, and color values were verified pixel-by-pixel.

Figma Mock

Original design (copied to personal workspace for API access):
🔗 Softlight Engineering Take-Home Assignment

Output Preview

The generated HTML/CSS replicates the following Figma screen:

Rounded mobile frame (393×852)

Title “Sign in” — Inter, Bold 48 px

Input block (email + password)

Gradient primary button → #95228C → #3A3CB3

Secondary button → solid #F3EEF6

Centered home indicator (139×5, #000)

The output was visually verified for accuracy across browsers.

Running Locally
1. Install dependencies
pip install -r requirements.txt

2. Test your Figma API connection
python src/test_connection.py

3. Generate HTML/CSS from your Figma file
python src/main.py

4. Open the generated page
output/index.html


Or run it with a local live server:

npx live-server output

Known Limitations

Gradient direction might require manual fine-tuning.

Minor differences in letter spacing or line height may appear across browsers.

Currently supports text, shapes, fills, and gradients only (no auto-layout yet).

Shadows and blend modes are simplified for consistent browser rendering.

Next Steps

Add recursive parsing for nested components.

Extend renderer for auto-layout and constraints.

Support relative positioning for adaptive layouts.

Add CLI arguments for file key and output directory.

Author

Vishnu Vardan Babu Pentela
Python Developer
📧 viancodes@gmail.com

Submitted as part of the Softlight Engineering Take-Home Assignment.
