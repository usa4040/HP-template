import json
import os
import sys

MANIFEST_PATH = os.path.join(os.getcwd(), "catalog-manifest.json")

def update_manifest(template_id, name, category, style, path):
    if not os.path.exists(MANIFEST_PATH):
        data = {"templates": []}
    else:
        with open(MANIFEST_PATH, "r") as f:
            data = json.load(f)

    # Check if template already exists
    for t in data["templates"]:
        if t["id"] == template_id:
            print(f"Template {template_id} already exists.")
            return

    data["templates"].append({
        "id": template_id,
        "name": name,
        "category": category,
        "style": style,
        "path": path
    })

    with open(MANIFEST_PATH, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Added {name} to manifest.")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python update_manifest.py <id> <name> <category> <style> <path>")
    else:
        update_manifest(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
