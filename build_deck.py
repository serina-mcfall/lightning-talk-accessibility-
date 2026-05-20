#!/usr/bin/env python3
"""
Build the Yellow Squiggles Are People lightning talk deck via gws CLI.

Slide 1 is built against the existing default slide's placeholders.
Slides 2-5 are created fresh.

Idempotent at the API level: object IDs are fixed, so re-running on the same
PRESENTATION_ID will fail with "already exists" errors. To rebuild cleanly,
create a new presentation first.
"""

import json
import subprocess
import sys

PRESENTATION_ID = "1p45f19ukVQuDtrKoJRPbZjxe6hymg1XZuG-dBtMcDXY"

# Drive file IDs for the images (already uploaded + made publicly readable)
IMAGE_URL = lambda fid: f"https://drive.google.com/uc?id={fid}"
IMG_SQUIGGLE = IMAGE_URL("1u_1lYgwS4jjJ6jQcu2jXr8wtewMPgWHL")
IMG_FIX = IMAGE_URL("176JERcn72J9A4PXxubjX8th5kj-DCvGx")
IMG_BUTTON = IMAGE_URL("1Qfa5JeVcEXjovILRIPVBLtJPa47JdxPz")
IMG_EYE = IMAGE_URL("1r6xYY_Jisbs-H1lnusCITPTZqicL03DU")
IMG_KEYBOARD = IMAGE_URL("1mOF8Z0hMUUu85iniVATAThKdiuO6_aRn")
IMG_PERSON = IMAGE_URL("1ejIuyK3d3gHAEiBqh6zBP0C2xABtP_BB")

# Colors
COLOR_TEXT = {"opaqueColor": {"rgbColor": {"red": 0.10, "green": 0.10, "blue": 0.10}}}
COLOR_MUTED = {"opaqueColor": {"rgbColor": {"red": 0.40, "green": 0.40, "blue": 0.40}}}
COLOR_ACCENT = {"opaqueColor": {"rgbColor": {"red": 1.0, "green": 0.70, "blue": 0.0}}}

FONT = "Lexend"


# ---------- API wrappers ----------

def batch_update(requests: list) -> dict:
    body = json.dumps({"requests": requests})
    params = json.dumps({"presentationId": PRESENTATION_ID})
    result = subprocess.run(
        ["gws", "slides", "presentations", "batchUpdate",
         "--params", params, "--json", body],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"ERROR: {result.stderr}", file=sys.stderr)
        print(f"STDOUT: {result.stdout}", file=sys.stderr)
        sys.exit(1)
    out = result.stdout
    start = out.find("{")
    return json.loads(out[start:]) if start >= 0 else {}


# ---------- Request builders ----------

def insert_text(object_id, text):
    return {"insertText": {"objectId": object_id, "text": text}}


def style_text(object_id, style, start=None, end=None):
    text_range = {"type": "ALL"} if start is None else {
        "type": "FIXED_RANGE", "startIndex": start, "endIndex": end
    }
    fields = ",".join(style.keys())
    return {
        "updateTextStyle": {
            "objectId": object_id, "textRange": text_range,
            "style": style, "fields": fields,
        }
    }


def center_paragraph(object_id):
    return {
        "updateParagraphStyle": {
            "objectId": object_id,
            "style": {"alignment": "CENTER"},
            "fields": "alignment",
            "textRange": {"type": "ALL"},
        }
    }


def create_text_box(object_id, slide_id, x, y, w, h):
    return {
        "createShape": {
            "objectId": object_id, "shapeType": "TEXT_BOX",
            "elementProperties": {
                "pageObjectId": slide_id,
                "size": {
                    "width": {"magnitude": w, "unit": "PT"},
                    "height": {"magnitude": h, "unit": "PT"},
                },
                "transform": {
                    "scaleX": 1, "scaleY": 1,
                    "translateX": x, "translateY": y, "unit": "PT",
                },
            },
        }
    }


def create_slide(slide_id, layout="BLANK"):
    return {
        "createSlide": {
            "objectId": slide_id,
            "slideLayoutReference": {"predefinedLayout": layout},
        }
    }


def create_image(object_id, slide_id, url, x, y, w, h):
    return {
        "createImage": {
            "objectId": object_id, "url": url,
            "elementProperties": {
                "pageObjectId": slide_id,
                "size": {
                    "width": {"magnitude": w, "unit": "PT"},
                    "height": {"magnitude": h, "unit": "PT"},
                },
                "transform": {
                    "scaleX": 1, "scaleY": 1,
                    "translateX": x, "translateY": y, "unit": "PT",
                },
            },
        }
    }


def set_alt_text(object_id, description):
    return {
        "updatePageElementAltText": {
            "objectId": object_id,
            "description": description,
            "title": "",
        }
    }


# ---------- Style presets ----------

def heading(size=32):
    return {
        "fontFamily": FONT, "fontSize": {"magnitude": size, "unit": "PT"},
        "bold": True, "foregroundColor": COLOR_TEXT,
    }


def body(size=16, muted=False):
    return {
        "fontFamily": FONT, "fontSize": {"magnitude": size, "unit": "PT"},
        "foregroundColor": COLOR_MUTED if muted else COLOR_TEXT,
    }


def accent_heading(size=48):
    return {
        "fontFamily": FONT, "fontSize": {"magnitude": size, "unit": "PT"},
        "bold": True, "foregroundColor": COLOR_ACCENT,
    }


