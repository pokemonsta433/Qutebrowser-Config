c.editor.command = ['nvim-qt', '{file}']
config.load_autoconfig()

#import setproctitle
#setproctitle.setproctitle("qutebrowser")

#I'll try dark mode
# config.set("colors.webpage.darkmode.enabled", True)

#Bindings
config.bind("gi", "hint inputs")
config.bind("<f12>", "inspector")
config.bind("xb", "config-cycle statusbar.show always never")
config.bind("xt", "config-cycle tabs.show always never")
config.bind("xx", "config-cycle statusbar.show always never;; config-cycle tabs.show always never")

# search engines
c.url.searchengines = \
    { "DEFAULT" : "https://duckduckgo.com/?q={}",\
    "w" : "http://en.wikipedia.org/w/index.php?search={}&title=Special:Search",\
    "y" : "http://www.youtube.com/results?search_query={}",\
    "d" : "http://dictionary.reference.com/browse/{}?s=t",\
    "b" : "https://search.brave.com/search?q={}&source=web"
    }

#Shortcuts

#c.tabs.position = "left"
#c.completion.shrink = True
c.zoom.default = 140

#-------------------
# PRETTIFICATION
#-------------------
#fonts
c.fonts.default_family = '11pt "calling code"'
c.fonts.keyhint = '11pt "calling code"'
c.fonts.hints = '11pt "calling code"'
c.fonts.downloads = '11pt "calling code"'
c.fonts.contextmenu = '11pt "calling code"'
c.fonts.completion.entry = '11pt "calling code"'
c.fonts.debug_console = '11pt "calling code"'
c.fonts.prompts = '11pt "calling code"'
c.fonts.statusbar = '11pt "calling code"'

#colors
m_background = "#FFF8E7"
m_lightback = "#B1B4A2"
m_darkback = "#202A31"
m_foreground = "#485A62"
m_altFore = "#ABB0C0"
m_lightFore = "#63757E"
m_darkfore = "#364850"
m_Splash1 = "#C44756" # red
m_Splash2 = "#007F8A" # grey-blue
m_Splash3 = "#0075C9" # blue
m_Splash4 = "#A154AE" # purple
m_Splash5 = "#F6C967" # yellow
m_Splash6 = "#1F8332" # green
m_Splash7 = "#916D03" #brown

c.colors.statusbar.normal.bg = m_background
c.colors.statusbar.command.bg = m_background
c.colors.statusbar.normal.fg = m_foreground
c.colors.statusbar.command.fg = m_foreground
c.colors.statusbar.url.success.https.fg = m_foreground
c.colors.tabs.even.bg = m_background
c.colors.tabs.odd.bg = m_lightback
c.colors.tabs.even.fg = m_foreground
c.colors.tabs.odd.fg = m_darkfore
c.colors.tabs.selected.even.bg = m_darkback
c.colors.tabs.selected.odd.bg = m_darkback
c.colors.tabs.selected.even.fg = m_altFore
c.colors.tabs.selected.odd.fg = m_altFore
c.colors.tabs.indicator.stop = m_Splash2
c.colors.completion.category.bg = m_darkback
c.colors.completion.category.fg = m_altFore
c.colors.completion.even.bg = m_background
c.colors.completion.odd.bg = m_lightback
c.colors.completion.fg = m_foreground
c.colors.completion.item.selected.bg = m_darkback
c.colors.completion.item.selected.fg = m_altFore
c.colors.completion.match.fg = m_Splash1
c.colors.downloads.bar.bg = m_Splash4
c.colors.downloads.error.bg = m_Splash1
c.colors.downloads.error.fg = m_darkfore
c.colors.downloads.start.bg = m_Splash4
c.colors.downloads.start.fg = m_darkfore
c.colors.downloads.stop.bg = m_Splash7
c.colors.downloads.stop.fg = m_darkfore

c.colors.hints.bg = m_Splash5
c.colors.hints.fg = m_darkfore
c.colors.hints.match.fg = m_Splash3
c.hints.border = m_darkfore

c.colors.keyhint.bg = m_Splash5
c.colors.keyhint.fg = m_darkfore

c.colors.prompts.bg = m_darkback
c.colors.prompts.bg = m_altFore
