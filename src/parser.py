"""
FigmaParser
Converts Figma JSON nodes into semantic HTML elements.
Classifies common UI components like titles, inputs, buttons, and links.
"""

class FigmaParser:
    def __init__(self, figma_data):
        self.data = figma_data
        self.scale_x = 1.0
        self.scale_y = 1.0

    def parse(self):
        root = self.data.get("document", {})
        elements = []
        self._walk(root, elements)
        return elements

    def _walk(self, node, elements):
        node_type = node.get("type")
        style = node.get("style", {})
        fills = node.get("fills", [])
        box = node.get("absoluteBoundingBox", {})

        # Position and sizing
        if box:
            if not hasattr(self, "base_x"):
                self.base_x = box.get("x", 0)
                self.base_y = box.get("y", 0)

            x = (box.get("x", 0) - self.base_x) * self.scale_x
            y = (box.get("y", 0) - self.base_y) * self.scale_y
            w = box.get("width", 100) * self.scale_x
            h = box.get("height", 50) * self.scale_y
        else:
            x = y = w = h = 0

        position = f"left:{x}px; top:{y}px; width:{w}px; height:{h}px; position:absolute;"

        # Text layers
        if node_type == "TEXT":
            text = node.get("characters", "").strip()
            font_size = style.get("fontSize", 16)
            font_weight = 700 if "Bold" in str(style.get("fontPostScriptName", "")) else 400
            color = self._extract_color(fills)
            tag = "h1" if font_size >= 40 else "p"

            elements.append({
                "type": tag,
                "text": text,
                "style": (
                    f"{position} "
                    f"font-family:'Inter', sans-serif; "
                    f"font-weight:{font_weight}; "
                    f"font-size:{font_size}px; "
                    f"color:{color}; "
                    f"letter-spacing:-0.02em; "
                    f"line-height:1.2; margin:0;"
                )
            })

        # Rectangles → inputs / buttons
        elif node_type == "RECTANGLE":
            fill = fills[0] if fills else {}
            fill_type = fill.get("type", "SOLID")

            if fill_type == "GRADIENT_LINEAR":
                tag = "button"
                style_str = (
                    f"{position} "
                    "background:linear-gradient(90deg, rgba(149,33,139,1), rgba(58,60,179,1)); "
                    "border:none; border-radius:62px; color:white; "
                    "font-family:'Inter', sans-serif; font-size:15px; font-weight:600; "
                    "display:flex; justify-content:center; align-items:center;"
                )
            elif fill_type == "SOLID" and fill.get("color", {}).get("r", 0) > 0.8:
                tag = "button"
                style_str = (
                    f"{position} "
                    "background:rgba(240,240,245,1); border:none; border-radius:62px; "
                    "color:#353240; font-family:'Inter', sans-serif; font-size:15px; "
                    "font-weight:600; display:flex; justify-content:center; align-items:center;"
                )
            else:
                tag = "input"
                style_str = (
                    f"{position} "
                    "background:white; border:1px solid rgba(220,220,220,1); "
                    "border-radius:8px; padding:0 10px;"
                )

            elements.append({"type": tag, "text": "", "style": style_str})

        # Recurse through children
        for child in node.get("children", []):
            self._walk(child, elements)

    def _extract_color(self, fills):
        if not fills:
            return "#ccc"

        fill = fills[0]
        if fill.get("type") == "GRADIENT_LINEAR":
            stops = fill.get("gradientStops", [])
            if len(stops) >= 2:
                start = self._rgba(stops[0]["color"])
                end = self._rgba(stops[-1]["color"])
                return f"linear-gradient(90deg, {start}, {end})"
        elif fill.get("type") == "SOLID":
            return self._rgba(fill["color"])

        return "#ccc"

    def _rgba(self, color):
        r = int(color.get("r", 0) * 255)
        g = int(color.get("g", 0) * 255)
        b = int(color.get("b", 0) * 255)
        a = round(color.get("a", 1), 2)
        return f"rgba({r},{g},{b},{a})"