# ---------- Slide builders ----------

def build_slide_2():
    """The squiggle — title + screenshot."""
    sid = "slide2"
    return [
        create_slide(sid),
        # Title
        create_text_box("s2_title", sid, 60, 30, 600, 50),
        insert_text("s2_title", "Last week, this happened."),
        style_text("s2_title", heading(28)),
        center_paragraph("s2_title"),
        # Screenshot
        create_image("s2_img", sid, IMG_SQUIGGLE, 160, 100, 400, 280),
        set_alt_text("s2_img",
            "VS Code editor showing a ClickyDiv React component with a yellow underline squiggle under the div onClick attribute."),
    ]


def build_slide_3():
    """Who got locked out — 3 columns."""
    sid = "slide3"
    requests = [
        create_slide(sid),
        # Title
        create_text_box("s3_title", sid, 60, 25, 600, 40),
        insert_text("s3_title", "Who got locked out"),
        style_text("s3_title", heading(28)),
        center_paragraph("s3_title"),
    ]
    # Three columns
    cols = [
        ("kbd", IMG_KEYBOARD, "Keyboard users",
         "Motor impairments, RSI, broken mouse. Can't Tab to a <div>.",
         "A simple line drawing of a keyboard.", 80),
        ("scr", IMG_PERSON, "Screen reader users",
         "Blind, low-vision. A <div> isn't announced as interactive.",
         "A simple line drawing of a person standing.", 290),
        ("swt", IMG_EYE, "Switch & eye-tracking users",
         "Severe motor impairments. All work through the keyboard layer.",
         "A simple line drawing of an eye.", 500),
    ]
    for code, img, head, body_text, alt, x in cols:
        # Icon (75x75)
        requests += [
            create_image(f"s3_{code}_icon", sid, img, x + 35, 100, 75, 75),
            set_alt_text(f"s3_{code}_icon", alt),
            # Heading
            create_text_box(f"s3_{code}_h", sid, x - 20, 200, 185, 30),
            insert_text(f"s3_{code}_h", head),
            style_text(f"s3_{code}_h", heading(16)),
            center_paragraph(f"s3_{code}_h"),
            # Body
            create_text_box(f"s3_{code}_b", sid, x - 20, 235, 185, 100),
            insert_text(f"s3_{code}_b", body_text),
            style_text(f"s3_{code}_b", body(12)),
            center_paragraph(f"s3_{code}_b"),
        ]
    return requests


def build_slide_4():
    """The fix — side-by-side code screenshots with OR pivot + takeaway."""
    sid = "slide4"
    return [
        create_slide(sid),
        # Title
        create_text_box("s4_title", sid, 60, 20, 600, 40),
        insert_text("s4_title", "The fix"),
        style_text("s4_title", heading(28)),
        center_paragraph("s4_title"),
        # Left caption
        create_text_box("s4_lcap", sid, 30, 75, 280, 24),
        insert_text("s4_lcap", "three-piece manual fix"),
        style_text("s4_lcap", body(14, muted=True)),
        center_paragraph("s4_lcap"),
        # Left image
        create_image("s4_limg", sid, IMG_FIX, 30, 105, 280, 200),
        set_alt_text("s4_limg",
            "VS Code editor showing a ClickyDivFixed React component using role button, tabIndex, onClick, and onKeyDown handlers."),
        # OR pivot
        create_text_box("s4_or", sid, 322, 175, 76, 60),
        insert_text("s4_or", "OR"),
        style_text("s4_or", accent_heading(40)),
        center_paragraph("s4_or"),
        # Right caption
        create_text_box("s4_rcap", sid, 410, 75, 280, 24),
        insert_text("s4_rcap", "just use <button>"),
        style_text("s4_rcap", body(14, muted=True)),
        center_paragraph("s4_rcap"),
        # Right image
        create_image("s4_rimg", sid, IMG_BUTTON, 410, 105, 280, 200),
        set_alt_text("s4_rimg",
            "VS Code editor showing a JustAButton React component using a native HTML button element."),
        # Takeaway
        create_text_box("s4_take", sid, 60, 340, 600, 50),
        insert_text("s4_take", "Use native HTML first. Reach for <div> last."),
        style_text("s4_take", heading(20)),
        center_paragraph("s4_take"),
    ]


def build_slide_5():
    """Closing — big statement + small footer."""
    sid = "slide5"
    return [
        create_slide(sid),
        # Big statement
        create_text_box("s5_big", sid, 60, 130, 600, 130),
        insert_text("s5_big",
            "Yellow squiggles aren't nitpicks.\nThey're people."),
        style_text("s5_big", heading(40)),
        center_paragraph("s5_big"),
        # Footer
        create_text_box("s5_foot", sid, 60, 320, 600, 30),
        insert_text("s5_foot",
            "Your future user.  Your future self.  Better software."),
        style_text("s5_foot", body(14, muted=True)),
        center_paragraph("s5_foot"),
    ]


# ---------- Run ----------

if __name__ == "__main__":
    print("Building Slide 2...")
    batch_update(build_slide_2())
    print("Building Slide 3...")
    batch_update(build_slide_3())
    print("Building Slide 4...")
    batch_update(build_slide_4())
    print("Building Slide 5...")
    batch_update(build_slide_5())
    print()
    print("Done. Open the deck at:")
    print(f"https://docs.google.com/presentation/d/{PRESENTATION_ID}/edit")
