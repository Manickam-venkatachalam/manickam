from pathlib import Path
from tqdm import tqdm

import requests
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
class ProgressBar(object):
    def upload_file(upload_url, fields, filepath):

        path = Path(filepath)
        total_size = path.stat().st_size
        filename = path.name

        with tqdm(
        desc=filename,
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        ) as bar:
            with open(filepath, "rb") as f:
                fields["file"] = ("filename", f)
                e = MultipartEncoder(fields=fields)
                m = MultipartEncoderMonitor(
                e, lambda monitor: bar.update(monitor.bytes_read - bar.n)
                )
                headers = {"Content-Type": m.content_type}
                requests.post(upload_url, data=m, headers=headers)