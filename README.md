# Softlight Figma Converter

This project is a Python system that connects to the Figma API, reads design data, and generates matching HTML/CSS output.  
The goal is to take any Figma mock and recreate it as a pixel-perfect web page — keeping layout, colors, typography, and spacing as close as possible.

---

## Project Structure


softlight-figma-converter/
│
├── src/
│ ├── figma_client.py # Handles API calls and authentication
│ ├── parser.py # Parses nodes, frames, text, fills, etc.
│ ├── renderer.py # Converts parsed layers into HTML/CSS
│ ├── main.py # Entry point for the conversion pipeline
│ └── test_connection.py # Quick check for Figma API access
│
├── output/
│ ├── index.html # Rendered design output
│ └── styles.css # Matching CSS for layout and typography
│
├── LICENSE
├── README.md
└── requirements.txt


---

## Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/viancodes/softlight-figma-converter.git
   cd softlight-figma-converter

2. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate       # Windows
   source venv/bin/activate    # macOS/Linux
   pip install -r requirements.txt


3. Create a .env file in the root folder with your Figma credentials:
   ```bash
   FIGMA_API_KEY=your_figma_token
   FIGMA_FILE_KEY=your_figma_file_key


You can get the file key from the Figma file URL and generate a token from your Figma account settings.

##Running the Converter

   Run the main script:
   
   python src/main.py


This will connect to the Figma API, fetch all nodes, and create index.html and styles.css inside the output/ folder.

To test if your setup is correct:

python src/test_connection.py

Notes

Works with both public and private Figma files (as long as the token has access).

The output HTML/CSS aims for visual accuracy, not complex interactions.

The code is modular — easy to extend for new Figma node types or export options.

License

MIT License
