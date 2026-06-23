from core.retrieval import get_db

db = get_db()

data = db.get()

filenames = set()

for metadata in data["metadatas"]:
    filenames.add(
        metadata.get("filename", "Unknown")
    )

for filename in sorted(filenames):
    print(filename)