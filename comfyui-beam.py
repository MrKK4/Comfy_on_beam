from beam import Image, Pod


image = (
    Image(base_image="ubuntu:22.04") #(python_version="python3.11")
    .add_commands(["apt update && apt install -y python3 python3-pip git ffmpeg libgl1-mesa-glx libglib2.0-0 aria2"])
    .add_python_packages(
        [
            "comfy-cli",
            "onnxruntime-gpu",
            "sageattention",
        ]
    )
    .add_commands(
        [
            "comfy --skip-prompt install --nvidia",
            "comfy node install https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git",
            "comfy node install https://github.com/kijai/ComfyUI-WanVideoWrapper",
            "comfy node install https://github.com/kijai/ComfyUI-KJNodes.git",
            "comfy node install https://github.com/kijai/ComfyUI-MelBandRoFormer",
            "comfy node install https://github.com/rgthree/rgthree-comfy.git",
            "comfy node install https://github.com/Fannovel16/comfyui_controlnet_aux",
            "comfy node install https://github.com/kijai/ComfyUI-segment-anything-2",
            "comfy node install https://github.com/talesofai/comfyui-browser.git",
            # "comfy node install https://github.com/hayden-fr/ComfyUI-Model-Manager.git",
            "mkdir -p /root/comfy/ComfyUI/models/unet/",
            "mkdir -p /root/comfy/ComfyUI/models/vae/",
            "mkdir -p /root/comfy/ComfyUI/models/clip/",
            "mkdir -p /root/comfy/ComfyUI/models/clip_vision/",
            "mkdir -p /root/comfy/ComfyUI/models/text_encoders/",
            "mkdir -p /root/comfy/ComfyUI/models/loras/",
        ]
    )
    .add_commands([
         '''
        aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/vae -o wan_2.1_vae.safetensors "https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true"

        aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/text_encoders -o umt5_xxl_fp8_e4m3fn_scaled.safetensors "https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors"

        aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/clip_vision -o clip_vision_h.safetensors "https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors?download=true"

        aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/loras -o lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors "https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors"

        aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/loras -o WanAnimate_relight_lora_fp16.safetensors "https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/LoRAs/Wan22_relight/WanAnimate_relight_lora_fp16.safetensors"

        aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/loras -o wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors"

        aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/loras -o wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors"

        aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/loras -o wan2.2_t2v_lightx2v_4steps_lora_v1_low_noise.safetensors "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_t2v_lightx2v_4steps_lora_v1.1_low_noise.safetensors?download=true"

        aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/loras -o wan2.2_t2v_lightx2v_4steps_lora_v1_high_noise.safetensors "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors?download=true"
        
        #=================================models for wan2.2==========================================
        #keep in mind beam doesn't have the ability to save too much files like modal so first download any model one at a time you prefer like only t2v models or i2v or only animate models I prefer downloading the animate model as the other two can be downloaded from the manager. 
        # aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/unet -o wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors?download=true"

        # aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/unet -o wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors?download=true"

        # aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/unet -o wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors?download=true"

        # aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/unet -o wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors?download=true"

        aria2c --console-log-level=error -c -x 16 -s 16 -k 1M -d /root/comfy/ComfyUI/models/unet -o Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors "https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/resolve/main/Wan22Animate/Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors"

        
        
        
        echo "✅ All downloads completed successfully!"
        '''
    ])

        
)

comfyui_server = Pod(
    name="my-comfyui-server",
    image=image,
    ports=[8000],
    cpu=8,
    memory="16Gi",
    gpu="RTX4090",
    entrypoint=["comfy", "launch", "--", "--listen", "0.0.0.0", "--port", "8000"]
  #after the url to comfyui shows up go to beam cloud and check logs on the app page as it takes some time to start the image
    # entrypoint=["sh", "-c", "comfy", "launch", "--", "--listen", "0.0.0.0", "--port", "8000"],
)

res = comfyui_server.create()
print("✨ ComfyUI hosted at:", res.url)
