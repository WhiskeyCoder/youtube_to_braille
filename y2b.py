import googleapiclient.discovery
import googleapiclient.errors
from youtube_transcript_api import YouTubeTranscriptApi
import os, sys
import win32print


API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # Replace with your own API key
channel_urls = ['https://www.youtube.com/c/UC16niRr50-MSBwiO3YDb3RA', # Add your Channel ID's Here
                'https://www.youtube.com/c/UCupvZG-5ko_eiXAupbDfxWw',
                ]


def get_transcript(url):
    video_id = url
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        print(f"Failed to retrieve transcript: {str(e)}")


def get_newest_video_info(channel_url):
    channel_id = channel_url.split('/')[-1]
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)
    try:
        channel_info = youtube.channels().list(part='contentDetails,snippet', id=channel_id).execute()
        if 'items' in channel_info and channel_info['items']:
            uploads_playlist_id = channel_info['items'][0]['contentDetails']['relatedPlaylists']['uploads']
            channel_name = channel_info['items'][0]['snippet']['title']
        else:
            print(f"No channel info found for {channel_url}")
            return None

        playlist_items = youtube.playlistItems().list(
            part='snippet',
            playlistId=uploads_playlist_id,
            maxResults=1
        ).execute()
        if 'items' in playlist_items and playlist_items['items']:
            latest_video = playlist_items['items'][0]
            video_id = latest_video['snippet']['resourceId']['videoId']
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            video_title = latest_video['snippet']['title']
            return channel_name, video_title, video_id
        else:
            print(f"No videos found for {channel_url}")
    except googleapiclient.errors.HttpError as e:
        print(f"Error fetching data for {channel_url}: {str(e)}")
    return None


def text_to_braille(text):
    asciicodes = [' ', '!', '"', '#', '$', '%', '&', '', '(', ')', '*', '+', ',', '-', '.', '/',
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '[', '\\', ']', '^', '_']

    brailles = ['⠀', '⠮', '⠐', '⠼', '⠫', '⠩', '⠯', '⠄', '⠷', '⠾', '⠡', '⠬', '⠠', '⠤', '⠨', '⠌', '⠴', '⠂', '⠆', '⠒', '⠲',
                '⠢',
                '⠖', '⠶', '⠦', '⠔', '⠱', '⠰', '⠣', '⠿', '⠜', '⠹', '⠈', '⠁', '⠃', '⠉', '⠙', '⠑', '⠋', '⠛', '⠓', '⠊', '⠚',
                '⠅',
                '⠇', '⠍', '⠝', '⠕', '⠏', '⠟', '⠗', '⠎', '⠞', '⠥', '⠧', '⠺', '⠭', '⠽', '⠵', '⠪', '⠳', '⠻', '⠘', '⠸']
    braille_text = ''
    for char in text.lower():
        if char in asciicodes:
            braille_text += brailles[asciicodes.index(char)]
        else:
            braille_text += char
    return braille_text


for channel_url in channel_urls:
    video_info = get_newest_video_info(channel_url)
    if video_info:
        channel_name, video_title, video_id = video_info
        video_transcript = get_transcript(video_id)
        header_string = (f'Channel Name: {channel_name} - Video Title: {video_title}')
        braille_header_result = text_to_braille(header_string)
        braille_video_result = text_to_braille(video_transcript)
        to_embosser = [braille_header_result, braille_video_result]
        #p = win32print.OpenPrinter('local_embosser_name') #will need to be updated with Embosser Name and Deatils
        #job = win32print.StartDocPrinter(p, 1, ("Embossing Data", None, "RAW"))
        #win32print.StartPagePrinter(p)
        #win32print.WritePrinter(p, f"{to_embosser}")
        #win32print.EndPagePrinter(p)
        print(f'{channel_name}Header: {braille_header_result}')
        print(f'Video: {braille_video_result}')

