import json
import os
import sys

MANIFEST_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "catalog-manifest.json")

def update_manifest(template_id, name, category, style, path, description="", tags=""):
    if not os.path.exists(MANIFEST_PATH):
        # Fallback or initialization if file doesn't exist
        print(f"Manifest file not found at {MANIFEST_PATH}, creating new.")
        data = {"templates": []}
    else:
        with open(MANIFEST_PATH, "r") as f:
            data = json.load(f)

    # Check if template already exists
    for t in data["templates"]:
        if t["id"] == template_id:
            print(f"Template {template_id} already exists.")
            return

    new_entry = {
        "id": template_id,
        "name": name,
        "category": category,
        "style": style,
        "path": path,
        "description": description,
        "tags": [tag.strip() for tag in tags.split(",") if tag.strip()] if tags else []
    }

    data["templates"].append(new_entry)

    with open(MANIFEST_PATH, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Added {name} to manifest.")

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python update_manifest.py <id> <name> <category> <style> <path> [description] [tags_comma_separated]")
    else:
        args = sys.argv[1:6]
        description = sys.argv[6] if len(sys.argv) > 6 else ""
        tags = sys.argv[7] if len(sys.argv) > 7 else ""
        update_manifest(*args, description=description, tags=tags)
