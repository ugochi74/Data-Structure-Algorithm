def add_tag(profile, tag):
    updated = profile.copy()
    # Fix: Create a new list instead of mutating the original list in place
    updated["tags"] = updated["tags"] + [tag]
    return updated

original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")

print(original["tags"])                  # Output: ['python'] (Safe!)
print(changed is original)               # Output: False
print(changed["tags"] is original["tags"]) # Output: False (Completely independent!)



def add_tag(profile, tag):
    updated = profile.copy()
    updated["tags"].append(tag)
    return updated
original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")
print(original["tags"])
print(changed is original)
print(changed["tags"] is original["tags"])

