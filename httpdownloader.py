import requests
import os
from tqdm import tqdm  

def download_file(url, dest_directory=None):
    try:
        
        file_name = os.path.basename(url)
        
       
        if dest_directory is None:
            dest_directory = os.getcwd()  # Use the current working directory if not specified
        save_path = os.path.join(dest_directory, file_name)

        
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for any errors in the response

        
        file_size = int(response.headers.get('content-length', 0))

        
        with open(save_path, 'wb') as file, tqdm(
            desc=file_name,
            total=file_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as progress_bar:
            for data in response.iter_content(chunk_size=1024):
                file.write(data)
                progress_bar.update(len(data))

        print(f"File downloaded successfully to {save_path}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_url = "https://example.com/yourfile.zip"  
    download_directory = "."  
  
    download_file(file_url, download_directory)
