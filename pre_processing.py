from utils.video_utils import stabilize_video
from utils.io_utils import extract_metadata

def process_media(media_file):
    """
    Process the incoming media: stabilize video, check metadata.
    """
    # Step 1: Extract metadata
    metadata = extract_metadata(media_file)
    
    # Step 2: Stabilize video for clear feature extraction
    stabilized_video = stabilize_video(media_file)

    # Step 3: Return processed media along with metadata
    return {"video": stabilized_video, "metadata": metadata}
