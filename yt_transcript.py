from langchain_community.document_loaders import YoutubeLoader


def get_transcript(video_url, translation_language="en"):
    loader = YoutubeLoader.from_youtube_url(
        video_url,
        add_video_info=True,
        language=["en", "id"],
        translation=translation_language,
    )
    text = loader.load()
    return text
