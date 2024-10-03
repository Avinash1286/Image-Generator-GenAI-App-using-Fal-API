import gradio as gr
import fal_client

def generate_image(prompt):
    handler = fal_client.submit(
        "fal-ai/flux/dev",
        arguments={
            "prompt": prompt
        },
    )
    
    result = handler.get()
    image_url = result['images'][0]['url']
    return image_url

iface = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter your prompt"),
    outputs=gr.Image(type="filepath", label="Generated Image"),
    title="fal-ai/flux/dev Image Generator",
    description="Enter a prompt to generate an image using the fal-ai/flux/dev model."
)

iface.launch()