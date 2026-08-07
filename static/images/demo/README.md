## Demo images

Drop `.jpg` / `.jpeg` / `.png` / `.gif` / `.webp` files directly in this folder.
They'll show up in the gallery automatically and be searchable — no AWS needed.

Search matches against two things for each image:
1. Words in the filename (e.g. `golden-retriever-beach.jpg` matches "dog" partially and "beach" exactly).
2. Optional labels you add in `labels.json` in this folder, e.g.:

```json
{
  "golden-retriever-beach.jpg": ["dog", "golden retriever", "beach", "sunset"],
  "city-skyline-night.jpg": ["city", "skyline", "night", "buildings"]
}
```

Labels in `labels.json` give much better search results than relying on
filenames alone, so add a few descriptive words per image if you can.
