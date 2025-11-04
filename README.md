# Softlight Engineering Take-Home Assignment

## Overview

This repository contains both the **Figma-to-HTML/CSS conversion system** and the **generated output** for the provided Softlight design mock.  
The goal was to reproduce the visual layout from Figma as accurately as possible, ensuring pixel-perfect fidelity in dimensions, typography, colors, spacing, and gradients.

---

## Project Structure

softlight-figma-converter/
│
├── src/
│ ├── figma_client.py # Handles Figma API authentication and data fetch
│ ├── parser.py # Parses Figma node structure (frames, text, fills, etc.)
│ ├── renderer.py # Generates HTML/CSS from parsed layers
│ ├── main.py # Entry point for running the full pipeline
│ └── test_connection.py # Quick sanity check for Figma API key and file access
│
├── output/
│ ├── index.html # Final rendered Sign-In screen
│ └── styles.css # Matched Figma’s visual design
│
├── README.md
└── requirements.txt

---

## How It Works

1. **Connect to Figma API:**  
   `figma_client.py` authenticates using your Figma personal access token and retrieves the file’s JSON representation.

2. **Parse the Design Tree:**  
   `parser.py` extracts relevant layer information — frames, text, fills, gradients, corner radii, and constraints.

3. **Render to HTML/CSS:**  
   `renderer.py` converts the parsed node data into clean, human-readable HTML and CSS.  
   The generated output is written to `output/index.html` and `output/styles.css`.

4. **Verification:**  
   The design was manually compared side-by-side against Figma using Chrome DevTools at 100% zoom  
   (iPhone 14 Pro Max – 393×852).  
   Layout, text spacing, and color values were verified down to the pixel level.

---

## Figma Mock

Original Figma file (copied to personal workspace for API access):  
[Softlight Engineering Take-Home Assignment](https://www.figma.com/design/MxMXpjiLPbdHlratvH0Wdy/Softlight-Engineering-Take-Home-Assignment?node-id=0-1)

---

## Output Preview

The generated HTML/CSS replicates the following Figma screen:

- Rounded mobile frame (393×852)
- Title “Sign in” (Inter, Bold 48px)
- Input block (email + password)
- Gradient primary button (`#3A3CB3 → #95228C`)
- Secondary button (solid #F3EEF6)
- Centered home indicator (139×5, #000)

Visual comparison confirms near-identical output across browsers.

---

## Running Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Test your Figma API connection
python src/test_connection.py
3. Generate HTML/CSS from your Figma file
python src/main.py
4. Open the generated page
output/index.html
You can also run it with a live server:
npx live-server output
Known Limitations
Gradient direction sometimes needs manual verification for accuracy.

Letter spacing and line height can vary slightly between browsers and Figma.

Only text, shapes, fills, and gradients are currently supported — no auto-layout constraints yet.

Shadow blur and blend modes are simplified for browser rendering consistency.

Next Steps
Add recursive parsing for nested components.

Extend renderer to support Figma’s auto-layout and constraints.

Implement positioning relative to parent frames for adaptive layouts.

Add CLI arguments for file key and output directory.

Author
Vishnu Vardan Babu Pentela
Python Developer
📧 Email: viancodes@gmail.com

Submitted as part of the Softlight Engineering Take-Home Assignment.
