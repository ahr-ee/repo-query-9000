MAX_EL = 5

def parse_curl(curl_blob):
    el_count = 0
    repo_list = []
    for el in curl_blob:
        if el_count >= MAX_EL:
            break

        name = None
        html_url = None
        description = None
        language = None

        if "name" in el:
            name = el["name"]
        if "html_url" in el:
            html_url = el["html_url"]
        if "description" in el:
            description = el["description"]
        if "language" in el:
            language = el["language"]


        repo_list.append({
                "name": name,
                "html_url": html_url,
                "description": description,
                "language": language,
            }
        )
        el_count += 1
    return repo_list
