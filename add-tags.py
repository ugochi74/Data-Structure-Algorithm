# import copy

def add_tag(profile, tag):
    # updated  = copy.deepcopy(profile)
    #updated["tags"].append(tag)
    updated = profile.copy()
    updated["tags"] = updated["tags"] + [tag]
    return updated
original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")
print(original["tags"])
print(changed is original)
print(changed["tags"] is original["tags"])


original = {"name": "Ada", "tags": ["python"]}

changed = add_tag(original, "testing")
assert original["tags"] == ["python"]
assert changed ["tags"] == ["python", "testing"]

changed["tags"].append("go")
assert original["tags"] == ["python"]



