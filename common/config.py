
"""
This is the folder configuration file. Extend this according to your need
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
                "xz"
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
                "jpeg",
                "svg",
                "gif"
            ],
            "subfolders": {
                "pictures": {
                    "extension_list": ["png", "jpg", "jpeg", "svg", "gif"],
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
                "pkg",
                "exe"
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
            "subfolders": {
                "keys": {
                    "extension_list": ["pem", "pub"],
                    "subfolders": {}
                },
                "xml": {
                    "extension_list": ["json", "xml"],
                    "subfolders": {}
                },
                "web": {
                    "extension_list": ["js", "html"],
                    "subfolders": {}
                },
                "python": {
                    "extension_list": ["py", "ipynb"],
                    "subfolders": {}
                },
                "shell": {
                    "extension_list": ["sh"],
                    "subfolders": {}
                }
            }
        }
    }
}
