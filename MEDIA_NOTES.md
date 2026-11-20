# Media notes

All imagery in Student360 is original, flat-vector illustration of fictional people and a fictional school. None of it is a photograph and none depicts a real family, student, teacher or school. The school name "Student360 Vidyalaya" is invented for this prototype and implies no accreditation or affiliation.

## Assets

- `assets/parent_portrait.png` (1024 x 1536): a mother in a saree and her daughter in school uniform completing a workbook at home. Parent entry page and request pages.
- `assets/school_portrait.png` (1024 x 1536): a teacher in a kurta with two students in uniform reviewing a workbook under a green chalkboard. Teacher / School entry page.
- `assets/school_building.png` (1080 x 1440): the fictional Student360 Vidyalaya building with students in uniform. School showcase and the school workspace header.
- `assets/favicon.svg`: unchanged.

The lower 30 percent of both portraits is intentionally dark navy so that the HTML text overlay stays readable. Text overlays are live HTML, not baked into the images, except the building's name board.

## Regenerating

The images are produced by code, so they can be edited and regenerated without an image-generation service:

```
cd tools/art && python scenes.py   # needs rsvg-convert (librsvg) on PATH
```

`tools/art/figs.py` draws the people (skin tones, school uniforms, saree, kurta, plaits, bindi, spectacles) and `tools/art/scenes.py` composes the three scenes and writes the PNGs into the current directory (run it from `tools/art`). Copy the PNGs into `assets/`.

No image generation runs in the deployed app.
