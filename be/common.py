MAX_EL = 5

def parse_curl(curl_blob):
    el_count = 0
    repo_list = []
    for el in curl_blob:
        if el_count >= MAX_EL:
            break
        repo_list.append({
                "name": el["name"],
                "html_url": el["html_url"],
                "description": el["description"],
                "language": el["language"],
            }
        )
        el_count += 1
    return repo_list
