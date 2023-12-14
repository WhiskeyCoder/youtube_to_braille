# YouTube Transcript to Braille Converter

## Overview

This Python script is designed to make YouTube content accessible to individuals with visual and hearing impairments by converting video transcripts into Braille. It allows users to input a list of YouTube channels, retrieve the latest video transcripts, and convert them into Braille format. The Braille text can then be sent to a Braille embosser for printing.

## Motivation

This tool was developed with a heartfelt intention. I have a close connection with someone facing the challenge of potential vision loss and hearing deterioration. This person enjoys watching YouTube content regularly, including podcasts and videos. The tool was created to ensure that, if the need arises, the script can be scheduled to run daily. It will generate Braille transcripts of the latest videos from their favorite channels. This way, they can continue to enjoy YouTube content without straining themselves.

## How It Works

The script utilizes the YouTube Data API and the YouTube Transcript API to accomplish its tasks. It performs the following steps:

1. **Retrieve Channel Information**: The script takes a list of YouTube channel URLs as input.

2. **Find Latest Video**: For each channel URL, it identifies the latest video uploaded to the channel.

3. **Retrieve Video Transcript**: It fetches the transcript of the latest video using the YouTube Transcript API.

4. **Convert Transcript to Braille**: The script converts the video transcript into Braille format. It uses a mapping of ASCII characters to Braille symbols for this purpose.

5. **Send to Braille Embosser**: While the code for sending the Braille text to a Braille embosser is provided in the script, it's currently commented out. You will need to configure your specific embosser details and uncomment the relevant code.

6. **Display and Print**: The Braille-translated text is displayed in the console, making it accessible to users. For printing, the script uses the Win32Print library to send the Braille text to the embosser.

## Prerequisites

To use this script, you will need:

- A Google API Key: Replace `"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"` with your own API key in the script.
- Python 3.x installed on your system.
- The required Python libraries installed. You can install them using `pip`:

  shell
  ```pip install google-api-python-client youtube-transcript-api pywin32```

  ## Usage
  1. Clone the Repo ```git clone https://github.com/yourusername/YouTubeTranscriptToBraille.git
cd YouTubeTranscriptToBraille```
  2. Edit the channel_urls list in the script, adding the YouTube channel URLs you want to monitor.
  3. Replace "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" with your own Google API Key.
  4. Configure your Braille embosser settings in the script, uncommenting the relevant code as needed.
  5. Run the script: ```python your_script_name.py```
  6. The script will display the Braille-translated text in the console and, if configured, send it to the Braille embosser for printing.
 
## Sample Output
There might be a few issues with translations from Braille to English, but so far seems to be working ok

Header: ⠉⠓⠁⠝⠝⠑⠇⠀⠝⠁⠍⠑⠱⠀⠃⠃⠉⠀⠝⠑⠺⠎⠀⠤⠀⠧⠊⠙⠑⠕⠀⠞⠊⠞⠇⠑⠱⠀⠃⠗⠊⠞⠊⠎⠓⠀⠞⠑⠑⠝⠁⠛⠑⠀⠎⠊⠎⠞⠑⠗⠎⠀⠍⠊⠎⠎⠊⠝⠛⠀⠁⠋⠞⠑⠗⠀⠓⠁⠍⠁⠎⠀⠁⠞⠞⠁⠉⠅⠎⠀⠤⠀⠃⠃⠉⠀⠝⠑⠺⠎

Header: channel name: bbc news - video title: british teenage sisters missing after hamas attacks - bbc news

