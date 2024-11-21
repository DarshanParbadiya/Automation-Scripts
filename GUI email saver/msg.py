from pathlib import Path
from extract_msg import openMsg
from compressed_rtf import decompress
from io import BytesIO
from rtfparse.parser import Rtf_Parser
from rtfparse.renderers.html_decapsulator import HTML_Decapsulator

class ConvertMessage():
    def __init__(self,source,dest):
        self.source = source
        self.dest = dest

    def save_to_html(self,source,dest):
        source_file = Path(r"C:\email\2024-05-21\Newsletter.msg")
        target_file = Path(r"C:\email\2024-05-21\target.html")
        source_file = Path(source)
        target_file = Path(dest)
        # Create parent directory of `target_path` if it does not already exist:
        target_file.parent.mkdir(parents=True, exist_ok=True)

        # Get a decompressed RTF bytes buffer from the MS Outlook message
        msg = openMsg(source_file)
        decompressed_rtf = decompress(msg.compressedRtf)
        rtf_buffer = BytesIO(decompressed_rtf)

        # Parse the rtf buffer
        parser = Rtf_Parser(rtf_file=rtf_buffer)
        parsed = parser.parse_file()

        # Decapsulate the HTML from the parsed RTF
        decapsulator = HTML_Decapsulator()
        with open(target_file, mode="w", encoding="utf-8") as html_file:
            decapsulator.render(parsed, html_file)