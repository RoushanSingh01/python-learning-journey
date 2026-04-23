def main():
    file_name = input("File name: ").strip().lower()

    mappings = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Default type
    media_type = "application/octet-stream"

    # Check for matches
    for ext in mappings:
        if file_name.endswith(ext):
            media_type = mappings[ext]
            break
    
    print(media_type)

main()
