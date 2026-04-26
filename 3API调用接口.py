import base64
from openai import OpenAI
client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL,
)
img = client.images.generate(
    model=MODEL,
    prompt=content,
    n=1,
    response_format="b64_json",
    size="1024x1024",
    extra_body={"seed": 42, "use_pe": True, "num_inference_steps": 8, "guidance_scale": 1.0}
)
image_bytes = base64.b64decode(img.data[0].b64_json)
with open("output2.png", "wb") as f:
    f.write(image_bytes)
