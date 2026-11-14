import re


def convert_curl_to_requests(curl_command):
    """
    解析 cURL 命令，返回 (url, headers, cookies, data)。
    data 是字符串（原样），没解析到就是 None。
    """
    head_data = {}
    cookies_data = {}
    data = None
    url = ''

    lines = curl_command.split(" \\")
    for index, line in enumerate(lines):
        if index == 0:
            url_match = re.search(r"curl\s+(?:.*url\s+)?['\"]([^'\"]+)['\"]", line)
            if url_match:
                url = url_match.group(1)
                continue

        try:
            line = line.strip()
            head_match = re.search(r"-H\s+['\"]([^:]+):\s*(.+)['\"]", line)
            head_data[head_match.group(1)] = head_match.group(2).strip()
        except AttributeError:
            line = line.strip()

            data_match = re.search(
                r"(?:--data-raw|--data-binary|--data-urlencode|--data|-d)\s+['\"](.*)['\"]$",
                line
            )
            if data_match:
                data = data_match.group(1)
                continue

            line = re.sub(r"^(?:-b|--cookie)\s+['\"]?", "", line)
            line = re.sub(r"['\"]$", "", line)

            pairs = re.findall(r"([^=;]+)=([^;]*)", line)
            for key, value in pairs:
                cookies_data[key.strip()] = value.strip()

    return url, head_data, cookies_data, data


# data = r"""curl --url 'https://api.bilibili.com/x/player/wbi/v2?aid=117086529592045&cid=40865303126&isGaiaAvoided=false&web_location=1315873&dm_img_list=\[\]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEludGVsLCBJbnRlbChSKSBVSEQgR3JhcGhpY3MgNjIwICgweDAwMDAzRUEwKSBEaXJlY3QzRDExIHZzXzVfMCBwc181XzAsIEQzRDExKUdvb2dsZSBJbmMuIChJbnRlbC&dm_img_inter=%7B%22ds%22:\[\],%22wh%22:\[2601,2002,1\],%22of%22:\[104,208,104\]%7D&w_rid=59437c9e6a7754a427d60509496140c9&wts=1788864602' \
#   -H 'accept: application/json, text/plain, */*' \
#   -H 'accept-language: zh-CN,zh;q=0.9' \
#   -H 'cache-control: no-cache' \
#   -b $'buvid4=EB51C7BE-5925-8FA6-0D43-F74F2E15C9A310482-023110616-evGPtmzq9mSNTZ70TOXQhCcxgIdeMrG7tCP3v81mfMbq8VqU5UusSA%3D%3D; enable_web_push=DISABLE; theme-tip-show=SHOWED; LIVE_BUVID=AUTO5317552635048299; _uuid=73F879F9-177D-F5104-108E10-495CC10A6934536956infoc; PVID=1; rpdid=|(kRRm|)k)Y0J\'u~Y)YllY~Y; buvid3=F2940984-A77A-732C-05FB-A8CBF5BA2C2622827infoc; b_nut=1770560222; DedeUserID=700392021; DedeUserID__ckMd5=849b7eb029c4598a; hit-dyn-v2=1; buvid_fp=93e78109208f40d386e460743f53f853; theme-avatar-tip-show=SHOWED; theme-switch-show=SHOWED; CURRENT_QUALITY=80; bp_t_offset_700392021=1244430442887643136; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODg4NzQ2MDgsImlhdCI6MTc4ODYxNTM0OCwicGx0IjotMX0.delXFI89gClqVyNXPZ0_OLWpRhxN7_UphjpFl5Yy7HE; bili_ticket_expires=1788874548; home_feed_column=4; browser_resolution=1396-639; SESSDATA=d999c94a%2C1804344918%2C71947%2A91CjARBaxn4KvBNCNp5fRboCatnyYcNZUD25fBDJIJlNbzMVxWM4XHZGa2EQ1DOIykx94SVkFOYmNOZmJsVGR5S2FvcUw1NGdZdnZ5QXh3Wm9uMlUycjl1c1lpY3pyQUhhZkk0NEhFTnVSUUNUdWpzbHItdU5tcjFtOGxNMjJ1MV8yNm5BS1NzclF3IIEC; bili_jct=19b41cec5146b1c9e9dd4ce7af22671c; sid=4z852r3i; CURRENT_FNVAL=4048; b_lsid=7F3149ED_1A080A39B68' \
#   -H 'origin: https://www.bilibili.com' \
#   -H 'pragma: no-cache' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.bilibili.com/video/BV1nRgn6pENP/?spm_id_from=333.1007.tianma.4-2-12.click&vd_source=eb4ed3971abb744ff0bdcd35f56cae2c' \
#   -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36'"""

# print(convert_curl_to_requests(data))