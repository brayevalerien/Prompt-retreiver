from PIL import Image
import ast

def get_raw_metadata(image: Image) -> dict:
    return (image.info or {}).copy()

def extract_info(raw_metadata: dict) -> tuple[str, str, str]:
    parameters = ast.literal_eval(raw_metadata["parameters"])
    positive = parameters["prompt"] or ""
    negative = parameters["negative_prompt"].split("unrealistic, saturated, high contrast, big nose, painting, drawing, sketch, cartoon, anime, manga, render, CG, 3d, watermark, signature, label")[0] or ""
    model = parameters["base_model"] or ""
    return positive, negative, model

def extract_metadata(image_path):
    if image_path is None: # handles the case when image is removed
        return "", "", ""
    raw_metadata = get_raw_metadata(Image.open(image_path))
    positive, negative, model = extract_info(raw_metadata)
    return positive, negative, model
    