Video:⠺⠑⠇⠇⠀⠁⠞⠀⠇⠑⠁⠎⠞⠀⠂⠠⠲⠴⠴⠀⠏⠑⠕⠏⠇⠑⠀⠺⠑⠗⠑⠀⠅⠊⠇⠇⠑⠙⠀⠊⠝⠀⠇⠁⠎⠞⠀⠺⠑⠑⠅'⠎⠀⠁⠞⠞⠁⠉⠅⠀⠃⠽⠀⠓⠁⠍⠁⠎⠀⠊⠝⠀⠎⠕⠥⠞⠓⠑⠗⠝⠀⠊⠎⠗⠁⠑⠇⠀⠁⠝⠙⠀⠁⠎⠀⠺⠑'⠧⠑⠀⠃⠑⠑⠝⠀⠓⠑⠁⠗⠊⠝⠛⠀⠎⠊⠭⠀⠺⠑⠗⠑⠀⠃⠗⠊⠞⠊⠎⠓⠀⠁⠍⠕⠝⠛⠀⠞⠓⠑⠀⠍⠊⠎⠎⠊⠝⠛⠀⠁⠗⠑⠀⠞⠺⠕⠀⠃⠗⠊⠞⠊⠎⠓⠀⠞⠑⠑⠝⠁⠛⠑⠀⠎⠊⠎⠞⠑⠗⠎⠀⠁⠎⠀⠇⠥⠉⠽⠀⠍⠁⠝⠝⠊⠝⠛⠀⠗⠑⠏⠕⠗⠞⠎⠀⠝⠕⠽⠁⠀⠂⠖⠀⠕⠝⠀⠞⠓⠑⠀⠇⠑⠋⠞⠀⠽⠑⠇⠀⠂⠒⠀⠕⠝⠀⠞⠓⠑⠀⠗⠊⠛⠓⠞⠀⠝⠕⠺⠀⠍⠊⠎⠎⠊⠝⠛⠀⠁⠋⠞⠑⠗⠀⠞⠓⠑⠀⠓⠁⠍⠁⠎⠀⠁⠞⠞⠁⠉⠅⠀⠕⠝⠀⠊⠎⠗⠁⠑⠇⠀⠊⠝⠀⠃⠑⠞⠺⠑⠑⠝⠀⠞⠓⠑⠍⠀⠞⠓⠑⠊⠗⠀⠍⠕⠍⠀⠇⠑⠁⠝⠀⠍⠥⠗⠙⠑⠗⠑⠙⠀⠃⠽⠀⠓⠁⠍⠁⠎⠀⠁⠇⠇⠀⠁⠗⠑⠀⠃⠗⠊⠞⠊⠎⠓⠀⠇⠑⠁⠝⠝⠑'⠎⠀⠋⠁⠍⠊⠇⠽⠀⠎⠁⠊⠙⠀⠎⠓⠑⠀⠇⠑⠙⠀⠁⠀⠃⠑⠁⠥⠞⠊⠋⠥⠇⠀⠇⠊⠋⠑⠀⠁⠝⠙⠀⠑⠝⠗⠊⠉⠓⠑⠙⠀⠞⠓⠑⠀⠇⠊⠧⠑⠎⠀⠕⠋⠀⠁⠇⠇⠀⠞⠓⠕⠎⠑⠀⠇⠥⠉⠅⠽⠀⠑⠝⠕⠥⠛⠓⠀⠞⠕⠀⠓⠁⠧⠑⠀⠅⠝⠕⠺⠝⠀⠁⠝⠙⠀⠇⠕⠧⠑⠙⠀⠓⠑⠗⠀⠎⠓⠑⠀⠺⠁⠎⠀⠁⠀⠃⠑⠇⠕⠧⠑⠙⠀⠙⠁⠥⠛⠓⠞⠑⠗⠀⠎⠊⠎⠞⠑⠗⠀⠍⠕⠞⠓⠑⠗⠀⠁⠝⠙⠀⠁⠥⠝⠞⠀⠞⠓⠑⠀⠛⠊⠗⠇'⠎⠀⠙⠁⠙⠀⠑⠇⠇⠊⠑⠀⠊⠎⠀⠁⠇⠎⠕⠀⠍⠊⠎⠎⠊⠝⠛⠀⠞⠓⠊⠎⠀⠊⠎⠀⠺⠓⠁⠞⠀⠓⠁⠏⠏⠑⠝⠑⠙⠀⠞⠕⠀⠁⠝⠀⠑⠝⠞⠊⠗⠑⠀⠋⠁⠍⠊⠇⠽⠀⠊⠝⠀⠊⠎⠗⠁⠑⠇⠀⠞⠓⠑⠽⠀⠇⠊⠧⠑⠙⠀⠕⠝⠀⠅⠊⠃⠕⠞⠀⠃⠑⠑⠗⠊⠀⠺⠓⠑⠗⠑⠀⠞⠓⠑⠀⠍⠥⠗⠙⠑⠗⠕⠥⠎⠀⠛⠥⠝⠍⠁⠝⠀⠎⠇⠁⠥⠛⠓⠞⠑⠗⠑⠙⠀⠎⠕⠀⠍⠁⠝⠽⠀⠝⠕⠁⠀⠊⠎⠀⠂⠖⠀⠽⠑⠁⠗⠎⠀⠕⠇⠙⠀⠎⠓⠑⠀⠺⠁⠎⠀⠓⠁⠏⠏⠊⠝⠑⠎⠎⠀⠁⠝⠙⠀⠎⠓⠑⠀⠇⠊⠅⠑⠀⠞⠕⠀⠓⠑⠗⠀⠓⠕⠃⠃⠊⠑⠎⠀⠞⠕⠀⠇⠊⠅⠑⠀⠎⠓⠑⠀⠇⠊⠅⠑⠎⠀⠞⠕⠀⠉⠕⠕⠅⠀⠽⠑⠁⠓⠀⠎⠓⠑⠀⠺⠁⠎⠀⠁⠀⠋⠥⠝⠝⠽⠀⠛⠊⠗⠇⠀⠎⠓⠑⠀⠺⠁⠎⠀⠁⠇⠇⠀⠁⠇⠇⠀⠞⠓⠑⠀⠞⠊⠍⠑⠀⠎⠓⠑⠀⠇⠊⠅⠑⠀⠞⠕⠀⠓⠑⠁⠗⠀⠍⠥⠎⠊⠉⠀⠁⠝⠙⠀⠎⠊⠝⠛⠊⠝⠛⠀⠋⠕⠗⠀⠥⠎⠀⠙⠁⠝⠉⠊⠝⠛⠀⠝⠁⠞⠁⠝⠑⠇⠀⠽⠕⠥⠝⠛⠀⠁⠇⠎⠕⠀⠃⠗⠊⠞⠊⠎⠓⠀⠁⠇⠎⠕⠀⠍⠥⠗⠙⠑⠗⠑⠙⠀⠃⠽⠀⠓⠁⠍⠁⠎⠀⠓⠊⠎⠀⠃⠗⠕⠞⠓⠑⠗⠀⠑⠇⠇⠊⠕⠞⠀⠗⠑⠍⠑⠍⠃⠑⠗⠎⠀⠁⠀⠆⠴⠤⠽⠑⠁⠗⠤⠕⠇⠙⠀⠺⠓⠕⠀⠺⠁⠎⠀⠁⠀⠇⠕⠝⠙⠕⠝⠑⠗⠀⠁⠀⠍⠥⠎⠊⠉⠀⠇⠕⠧⠑⠗⠀⠁⠀⠏⠗⠕⠥⠙⠀⠚⠑⠺⠀⠝⠁⠞⠁⠝⠑⠇⠀⠥⠓⠀⠽⠕⠥⠀⠅⠝⠕⠺⠀⠓⠑⠀⠚⠥⠎⠞⠀⠇⠕⠧⠑⠙⠀⠇⠊⠋⠑⠀⠓⠑⠀⠥⠍⠀⠓⠁⠙⠀⠁⠀⠇⠕⠞⠀⠕⠋⠀⠗⠑⠎⠏⠑⠉⠞⠀⠋⠕⠗⠀⠍⠽⠀⠥⠓⠀⠏⠁⠗⠑⠝⠞⠎⠀⠓⠑⠀⠥⠓⠀⠺⠁⠝⠞⠑⠙⠀⠞⠕⠀⠥⠍⠀⠅⠑⠑⠏⠀⠓⠊⠎⠀⠏⠑⠕⠏⠇⠑⠀⠎⠁⠋⠑⠀⠁⠝⠙⠀⠙⠑⠋⠑⠝⠙⠀⠞⠓⠊⠎⠀⠉⠕⠥⠝⠞⠗⠽⠀⠺⠑'⠗⠑⠀⠁⠇⠇⠀⠚⠥⠎⠞⠀⠃⠗⠕⠅⠑⠝⠀⠊⠞'⠎⠀⠺⠑'⠗⠑⠀⠎⠞⠊⠇⠇⠀⠉⠕⠍⠊⠝⠛⠀⠞⠕⠀⠞⠑⠗⠍⠎⠀⠺⠊⠞⠓⠀⠞⠓⠑⠀⠝⠑⠺⠎⠀⠺⠓⠁⠞⠀⠺⠊⠇⠇⠀⠽⠕⠥⠀⠍⠊⠎⠎⠀⠁⠃⠕⠥⠞⠀⠝⠁⠞⠁⠝⠑⠇⠀⠞⠓⠑⠀⠇⠁⠎⠞⠀⠞⠊⠍⠑⠀⠊⠀⠎⠁⠺⠀⠓⠊⠍⠀⠺⠁⠎⠀⠥⠓⠀⠑⠭⠁⠉⠞⠇⠽⠀⠁⠀⠺⠑⠑⠅⠀⠃⠑⠋⠕⠗⠑⠀⠓⠑⠀⠺⠁⠎⠀⠅⠊⠇⠇⠑⠙⠀⠃⠽⠀⠞⠓⠑⠀⠓⠁⠍⠁⠎⠀⠞⠑⠗⠗⠕⠗⠊⠎⠞⠀⠥⠍⠀⠁⠝⠙⠀⠊⠀⠞⠓⠊⠝⠅⠀⠊⠋⠀⠊⠀⠇⠕⠕⠅⠀⠃⠁⠉⠅⠀⠁⠞⠀⠞⠓⠁⠞⠀⠙⠁⠽⠀⠊⠞'⠎⠀⠓⠊⠎⠀⠥⠍⠀⠊⠝⠋⠑⠉⠞⠊⠕⠥⠎⠀⠎⠍⠊⠇⠑⠀⠁⠞⠀⠞⠓⠑⠀⠋⠥⠝⠑⠗⠁⠇⠀⠕⠝⠀⠍⠕⠝⠙⠁⠽⠀⠞⠓⠑⠀⠍⠕⠗⠝⠊⠝⠛⠀⠊⠝⠞⠑⠗⠗⠥⠏⠞⠑⠙⠀⠁⠊⠗⠀⠗⠁⠊⠙⠀⠎⠊⠗⠑⠝⠎⠀⠏⠊⠑⠗⠉⠑⠙⠀⠞⠓⠑⠀⠛⠗⠊⠑⠧⠊⠝⠛⠀⠁⠎⠀⠍⠕⠥⠗⠝⠑⠗⠎⠀⠺⠑⠗⠑⠀⠋⠕⠗⠉⠑⠙⠀⠕⠝⠞⠕⠀⠞⠓⠑⠀⠉⠑⠍⠑⠞⠑⠗⠽⠀⠛⠗⠕⠥⠝⠙⠀⠞⠕⠀⠎⠓⠊⠑⠇⠙⠀⠋⠗⠕⠍⠀⠊⠝⠉⠕⠍⠊⠝⠛⠀⠓⠁⠍⠁⠎⠀⠍⠊⠎⠎⠊⠇⠑⠎⠀⠊⠞⠀⠺⠁⠎⠀⠞⠑⠗⠗⠊⠋⠽⠊⠝⠛⠀⠁⠝⠙⠀⠽⠕⠥⠀⠅⠝⠕⠺⠀⠞⠓⠑⠀⠞⠓⠑⠀⠞⠓⠊⠝⠛⠀⠕⠃⠧⠊⠕⠥⠎⠇⠽⠀⠞⠓⠁⠞⠀⠺⠑⠝⠞⠀⠞⠓⠗⠕⠥⠛⠓⠀⠍⠽⠀⠓⠑⠁⠙⠀⠊⠎⠀⠞⠓⠑⠀⠋⠁⠉⠞⠀⠞⠓⠁⠞⠀⠽⠕⠥⠀⠅⠝⠕⠺⠀⠑⠧⠑⠝⠀⠑⠧⠑⠝⠀⠺⠓⠊⠇⠑⠀⠊'⠍⠀⠞⠗⠽⠊⠝⠛⠀⠞⠕⠀⠎⠁⠽⠀⠛⠕⠕⠙⠃⠽⠑⠀⠞⠕⠀⠍⠽⠀⠃⠗⠕⠞⠓⠑⠗⠀⠥⠍⠀⠞⠓⠑⠽'⠗⠑⠀⠞⠗⠽⠊⠝⠛⠀⠞⠕⠀⠅⠊⠇⠇⠀⠍⠑⠀⠊⠞⠀⠺⠁⠎⠀⠧⠑⠗⠽⠀⠎⠉⠁⠗⠽⠀⠑⠎⠏⠑⠉⠊⠁⠇⠇⠽⠀⠉⠕⠝⠎⠊⠙⠑⠗⠊⠝⠛⠀⠥⠍⠀⠺⠓⠁⠞⠀⠺⠑'⠧⠑⠀⠃⠑⠑⠝⠀⠞⠓⠗⠕⠥⠛⠓⠀⠁⠝⠙⠀⠞⠓⠁⠞⠀⠍⠽⠀⠏⠁⠗⠑⠝⠞⠎⠀⠺⠓⠕⠀⠇⠊⠧⠑⠀⠊⠝⠀⠇⠕⠝⠙⠕⠝⠀⠓⠁⠙⠀⠚⠥⠎⠞⠀⠁⠗⠗⠊⠧⠑⠙⠀⠊⠝⠀⠊⠎⠗⠁⠑⠇⠀⠞⠕⠀⠃⠥⠗⠽⠀⠞⠓⠑⠊⠗⠀⠎⠕⠝⠀⠝⠁⠞⠁⠝⠑⠇⠀⠚⠥⠎⠞⠀⠕⠝⠑⠀⠕⠋⠀⠂⠠⠲⠴⠴⠀⠍⠥⠗⠙⠑⠗⠑⠙⠀⠃⠽⠀⠓⠁⠍⠁⠎⠀⠊⠝⠀⠕⠝⠑⠀⠙⠁⠽⠀⠇⠥⠉⠽⠀⠍⠁⠝⠝⠊⠝⠛⠀⠃⠃⠉⠀⠝⠑⠺⠎

