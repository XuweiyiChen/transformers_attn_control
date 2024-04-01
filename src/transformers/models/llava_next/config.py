class Global_Config:
    output_path = ""
    image_folder = ""
    filename = ""
    bbox = []  # now this is a list of bboxs
    obj_id = -1
    image_height = -1
    image_width = -1
    generated_token = -1
    attention_manipulation = False
    attention_manipulation_version = 1
    attention_manipulation_scale = 5
    selected_patches_for_base_list = []
    selected_patches_for_hd_list = []
    high_resolution_image_feature_height = 0
    high_resolution_image_feature_width = 0
    text_to_over_write = None
    base_image_offset = -1
    system_prompt_offset = -1
    is_seven_billion = True
    scale_down_factor = 0.75
    scale_up_factor = 1.35
    is_write = True
    text_preprocess = None


PER_OBJECT_CONFIG = Global_Config()
