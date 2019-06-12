
"""
Write something here
"""
configurations = {
    "root": {
        "documents": {
            "extension_list": [
                "pdf",
                "doc",
                "docx",
                "csv",
                "key",
                "xlsx",
                "zip",
                "tar",
                "tgz",
                "gz",
                "txt",
                "numbers"
            ],
            "subfolders": {
                "docs": {
                    "extension_list": ["pdf", "doc", "docx", "key", "txt"],
                    "subfolders": {
                        "pdfs": {
                            "extension_list": ["pdf"],
                            "subfolders": {}
                        },
                        "microsoft docs": {
                            "extension_list": ["doc", "docx"],
                            "subfolders": {}
                        },
                        "apple keynotes": {
                            "extension_list": ["key"],
                            "subfolders": {}
                        },
                        "text": {
                            "extension_list": ["txt"],
                            "subfolders": {}
                        }
                    }
                },
                "sheets": {
                    "extension_list": ["csv", "xlsx", "numbers"],
                    "subfolders": {
                        "excel sheets": {
                            "extension_list": ["xlsx", "numbers"],
                            "subfolders": {}
                        },
                        "csv sheets": {
                            "extension_list": ["csv"],
                            "subfolders": {}
                        }
                    }
                },
                "compressed": {
                    "extension_list": ["zip", "tar", "tgz", "gz", "tar"],
                    "subfolders": {}
                }
            }
        },
        "media": {
            "extension_list": [
                "mp3",
                "mp4",
                "wav",
                "mov",
                "png",
                "jpg",
                "jpeg"
            ],
            "subfolders": {
                "pictures": {
                    "extension_list": ["png", "jpg", "jpeg"],
                    "subfolders": {}
                },
                "video": {
                    "extension_list": ["mp4", "mov"],
                    "subfolders": {}
                },
                "music": {
                    "extension_list": ["mp3", "wav"],
                    "subfolders": {}
                }
            }
        },
        "software": {
            "extension_list": [
                "dmg",
                "pkg"
            ],
            "subfolders": {}
        },
        "code": {
            "extension_list": [
                "sh",
                "ipynb",
                "pem",
                "json",
                "py",
                "js",
                "html",
                "pub"
            ],
            "subfolders": {}
        }
    }
}
