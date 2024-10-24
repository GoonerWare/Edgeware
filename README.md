# Edgeware
**First and foremost as a disclaimer: this is NOT actually malicious software. It is intended for entertainment purposes only. Any and all damage caused to your files or computer is _YOUR_ responsibility. If you're worried about losing things, BACK THEM UP.**

**Please Note:** This is a fork of the [original Edgeware project](https://github.com/PetitTournesol/Edgeware) which has not been updated since 2022. Versions 2.5.0 Beta and above are provided by this fork.

If you get error "TypeError: unsupported operand type(s) for |: 'type' and 'type'", please make sure your Python is up to date! This fork is being developed on Python 3.12.x (at time of writing, 3.12.7)

_**[Maintainer's Note]**_

Hello! EdgewarePlusPlus is great, but has diverged enough from the original Edgeware following the rewrite that it should now be considered its own thing IMO. As great at it is, there are also some changes I am not a fan of and some outstanding bugs for things that I consider core functionality.

The initial idea behind this fork is to update the original Edgeware project so that it supports modern versions of Python out of the box. Improved functionality that doesn't change the core design of the original Edgeware may also be brought in though it may diverge over time.

_**[Release Notes]**_

Current version:

2.5.0 Beta Update *WIP version - will be updated*

- **Python Update** - *Updated Python installed by default to 3.12.7*
- **Popups & Start Screen** - *Changed resize method from ANTIALIAS to LANCZOS*
- **Discord Presence** - *Fixed issue with default packs, adds fallbacks*
- **Display Changes** - *Switches monitor handling to use screeninfo. Can optionally set Popups to only display on primary monitor*
- **Video Changes** - *Optionally enables video playback via VLC for improved performance*
- **GIF Changes** - *Now handles static GIFs as images instead of logging error*

**Important:** For the moment multi-monitor and VLC settings can be set via the Advanced tab:
- To enable VLC support make sure you have the correct version installed (e.g. 64bit for 64bit systems) and set `vlcMode` to 1
- To make Edgeware only display popups on your primary monitor, set `multiMonitor` to 0

The full release notes for past versions can be found [here](https://github.com/GoonerWare/Edgeware/blob/main/RELEASENOTES.md).

_**[How to Use]**_

Start by downloading this repository as a zip, and then extracting it somewhere on your computer.

(*If not using a premade package, skip this step.*)
Download one of the premade packages listed below. Once it's downloaded (if using a premade package), place it into the Edgeware folder inside Edgeware-main.

Double click "EdgewareSetup.bat" and follow the instructions. It should check your Python version, and then automatically download the correct installer from python.org and run it. Once you finish with that installation, it will run start.pyw, which will walk through an automated first time setup. Once this setup is complete, it will provide you with the config window to select your settings, and then run! (The installations only need to be performed on the first run)

   _**[Premade Packages]**_

Can be found on the [original repo](https://github.com/PetitTournesol/Edgeware).

__**FAQ**__

**Q: "Why do I keep getting white circles in my popups?"**

**A: *This occurs when the resource folder is generated without any resource zip in the script folder. Either delete your resource folder and restart Edgeware with the zip located properly or manually import your zip with the config function.***

**Q: "Where does the booru downloader save files?"**

**A: *The booru downloader saves all files it downloads into the /resource/img/ folder.***


__**What is Edgeware?**__

Edgeware is an Elsavirus inspired fetishware tool, built from the ground up to use interchangeable resource packages for easily customized user experience.

Much like Elsavirus and Doppelvirus, this program was written in brainlet level Python, but unlike the two of them, has no compiled executables. If you're the type to fear some hidden actually malicious scripts, this ensures that *all* of the code is front and center; no C++/C# forms or other tricks that might hide the true nature of the application.


The software features the popups, hard drive filling, porn library replacing, website opening features of its predecesors.

Edgeware *does* include some unique features to make it more widely applicable than just the previous respective target demographics of /beta/ participants and finsub followers. Namely its packaging system, which allows anyone to cater the experience to their own particular interests or fetishes. Either place a properly assembled zip file named "resources.zip" in the same folder as the scripts so that the program can unpack it or manually extract the resources folder into the said directory.

I more or less went into this wanting to make my own version of Elsavirus/Doppelvirus for fun, but figured around halfway that it might be worthwhile to share it with others who might have similar tastes.

Obviously you need to have Python installed, but other than that there should be no dependencies that aren't natively packaged with the language itself.

__**Packages**__

  Packages must be structured as follows:

    (name).zip
       ->aud
         (Audio Files) (Optional)
       ->img
         (Image Files, Gif Files)
	   ->subliminals
	     (Gif files only) (Optional)
       ->vid
         (Video Files) (Optional)
       icon.ico
       wallpaper.png
       web.json (Optional)
       prompt.json (Optional)
	   discord.dat (Optional)
	   captions.json (Optional)

  The web.json file should contain two sets:

    {"urls":["url1", "url2", ...], "args":["arg1,arg2,arg3", "", "arg1,arg2", ...]}
    ->urls - set of urls
    ->args - corresponding set of arguments; even if a url should take no argument, there must be a "" in this
      ->args are separated by commas within their strings, eg "arg1,arg2,arg3"
      ->ensure that urls and args are aligned; if the first URL can take the args "a,b" the first args value should be "a,b"
      ->args will be selected randomly and appended to the end of the url
        ->eg, "https://www.google.com/" with args "hello,goodbye" cound randomly return one of
        ->https://www.google.com/hello  https://www.google.com/goodbye

  The prompt.json file should contain any number of sets:

    {"moods":["mood1", "mood2", "angryMood"], "freqList":[10, 40, 50], "minLen":2, "maxLen"=4, "mood1":["mood1 sentence 1.", "mood1 sentence 2."], "mood2":["mood2 only has 1 sentence."], "angryMood":["angryMood also has one sentence."]}
        ->moods - names don't matter, as long as they're accounted for later in the set.
        ->freqList - correspond to each value in moods, define the frequency of that mood being selected.
        ->min/maxLen - minimum number of sentences that can be selected vs maximum.
        ->mood name
            ->can contain any number of mood related sentences.
            ->will ONLY select from this set if that mood is selected.

If resources are present, but not properly structured, the application could crash or exhibit strange behavior.

If you wish to make a donation, please do so to the original developer, note from them:
*If you like my work and would like to help me pay for food, please feel free to donate; Cashapp is $PetitTournesol*