Video: well at least 1,400 people were killed in last week's attack by hamas in southern israel and as we've been hearing six were british among the missing are two british teen'\xffa0'\x00a0ge sisters as lucy manning reports noya 16 on the left yel 13 on the right now missing after the hamas attack on israel in between them their mom lean murdered by hamas'\x0001'll are british leanne's family said she led a beautiful life and enriched the lives of all those lucky enough to have known and loved her she was a beloved daughter sist'\xffa0'\x00a0r mother and aunt the girl's dad ellie is also missing this is what happened to an entire family in israel they lived on kibot beeri where the murderous gunman slaughtere'\x0019' so many noa is 16 years old she was happiness and she like to her hobbies to like she likes to cook yeah she was a funny girl she was all all the time she like to hear'\xffa0'\x00a0music and singing for us dancing natanel young also british also murdered by hamas his brother elliot remembers a 20-year-old who was a londoner a music lover a proud je`3 natanel uh you know he just loved life he um had a lot of respect for my uh parents he uh wanted to um keep his people safe and defend this country we're all just broke'\xffa0'\x00a0it's we're still coming to terms with the news what will you miss about natanel the last time i saw him was uh exactly a week before he was killed by the hamas terrorist'\xffa0'\x00a0um and i think if i look back at that day it's his um infectious smile at the funeral on monday the morning interrupted air raid sirens pierced the grieving as mourners w'\x0011're forced onto the cemetery ground to shield from incoming hamas missiles it was terrifying and you know the the thing obviously that went through my head is the fact t'\xffa0'\x00a0at you know even even while i'm trying to say goodbye to my brother um they're trying to kill me it was very scary especially considering um what we've been through and th'\x0001't my parents who live in london had just arrived in israel to bury their son natanel just one of 1,400 murdered by hamas in one day lucy manning bbc news


## Contributing
Contributions to this project are welcome! Feel free to open issues, submit pull requests, or suggest improvements.

## Acknowledgments
This project was inspired by BrailleRap, an open-source Braille embosser project. We encourage you to check it out.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
