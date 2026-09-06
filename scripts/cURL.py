import re


def convert_curl_to_requests(curl_command):
    """
    Converts a cURL command to a Python requests code snippet.
    
    Args:
        curl_command (str): The cURL command to convert.
        
    Returns:
        str: The equivalent Python requests code snippet.
    """
    lines = curl_command.split("\\")
    # print(lines[1].split(":")[0].split("-H")[1])
    
    
    return f"import requests\n\nresponse = requests.get('https://example.com')\nprint(response.text)"

test = r"""curl --url 'https://www.bilibili.com/' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'cache-control: no-cache' \
  -b $'buvid4=EB51C7BE-5925-8FA6-0D43-F74F2E15C9A310482-023110616-evGPtmzq9mSNTZ70TOXQhCcxgIdeMrG7tCP3v81mfMbq8VqU5UusSA%3D%3D; enable_web_push=DISABLE; theme-tip-show=SHOWED; LIVE_BUVID=AUTO5317552635048299; _uuid=73F879F9-177D-F5104-108E10-495CC10A6934536956infoc; PVID=1; rpdid=|(kRRm|)k)Y0J\'u~Y)YllY~Y; buvid3=F2940984-A77A-732C-05FB-A8CBF5BA2C2622827infoc; b_nut=1770560222; DedeUserID=700392021; DedeUserID__ckMd5=849b7eb029c4598a; hit-dyn-v2=1; buvid_fp=93e78109208f40d386e460743f53f853; theme-avatar-tip-show=SHOWED; theme-switch-show=SHOWED; CURRENT_QUALITY=80; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; bmg_af_sc={"none":{"on":1,"def":"i2.hdslb.com"},"sgp":{"on":1,"def":"i2-sgp.hdslb.com"}}; SESSDATA=7846a56a%2C1803913505%2C0a086%2A91CjAYWxgrjZdf0S2W8xdoX3IjBp9amFL2kcND0QU82d9z1dOs6SK_xm5ZIF6Dji66woMSVnN5M1MxdXZKZWh4TVlzT3NFZHVWb2huVnNvVk16TGd2dnVJM3FTd0RVTHY4NXhfNWgzLVliOVhMdFJvbWRoMnRoQUhFWWZfdlhQVkVvUC1zenlYaFlBIIEC; bili_jct=a167f42c5f86b45e72961ce8d8d58c7d; sid=4w0azj0r; bp_t_offset_700392021=1244430442887643136; home_feed_column=4; CURRENT_FNVAL=4048; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3ODg4NzQ2MDgsImlhdCI6MTc4ODYxNTM0OCwicGx0IjotMX0.delXFI89gClqVyNXPZ0_OLWpRhxN7_UphjpFl5Yy7HE; bili_ticket_expires=1788874548; browser_resolution=660-639; b_lsid=E214058B_1A071CF9B33' \
  -H 'pragma: no-cache' \
  -H 'priority: u=0, i' \
  -H 'sec-ch-ua: "Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36'"""

print(convert_curl_to_requests(test))


