# MediaFire-URL-Download-Seed-Generator
The tool generates a wordlist with seeds to get access to random downloads which can contain some juicy stuff.Just run the tool and it will 
generate a list of seeds for MediaFire downloads. Some are false-positives as the owner could have removed the file/folder.Seedgen made for MediaFire fishing in combination with wfuzz. S is for how many letters/numbers will be generated. Range is for how many seeds will be generated.

Run with: wfuzz -c -v -w seeds.txt --hc=404 https://www.mediafire.com/file/FUZZ (The URL can also be http://www.mediafire.com/download/*SEED*)

For example this link https://www.mediafire.com/file/c0o3k17wzxiq3g0/xor_output.txt/file only need the seed "c0o3k17wzxiq3g0" to redirect to the full download. Use verbose for checking which 302 redirects to a download.

Youtube example: https://www.youtube.com/watch?v=AQPeCIsmU44

![github](https://user-images.githubusercontent.com/63813294/162187569-ac217b84-3466-4553-99c3-0e3282fa8fea.png)
