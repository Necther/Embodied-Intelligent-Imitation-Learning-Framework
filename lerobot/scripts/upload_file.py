from huggingface_hub import HfApi

api = HfApi()

# Upload all the content from the local folder to your remote Space.
# By default, files are uploaded at the root of the repo

api.upload_folder(

    folder_path="/home/xsj/code/lerobot/data/local_user/koch_test_t",

    repo_id="xsj/koch1",

    repo_type="space",

)