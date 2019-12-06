def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class ConstTestCaseFailReason():
    @constant
    def BELL_LOGO_NOT_FOUND():
        return "Bell logo launch timeout"    
    @constant
    def YOUTUBE_LAUNCH_TIMEOUT():
        return "Youtube launch timeout"
    @constant
    def BELL_APP_LAUNCHER_TIMEOUT():
        return "Bell app launcher launch timeout"
    @constant
    def WEATHER_NETWORK_LANUCH_TIMEOUT():
        return "Weather network launch timeout"
    @constant
    def VOD_LAUNCH_FROM_MENU_TIMEOUT():
        return "VOD launch from the menu, timout"
    @constant
    def VOD_LAUNCH_TIMEOUT():
        return "VOD launch timout"
    @constant
    def MY_FIBE_ICON_TIMEOUT():
        return "My fibe icon launch timeout"
    @constant
    def TC_DEFAULT_PAGE_TEXT_LOAD_TIMEOUT():
        return "Verification of \"Continue enjoying\" and \"My list\" failed"
    @constant
    def ASSET_MATCHED_FAILED():
        return "Asset match failed"
    @constant
    def MOTION_DETECTION_FAILED():
        return "Motion detection failed"
    @constant
    def SEASONS_TITLES_MATCH_FAILED():
        return "Matching of season's title failed"
    @constant
    def SEASONS_MATCH_FAILED():
        return "Seasons match failed"
    @constant
    def TEXT_NOT_FOUND():
        return "Text \"%s\" not found"
    @constant
    def ASSET_TITLES_MATCH_FAILED():
        return "Asset titles match failed"
    @constant
    def CATEGORY_MATCH_FAILED():
        return "Categories match failed"
    @constant
    def CATEGORY_MATCH_FAILED():
        return "Categories match failed"
    @constant
    def NETFLIX_LAUNCH_TIMEOUT():
        return "Netflix launch timeout"
    @constant
    def MOVIE_OR_SEASON_NOT_FOUND():
        return "Movie or Season not found"
    @constant
    def TIME_NOT_FOUND():
        return "Time not found"
    @constant
    def FORWARD_COMMAND_FAIL():
        return "Foward voice command failed"
    @constant
    def RECORING_NOT_LOADED():
        return "Recording screen didn't load"
    @constant
    def NO_RECORING_FOUND():
        return "There were no recordings"
    @constant
    def PLAY_BTN_NOT_FOUND():
        return "Play button not found"
    
    def text_not_found(self,text):
        return self.TEXT_NOT_FOUND % text

class ConstDeviceNames():
    @constant
    def MEDIA_FIRST():
        return "mediafirst"

    @constant
    def MEDIA_ROOM():
        return "mediaroom"
