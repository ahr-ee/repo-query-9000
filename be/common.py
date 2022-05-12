MAX_EL = 5

def parse_curl(curl_blob):
    el_count = 0
    repo_list = []
    for el in curl_blob:
        if el_count >= MAX_EL:
            break

        if (("name" not in el) | ("html_url" not in el) | ("description" not in el) | ("language" not in el)):
            continue

        name = el["name"]
        html_url = el["html_url"]
        description = el["description"]
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
