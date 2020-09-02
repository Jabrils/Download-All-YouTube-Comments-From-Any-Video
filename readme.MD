# Download All YouTube Comments From Any Video - v1

## Instructions
Step|Task
-|-
1|Open [DumpAllComments.py](./DumpAllComments.py)
2|Enter your API key that you got from the YouTube Data API v3 into `api_key = "ENTER_YOUR_API_KEY_HERE"`
4|Run the script from a terminal: `python DumpAllComments.py [VIDEO_ID_GOES_HERE]`
5|The default output file is `allComments.tsv`; you can specify a different file name by using the flag `--fName` as such: `python DumpAllComments.py [VIDEO_ID_GOES_HERE] --fName [FILE_NAME_GOES_HERE]`. The `.tsv` is added automatically, so just write the file name as the argument
5|Check the main directory for the .tsv file (its a tabs seperated values file), which will be allComments.tsv if you did not pass in an `--fName` argument
6|Profit

Follow the first half of this video to obtain an API for YouTube Data API v3; [YouTube Data API and Python -- Part 2 by LucidProgramming](https://youtu.be/ZkYOvViSx3E)