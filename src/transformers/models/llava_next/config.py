class Global_Config:
    output_path = ""
    image_folder = ""
    filename = ""
    bbox = []
    obj_id = -1
    image_height = -1
    image_width = -1
    generated_token = -1
    attention_manipulation = False
    selected_patches_for_base = []
    selected_patches_for_hd = []
    high_resolution_image_feature_height = 0
    high_resolution_image_feature_width = 0
    text_to_over_write = None

PER_OBJECT_CONFIG = Global_Config()