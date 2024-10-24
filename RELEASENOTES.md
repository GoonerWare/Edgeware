# Release Notes

**Current version:**

Release notes can be found in [README.md](https://github.com/GoonerWare/Edgeware/blob/main/README.md)

**Changes below this point were from the original developer, PetitTournesol.**

2.4.2_A Update

•*Fixed bugs with popups that caused videos and subliminal adjusted images to not load properly*

(Small) 2.4.2 Update

•*Popups should open faster and take up less memory while running*

•*Added a small message in the Booru Downloader section of config*

Hiya! I'm not dead! This update fixes some issues with popups that have been nagging at me in the back of my head for a while and adds a direct, in-application answer to the most common question I get messages about. I'd like to come back to the project when I have some more time, and it's possible that a code overhaul is in the future, but as life tends to be a roller coaster I can make no definite promises for the timeframe of that sort of an update. But know that this is a project I hope to fix up in the future, even if there will be fewer new features added with time.

Bugfix Version 2.4.1_2 Update

•*Properly re-fixed the issue causing config to corrupt the config file under specific circumstances which resulted in start and config crashing*

Bugfix Version 2.4.1_1 Update

•*Fixed Run on Startup*

Version 2.4.1 Update

•*Fixed bug where start and config would crash on startup for new users due to PIL not being properly placed into the safe import blocks*

Version 2.4.0 Updates

   _**[Large Additions]**_

•**Timer Mode** *Timed runs can now be set, during which the Panic features cannot be used (unless a password is set and used). Run on startup is also forcibly enabled during this time.*

•**Mode Presets** *Config files can now be saved as "Presets," and can be freely swapped between in the config menu itself. These can have descriptions along with them, stored as [preset name].txt text files inside the preset folder.*

•**Lowkey Mode** *A more laid back way to enjoy Edgeware, but more active than Hibernate Mode. Popups will flash from corner to corner before slowly fading away and being replaced by another new popup.*

•**Denial Mode** *While Denial Mode is toggled, popups can randomly be blurred out or otherwise censored. Text will appear on top of them, either a default phrase or a phrase selected from the captions.json file under the "denial" tag.*

•**Popup Subliminals** *Popups can now have subliminal gifs overlayed on top of them. To accompany this, a "submliminals" folder is now supported in resource packs, from which a subliminal gif will be randomly selected and overlayed on top of the image. If none are present, the default gif in default_resources will be used.*

     •*Please be aware that this feature can potentially be very memory/cpu intensive and set your popup fadeout accordingly.*

•**Booru Downloader Update** *The previous booru downloader was incompatible with Rule34, and had actually completely broken due to a Booru update. The new version is more efficient and easier to maintain/fix if the issue arises again, and is also now able to handle exceptions to standard Booru URLs like Rule34.*

  _**[Small Additions]**_

•**Logging** *Start, config, and popup now all generate log files detailing their operation and any errors they encounter with greater detail.*

•**Panic Wallpaper** *Panic wallpaper is now previewed in the config menu, and can be changed to an image of your choice there, under the wallpaper tab.*

•**Debug Tool** *For other errors/viewing of print statements, a small debug batch tool has been added.*

•**Popup Opacity** *Added a new opacity setting for popups.*

•**Tray Icon** *Added a tray icon for Edgeware, which allows you to easily use the panic feature even while no popups are on the screen without manually running the panic files.*

   _**[Updated Features]**_

•**Panic Button** *The panic button is now "e" by default instead of "\`".*

•**Fill Delay** *Updated fill delay setting, now ranges from 0ms to 2500ms instead of the previous 0-25ms.*

•**Video Player** *Videos no longer play in a web browser, and instead now play in popup windows. The volume of the videos can also be configured on the config menu.*

•**Audio Handling** *Updated how audio is played, so now mp3 OR wav files, probably others too but I haven't tested them.*

•**Wallpaper Handling** *Updated wallpaper handling, which should result in wallpapers being more stable for config to handle, and prevent any accidental self doxxing when sharing config files.*

•**Library Imports** *Updated library importing at the start of start and config. Much more standardized and no longer requires checks in the config file.*

•**Config Layout** *Config layout has been updated, with features being more spaced out.*

•**General Standardization** *Start and Config have been updated to make their code more standardized. (I did my best to comply with pep8 but I'm very stupid so please bear with me programmers)*

•**Advanced Tab** *Minor adjustments to the Advanced tab layout, bringing it into line with the rest of the config menu.*

   _**[Bugfixes]**_

•**Popup Borders** *Popups now properly have borders that go all the way around the image instead of just the top and left sides.*

•**Config/Start Crash** *Fixed bug where the config file would be corrupted by config.cfg saving wallpapers in a certain configuration.*

•**Wallpaper Crash** *Fixed bug where missing wallpaper setting would cause config to crash when opening.*

•**Run on Startup Failure** *Fixed bug where the startup bat would not be placed into the windows startup folder. (This should be fixed, but it's always possible I just fixed a different but connected issue instead.)*