import gradio as gr
import metadata_extracter as emd

groot = gr.Blocks(title="Prompt Retreiver")

with groot:
    with gr.Column():
        input_image = gr.Image(type="filepath")
        positive = gr.Text(label="Positive prompt", show_label=True, show_copy_button=True)
        negative = gr.Text(label="Negative prompt", show_label=True, show_copy_button=True)
        model = gr.Text(label="Model name", show_label=True, show_copy_button=True)
        
    input_image.change(
        fn=emd.extract_metadata,
        inputs=input_image, 
        outputs=[positive, negative, model]
    )


groot.launch(inbrowser=True, server_port=6006)