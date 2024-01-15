"""
* @Description: Sequencer for Telegram bot
* @Author: ArabianCoconut
* @Version: Alpha build
"""
import requests
from Bio.Align import PairwiseAligner

# ! Might Reuse this code in the future
# def load_json(json_stream):
#     """
#     * This function loads the json stream and returns the results
#     * @param {string} json_stream
#     * @return {string} load_dump
#     """
#     j_load: object = json.loads(json_stream)
#     sequence_alignment(j_load['Target'], j_load['Query'], j_load['Mode'])
#     qr_code(j_load['Url'])
#     return 0


def sequence_alignment(target: str, query: str, mode: str):
    """
    * This function performs the sequence alignment
    * @param {string} target, the target sequence
    * @param {string} query, the query sequence
    * @param {string} mode, the mode of alignment (global,local)
    """
    alignments: object = PairwiseAligner()
    alignments.mode = mode.lower()
    alignments = alignments.align(target, query)
    results: list = []
    try:
        with open('./Modules/alignment.txt', 'w') as file:
            for alignment in alignments:
                results.append(alignment)
                file.write(str(alignment))
    except(FileNotFoundError):
        with open("./Modules/alignment.txt","x+") as file:
            for alignment in alignments:
                results.append(alignment)
                file.write(str(alignment))



# noinspection SpellCheckingInspection
def qr_code(qr):
    """
    * This function generates the QR code from Google chart API
    * @param {string} hostname, the hostname of the server
    * @param {string} port, the port of the server
    """
    text: str = qr + "api/results"
    url = "https://chart.googleapis.com/chart?cht=qr&cht=qr&chs=200x200&chl="
    encoding = "&choe=" + "UTF-8"
    req = requests.get(url + text + encoding, timeout=120)
    with open('static/qr.png', 'wb+') as file:
        file.write(req.content)
    return 0
