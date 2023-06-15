import os
from google.colab import auth
from googleapiclient.discovery import build
from apiclient.http import MediaIoBaseDownload
from tqdm.auto import tqdm


import os  
from io import io

auth.authenticate_user()
drive_service = build('drive', 'v3')

model_type = 'mega'
model_path = '/content/grover/models'
model_dir = os.path.join(model_path, model_type)
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

NUMBER = 800000
MODEL = "grover_mega_owt_fix"

local_file_ids = ['1t1B5JfjolytwSSUAGOZCnstVlaL2Bg25', '1kojGap2kXzkJBWtwIZtOXgeV3IWnNMtO', '1FITtxBwJsagKfaLz9tgsguHbbdMCyeQw']
local_filenames = ['.data-00000-of-00001', '.index', '.meta']
for ext, id_ in zip(local_filenames, local_file_ids):
    ext = str(NUMBER) + ext
    filename = '%s/%s/model.ckpt.%s' % (model_path, model_type, ext) 
    
    request = drive_service.files().get_media(fileId=id_)
    with open(filename, 'wb') as f:
      downloader = MediaIoBaseDownload(f, request, chunksize=100*1024*1024)
      done = False
      pbar = tqdm(total=100, desc='%s' % ext)
      progress = 0
      while done is False:
        status, done = downloader.next_chunk()
        new_progress = int(status.progress() * 100)
        pbar.update(new_progress - progress)
        progress = new_progress

      pbar.close()
      print('Downloaded %s' % filename)


    