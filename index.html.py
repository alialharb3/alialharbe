birth_year = input('Birth year: ')
age = 2023 - int(birth_year)
print(age)

< html
lang = "en" > < head >

< !-- Error
reporting -->
< script async=""
src = "https://www.clarity.ms/s/0.7.8/clarity.js" > < / script > < script async=""
src = "https://www.clarity.ms/tag/uet/5220035" > < / script > < script
type = "text/javascript" async=""
src = "https://www.google-analytics.com/plugins/ua/ec.js" > < / script > < script
type = "text/javascript" async=""
src = "https://www.google-analytics.com/plugins/ua/linkid.js" > < / script > < script
type = "text/javascript" async=""
src = "//munchkin.marketo.net/163/munchkin.js" > < / script > < script
type = "text/javascript" async=""
src = "https://www.googletagmanager.com/gtag/js?id=G-9J976DJZ68&amp;l=dataLayer&amp;cx=c" > < / script > < script
type = "text/javascript" async=""
src = "https://www.google-analytics.com/analytics.js" > < / script > < script
src = "//bat.bing.com/bat.js" async="" > < / script > < script
src = "https://connect.facebook.net/signals/config/614099138684330?v=2.9.104&amp;r=stable" async="" > < / script > < script
src = "https://connect.facebook.net/signals/config/357569036421264?v=2.9.104&amp;r=stable" async="" > < / script > < script
src = "https://connect.facebook.net/signals/plugins/identity.js?v=2.9.104" async="" > < / script > < script
type = "text/javascript" async=""
src = "https://connect.facebook.net/en_US/fbevents.js" > < / script > < script
type = "text/javascript" async=""
src = "https://snap.licdn.com/li.lms-analytics/insight.min.js" > < / script > < script
type = "text/javascript" async=""
src = "https://static.ads-twitter.com/uwt.js" > < / script > < script async=""
src = "https://www.googletagmanager.com/gtm.js?id=GTM-5P98" > < / script > < script > (function(){
window.reportError = function(msg, file, line, col, err, isUnhandledRejection)
{};
var
prevOnError = window.onerror;
var
onError = function(msg, file, line, col, err)
{
    reportError(msg, file, line, col, err, false);
prevOnError & & prevOnError.apply(window, arguments);
return false;
};
window.onerror = onError;
// Setup
reporting
for unhandled Promise rejection errors
window.addEventListener("unhandledrejection", function(e) {
if (!e.reason)
return;
var
l = getSrcLocation(e.reason);
reportError(e.reason.message, l.file, l.line, l.col, e.reason, true);
});
// Setup
reporting
for console.error and console.warn calls
patchConsole('error');
patchConsole('warn');
// Utility functions
function patchConsole(fnName) {
var fn = console[fnName];
console[fnName] = function() {
fn.apply(console, arguments);
var
l; try {
    throw
new
Error('_');
} catch(err)
{
    l = getSrcLocation(err, 1);
}
var
msg = 'console.' + fnName + ': ' + Array.prototype.join.call(arguments, ' ');
reportError(msg, l.file, l.line, l.col, undefined, false);
};
}
function
getSrcLocation(err, sd)
{
    var
s = err & & err.stack;
var
l = s & & s.split("\n")[1 + (sd | 0)];
var
r = l & & (/ ^ \s * at[^ (] * \((.* ?):(\d+)(:\d +)?\)$ /.exec(l) | | / ^ \s * at(. *?):(\d+)(:\d +)?$ /.exec(l));
return r ? {file: r[1], line: r[2], col: r[3]}: {};
}
})(); < / script >
          <!-- Error
reporting --> < !-- Google
Tag
Manager -->
< script > (function() {
// Initialize Tag Manager queue
window.dataLayer = window.dataLayer | |[];
window.gtmLoaded = false;
// Setup reporting for errors that occurred before Tag Manager initialized
var prevReportError = window.reportError;
var reportError = function(msg, file, line, col, err, isUnhandledRejection)
{
if (!window.gtmLoaded | | isUnhandledRejection) {
// Reproduce the behavior of the Tag Manager error handler
window.dataLayer.push(makeEvt(msg, file, line));
}
prevReportError & & prevReportError.apply(window, arguments);
};
window.reportError = reportError;
// Utility
functions
function
makeEvt(msg, file, line)
{
return {
    event: "gtm.pageError", "gtm.errorMessage": msg,
    "gtm.errorUrl": file, "gtm.errorLineNumber": line
};
}
})(); < / script >
          < script > (function(w, d, s, l, i){w[l]=w[l] | |[];w[l].push({'gtm.start':
new Date().getTime(), event: 'gtm.js'});var
f = d.getElementsByTagName(s)[0],
j = d.createElement(s), dl = l != 'dataLayer'?'&l=' + l: '';
j.async=true;
j.src = \
    'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
j.addEventListener(
'load', function()
{window.gtmLoaded = true});f.parentNode.insertBefore(j, f);
})(window, document, 'script', 'dataLayer', 'GTM-5P98'); < / script >
                                                             <!-- End
Google
Tag
Manager -->
< title > Thank
you
for downloading PyCharm! < /title >

< meta charset="utf-8" >
< meta http-equiv="x-ua-compatible" content="IE=edge" >
< meta name="viewport" content="width=device-width, maximum-scale=1" >

< link rel="icon" href="/favicon.ico?r=1234" type="image/x-icon" > < !-- 48×48 -->
< link rel="icon" href="/icon.svg?r=1234" type="image/svg+xml" sizes="any" >
< link rel="apple-touch-icon" href="/apple-touch-icon.png?r=1234" sizes="180x180" > < !-- 180×180 -->
< link rel="icon" href="/icon-512.png?r=1234" type="image/png" sizes="512x512" >
< link rel="manifest" href="/site.webmanifest" >

< meta name="apple-mobile-web-app-title" content="JetBrains" >
< meta name="application-name" content="JetBrains" >
< meta name="msapplication-TileColor" content="#000000" >
< meta name="theme-color" content="#000000" >
< link rel="canonical" href="https://www.jetbrains.com/pycharm/download/download-thanks.html" > < !-- .385-->
< meta name="description" content="Intelligent Python IDE with refactorings, debugger, code completion, on-the-fly code analysis and coding productivity orientation
">

< link rel="alternate" hreflang="x-default" href="https://www.jetbrains.com/pycharm/download/download-thanks.html" >

< link rel="alternate" hreflang="en" href="https://www.jetbrains.com/pycharm/download/download-thanks.html" >
< link rel="alternate" hreflang="en-CN" href="https://www.jetbrains.com.cn/en-us/pycharm/download/download-thanks.html" >
< link rel="alternate" hreflang="de" href="https://www.jetbrains.com/de-de/pycharm/download/download-thanks.html" >
< link rel="alternate" hreflang="es" href="https://www.jetbrains.com/es-es/pycharm/download/download-thanks.html" >
< link rel="alternate" hreflang="fr" href="https://www.jetbrains.com/fr-fr/pycharm/download/download-thanks.html" >
< link rel="alternate" hreflang="ja" href="https://www.jetbrains.com/ja-jp/pycharm/download/download-thanks.html" >
< link rel="alternate" hreflang="ko" href="https://www.jetbrains.com/ko-kr/pycharm/download/download-thanks.html" >
< link rel="alternate" hreflang="ru" href="https://www.jetbrains.com/ru-ru/pycharm/download/download-thanks.html" >
< link rel="alternate" hreflang="zh-Hans" href="https://www.jetbrains.com/zh-cn/pycharm/download/download-thanks.html" >
< link rel="alternate" hreflang="zh-CN" href="https://www.jetbrains.com.cn/pycharm/download/download-thanks.html" >
< link rel="alternate" hreflang="pt-BR" href="https://www.jetbrains.com/pt-br/pycharm/download/download-thanks.html" >

< meta name="robots" content="noindex" >

< script >
default_site_language = 'en-us';
var current_lang = 'en-us';
var i18n_info = {"current_lang": "en-us", "languages": [
    {"canonical": "en", "code": "en-us", "label": "English", "page_translated": true,
     "url": "/pycharm/download/download-thanks.html"},
    {"canonical": "de", "code": "de-de", "label": "Deutsch", "page_translated": true,
     "url": "/de-de/pycharm/download/download-thanks.html"},
    {"canonical": "es", "code": "es-es", "label": "Espa\u00f1ol", "page_translated": true,
     "url": "/es-es/pycharm/download/download-thanks.html"},
    {"canonical": "fr", "code": "fr-fr", "label": "Fran\u00e7ais", "page_translated": true,
     "url": "/fr-fr/pycharm/download/download-thanks.html"},
    {"canonical": "ja", "code": "ja-jp", "label": "\u65e5\u672c\u8a9e", "page_translated": true,
     "url": "/ja-jp/pycharm/download/download-thanks.html"},
    {"canonical": "ko", "code": "ko-kr", "label": "\ud55c\uad6d\uc5b4", "page_translated": true,
     "url": "/ko-kr/pycharm/download/download-thanks.html"},
    {"canonical": "ru", "code": "ru-ru", "label": "\u0420\u0443\u0441\u0441\u043a\u0438\u0439", "page_translated": true,
     "url": "/ru-ru/pycharm/download/download-thanks.html"},
    {"canonical": "zh-Hans", "code": "zh-cn", "label": "\u7b80\u4f53\u4e2d\u6587", "page_translated": true,
     "url": "/zh-cn/pycharm/download/download-thanks.html"},
    {"canonical": "pt-BR", "code": "pt-br", "label": "Portugu\u00eas do Brasil", "page_translated": true,
     "url": "/pt-br/pycharm/download/download-thanks.html"}]};
var
navigationMenu = {"primary": {"items": [{"title": "Developer Tools", "banners": [
    {"isActive": false, "title": "Space", "description": "A complete software development platform",
     "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/space/space.svg",
     "actionLabel": "Explore Space", "url": "/space/", "isUrlShouldBeLocalized": true, "bgColor": "#167DFF",
     "bgGradient": "linear-gradient(117.63deg, rgb(8 89 255) -0.78%, rgb(0 154 231) 55.03%, rgb(221 255 84) 111.19%)",
     "cleaned_url": "/space/"}, {"isActive": false, "title": "Fleet", "description": "Next-generation IDE by JetBrains",
                                 "logoSrc": "/img/banners-menu-main/fleet.png", "actionLabel": "Learn more",
                                 "url": "/fleet/", "isUrlShouldBeLocalized": true, "bgColor": "#8701C7",
                                 "bgGradient": "linear-gradient(130.93deg, #69029A 0%, #8701C7 32.33%, #6B57FF 97.76%)",
                                 "cleaned_url": "/fleet/"}], "suggestions": [
    {"isActive": false, "url": "/products/", "isUrlShouldBeLocalized": true,
     "title": "Not sure which tool is best for you?",
     "description": "Whichever technologies you use, there's a JetBrains tool to match",
     "actionLabel": "Find your tool", "cleaned_url": "/products/"}],
                                         "submenu": {"layout": "auto-fill inline inline inline", "columns": [
                                             {"title": "IDEs", "mobileLayout": "forceTwoColumns", "subColumns": [{
                                                                                                                     "items": [
                                                                                                                         {
                                                                                                                             "isActive": false,
                                                                                                                             "title": "AppCode",
                                                                                                                             "url": "/objc/",
                                                                                                                             "isUrlShouldBeLocalized": true,
                                                                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/appcode/appcode.svg",
                                                                                                                             "cleaned_url": "/objc/"},
                                                                                                                         {
                                                                                                                             "isActive": false,
                                                                                                                             "title": "Aqua",
                                                                                                                             "url": "/aqua/",
                                                                                                                             "isUrlShouldBeLocalized": true,
                                                                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/aqua/aqua.svg",
                                                                                                                             "cleaned_url": "/aqua/"},
                                                                                                                         {
                                                                                                                             "isActive": false,
                                                                                                                             "title": "CLion",
                                                                                                                             "url": "/clion/",
                                                                                                                             "isUrlShouldBeLocalized": true,
                                                                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/clion/clion.svg",
                                                                                                                             "cleaned_url": "/clion/"},
                                                                                                                         {
                                                                                                                             "isActive": false,
                                                                                                                             "title": "DataGrip",
                                                                                                                             "url": "/datagrip/",
                                                                                                                             "isUrlShouldBeLocalized": true,
                                                                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/datagrip/datagrip.svg",
                                                                                                                             "cleaned_url": "/datagrip/"},
                                                                                                                         {
                                                                                                                             "isActive": false,
                                                                                                                             "title": "DataSpell",
                                                                                                                             "url": "/dataspell/",
                                                                                                                             "isUrlShouldBeLocalized": true,
                                                                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/dataspell/dataspell.svg",
                                                                                                                             "cleaned_url": "/dataspell/"},
                                                                                                                         {
                                                                                                                             "isActive": false,
                                                                                                                             "title": "Fleet",
                                                                                                                             "url": "/fleet/",
                                                                                                                             "isUrlShouldBeLocalized": true,
                                                                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/fleet/fleet.svg",
                                                                                                                             "cleaned_url": "/fleet/"},
                                                                                                                         {
                                                                                                                             "isActive": false,
                                                                                                                             "title": "GoLand",
                                                                                                                             "url": "/go/",
                                                                                                                             "isUrlShouldBeLocalized": true,
                                                                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/goland/goland.svg",
                                                                                                                             "cleaned_url": "/go/"}]},
                                                                                                                 {
                                                                                                                     "items": [
                                                                                                                         {
                                                                                                                             "isActive": false,
                                                                                                                             "title": "IntelliJ&nbsp;IDEA",
                                                                                                                             "url": "/idea/",
                                                                                                                             "isUrlShouldBeLocalized": true,
                                                                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/intellij-idea/intellij-idea.svg",
                                                                                                                             "cleaned_url": "/idea/"},
                                                                                                                         {
                                                                                                                             "isActive": false,
                                                                                                                             "title": "PhpStorm",
                                                                                                                             "url": "/phpstorm/",
                                                                                                                             "isUrlShouldBeLocalized": true,
                                                                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/phpstorm/phpstorm.svg",
                                                                                                                             "cleaned_url": "/phpstorm/"},
                                                                                                                         {
                                                                                                                             "isActive": false,
                                                                                                                             "title": "PyCharm",
                                                                                                                             "url": "/pycharm/",
                                                                                                                             "isUrlShouldBeLocalized": true,
                                                                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/pycharm/pycharm.svg",
                                                                                                                             "cleaned_url": "/pycharm/"},
                                                                                                                         {
                                                                                                                             "isActive": false,
                                                                                                                             "title": "Rider",
                                                                                                                             "url": "/rider/",
                                                                                                                             "isUrlShouldBeLocalized": true,
                                                                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/rider/rider.svg",
                                                                                                                             "cleaned_url": "/rider/"},
                                                                                                                         {
                                                                                                                             "isActive": false,
                                                                                                                             "title": "RubyMine",
                                                                                                                             "url": "/ruby/",
                                                                                                                             "isUrlShouldBeLocalized": true,
                                                                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/rubymine/rubymine.svg",
                                                                                                                             "cleaned_url": "/ruby/"},
                                                                                                                         {
                                                                                                                             "isActive": false,
                                                                                                                             "title": "WebStorm",
                                                                                                                             "url": "/webstorm/",
                                                                                                                             "isUrlShouldBeLocalized": true,
                                                                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/webstorm/webstorm.svg",
                                                                                                                             "cleaned_url": "/webstorm/"}]}]},
                                             {"title": "PLUGINS & SERVICES", "mobileLayout": "forceTwoColumns",
                                              "items": [{"isActive": false, "title": "All Plugins",
                                                         "url": "https://plugins.jetbrains.com/",
                                                         "cleaned_url": "https://plugins.jetbrains.com/"},
                                                        {"isActive": false, "title": "IDE Themes",
                                                         "url": "https://plugins.jetbrains.com/search?tags=Theme",
                                                         "cleaned_url": "https://plugins.jetbrains.com/search?tags=Theme"},
                                                        {"isActive": false, "title": "Big Data Tools",
                                                         "url": "https://plugins.jetbrains.com/plugin/12494-big-data-tools",
                                                         "cleaned_url": "https://plugins.jetbrains.com/plugin/12494-big-data-tools"},
                                                        {"isActive": false, "title": "Code With Me",
                                                         "url": "/code-with-me/", "isUrlShouldBeLocalized": true,
                                                         "cleaned_url": "/code-with-me/"},
                                                        {"isActive": false, "title": "RiderFlow", "url": "/riderflow/",
                                                         "isUrlShouldBeLocalized": true, "cleaned_url": "/riderflow/"},
                                                        {"isActive": false, "title": "Rust", "url": "/rust/",
                                                         "isUrlShouldBeLocalized": true, "cleaned_url": "/rust/"},
                                                        {"isActive": false, "title": "Scala",
                                                         "url": "https://plugins.jetbrains.com/plugin/1347-scala",
                                                         "cleaned_url": "https://plugins.jetbrains.com/plugin/1347-scala"},
                                                        {"isActive": false, "title": "Toolbox App",
                                                         "url": "/toolbox-app/", "isUrlShouldBeLocalized": true,
                                                         "cleaned_url": "/toolbox-app/"},
                                                        {"isActive": false, "title": "Toolbox Enterprise",
                                                         "url": "/toolbox-enterprise/", "isUrlShouldBeLocalized": false,
                                                         "cleaned_url": "/toolbox-enterprise/"}]},
                                             {"title": ".NET & VISUAL STUDIO", "hasSeparator": true, "items": [
                                                 {"isActive": false, "title": "Rider", "url": "/rider/",
                                                  "isUrlShouldBeLocalized": true,
                                                  "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/rider/rider.svg",
                                                  "cleaned_url": "/rider/"},
                                                 {"isActive": false, "title": "ReSharper", "url": "/resharper/",
                                                  "isUrlShouldBeLocalized": true,
                                                  "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/resharper/resharper.svg",
                                                  "cleaned_url": "/resharper/"},
                                                 {"isActive": false, "title": "ReSharper C++", "url": "/resharper-cpp/",
                                                  "isUrlShouldBeLocalized": true,
                                                  "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/resharper-cpp/resharper-cpp.svg",
                                                  "cleaned_url": "/resharper-cpp/"},
                                                 {"isActive": false, "title": "dotCover", "url": "/dotcover/",
                                                  "isUrlShouldBeLocalized": true,
                                                  "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/dotcover/dotcover.svg",
                                                  "cleaned_url": "/dotcover/"},
                                                 {"isActive": false, "title": "dotMemory", "url": "/dotmemory/",
                                                  "isUrlShouldBeLocalized": true,
                                                  "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/dotmemory/dotmemory.svg",
                                                  "cleaned_url": "/dotmemory/"},
                                                 {"isActive": false, "title": "dotPeek", "url": "/decompiler/",
                                                  "isUrlShouldBeLocalized": true,
                                                  "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/dotpeek/dotpeek.svg",
                                                  "cleaned_url": "/decompiler/"},
                                                 {"isActive": false, "title": "dotTrace", "url": "/profiler/",
                                                  "isUrlShouldBeLocalized": true,
                                                  "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/dottrace/dottrace.svg",
                                                  "cleaned_url": "/profiler/"},
                                                 {"isActive": false, "title": ".NET Tools Plugins",
                                                  "url": "https://plugins.jetbrains.com/search?isFeaturedSearch=true&products=resharper&products=rider",
                                                  "cleaned_url": "https://plugins.jetbrains.com/search?isFeaturedSearch=true&products=resharper&products=rider"}]},
                                             {"title": "LANGUAGES & FRAMEWORKS", "hasSeparator": true, "items": [
                                                 {"isActive": false, "title": "Kotlin",
                                                  "url": "https://kotlinlang.org/",
                                                  "cleaned_url": "https://kotlinlang.org/"},
                                                 {"isActive": false, "title": "Ktor", "url": "https://ktor.io/",
                                                  "cleaned_url": "https://ktor.io/"},
                                                 {"isActive": false, "title": "MPS", "url": "/mps/",
                                                  "isUrlShouldBeLocalized": true, "cleaned_url": "/mps/"},
                                                 {"isActive": false, "title": "Compose Multiplatform",
                                                  "url": "/lp/compose-multiplatform/", "isUrlShouldBeLocalized": true,
                                                  "cleaned_url": "/lp/compose-multiplatform/"}]}]}},
                                        {"title": "Team Tools", "banners": [{"isActive": false, "title": "Datalore",
                                                                             "description": "A collaborative data science platform. Available online and on-premises",
                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/datalore/datalore.svg",
                                                                             "actionLabel": "Learn more",
                                                                             "url": "/datalore/",
                                                                             "isUrlShouldBeLocalized": true,
                                                                             "bgColor": "#005CD1",
                                                                             "bgGradient": "linear-gradient(120.81deg, #003396 11.31%, #009CF4 95.37%)",
                                                                             "cleaned_url": "/datalore/"},
                                                                            {"isActive": false, "title": "YouTrack",
                                                                             "description": "Powerful project management for all your teams",
                                                                             "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/youtrack/youtrack.svg",
                                                                             "actionLabel": "Learn more",
                                                                             "url": "/youtrack/",
                                                                             "isUrlShouldBeLocalized": true,
                                                                             "bgColor": "#6B57FF",
                                                                             "bgGradient": "linear-gradient(141.09deg, #D80663 -21.81%, #834CEF 33.98%, #00B5E2 100.21%)",
                                                                             "cleaned_url": "/youtrack/"}],
                                         "submenu": {"layout": "8 4", "columns": [
                                             {"title": "IN-CLOUD AND ON-PREMISES SOLUTIONS", "subColumns": [{"items": [
                                                 {"isActive": false, "title": "Datalore", "url": "/datalore/",
                                                  "isUrlShouldBeLocalized": true,
                                                  "description": "A collaborative data science platform",
                                                  "cleaned_url": "/datalore/"},
                                                 {"isActive": false, "title": "Space", "url": "/space/",
                                                  "isUrlShouldBeLocalized": true,
                                                  "description": "A complete software development platform",
                                                  "cleaned_url": "/space/"},
                                                 {"isActive": false, "title": "TeamCity", "url": "/teamcity/",
                                                  "isUrlShouldBeLocalized": true,
                                                  "description": "Powerful Continuous Integration out of the box",
                                                  "cleaned_url": "/teamcity/"}]}, {"items": [
                                                 {"isActive": false, "title": "YouTrack", "url": "/youtrack/",
                                                  "isUrlShouldBeLocalized": true,
                                                  "description": "Powerful project management for all your teams",
                                                  "cleaned_url": "/youtrack/"},
                                                 {"isActive": false, "title": "Qodana", "url": "/qodana/",
                                                  "isUrlShouldBeLocalized": true,
                                                  "description": "The code quality platform for your favorite CI",
                                                  "cleaned_url": "/qodana/"}]}]},
                                             {"title": "EXTENSIONS", "hasSeparator": true, "items": [
                                                 {"isActive": false, "title": "TeamCity Plugins",
                                                  "url": "https://plugins.jetbrains.com/teamcity/",
                                                  "cleaned_url": "https://plugins.jetbrains.com/teamcity/"},
                                                 {"isActive": false, "title": "YouTrack Extensions",
                                                  "url": "https://plugins.jetbrains.com/youtrack/",
                                                  "cleaned_url": "https://plugins.jetbrains.com/youtrack/"},
                                                 {"isActive": false, "title": "JetBrains Hub", "url": "/hub/",
                                                  "isUrlShouldBeLocalized": true, "cleaned_url": "/hub/"}]}]}},
                                        {"title": "Education", "banners": [
                                            {"isActive": false, "title": "JetBrains Academy",
                                             "description": "Find your way in learning or teaching computer science",
                                             "actionLabel": "Discover more", "url": "/academy",
                                             "isUrlShouldBeLocalized": true,
                                             "logoSrc": "/img/banners-menu-main/academy-logo.svg", "bgColor": "#B01DF6",
                                             "bgGradient": "linear-gradient(335.07deg, #636CEA 0%, #834CEF 40.63%, #771F89 100%)",
                                             "cleaned_url": "/academy"}], "submenu": {"columns": [
                                            {"title": "FOR LEARNERS", "layout": "11 11 11", "subColumns": [{"items": [
                                                {"isActive": false, "title": "Programming languages",
                                                 "url": "/academy/#learn", "isUrlShouldBeLocalized": true,
                                                 "description": "Select a language and try different approaches to learning it",
                                                 "cleaned_url": "/academy/#learn"},
                                                {"isActive": false, "title": "Career fields",
                                                 "url": "/academy/#careers", "isUrlShouldBeLocalized": true,
                                                 "description": "Explore careers and see where programming could take you",
                                                 "cleaned_url": "/academy/#careers"},
                                                {"isActive": false, "title": "University relations",
                                                 "url": "/education/university-relations/",
                                                 "isUrlShouldBeLocalized": true,
                                                 "description": "Study offline with academic programs",
                                                 "cleaned_url": "/education/university-relations/"},
                                                {"isActive": false, "title": "Internships",
                                                 "url": "/careers/internships/", "isUrlShouldBeLocalized": true,
                                                 "description": "Apply for internships and flexible jobs for students\n",
                                                 "cleaned_url": "/careers/internships/"}]}]},
                                            {"title": "FOR EDUCATORS", "layout": "11 11 11", "subColumns": [{"items": [
                                                {"isActive": false, "title": "Teaching with JetBrains IDEs",
                                                 "url": "/pages/academy/teaching/", "isUrlShouldBeLocalized": true,
                                                 "description": "Create courses and share your knowledge",
                                                 "cleaned_url": "/pages/academy/teaching/"},
                                                {"isActive": false, "title": "Kotlin for education",
                                                 "url": "https://kotlinlang.org/education/",
                                                 "isUrlShouldBeLocalized": true,
                                                 "description": "Teach a wide range of Kotlin courses",
                                                 "cleaned_url": "https://kotlinlang.org/education/"}]}, {
                                                                                                                "title": "FOR TEAMS",
                                                                                                                "items": [
                                                                                                                    {
                                                                                                                        "isActive": false,
                                                                                                                        "title": "Professional development",
                                                                                                                        "url": "https://lp.jetbrains.com/academy/for-organizations",
                                                                                                                        "isUrlShouldBeLocalized": true,
                                                                                                                        "description": "Ensure your team has up-to-date technical skills",
                                                                                                                        "cleaned_url": "https://lp.jetbrains.com/academy/for-organizations"}]}]},
                                            {"title": "FREE LICENSES", "hasSeparator": true, "items": [
                                                {"isActive": false, "title": "For students and teachers",
                                                 "url": "/community/education/#students/",
                                                 "isUrlShouldBeLocalized": true,
                                                 "description": "JetBrains IDEs for individual academic use",
                                                 "cleaned_url": "/community/education/#students/"},
                                                {"isActive": false, "title": "For educational institutions",
                                                 "url": "/community/education/#classrooms",
                                                 "isUrlShouldBeLocalized": true,
                                                 "description": "JetBrains IDEs and team tools for classroom use",
                                                 "cleaned_url": "/community/education/#classrooms"},
                                                {"isActive": false, "title": "For bootcamps and courses",
                                                 "url": "/community/education/#courses", "isUrlShouldBeLocalized": true,
                                                 "description": "JetBrains IDEs for your students",
                                                 "cleaned_url": "/community/education/#courses"}]}]}},
                                        {"title": "Solutions", "banners": [
                                            {"isActive": false, "title": "Developer Tools for Your Business",
                                             "description": "Professional tools for productive development",
                                             "actionLabel": "Learn more", "url": "/store/business/",
                                             "isUrlShouldBeLocalized": true,
                                             "logoSrc": "/img/banners-menu-main/containers.svg", "bgColor": "#6B57FF",
                                             "bgGradient": "linear-gradient(246.1deg, rgb(0 224 214) 1.67%, rgb(126 27 253) 92.48%)",
                                             "cleaned_url": "/store/business/"},
                                            {"isActive": false, "title": "Remote Development",
                                             "description": "Connect to remote dev environments from anywhere in seconds",
                                             "actionLabel": "Discover more", "url": "/remote-development/",
                                             "isUrlShouldBeLocalized": true, "bgColor": "#2DF388",
                                             "bgGradient": "linear-gradient(240.88deg, #2DF388 0%, #05BF87 37.75%, #027474 98.39%)",
                                             "cleaned_url": "/remote-development/"}], "submenu": {"layout": "8 4",
                                                                                                  "columns": [{
                                                                                                                  "title": "BY INDUSTRY & TECHNOLOGY",
                                                                                                                  "layout": "6 6",
                                                                                                                  "subColumns": [
                                                                                                                      {
                                                                                                                          "items": [
                                                                                                                              {
                                                                                                                                  "isActive": false,
                                                                                                                                  "title": "Remote Development",
                                                                                                                                  "url": "/remote-development/",
                                                                                                                                  "isUrlShouldBeLocalized": true,
                                                                                                                                  "description": "Tools for remote development for you and your team",
                                                                                                                                  "cleaned_url": "/remote-development/"},
                                                                                                                              {
                                                                                                                                  "isActive": false,
                                                                                                                                  "title": "Game Development",
                                                                                                                                  "url": "/gamedev/",
                                                                                                                                  "isUrlShouldBeLocalized": true,
                                                                                                                                  "description": "Tools for game development for any platform",
                                                                                                                                  "cleaned_url": "/gamedev/"},
                                                                                                                              {
                                                                                                                                  "isActive": false,
                                                                                                                                  "title": "DevOps",
                                                                                                                                  "url": "/devops/",
                                                                                                                                  "isUrlShouldBeLocalized": true,
                                                                                                                                  "description": "Tools and integrations for any infrastructure",
                                                                                                                                  "cleaned_url": "/devops/"},
                                                                                                                              {
                                                                                                                                  "isActive": false,
                                                                                                                                  "title": "Quality Assurance",
                                                                                                                                  "url": "/quality-assurance-solutions/",
                                                                                                                                  "isUrlShouldBeLocalized": true,
                                                                                                                                  "description": "Tools for Quality Assurance and Test Automation",
                                                                                                                                  "cleaned_url": "/quality-assurance-solutions/"}]},
                                                                                                                      {
                                                                                                                          "items": [
                                                                                                                              {
                                                                                                                                  "isActive": false,
                                                                                                                                  "title": "C++ Tools",
                                                                                                                                  "url": "/cpp/",
                                                                                                                                  "isUrlShouldBeLocalized": true,
                                                                                                                                  "description": "Tools for C/C++ development for any platform",
                                                                                                                                  "cleaned_url": "/cpp/"},
                                                                                                                              {
                                                                                                                                  "isActive": false,
                                                                                                                                  "title": "Data Tools",
                                                                                                                                  "url": "/data-tools/",
                                                                                                                                  "isUrlShouldBeLocalized": true,
                                                                                                                                  "description": "Tools for Big Data and Data Science",
                                                                                                                                  "cleaned_url": "/data-tools/"},
                                                                                                                              {
                                                                                                                                  "isActive": false,
                                                                                                                                  "title": "Software Development",
                                                                                                                                  "url": "/space/solutions/software-teams/",
                                                                                                                                  "isUrlShouldBeLocalized": true,
                                                                                                                                  "description": "All-in-one solution for software projects and teams",
                                                                                                                                  "cleaned_url": "/space/solutions/software-teams/"},
                                                                                                                              {
                                                                                                                                  "isActive": false,
                                                                                                                                  "title": "License Vault",
                                                                                                                                  "url": "/license-vault/",
                                                                                                                                  "isUrlShouldBeLocalized": true,
                                                                                                                                  "description": "Efficient management of JetBrains licenses",
                                                                                                                                  "cleaned_url": "/license-vault/"}]}]},
                                                                                                              {
                                                                                                                  "title": "RECOMMENDED",
                                                                                                                  "hasSeparator": true,
                                                                                                                  "items": [
                                                                                                                      {
                                                                                                                          "isActive": false,
                                                                                                                          "title": "All Products Pack",
                                                                                                                          "url": "/all/",
                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                          "cleaned_url": "/all/"},
                                                                                                                      {
                                                                                                                          "isActive": false,
                                                                                                                          "title": ".NET Tools",
                                                                                                                          "url": "/dotnet/",
                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                          "cleaned_url": "/dotnet/"},
                                                                                                                      {
                                                                                                                          "isActive": false,
                                                                                                                          "title": "JetBrains for Education",
                                                                                                                          "url": "/education/",
                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                          "cleaned_url": "/education/"},
                                                                                                                      {
                                                                                                                          "isActive": false,
                                                                                                                          "title": "All JetBrains Products",
                                                                                                                          "url": "/products/",
                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                          "cleaned_url": "/products/"},
                                                                                                                      {
                                                                                                                          "isActive": false,
                                                                                                                          "title": "JetBrains Marketplace",
                                                                                                                          "url": "https://plugins.jetbrains.com/",
                                                                                                                          "cleaned_url": "https://plugins.jetbrains.com/"}]}]}},
                                        {"title": "Support", "banners": [
                                            {"isActive": false, "title": "Download and Install",
                                             "actionLabel": "Download and Install", "url": "/products/",
                                             "isUrlShouldBeLocalized": true,
                                             "logoSrc": "/img/banners-menu-main/download.svg", "bgColor": "#6B57FF",
                                             "bgGradient": "linear-gradient(294.91deg, #FF318C -50.1%, #6B57FF 97.43%)",
                                             "cleaned_url": "/products/"},
                                            {"isActive": false, "title": "Contact us", "actionLabel": "Contact us",
                                             "url": "/company/contacts/", "isUrlShouldBeLocalized": true,
                                             "logoSrc": "/img/banners-menu-main/test-review.svg", "bgColor": "#21D789",
                                             "bgGradient": "linear-gradient(283.8deg, #087CFA 5.73%, #21D789 100%)",
                                             "cleaned_url": "/company/contacts/"}], "submenu": {"columns": [
                                            {"title": "PRODUCT & TECHNICAL SUPPORT", "layout": "12", "subColumns": [{
                                                                                                                        "items": [
                                                                                                                            {
                                                                                                                                "isActive": false,
                                                                                                                                "title": "Support Center",
                                                                                                                                "url": "/support/",
                                                                                                                                "isUrlShouldBeLocalized": true,
                                                                                                                                "cleaned_url": "/support/"},
                                                                                                                            {
                                                                                                                                "isActive": false,
                                                                                                                                "title": "Product Documentation",
                                                                                                                                "url": "/help/",
                                                                                                                                "isUrlShouldBeLocalized": true,
                                                                                                                                "cleaned_url": "/help/"},
                                                                                                                            {
                                                                                                                                "isActive": false,
                                                                                                                                "title": "Webinars",
                                                                                                                                "url": "/company/webinars/",
                                                                                                                                "isUrlShouldBeLocalized": true,
                                                                                                                                "cleaned_url": "/company/webinars/"},
                                                                                                                            {
                                                                                                                                "isActive": false,
                                                                                                                                "title": "Newsletters",
                                                                                                                                "url": "/resources/newsletters/",
                                                                                                                                "isUrlShouldBeLocalized": true,
                                                                                                                                "cleaned_url": "/resources/newsletters/"},
                                                                                                                            {
                                                                                                                                "isActive": false,
                                                                                                                                "title": "Early Access",
                                                                                                                                "url": "/resources/eap/",
                                                                                                                                "isUrlShouldBeLocalized": true,
                                                                                                                                "cleaned_url": "/resources/eap/"},
                                                                                                                            {
                                                                                                                                "isActive": false,
                                                                                                                                "title": "Blog",
                                                                                                                                "url": "https://blog.jetbrains.com/",
                                                                                                                                "isUrlShouldBeLocalized": true,
                                                                                                                                "cleaned_url": "https://blog.jetbrains.com/"}]}]},
                                            {"title": "FREQUENT TASKS", "hasSeparator": true, "items": [
                                                {"isActive": false, "title": "Manage your account",
                                                 "url": "https://account.jetbrains.com/profile-details",
                                                 "cleaned_url": "https://account.jetbrains.com/profile-details"},
                                                {"isActive": false, "title": "Manage your licenses",
                                                 "url": "https://account.jetbrains.com/licenses",
                                                 "cleaned_url": "https://account.jetbrains.com/licenses"},
                                                {"isActive": false, "title": "Contact Sales", "url": "/support/sales/",
                                                 "isUrlShouldBeLocalized": true, "cleaned_url": "/support/sales/"},
                                                {"isActive": false, "title": "Licensing FAQ",
                                                 "url": "https://sales.jetbrains.com", "isUrlShouldBeLocalized": true,
                                                 "cleaned_url": "https://sales.jetbrains.com"}]}]}}, {"title": "Store",
                                                                                                      "banners": [{
                                                                                                                      "isActive": false,
                                                                                                                      "title": "All Products Pack",
                                                                                                                      "description": "Get all JetBrains desktop tools including 10&nbsp;IDEs,<br />2&nbsp;profilers, and 3&nbsp;extensions",
                                                                                                                      "actionLabel": "Learn more",
                                                                                                                      "url": "/all/",
                                                                                                                      "isUrlShouldBeLocalized": true,
                                                                                                                      "logoSrc": "/img/banners-menu-main/discount.svg",
                                                                                                                      "bgColor": "#FF318C",
                                                                                                                      "bgGradient": "linear-gradient(293.2deg, rgb(253 13 122) 13.45%, rgb(252 100 67) 73.57%, rgb(248 158 7) 100%)",
                                                                                                                      "cleaned_url": "/all/"},
                                                                                                                  {
                                                                                                                      "isActive": false,
                                                                                                                      "title": "The Total Economic Impact\u2122 of IntelliJ&nbsp;IDEA study",
                                                                                                                      "description": "Commissioned TEI research conducted by Forrester Consulting",
                                                                                                                      "actionLabel": "Learn more",
                                                                                                                      "url": "/lp/intellijidea-forrester-tei/",
                                                                                                                      "isUrlShouldBeLocalized": true,
                                                                                                                      "logoSrc": "${RESOURCES_URL_PLACEHOLDER}/storage/products/v/jb-logos/intellij-idea/intellij-idea.svg",
                                                                                                                      "bgColor": "#6B57FF",
                                                                                                                      "bgGradient": "linear-gradient(304.12deg, #087CFA -14.07%, #353535 109.22%)",
                                                                                                                      "cleaned_url": "/lp/intellijidea-forrester-tei/"}],
                                                                                                      "submenu": {
                                                                                                          "columns": [{
                                                                                                                          "title": "DEVELOPER TOOLS",
                                                                                                                          "layout": "12 12 12",
                                                                                                                          "subColumns": [
                                                                                                                              {
                                                                                                                                  "items": [
                                                                                                                                      {
                                                                                                                                          "isActive": false,
                                                                                                                                          "title": "For Individual Use",
                                                                                                                                          "url": "/store/#personal",
                                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                                          "cleaned_url": "/store/#personal"},
                                                                                                                                      {
                                                                                                                                          "isActive": false,
                                                                                                                                          "title": "For Teams and Organizations",
                                                                                                                                          "url": "/store/#commercial",
                                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                                          "cleaned_url": "/store/#commercial"},
                                                                                                                                      {
                                                                                                                                          "isActive": false,
                                                                                                                                          "title": "Special offers & programs",
                                                                                                                                          "url": "/store/#discounts",
                                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                                          "cleaned_url": "/store/#discounts"}]},
                                                                                                                              {
                                                                                                                                  "title": "SERVICES & PLUGINS",
                                                                                                                                  "items": [
                                                                                                                                      {
                                                                                                                                          "isActive": false,
                                                                                                                                          "title": "Marketplace",
                                                                                                                                          "url": "/store/plugins/",
                                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                                          "cleaned_url": "/store/plugins/"}]},
                                                                                                                              {
                                                                                                                                  "title": "LEARNING TOOLS",
                                                                                                                                  "items": [
                                                                                                                                      {
                                                                                                                                          "isActive": false,
                                                                                                                                          "title": "JetBrains Academy",
                                                                                                                                          "url": "/academy/buy/",
                                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                                          "cleaned_url": "/academy/buy/"}]}]},
                                                                                                                      {
                                                                                                                          "title": "TEAM TOOLS",
                                                                                                                          "layout": "12 12 12",
                                                                                                                          "subColumns": [
                                                                                                                              {
                                                                                                                                  "items": [
                                                                                                                                      {
                                                                                                                                          "isActive": false,
                                                                                                                                          "title": "Space",
                                                                                                                                          "url": "/store/teamware#space-store-section",
                                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                                          "cleaned_url": "/store/teamware#space-store-section"},
                                                                                                                                      {
                                                                                                                                          "isActive": false,
                                                                                                                                          "title": "TeamCity",
                                                                                                                                          "url": "/store/teamware#teamcity-store-section",
                                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                                          "cleaned_url": "/store/teamware#teamcity-store-section"},
                                                                                                                                      {
                                                                                                                                          "isActive": false,
                                                                                                                                          "title": "YouTrack",
                                                                                                                                          "url": "/store/teamware#youtrack-store-section",
                                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                                          "cleaned_url": "/store/teamware#youtrack-store-section"},
                                                                                                                                      {
                                                                                                                                          "isActive": false,
                                                                                                                                          "title": "Datalore",
                                                                                                                                          "url": "/datalore/",
                                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                                          "cleaned_url": "/datalore/"}]},
                                                                                                                              {
                                                                                                                                  "title": "COLLABORATIVE DEVELOPMENT",
                                                                                                                                  "items": [
                                                                                                                                      {
                                                                                                                                          "isActive": false,
                                                                                                                                          "title": "Code With Me",
                                                                                                                                          "url": "/code-with-me/buy/",
                                                                                                                                          "isUrlShouldBeLocalized": true,
                                                                                                                                          "cleaned_url": "/code-with-me/buy/"}]}]},
                                                                                                                      {
                                                                                                                          "title": "SALES SUPPORT",
                                                                                                                          "hasSeparator": true,
                                                                                                                          "items": [
                                                                                                                              {
                                                                                                                                  "isActive": false,
                                                                                                                                  "title": "Contact Sales",
                                                                                                                                  "url": "/support/sales/",
                                                                                                                                  "isUrlShouldBeLocalized": true,
                                                                                                                                  "cleaned_url": "/support/sales/"},
                                                                                                                              {
                                                                                                                                  "isActive": false,
                                                                                                                                  "title": "Purchase Terms",
                                                                                                                                  "url": "/legal/docs/store/terms/",
                                                                                                                                  "isUrlShouldBeLocalized": true,
                                                                                                                                  "cleaned_url": "/legal/docs/store/terms/"},
                                                                                                                              {
                                                                                                                                  "isActive": false,
                                                                                                                                  "title": "FAQ",
                                                                                                                                  "url": "https://sales.jetbrains.com/",
                                                                                                                                  "isUrlShouldBeLocalized": true,
                                                                                                                                  "cleaned_url": "https://sales.jetbrains.com/"},
                                                                                                                              {
                                                                                                                                  "isActive": false,
                                                                                                                                  "title": "Partners and Resellers",
                                                                                                                                  "url": "/company/partners/",
                                                                                                                                  "isUrlShouldBeLocalized": true,
                                                                                                                                  "cleaned_url": "/company/partners/"}]}]}},
                                        {"isActive": false, "title": "Login", "url": "https://account.jetbrains.com/",
                                         "isMobileOnly": true, "cleaned_url": "https://account.jetbrains.com/"}]},
                  "secondary": {"isActive": true, "id": "product_pycharm", "logoId": "pycharm", "url": "/pycharm/",
                                "title": "PyCharm", "items": [
                          {"isActive": false, "title": "Coming in new version", "url": "/pycharm/nextversion/",
                           "isEapItem": true, "isItemHidden": true, "eapProductId": "pycharm",
                           "cleaned_url": "/pycharm/nextversion/"},
                          {"isActive": false, "title": "What's New", "version": "2023.1", "url": "/pycharm/whatsnew/",
                           "items": [
                               {"isActive": false, "title": "What's New 2022.3", "url": "/pycharm/whatsnew/2022-3/",
                                "cleaned_url": "/pycharm/whatsnew/2022-3/"},
                               {"isActive": false, "title": "What's New 2022.2", "url": "/pycharm/whatsnew/2022-2/",
                                "cleaned_url": "/pycharm/whatsnew/2022-2/"}], "cleaned_url": "/pycharm/whatsnew/"},
                          {"isActive": false, "title": "Features", "url": "/pycharm/features/",
                           "heading": "Features overview", "items": [
                              {"isActive": false, "title": "Intelligent Coding Assistance",
                               "url": "/pycharm/features/coding_assistance.html",
                               "cleaned_url": "/pycharm/features/coding_assistance.html"},
                              {"isActive": false, "title": "Built-in Developer Tools",
                               "url": "/pycharm/features/tools.html", "cleaned_url": "/pycharm/features/tools.html"},
                              {"isActive": false, "title": "Full-stack Web Development",
                               "url": "/pycharm/features/web_development.html",
                               "cleaned_url": "/pycharm/features/web_development.html"},
                              {"isActive": false, "title": "Scientific Tools",
                               "url": "/pycharm/features/scientific_tools.html",
                               "cleaned_url": "/pycharm/features/scientific_tools.html"},
                              {"isActive": false, "title": "Customizable and Cross-platform IDE",
                               "url": "/pycharm/features/customizable_and_cross_platform_ide.html",
                               "cleaned_url": "/pycharm/features/customizable_and_cross_platform_ide.html"},
                              {"isActive": false, "title": "Python Debugger", "url": "/pycharm/features/debugger.html",
                               "cleaned_url": "/pycharm/features/debugger.html"},
                              {"isActive": false, "title": "PyCharm Editions Comparison",
                               "url": "/pycharm/features/editions_comparison_matrix.html",
                               "cleaned_url": "/pycharm/features/editions_comparison_matrix.html"}],
                           "cleaned_url": "/pycharm/features/"},
                          {"isActive": false, "title": "Learn", "url": "/pycharm/learn/",
                           "cleaned_url": "/pycharm/learn/"},
                          {"isActive": false, "title": "Pricing", "url": "/pycharm/buy/", "type": "outlineButton",
                           "cleaned_url": "/pycharm/buy/"},
                          {"isActive": false, "title": "Download", "url": "/pycharm/download/", "type": "button",
                           "cleaned_url": "/pycharm/download/"}], "cleaned_url": "/pycharm/"}};

var
is_layout_adaptive = false;
is_layout_adaptive = true;

var
disable_language_picker = false;

var
localized_domains = [{"defaultLanguage": "en", "domain": "blog.jetbrains.com",
                      "locales": {"de-de": "de", "en-us": "en", "es-es": "es", "fr-fr": "fr", "ja-jp": "ja",
                                  "ko-kr": "ko", "pt-br": "pt-br", "ru-ru": "ru", "zh-cn": "zh-hans"},
                      "pathsLocalization": false, "suffixDefault": false},
                     {"defaultLanguage": "en-us", "domain": "lp.jetbrains.com",
                      "locales": {"de-de": "de-de", "en-us": "en-us", "es-es": "es-es", "fr-fr": "fr-fr",
                                  "ja-jp": "ja-jp", "ko-kr": "ko-kr", "pt-br": "pt-br", "ru-ru": "ru-ru",
                                  "zh-cn": "zh-cn"}, "pathsLocalization": true, "suffixDefault": false},
                     {"defaultLanguage": "en-us", "domain": "sales.jetbrains.com",
                      "locales": {"de-de": "de", "en-us": "en-gb", "es-es": "es", "fr-fr": "fr", "ja-jp": "ja",
                                  "ko-kr": "ko", "pt-br": "pt-br", "ru-ru": "ru", "zh-cn": "zh-cn"},
                      "pathsLocalization": true, "prefixPath": "hc", "suffixDefault": true}];

var
english_only_url_prefixes = [];

var
is_landing_view = false;

var
theme = 'light';
< / script >

    < script > < / script >

                   < link
href = "/_assets/common.6c1e09c5b5de11d53087.css"
rel = "stylesheet"
type = "text/css" >
       < link
href = "/_assets/default-page.764a612e13a7a6454ef1.css"
rel = "stylesheet"
type = "text/css" >
       < script
src = "/_assets/common.823051bf18d546d60816.js"
type = "text/javascript" > < / script >
                               < script
src = "/_assets/default-page.674a41590f2513dd2a57.js"
type = "text/javascript" > < / script >
                               < script
src = "/_assets/pycharm/download/download-thanks.entry.cc6f090c9ad4b4f268b6.js"
type = "text/javascript" > < / script >
                               < script
src = "/_assets/pycharm/inc/social-footer/index.entry.051514680737b14e0d24.js"
type = "text/javascript" > < / script >

                               <!-- Social
Media
tag
Starts -->
< !-- Open
Graph
data -->
< meta
property = "og:title"
content = "Thank you for downloading PyCharm!" >

          < meta
property = "og:description"
content = "Intelligent Python IDE with refactorings, debugger, code completion, on-the-fly code analysis and coding productivity orientation
          ">
          < meta
property = "og:image"
content = "https://resources.jetbrains.com/storage/products/pycharm/img/meta/preview.png" >

          < meta
property = "og:site_name"
content = "JetBrains" >
          < meta
property = "og:type"
content = "website" >
          < meta
property = "og:url"
content = "https://www.jetbrains.com/pycharm/download/download-thanks.html" >
          <!-- OpenGraph
End -->

< !-- Schema.org
data -->
< script
type = "application/ld+json" >
       {"@context": "http://schema.org/", "@type": "Product", "alternateName": "JetBrains PyCharm",
        "brand": {"@type": "Brand", "name": "JetBrains"},
        "description": "PyCharm: Python IDE for Professional Developers by JetBrains",
        "image": "https://resources.jetbrains.com/storage/products/pycharm/img/meta/preview.png",
        "logo": "https://resources.jetbrains.com/storage/products/pycharm/img/meta/pycharm_logo_300x300.png",
        "name": "PyCharm",
        "offers": {"@type": "AggregateOffer", "highPrice": "19.90", "lowPrice": "8.90", "priceCurrency": "USD"},
        "releaseDate": "2021-06-02T09:00",
        "sameAs": ["https://twitter.com/pycharm", "http://www.wikidata.org/entity/Q1484375"]}
       < / script >
           < script
type = "application/ld+json" >
       {"@context": "http://schema.org", "@type": "SoftwareApplication", "applicationCategory": "DeveloperApplication",
        "author": {"@type": "Organization", "name": "JetBrains"}, "datePublished": "2021-06-02T09:00",
        "downloadUrl": "https://www.jetbrains.com/pycharm/download/",
        "image": "https://resources.jetbrains.com/storage/products/pycharm/img/meta/preview.png", "name": "PyCharm",
        "operatingSystem": "Windows, macOS, Linux", "publisher": {"@type": "Organization", "name": "JetBrains"},
        "requirements": "RAM: 2 GB, Free space: 2.5 GB, Screen Resolution: 1024x768",
        "screenshot": "https://www.jetbrains.com/pycharm/img/screenshots/simpleLook@2x.jpg",
        "softwareVersion": "2021.1", "url": "https://www.jetbrains.com/pycharm/"}
       < / script >
           < script
type = "application/ld+json" >
       {
           "@context": "http://schema.org",
           "@type": "WebPage",
           "@id": "https://www.jetbrains.com/pycharm/download/download-thanks.html#webpage",
           "url": "https://www.jetbrains.com/pycharm/download/download-thanks.html",
           "name": "Thank you for downloading PyCharm!",
           "description": "Intelligent Python IDE with refactorings, debugger, code completion, on-the-fly code analysis and coding productivity orientation",
           "image": "https://resources.jetbrains.com/storage/products/pycharm/img/meta/pycharm_1280x800.png"
       } < / script >
             <!-- Schema.org
end -->

< !-- Twitter
data -->
< meta
name = "twitter:description"
content = "Intelligent Python IDE with refactorings, debugger, code completion, on-the-fly code analysis and coding productivity orientation
          ">

          < meta
name = "twitter:title"
content = "Thank you for downloading PyCharm!" >

          < meta
name = "twitter:card"
content = "summary_large_image" >
          < meta
name = "twitter:site"
content = "@pycharm" >
          < meta
name = "twitter:creator"
content = "@pycharm" >
          < meta
name = "twitter:image:src"
content = "https://resources.jetbrains.com/storage/products/pycharm/img/meta/preview.png" >
          < meta
name = "twitter:label1"
content = "Platforms:" >
          < meta
name = "twitter:data1"
content = "Windows, macOS, Linux" >
          <!-- Twitter
End -->
< !-- Social
Media
tag
Ends -->
< script
charset = "utf-8"
src = "/_assets/904.feb5ad9b58c8f7209f8d.js" > < / script > < meta
http - equiv = "origin-trial"
content = "AymqwRC7u88Y4JPvfIF2F37QKylC04248hLCdJAsh8xgOfe/dVJPV3XS3wLFca1ZMVOtnBfVjaCMTVudWM//5g4AAAB7eyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGV0YWdtYW5hZ2VyLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjk1MTY3OTk5LCJpc1RoaXJkUGFydHkiOnRydWV9" > < script
type = "text/javascript" async=""
src = "https://googleads.g.doubleclick.net/pagead/viewthroughconversion/1071903267/?random=1685503736065&amp;cv=11&amp;fst=1685503736065&amp;bg=ffffff&amp;guid=ON&amp;async=1&amp;gtm=45He35o0&amp;u_w=1920&amp;u_h=1080&amp;url=https%3A%2F%2Fwww.jetbrains.com%2Fpycharm%2Fdownload%2Fdownload-thanks.html%3Fplatform%3Dwindows%26code%3DPCC&amp;ref=https%3A%2F%2Fwww.jetbrains.com%2Fpycharm%2Fdownload%2F&amp;hn=www.googleadservices.com&amp;frm=0&amp;tiba=Thank%20you%20for%20downloading%20PyCharm!&amp;auid=1361546107.1685503212&amp;uaa=x86&amp;uab=64&amp;uafvl=Google%2520Chrome%3B113.0.5672.127%7CChromium%3B113.0.5672.127%7CNot-A.Brand%3B24.0.0.0&amp;uamb=0&amp;uap=Windows&amp;uapv=10.0.0&amp;uaw=0&amp;rfmt=3&amp;fmt=4" > < / script > < script
type = "text/javascript" async=""
src = "//munchkin.marketo.net/munchkin.js" > < / script > < script
src = "https://bat.bing.com/p/action/5220035.js"
type = "text/javascript" async=""
data - ueto = "ueto_4073c6d9df" > < / script > < meta
http - equiv = "origin-trial"
content = "AymqwRC7u88Y4JPvfIF2F37QKylC04248hLCdJAsh8xgOfe/dVJPV3XS3wLFca1ZMVOtnBfVjaCMTVudWM//5g4AAAB7eyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGV0YWdtYW5hZ2VyLmNvbTo0NDMiLCJmZWF0dXJlIjoiUHJpdmFjeVNhbmRib3hBZHNBUElzIiwiZXhwaXJ5IjoxNjk1MTY3OTk5LCJpc1RoaXJkUGFydHkiOnRydWV9" > < / head >

                                                                                                                                                                                                                                                                                   < body


class ="body-adaptive page-color-blue wt-primary-map" style="overflow: visible;" data-new-gr-c-s-check-loaded="14.1110.0" data-gr-ext-installed="" > < svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink = "http://www.w3.org/1999/xlink"


style = "position: absolute; width: 0; height: 0"
id = "__SVG_SPRITE_NODE__" > < symbol
xmlns = "http://www.w3.org/2000/svg"
viewBox = "0 0 700 700"
id = "jetbrains-simple" > < path
d = "M0 0h700v700H0z" > < / path > < path
fill = "#fff"
d = "M60.379 568.75h262.5v43.75h-262.5zM57.428 184.315 77.8 165.083c5.542 6.682 10.758 10.594 17.929 10.594 7.823 0 12.877-5.378 12.877-15.972V87.5h31.457v72.367c0 14.343-3.586 24.448-11.246 32.109-7.5 7.5-18.254 11.572-31.294 11.572-19.885 0-31.946-8.312-40.095-19.233zM147.394 87.5h91.762v26.73h-60.468v17.44h54.763v24.937h-54.763v18.092h61.283v26.893h-92.577zM280.491 115.208h-34.064V87.5h99.911v27.708h-34.227v86.384h-31.62zM139.736 282.7c10.106-4.4 17.6-12.224 17.6-25.426v-.326A25.675 25.675 0 0 0 150 238.364c-6.682-6.52-16.788-10.106-31.131-10.106H60.362V342.35H119.2c27.218 0 43.191-11.9 43.191-31.457v-.326c.001-15.484-8.8-23.307-22.655-27.867zm-48.57-29.011h20.7c9.29 0 14.343 3.422 14.343 9.779v.326c0 6.682-5.542 9.942-15.158 9.942H91.166v-20.051zm39.607 52.808c0 6.682-5.379 10.431-15.158 10.431H91.166V295.9h24.123c10.594 0 15.484 4.075 15.484 10.269v.326zM335.8 227.444h-30.475l-42.63 101.193-17.833-26.056c14.18-6.031 23.469-17.6 23.469-35.205v-.326c0-11.246-3.422-19.885-10.1-26.567-7.661-7.661-19.722-12.224-37.162-12.224h-53.953V342.35h31.619V307.8h14.017l22.981 34.553H290l8.15-20.536h44.169l8.149 20.536h33.9zm-99.093 42.05c0 8.312-6.357 13.529-16.951 13.529h-21.02v-27.546H219.6c10.432 0 17.114 4.564 17.114 13.692v.325zm70.737 27.706 12.877-32.271 12.712 32.271zM388.119 228.258h31.619V342.35h-31.619zM427.56 228.258h29.501l46.94 60.306v-60.306h31.294V342.35H507.75l-48.896-62.587v62.587H427.56zM537.277 325.4l17.6-21.025c11.409 8.964 23.8 13.691 37 13.691 8.638 0 13.2-2.934 13.2-7.824v-.325c0-4.89-3.749-7.335-19.4-11.084-24.286-5.541-43.03-12.387-43.03-35.694v-.326c0-21.188 16.788-36.509 44.17-36.509 19.4 0 34.553 5.216 46.94 15.158l-15.801 22.328c-10.431-7.5-21.84-11.246-31.946-11.246-7.66 0-11.409 3.1-11.409 7.334v.322c0 5.216 3.912 7.5 19.885 11.083 26.078 5.7 42.377 14.18 42.377 35.531v.326c0 23.307-18.418 37.161-46.126 37.161-20.211.005-39.28-6.351-53.46-18.901z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "intellij-idea" > < defs > < linearGradient
id = "intellij-idea_intellij-idea_svg__a"
x1 = "5.174"
x2 = "40.014"
y1 = "39.889"
y2 = "38.123"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".091"
stop - color = "#FC801D" > < / stop > < stop
offset = ".231"
stop - color = "#B07F61" > < / stop > < stop
offset = ".409"
stop - color = "#577DB3" > < / stop > < stop
offset = ".533"
stop - color = "#1E7CE6" > < / stop > < stop
offset = ".593"
stop - color = "#087CFA" > < / stop > < / linearGradient > < linearGradient
id = "intellij-idea_intellij-idea_svg__b"
x1 = "61.991"
x2 = "50.158"
y1 = "36.915"
y2 = "1.557"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#FE2857" > < / stop > < stop
offset = ".078"
stop - color = "#CB3979" > < / stop > < stop
offset = ".16"
stop - color = "#9E4997" > < / stop > < stop
offset = ".247"
stop - color = "#7557B2" > < / stop > < stop
offset = ".339"
stop - color = "#5362C8" > < / stop > < stop
offset = ".436"
stop - color = "#386CDA" > < / stop > < stop
offset = ".541"
stop - color = "#2373E8" > < / stop > < stop
offset = ".658"
stop - color = "#1478F2" > < / stop > < stop
offset = ".794"
stop - color = "#0B7BF8" > < / stop > < stop
offset = "1"
stop - color = "#087CFA" > < / stop > < / linearGradient > < linearGradient
id = "intellij-idea_intellij-idea_svg__c"
x1 = "10.066"
x2 = "53.876"
y1 = "16.495"
y2 = "88.96"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#FE2857" > < / stop > < stop
offset = ".08"
stop - color = "#FE295F" > < / stop > < stop
offset = ".206"
stop - color = "#FF2D76" > < / stop > < stop
offset = ".303"
stop - color = "#FF318C" > < / stop > < stop
offset = ".385"
stop - color = "#EA3896" > < / stop > < stop
offset = ".553"
stop - color = "#B248AE" > < / stop > < stop
offset = ".792"
stop - color = "#5A63D6" > < / stop > < stop
offset = "1"
stop - color = "#087CFA" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#intellij-idea_intellij-idea_svg__a)"
d = "M11.2 49.467.7 41.3 9 26l9.5 7.5-7.3 15.967Z" > < / path > < path
fill = "#087CFA"
d = "m70 18.667-1.167 40.6L41.767 70l-14.7-9.567 14.7-22.933L70 18.667Z" > < / path > < path
fill = "url(#intellij-idea_intellij-idea_svg__b)"
d = "M70 18.667 55.5 33 37 15 48.067 1.167 70 18.667Z" > < / path > < path
fill = "url(#intellij-idea_intellij-idea_svg__c)"
d = "M27.067 60.433 5.6 68.367 10.033 52.5l5.834-19.367L0 27.767 10.033 0l23.1 2.8L54.5 31l1 2-28.433 27.433Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < g
fill = "#FFF" > < path
d = "M27.137 22.143V19.25h-7.864v2.893h2.194v9.964h-2.194v2.87h7.864v-2.87H24.92v-9.964h2.217ZM34.697 35.21c-1.237 0-2.264-.233-3.08-.7a7.355 7.355 0 0 1-2.054-1.657l2.17-2.426c.444.49.91.886 1.354 1.166.466.28.956.42 1.516.42.654 0 1.167-.21 1.54-.63.374-.42.56-1.073.56-1.983V19.273h3.547v10.29c0 .934-.117 1.75-.373 2.45-.257.7-.63 1.284-1.097 1.75-.49.49-1.073.84-1.773 1.097-.7.233-1.47.35-2.31.35ZM34.417 48.65h-15.75v2.683h15.75V48.65Z" > < / path > < / g > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "intellij-idea-ce" > < defs > < linearGradient
id = "intellij-idea-ce_intellij-idea-ce_svg__a"
x1 = "70.506"
x2 = "-11.423"
y1 = "70.462"
y2 = "-11.466"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".347"
stop - color = "#087CFA" > < / stop > < stop
offset = ".856"
stop - color = "#FE2857" > < / stop > < stop
offset = "1"
stop - color = "#FE2857" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#intellij-idea-ce_intellij-idea-ce_svg__a)"
d = "M64 6H6v58h58V6Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M27.137 22.143V19.25h-7.864v2.893h2.194v9.964h-2.194v2.87h7.864v-2.87H24.92v-9.964h2.217ZM34.697 35.21c-1.237 0-2.264-.233-3.08-.7a7.355 7.355 0 0 1-2.054-1.657l2.17-2.426c.444.49.91.886 1.354 1.166.466.28.956.42 1.516.42.654 0 1.167-.21 1.54-.63.374-.42.56-1.073.56-1.983V19.273h3.547v10.29c0 .934-.117 1.75-.373 2.45-.257.7-.63 1.284-1.097 1.75-.49.49-1.073.84-1.773 1.097-.7.233-1.47.35-2.31.35ZM34.417 48.65h-15.75v2.683h15.75V48.65Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "pycharm" > < defs > < linearGradient
id = "pycharm_pycharm_svg__a"
x1 = "24.999"
x2 = "66.656"
y1 = "27.046"
y2 = "27.046"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#21D789" > < / stop > < stop
offset = "1"
stop - color = "#07C3F2" > < / stop > < / linearGradient > < linearGradient
id = "pycharm_pycharm_svg__b"
x1 = "-24.559"
x2 = "61.22"
y1 = "59.081"
y2 = "-4.241"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".011"
stop - color = "#FCF84A" > < / stop > < stop
offset = ".112"
stop - color = "#A7EB62" > < / stop > < stop
offset = ".206"
stop - color = "#5FE077" > < / stop > < stop
offset = ".273"
stop - color = "#32DA84" > < / stop > < stop
offset = ".306"
stop - color = "#21D789" > < / stop > < stop
offset = ".577"
stop - color = "#21D789" > < / stop > < stop
offset = ".597"
stop - color = "#21D789" > < / stop > < stop
offset = ".686"
stop - color = "#20D68C" > < / stop > < stop
offset = ".763"
stop - color = "#1ED497" > < / stop > < stop
offset = ".835"
stop - color = "#19D1A9" > < / stop > < stop
offset = ".904"
stop - color = "#13CCC2" > < / stop > < stop
offset = ".971"
stop - color = "#0BC6E1" > < / stop > < stop
offset = "1"
stop - color = "#07C3F2" > < / stop > < / linearGradient > < linearGradient
id = "pycharm_pycharm_svg__c"
x1 = "9.33"
x2 = "23.637"
y1 = "77.654"
y2 = "32.76"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#21D789" > < / stop > < stop
offset = ".16"
stop - color = "#24D888" > < / stop > < stop
offset = ".298"
stop - color = "#2FD985" > < / stop > < stop
offset = ".427"
stop - color = "#41DC80" > < / stop > < stop
offset = ".552"
stop - color = "#5AE079" > < / stop > < stop
offset = ".673"
stop - color = "#7AE46F" > < / stop > < stop
offset = ".791"
stop - color = "#A1EA64" > < / stop > < stop
offset = ".904"
stop - color = "#CFF157" > < / stop > < stop
offset = "1"
stop - color = "#FCF84A" > < / stop > < / linearGradient > < linearGradient
id = "pycharm_pycharm_svg__d"
x1 = "28.275"
x2 = "59.409"
y1 = "38.623"
y2 = "-3.236"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#21D789" > < / stop > < stop
offset = ".093"
stop - color = "#23D986" > < / stop > < stop
offset = ".172"
stop - color = "#2ADE7B" > < / stop > < stop
offset = ".247"
stop - color = "#36E669" > < / stop > < stop
offset = ".271"
stop - color = "#3BEA62" > < / stop > < stop
offset = ".35"
stop - color = "#47EB61" > < / stop > < stop
offset = ".494"
stop - color = "#67ED5D" > < / stop > < stop
offset = ".686"
stop - color = "#9AF156" > < / stop > < stop
offset = ".915"
stop - color = "#E0F64D" > < / stop > < stop
offset = "1"
stop - color = "#FCF84A" > < / stop > < / linearGradient > < linearGradient
id = "pycharm_pycharm_svg__e"
x1 = "75.889"
x2 = "13.158"
y1 = "43.95"
y2 = "43.369"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".387"
stop - color = "#FCF84A" > < / stop > < stop
offset = ".463"
stop - color = "#ECF74C" > < / stop > < stop
offset = ".611"
stop - color = "#C1F451" > < / stop > < stop
offset = ".815"
stop - color = "#7EEF5A" > < / stop > < stop
offset = "1"
stop - color = "#3BEA62" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#pycharm_pycharm_svg__a)"
d = "M49 10.967 69.533 28l-7.466 14.934-12.134-3.267H39.2l9.8-28.7Z" > < / path > < path
fill = "url(#pycharm_pycharm_svg__b)"
d = "M28.467 22.167 24.5 42.933l-.467 7.234-9.8 4.433L0 56l4.2-45.267L29.867 0l15.866 10.267-17.266 11.9Z" > < / path > < path
fill = "url(#pycharm_pycharm_svg__c)"
d = "m28.467 22.167 1.866 40.366-6.3 7.467L0 56l19.6-29.4 8.867-4.433Z" > < / path > < path
fill = "url(#pycharm_pycharm_svg__d)"
d = "M54.833 19.133H30.567L52.033 0l2.8 19.133Z" > < / path > < path
fill = "url(#pycharm_pycharm_svg__e)"
d = "m70 62.533-21.467 7.234L20.3 61.833l8.167-39.666 3.266-3.034L49 17.5 47.6 35l13.767-5.367L70 62.533Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M19.133 19.133h6.417c3.733 0 6.067 2.217 6.067 5.484 0 3.616-2.8 5.483-6.417 5.483h-2.683v4.667h-3.5V19.133h.116Zm6.184 8.05c1.75 0 2.683-1.166 2.683-2.45 0-1.516-1.05-2.333-2.8-2.333h-2.683v4.783h2.8ZM33.6 27.067c0-4.434 3.267-8.167 8.167-8.167 3.033 0 4.666.933 6.3 2.333l-2.1 2.567C44.8 22.633 43.633 21.933 42 21.933c-2.567 0-4.667 2.1-4.667 4.9 0 2.8 1.867 4.9 4.667 4.9 1.867 0 2.8-.7 4.2-1.866l2.1 2.333c-1.867 1.867-3.733 2.8-6.767 2.8-4.666 0-7.933-3.5-7.933-7.933ZM34.417 48.65h-15.75v2.683h15.75V48.65Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "pycharm-ce" > < defs > < linearGradient
id = "pycharm-ce_pycharm-ce_svg__a"
x1 = "63.157"
x2 = "-9.078"
y1 = "63.192"
y2 = "-9.043"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".482"
stop - color = "#FCF84A" > < / stop > < stop
offset = ".726"
stop - color = "#21D789" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#pycharm-ce_pycharm-ce_svg__a)"
d = "M64 6H6v58h58V6Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M19.133 19.133h6.417c3.733 0 6.067 2.217 6.067 5.484 0 3.616-2.8 5.483-6.417 5.483h-2.683v4.667h-3.5V19.133h.116Zm6.184 8.05c1.75 0 2.683-1.166 2.683-2.45 0-1.516-1.05-2.333-2.8-2.333h-2.683v4.783h2.8ZM33.6 27.067c0-4.434 3.267-8.167 8.167-8.167 3.033 0 4.666.933 6.3 2.333l-2.1 2.567C44.8 22.633 43.633 21.933 42 21.933c-2.567 0-4.667 2.1-4.667 4.9 0 2.8 1.867 4.9 4.667 4.9 1.867 0 2.8-.7 4.2-1.866l2.1 2.333c-1.867 1.867-3.733 2.8-6.767 2.8-4.666 0-7.933-3.5-7.933-7.933ZM34.417 48.65h-15.75v2.683h15.75V48.65Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "rubymine" > < defs > < linearGradient
id = "rubymine_rubymine_svg__a"
x1 = "44.877"
x2 = "36.032"
y1 = "40.487"
y2 = "17.268"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#FE2857" > < / stop > < stop
offset = ".056"
stop - color = "#FE3052" > < / stop > < stop
offset = ".325"
stop - color = "#FD533B" > < / stop > < stop
offset = ".58"
stop - color = "#FC6C2A" > < / stop > < stop
offset = ".811"
stop - color = "#FC7B20" > < / stop > < stop
offset = "1"
stop - color = "#FC801D" > < / stop > < / linearGradient > < linearGradient
id = "rubymine_rubymine_svg__b"
x1 = "28.02"
x2 = "41.687"
y1 = "7.252"
y2 = "19.779"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#6B57FF" > < / stop > < stop
offset = "1"
stop - color = "#FE2857" > < / stop > < / linearGradient > < linearGradient
id = "rubymine_rubymine_svg__c"
x1 = ".306"
x2 = "45.3"
y1 = "11.212"
y2 = "68.408"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".001"
stop - color = "#6B57FF" > < / stop > < stop
offset = ".297"
stop - color = "#FE2857" > < / stop > < stop
offset = ".629"
stop - color = "#FE2857" > < / stop > < stop
offset = ".641"
stop - color = "#FE3052" > < / stop > < stop
offset = ".701"
stop - color = "#FD533B" > < / stop > < stop
offset = ".757"
stop - color = "#FC6C2A" > < / stop > < stop
offset = ".808"
stop - color = "#FC7B20" > < / stop > < stop
offset = ".85"
stop - color = "#FC801D" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#rubymine_rubymine_svg__a)"
d = "m58.188 0-19.98 7.146L22.385 0l-5.177 13.125h-3.354v38.646l48.563.437L70 13.708 58.187 0Z" > < / path > < path
fill = "url(#rubymine_rubymine_svg__b)"
d = "M57.604 25.156 25.667 6.125l31.937 37.552v-18.52Z" > < / path > < path
fill = "url(#rubymine_rubymine_svg__c)"
d = "m29.167 68.177 26.104-3.5-4.01-7.802-2.407-5.104 2.406-4.193 4.01-8.203-29.676-33.25L0 12.395v36.75L14.73 70l14.29-1.823h.147Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM34.86 19.25h3.775l4.125 6.642 4.125-6.642h3.775v15.73h-3.495V24.703l-4.405 6.712h-.07l-4.404-6.642V34.98H34.86V19.25ZM19.34 19.25h7.2c2.028 0 3.496.56 4.615 1.608.909.909 1.328 2.097 1.328 3.565v.07c0 1.259-.28 2.307-.909 3.146a5.636 5.636 0 0 1-2.447 1.748l3.846 5.593h-4.055l-3.286-4.824h-2.866v4.824H19.27V19.25h.07Zm6.991 7.62c.839 0 1.538-.21 1.958-.629.489-.42.699-.979.699-1.608v-.07c0-.769-.21-1.328-.7-1.678-.489-.35-1.118-.559-2.027-.559h-3.425v4.544h3.495Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "phpstorm" > < defs > < linearGradient
id = "phpstorm_phpstorm_svg__a"
x1 = "17.617"
x2 = "23.56"
y1 = "21.533"
y2 = "9.655"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#AF1DF5" > < / stop > < stop
offset = ".21"
stop - color = "#BC20E4" > < / stop > < stop
offset = ".63"
stop - color = "#DD29B8" > < / stop > < stop
offset = "1"
stop - color = "#FF318C" > < / stop > < / linearGradient > < linearGradient
id = "phpstorm_phpstorm_svg__b"
x1 = "2.258"
x2 = "31.498"
y1 = "48.027"
y2 = "9.401"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".02"
stop - color = "#6B57FF" > < / stop > < stop
offset = ".42"
stop - color = "#B74AF7" > < / stop > < stop
offset = ".75"
stop - color = "#FF318C" > < / stop > < / linearGradient > < linearGradient
id = "phpstorm_phpstorm_svg__c"
x1 = "53.04"
x2 = "35.657"
y1 = "47.667"
y2 = "6.426"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#293896" > < / stop > < stop
offset = ".08"
stop - color = "#3B3AA2" > < / stop > < stop
offset = ".29"
stop - color = "#6740C0" > < / stop > < stop
offset = ".49"
stop - color = "#8A44D8" > < / stop > < stop
offset = ".68"
stop - color = "#A347E9" > < / stop > < stop
offset = ".86"
stop - color = "#B249F3" > < / stop > < stop
offset = "1"
stop - color = "#B74AF7" > < / stop > < / linearGradient > < linearGradient
id = "phpstorm_phpstorm_svg__d"
x1 = "50.044"
x2 = "23.634"
y1 = "61.283"
y2 = "22.588"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".02"
stop - color = "#6B57FF" > < / stop > < stop
offset = ".78"
stop - color = "#B74AF7" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#phpstorm_phpstorm_svg__a)"
d = "M38.646 12.323 36.312 5.25 11.959 0 0 13.49l13.125 6.708 21.802 9.843 3.719-17.718Z" > < / path > < path
fill = "url(#phpstorm_phpstorm_svg__b)"
d = "m26.98 20.489-26.98-7 6.635 40.104 19.834-.073.51-33.031Z" > < / path > < path
fill = "url(#phpstorm_phpstorm_svg__c)"
d = "M18.958 25.666 34.052 12.25l9.187-8.094 17.646 3.281L70 30.041 56.875 43.093 18.958 25.666Z" > < / path > < path
fill = "url(#phpstorm_phpstorm_svg__d)"
d = "m49.948 17.063-35.73-.146 5.032 39.156.948 5.687L43.896 70 70 54.323l-20.052-37.26Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM32.97 32.76 35 30.31c1.4 1.19 2.94 1.89 4.69 1.89 1.4 0 2.31-.56 2.31-1.47v-.07c0-.91-.56-1.33-3.15-2.03-3.22-.77-5.25-1.68-5.25-4.83v-.07c0-2.87 2.31-4.76 5.53-4.76 2.31 0 4.27.7 5.88 2.03l-1.82 2.59c-1.4-.98-2.8-1.54-4.13-1.54s-2.03.63-2.03 1.4v.07c0 1.05.7 1.4 3.43 2.1 3.22.84 5.04 1.96 5.04 4.76v.07c0 3.15-2.38 4.9-5.81 4.9-2.38-.07-4.83-.91-6.72-2.59ZM19.25 19.25h6.44c3.78 0 6.02 2.24 6.02 5.46v.07c0 3.64-2.8 5.53-6.37 5.53h-2.66V35h-3.43V19.25Zm6.23 7.91c1.75 0 2.73-1.05 2.73-2.38v-.07c0-1.54-1.05-2.38-2.8-2.38h-2.66v4.83h2.73Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "goland" > < defs > < linearGradient
id = "goland_goland_svg__a"
x1 = "68.929"
x2 = "41.588"
y1 = "39.874"
y2 = "63.009"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#087CFA" > < / stop > < stop
offset = ".023"
stop - color = "#0D7BFA" > < / stop > < stop
offset = ".373"
stop - color = "#5566F9" > < / stop > < stop
offset = ".663"
stop - color = "#8A57F8" > < / stop > < stop
offset = ".881"
stop - color = "#AB4EF7" > < / stop > < stop
offset = "1"
stop - color = "#B74AF7" > < / stop > < / linearGradient > < linearGradient
id = "goland_goland_svg__b"
x1 = "24.089"
x2 = "40.706"
y1 = "21.699"
y2 = "2.794"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#087CFA" > < / stop > < stop
offset = ".023"
stop - color = "#0D7BFA" > < / stop > < stop
offset = ".373"
stop - color = "#5566F9" > < / stop > < stop
offset = ".663"
stop - color = "#8A57F8" > < / stop > < stop
offset = ".881"
stop - color = "#AB4EF7" > < / stop > < stop
offset = "1"
stop - color = "#B74AF7" > < / stop > < / linearGradient > < linearGradient
id = "goland_goland_svg__c"
x1 = "9.725"
x2 = "60.22"
y1 = "61.15"
y2 = "28.702"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#087CFA" > < / stop > < stop
offset = ".102"
stop - color = "#1598D3" > < / stop > < stop
offset = ".225"
stop - color = "#23B6AA" > < / stop > < stop
offset = ".345"
stop - color = "#2DCC8B" > < / stop > < stop
offset = ".462"
stop - color = "#35DD74" > < / stop > < stop
offset = ".572"
stop - color = "#39E767" > < / stop > < stop
offset = ".67"
stop - color = "#3BEA62" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#goland_goland_svg__a)"
d = "M61.688 27.052 70 45.572 55.708 70 38.5 42l23.188-14.948Z" > < / path > < path
fill = "#B74AF7"
d = "m44.5 44 11.208 26-22.093-7.583L44.5 44Z" > < / path > < path
fill = "url(#goland_goland_svg__b)"
d = "M49.292 19.76 44.77 0H19.615L0 30.042l5.688 13.78L0 56.438 49.292 37V19.76Z" > < / path > < path
fill = "url(#goland_goland_svg__c)"
d = "m70 14.875-29.385 6.927L0 56.438 26.25 70l20.708-21.365L70 14.875Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM18 27.224c0-4.543 3.52-8.254 8.318-8.254 2.88 0 4.543.768 6.206 2.175l-2.175 2.688c-1.216-1.024-2.303-1.6-4.159-1.6-2.56 0-4.543 2.24-4.543 4.927v.064c0 2.88 1.984 4.99 4.799 4.99 1.28 0 2.367-.32 3.263-.959v-2.24H26.19v-3.007h6.846v6.847c-1.535 1.407-3.775 2.495-6.654 2.495-4.99 0-8.382-3.455-8.382-8.126ZM34.572 27.224c0-4.543 3.52-8.254 8.446-8.254 4.863 0 8.382 3.647 8.382 8.126v.064c0 4.479-3.52 8.19-8.446 8.19-4.863 0-8.382-3.647-8.382-8.126Zm13.18 0c0-2.751-1.983-4.99-4.798-4.99s-4.735 2.239-4.735 4.926v.064c0 2.687 1.984 4.99 4.799 4.99 2.815-.063 4.735-2.239 4.735-4.99Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "webstorm" > < defs > < linearGradient
id = "webstorm_webstorm_svg__a"
x1 = "25.068"
x2 = "43.183"
y1 = "1.46"
y2 = "66.675"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".285"
stop - color = "#07C3F2" > < / stop > < stop
offset = ".941"
stop - color = "#087CFA" > < / stop > < / linearGradient > < linearGradient
id = "webstorm_webstorm_svg__b"
x1 = "30.72"
x2 = "61.365"
y1 = "9.734"
y2 = "54.671"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".14"
stop - color = "#FCF84A" > < / stop > < stop
offset = ".366"
stop - color = "#07C3F2" > < / stop > < / linearGradient > < linearGradient
id = "webstorm_webstorm_svg__c"
x1 = "61.082"
x2 = "65.106"
y1 = "15.29"
y2 = "29.544"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".285"
stop - color = "#07C3F2" > < / stop > < stop
offset = ".941"
stop - color = "#087CFA" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#webstorm_webstorm_svg__a)"
d = "M9.406 63.292 0 7.365 17.427.073l11.156 6.635L38.792 1.24l21.291 8.166L48.125 70 9.406 63.292Z" > < / path > < path
fill = "url(#webstorm_webstorm_svg__b)"
d = "M70 23.698 60.958 1.385 44.552 0 19.25 24.281l6.854 31.354 12.688 8.896L70 46.011l-7.656-14.292L70 23.698Z" > < / path > < path
fill = "url(#webstorm_webstorm_svg__c)"
d = "m56 20.344 6.344 11.375L70 23.698 64.385 9.844 56 20.344Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM34.16 19.25l-2.38 9.17-2.66-9.17h-2.66l-2.66 9.17-2.38-9.17h-3.64L22.26 35h2.94l2.59-9.1 2.52 9.1h3.01l4.48-15.75h-3.64ZM38.5 32.76l2.03-2.45c1.4 1.19 2.94 1.89 4.69 1.89 1.4 0 2.31-.56 2.31-1.47v-.07c0-.91-.56-1.33-3.15-2.03-3.15-.84-5.25-1.68-5.25-4.83v-.07c0-2.87 2.31-4.76 5.53-4.76 2.31 0 4.27.7 5.88 2.03l-1.82 2.59c-1.4-.98-2.8-1.54-4.13-1.54s-2.03.63-2.03 1.4v.07c0 1.05.7 1.4 3.43 2.1 3.22.84 5.04 1.96 5.04 4.76v.07c0 3.15-2.38 4.9-5.81 4.9-2.45-.07-4.83-.91-6.72-2.59Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "datagrip" > < defs > < linearGradient
id = "datagrip_datagrip_svg__a"
x1 = "64.084"
x2 = "66.131"
y1 = "26.335"
y2 = "44.156"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".16"
stop - color = "#21D789" > < / stop > < stop
offset = ".54"
stop - color = "#419FBC" > < / stop > < stop
offset = "1"
stop - color = "#6B57FF" > < / stop > < / linearGradient > < linearGradient
id = "datagrip_datagrip_svg__b"
x1 = "45.467"
x2 = "50.644"
y1 = "18.684"
y2 = "5.439"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#6B57FF" > < / stop > < stop
offset = ".952"
stop - color = "#21D789" > < / stop > < / linearGradient > < linearGradient
id = "datagrip_datagrip_svg__c"
x1 = "16.86"
x2 = "21.888"
y1 = "35.34"
y2 = "57.248"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#6B57FF" > < / stop > < stop
offset = ".022"
stop - color = "#685CFB" > < / stop > < stop
offset = ".281"
stop - color = "#4A91CA" > < / stop > < stop
offset = ".506"
stop - color = "#34B7A7" > < / stop > < stop
offset = ".685"
stop - color = "#26CE91" > < / stop > < stop
offset = ".797"
stop - color = "#21D789" > < / stop > < / linearGradient > < linearGradient
id = "datagrip_datagrip_svg__d"
x1 = "4.36"
x2 = "65.7"
y1 = "35.008"
y2 = "68.875"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".075"
stop - color = "#21D789" > < / stop > < stop
offset = ".887"
stop - color = "#6B57FF" > < / stop > < / linearGradient > < linearGradient
id = "datagrip_datagrip_svg__e"
x1 = "4.735"
x2 = "66.381"
y1 = "26.84"
y2 = "26.84"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".309"
stop - color = "#21D789" > < / stop > < stop
offset = ".487"
stop - color = "#59A3B2" > < / stop > < stop
offset = ".767"
stop - color = "#B74AF7" > < / stop > < stop
offset = "1"
stop - color = "#FF45ED" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#datagrip_datagrip_svg__a)"
d = "M65.552 10.865 70 39.52l-8.24 4.812L56.5 26.5l9.052-15.635Z" > < / path > < path
fill = "url(#datagrip_datagrip_svg__b)"
d = "M65.552 10.865 40.47 0l-7 5.833L45 17l20.552-6.135Z" > < / path > < path
fill = "url(#datagrip_datagrip_svg__c)"
d = "M47.323 70 11 30.5.583 62.49 47.323 70Z" > < / path > < path
fill = "url(#datagrip_datagrip_svg__d)"
d = "M54.5 45 0 32.302 47.323 70 54.5 45Z" > < / path > < path
fill = "url(#datagrip_datagrip_svg__e)"
d = "M0 .51v31.792l60.74 20.854 4.812-42.291L0 .51Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM35.8 27.224c0-4.543 3.52-8.254 8.318-8.254 2.88 0 4.543.768 6.206 2.175l-2.175 2.688c-1.216-1.024-2.303-1.6-4.159-1.6-2.56 0-4.543 2.24-4.543 4.927v.064c0 2.88 1.984 4.99 4.799 4.99 1.28 0 2.367-.32 3.263-.959v-2.24H43.99v-3.007h6.846v6.847c-1.535 1.407-3.775 2.495-6.654 2.495-4.99 0-8.382-3.455-8.382-8.126ZM18.5 19.133h6.183c5.017 0 8.4 3.355 8.4 7.75s-3.383 7.865-8.4 7.865l-6.183.115v-15.73Zm3.5 3.123v9.485h2.683c2.8 0 4.784-1.851 4.784-4.627s-1.867-4.742-4.784-4.742L22 22.256Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "clion" > < defs > < linearGradient
id = "clion_clion_svg__a"
x1 = "25.161"
x2 = "45.217"
y1 = "13.686"
y2 = "13.686"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#FF318C" > < / stop > < stop
offset = ".149"
stop - color = "#FB348C" > < / stop > < stop
offset = ".285"
stop - color = "#F03C8C" > < / stop > < stop
offset = ".416"
stop - color = "#DE4A8C" > < / stop > < stop
offset = ".543"
stop - color = "#C45D8B" > < / stop > < stop
offset = ".669"
stop - color = "#A2778B" > < / stop > < stop
offset = ".793"
stop - color = "#79958A" > < / stop > < stop
offset = ".913"
stop - color = "#49B98A" > < / stop > < stop
offset = "1"
stop - color = "#21D789" > < / stop > < / linearGradient > < linearGradient
id = "clion_clion_svg__b"
x1 = "17.131"
x2 = "6.836"
y1 = "8.883"
y2 = "77.965"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".091"
stop - color = "#21D789" > < / stop > < stop
offset = ".903"
stop - color = "#009AE5" > < / stop > < / linearGradient > < linearGradient
id = "clion_clion_svg__c"
x1 = "63.836"
x2 = "-6.583"
y1 = "6.492"
y2 = "80.865"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".091"
stop - color = "#21D789" > < / stop > < stop
offset = ".903"
stop - color = "#009AE5" > < / stop > < / linearGradient > < linearGradient
id = "clion_clion_svg__d"
x1 = "42.791"
x2 = "66.875"
y1 = "51.126"
y2 = "54.551"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".091"
stop - color = "#21D789" > < / stop > < stop
offset = ".903"
stop - color = "#009AE5" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#clion_clion_svg__a)"
d = "M20 41.5 26.688 0l15.895 8.823L20 41.5Z" > < / path > < path
fill = "url(#clion_clion_svg__b)"
d = "M26.688 39V0L6.49 12.76 0 51.48 26.688 39Z" > < / path > < path
fill = "url(#clion_clion_svg__c)"
d = "M68.615 21 59.573 2.698l-16.99 6.125-17.427 18.52L0 51.48l22.677 16.48 28.583-25.74L68.615 21Z" > < / path > < path
fill = "url(#clion_clion_svg__d)"
d = "M56.875 40.104 45.937 35l-19.14 20.234 14.692 10.974L58.99 70 70 45.062l-13.124-4.958Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65Z" > < / path > < g
fill = "#FFF" > < path
d = "M36 19.13h3.458v12.725h6.847v2.905H36V19.13ZM18 27.067c0-4.434 3.267-8.167 8.167-8.167 3.033 0 4.666.933 6.3 2.333l-2.1 2.567c-1.167-1.167-2.334-1.867-3.967-1.867-2.567 0-4.667 2.1-4.667 4.9 0 2.8 1.867 4.9 4.667 4.9 1.867 0 2.8-.7 4.2-1.866l2.1 2.333c-1.867 1.867-3.733 2.8-6.767 2.8C21.267 35 18 31.5 18 27.067Z" > < / path > < / g > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "appcode" > < defs > < linearGradient
id = "appcode_appcode_svg__a"
x1 = "30.221"
x2 = "69.796"
y1 = "63.074"
y2 = "63.074"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".194"
stop - color = "#07C3F2" > < / stop > < stop
offset = ".903"
stop - color = "#087CFA" > < / stop > < / linearGradient > < linearGradient
id = "appcode_appcode_svg__b"
x1 = "1.274"
x2 = "38.41"
y1 = "16.036"
y2 = "16.036"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".194"
stop - color = "#07C3F2" > < / stop > < stop
offset = ".903"
stop - color = "#087CFA" > < / stop > < / linearGradient > < linearGradient
id = "appcode_appcode_svg__c"
x1 = "45.876"
x2 = "11.197"
y1 = "72.222"
y2 = "23.824"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".091"
stop - color = "#21D789" > < / stop > < stop
offset = ".484"
stop - color = "#07C3F2" > < / stop > < stop
offset = ".903"
stop - color = "#087CFA" > < / stop > < / linearGradient > < / defs > < path
fill = "#087CFA"
d = "M53.52 70 70 26.323l-28.438-6.636L53.522 70Z" > < / path > < path
fill = "url(#appcode_appcode_svg__a)"
d = "M69.781 56.146 53.521 70l-23.334-5.98L42 54.5l27.781 1.646Z" > < / path > < path
fill = "url(#appcode_appcode_svg__b)"
d = "M8.75 32.083 1.24 10.792 38.427 0 29.5 21.5 8.75 32.083Z" > < / path > < path
fill = "url(#appcode_appcode_svg__c)"
d = "M61.104 40.542 50.677 22.75l.146-.146L38.427 0 0 41.49V70l69.781-13.854-8.677-15.604Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65Z" > < / path > < g
fill = "#FFF" > < path
d = "M24.8 19.13h3.125l6.67 15.63H31.05l-1.389-3.473h-6.6l-1.389 3.473H18.2l6.6-15.63Zm3.542 9.1-2.084-5.07-2.084 5.07h4.168ZM34.6 27.067c0-4.434 3.267-8.167 8.167-8.167 3.033 0 4.666.933 6.3 2.333l-2.1 2.567C45.8 22.633 44.633 21.933 43 21.933c-2.567 0-4.667 2.1-4.667 4.9 0 2.8 1.867 4.9 4.667 4.9 1.867 0 2.8-.7 4.2-1.866l2.1 2.333c-1.867 1.867-3.733 2.8-6.767 2.8-4.666 0-7.933-3.5-7.933-7.933Z" > < / path > < / g > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "rider" > < defs > < linearGradient
id = "rider_rider_svg__a"
x1 = "65.5"
x2 = "11.542"
y1 = "40.101"
y2 = "9.137"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#DD1265" > < / stop > < stop
offset = ".483"
stop - color = "#DD1265" > < / stop > < stop
offset = ".942"
stop - color = "#FDB60D" > < / stop > < / linearGradient > < linearGradient
id = "rider_rider_svg__b"
x1 = "33.416"
x2 = "54.805"
y1 = "6.112"
y2 = "65.175"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".139"
stop - color = "#087CFA" > < / stop > < stop
offset = ".476"
stop - color = "#DD1265" > < / stop > < stop
offset = ".958"
stop - color = "#087CFA" > < / stop > < / linearGradient > < linearGradient
id = "rider_rider_svg__c"
x1 = "17.395"
x2 = "33.194"
y1 = "7.934"
y2 = "64.079"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".278"
stop - color = "#DD1265" > < / stop > < stop
offset = ".968"
stop - color = "#FDB60D" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#rider_rider_svg__a)"
d = "M70 27.27 20.927 0l32.886 48.854 6.708-4.448L70 27.271Z" > < / path > < path
fill = "url(#rider_rider_svg__b)"
d = "M50.458 16.115 44.26 1.094 30.698 14.51l5.541 48.563L49.438 70 70 57.969 50.458 16.115Z" > < / path > < path
fill = "url(#rider_rider_svg__c)"
d = "M20.927 0 0 14.073l7.802 48.125 20.052 7.656 25.958-21L20.927 0Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM35.5 19.25h6.183c5.017 0 8.4 3.354 8.4 7.75 0 4.395-3.383 7.864-8.4 7.864l-6.183.116V19.25Zm3.5 3.123v9.484h2.683c2.8 0 4.784-1.85 4.784-4.626 0-2.776-1.867-4.743-4.784-4.743L39 22.373ZM19.34 19.25h7.2c2.028 0 3.496.56 4.615 1.608.909.909 1.328 2.097 1.328 3.565v.07c0 1.259-.28 2.307-.909 3.146a5.636 5.636 0 0 1-2.447 1.748l3.846 5.593h-4.055l-3.286-4.824h-2.866v4.824H19.27V19.25h.07Zm6.991 7.62c.839 0 1.538-.21 1.958-.629.489-.42.699-.979.699-1.608v-.07c0-.769-.21-1.328-.7-1.678-.489-.35-1.118-.559-2.027-.559h-3.425v4.544h3.495Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "resharper" > < defs > < linearGradient
id = "resharper_resharper_svg__a"
x1 = "34.448"
x2 = "64.631"
y1 = "70.146"
y2 = "26.155"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".016"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".4"
stop - color = "#DD1265" > < / stop > < stop
offset = "1"
stop - color = "#FDB60D" > < / stop > < / linearGradient > < linearGradient
id = "resharper_resharper_svg__b"
x1 = "1.828"
x2 = "48.825"
y1 = "53.428"
y2 = "9.226"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".016"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".661"
stop - color = "#DD1265" > < / stop > < / linearGradient > < linearGradient
id = "resharper_resharper_svg__c"
x1 = "47.598"
x2 = "48.08"
y1 = "-1.658"
y2 = "26.117"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#DD1265" > < / stop > < stop
offset = ".055"
stop - color = "#DF1961" > < / stop > < stop
offset = ".701"
stop - color = "#F46330" > < / stop > < stop
offset = "1"
stop - color = "#FC801D" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#resharper_resharper_svg__a)"
d = "M51.197 15.72 26.38 47.07 20.782 70h37.666L70 23.067 51.197 15.72Z" > < / path > < path
fill = "url(#resharper_resharper_svg__b)"
d = "M48.986 0H11.613L0 47.07h55.607L48.986 0Z" > < / path > < path
fill = "url(#resharper_resharper_svg__c)"
d = "M50.934 13.316 48.986 0l-4.204 13.316h6.152Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM36.078 31.36H34.37v-2.877h2.203l.561-3.326h-1.977v-2.876h2.472l.561-3.28h2.967l-.562 3.28h3.259l.56-3.28h2.967l-.561 3.28h1.707v2.877h-2.202l-.562 3.325h1.978v2.877H45.27l-.585 3.37H41.72l.584-3.37h-3.258l-.585 3.37h-2.966l.584-3.37Zm6.72-2.877.561-3.326H40.1l-.561 3.326h3.258ZM19 19h7.187c1.991 0 3.519.532 4.582 1.594a4.86 4.86 0 0 1 1.347 3.593v.046a4.927 4.927 0 0 1-.932 3.11 5.398 5.398 0 0 1-2.437 1.763l3.841 5.615h-4.042l-3.254-4.829H22.44l.02 4.828H19V19Zm6.962 7.635a2.872 2.872 0 0 0 1.966-.606 2.054 2.054 0 0 0 .685-1.617v-.045a2.009 2.009 0 0 0-.72-1.684 3.176 3.176 0 0 0-1.998-.561h-3.436v4.513h3.503Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "resharper-cpp" > < defs > < linearGradient
id = "resharper-cpp_resharper-cpp_svg__a"
x1 = "5.126"
x2 = "26.323"
y1 = "17.302"
y2 = "70.918"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".22"
stop - color = "#DD1265" > < / stop > < stop
offset = ".736"
stop - color = "#FF45ED" > < / stop > < stop
offset = "1"
stop - color = "#FDB60D" > < / stop > < / linearGradient > < linearGradient
id = "resharper-cpp_resharper-cpp_svg__b"
x1 = "52.282"
x2 = ".445"
y1 = "73.292"
y2 = "18.152"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".113"
stop - color = "#FDB60D" > < / stop > < stop
offset = ".509"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".765"
stop - color = "#FF45ED" > < / stop > < stop
offset = "1"
stop - color = "#FDB60D" > < / stop > < / linearGradient > < linearGradient
id = "resharper-cpp_resharper-cpp_svg__c"
x1 = "25.5"
x2 = "69.96"
y1 = "-1.93"
y2 = "51.168"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".175"
stop - color = "#FDB60D" > < / stop > < stop
offset = ".49"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".819"
stop - color = "#DD1265" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#resharper-cpp_resharper-cpp_svg__a)"
d = "m18.894 15.685-2.062 36.641L11.552 70 0 23.067l18.894-7.382Z" > < / path > < path
fill = "url(#resharper-cpp_resharper-cpp_svg__b)"
d = "M18.894 15.685 21.014 0l28.204 70H11.553l5.28-17.674 2.062-36.64Z" > < / path > < path
fill = "url(#resharper-cpp_resharper-cpp_svg__c)"
d = "M35.26 47.07H70L58.387 0H21.014L35.26 47.07Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM19 19h7.29c2.019 0 3.568.54 4.646 1.617a4.929 4.929 0 0 1 1.367 3.644v.046a4.998 4.998 0 0 1-.946 3.155 5.475 5.475 0 0 1-2.47 1.788l3.895 5.695h-4.1l-3.3-4.898h-2.893l.02 4.897H19V19Zm7.062 7.744a2.913 2.913 0 0 0 1.993-.615 2.082 2.082 0 0 0 .695-1.64v-.045a2.036 2.036 0 0 0-.73-1.709 3.22 3.22 0 0 0-2.027-.569h-3.485v4.578h3.554ZM43.872 24.263h-3.615V21.05h3.615V17.46h3.305v3.591h3.614v3.212h-3.614v3.59h-3.305v-3.59ZM36.955 32.962h-3.614v-3.211h3.614V26.16h3.305v3.59h3.614v3.212H40.26v3.592h-3.305v-3.592Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "datalore" > < defs > < linearGradient
id = "datalore_datalore_svg__a"
x1 = "21.41"
x2 = "63.882"
y1 = "17.36"
y2 = "25.844"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".242"
stop - color = "#3BEA62" > < / stop > < stop
offset = ".857"
stop - color = "#FCF84A" > < / stop > < / linearGradient > < linearGradient
id = "datalore_datalore_svg__b"
x1 = "16.862"
x2 = "57.518"
y1 = "4.912"
y2 = "66.891"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".018"
stop - color = "#3BEA62" > < / stop > < stop
offset = ".786"
stop - color = "#087CFA" > < / stop > < / linearGradient > < linearGradient
id = "datalore_datalore_svg__c"
x1 = "16.295"
x2 = "67.926"
y1 = "39.35"
y2 = "58.041"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".121"
stop - color = "#1FAEB5" > < / stop > < stop
offset = ".975"
stop - color = "#087CFA" > < / stop > < / linearGradient > < linearGradient
id = "datalore_datalore_svg__d"
x1 = "1.435"
x2 = "68.11"
y1 = "42.252"
y2 = "12.633"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".121"
stop - color = "#1FAEB5" > < / stop > < stop
offset = ".856"
stop - color = "#FCF84A" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#datalore_datalore_svg__a)"
d = "M64.977 8.3c-.803-.437-1.896-.8-2.771-.946-.584 0-37.842-7.13-39.81-7.275-.948-.072-1.97 0-2.917.146C2.2 2.77-2.176 23.795 12.115 32.597c3.354 2.037 7.364 2.764 11.228 1.891 6.781-1.455 37.259-8.948 39.227-9.384 8.458-1.819 10.281-12.658 2.407-16.804Z" > < / path > < path
fill = "url(#datalore_datalore_svg__b)"
d = "M65.341 40.671C63.883 38.998 37.49 9.1 31.874 4.226c-1.093-.946-2.406-1.819-3.864-2.62A13.9 13.9 0 0 0 19.48.153C3.875 2.552-1.229 19.939 8.47 29.759c1.02 1.092 30.04 33.245 30.33 33.609 1.313 1.6 2.917 3.128 4.959 4.365 3.354 2.11 7.437 2.764 11.374 1.891 14.291-3.2 18.885-19.277 10.208-28.953Z" > < / path > < path
fill = "url(#datalore_datalore_svg__c)"
d = "M59.8 36.452c-.583-.29-1.167-.582-1.823-.8-.51-.146-39.737-12.512-40.612-12.73a11.48 11.48 0 0 0-4.448-.219c-14 2.037-17.572 19.132-5.979 26.334C9.636 50.71 45.436 68.606 46.384 68.97a15.326 15.326 0 0 0 8.676.582c16.77-3.637 20.197-25.024 4.74-33.099Z" > < / path > < path
fill = "url(#datalore_datalore_svg__d)"
d = "M64.977 8.3c-1.313-.728-2.844-.946-4.375-.728-.802.146-1.531.291-2.26.582C54.915 9.536 10 23.285 8.76 23.867c-10.427 4.51-12.103 18.768-1.823 25.17a12.25 12.25 0 0 0 9.187 1.528c1.24-.291 2.48-.655 3.5-1.164 5.541-2.619 44.987-24.88 45.79-25.316 5.905-3.419 6.415-12.148-.438-15.785Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65Z" > < / path > < g
fill = "#FFF" > < path
d = "M36 19.13h3.458v12.725h6.847v2.905H36V19.13ZM18.67 19.13h6.086c4.91 0 8.3 3.389 8.3 7.746v.069c0 4.426-3.39 7.815-8.3 7.815H18.67V19.13Zm3.458 3.112v9.406h2.628c2.836 0 4.703-1.867 4.703-4.634v-.069c0-2.766-1.867-4.703-4.703-4.703h-2.628Z" > < / path > < / g > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
viewBox = "0 0 60 60"
id = "kotlin" > < radialGradient
id = "kotlin_kotlin_svg__a"
cx = "240.403"
cy = "-23.657"
r = "81.297"
gradientTransform = "matrix(.8455 0 0 -.8455 -145.249 -17.54)"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".003"
stop - color = "#e44857" > < / stop > < stop
offset = ".469"
stop - color = "#c711e1" > < / stop > < stop
offset = "1"
stop - color = "#7f52ff" > < / stop > < / radialGradient > < path
fill = "url(#kotlin_kotlin_svg__a)"
d = "M60 60H0V0h60L29.4 29.6z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "youtrack" > < defs > < linearGradient
id = "youtrack_youtrack_svg__a"
x1 = "7.088"
x2 = "64.122"
y1 = "54.736"
y2 = "28.739"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#905CFB" > < / stop > < stop
offset = ".165"
stop - color = "#6677F8" > < / stop > < stop
offset = ".378"
stop - color = "#3596F5" > < / stop > < stop
offset = ".54"
stop - color = "#17A9F3" > < / stop > < stop
offset = ".632"
stop - color = "#0CB0F2" > < / stop > < / linearGradient > < linearGradient
id = "youtrack_youtrack_svg__b"
x1 = "30.319"
x2 = "1.071"
y1 = "28.108"
y2 = "2.276"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#905CFB" > < / stop > < stop
offset = ".072"
stop - color = "#A554E6" > < / stop > < stop
offset = ".252"
stop - color = "#D641B5" > < / stop > < stop
offset = ".39"
stop - color = "#F43597" > < / stop > < stop
offset = ".468"
stop - color = "#FF318C" > < / stop > < / linearGradient > < linearGradient
id = "youtrack_youtrack_svg__c"
x1 = "4.988"
x2 = "74.041"
y1 = "58.67"
y2 = "15.161"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#905CFB" > < / stop > < stop
offset = ".165"
stop - color = "#6677F8" > < / stop > < stop
offset = ".378"
stop - color = "#3596F5" > < / stop > < stop
offset = ".54"
stop - color = "#17A9F3" > < / stop > < stop
offset = ".632"
stop - color = "#0CB0F2" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#youtrack_youtrack_svg__a)"
d = "M66.916 47.482c-.2-.2-13.102-12.603-13.102-12.603s9.801-10.402 12.402-13.003c.525-.525 1.41-1.6 2-2.6 3.6-6.102 1.5-13.903-4.6-17.504-4.501-2.6-10.102-2.2-14.103.8-.7.5-1.3 1-1.9 1.6-.3.4-13.903 12.803-25.705 23.606L44.012 41.78 20.808 67.887c-1.4 1-2.8 1.6-4.301 1.9.3 0 1.2.1 1.5 0 4.601-.7 43.208-7.402 45.108-7.802 2.3-.4 4.401-1.8 5.701-3.9 2.2-3.601 1.2-8.102-1.9-10.603Z" > < / path > < path
fill = "url(#youtrack_youtrack_svg__b)"
d = "M45.912 30.478c-.4-2.7-1.8-4.901-3.8-6.501-2.101-1.6-18.304-18.404-20.104-20.305-2.8-2.7-6.801-4.2-10.902-3.5C4.105 1.171-.796 7.772.304 14.774c.5 3.5 2.5 6.501 5.1 8.402 2.601 2 23.005 16.003 24.305 17.003 2.1 1.6 4.901 2.5 7.702 2 5.5-1 9.401-6.2 8.501-11.702Z" > < / path > < path
fill = "url(#youtrack_youtrack_svg__c)"
d = "M23.008 67.787c.1 0 23.304-26.106 23.304-26.106L22.908 26.877C14.606 34.48 6.905 41.381 5.105 43.081c-1.1 1-2.2 2.3-3 3.7a15.398 15.398 0 0 0 5.6 21.106c3 1.7 9.802 3.8 15.303-.1Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM24.774 34.73h3.46v-6.27L34.28 19h-3.933l-3.82 6.314L22.774 19H18.73l6.044 9.528v6.202ZM36.414 19v3.19H41.2V34.73h3.46V22.191h4.786V19H36.414Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "upsource" > < defs > < linearGradient
id = "upsource_upsource_svg__a"
x1 = "65.007"
x2 = "17.554"
y1 = "11.017"
y2 = "18.131"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#FF8200" > < / stop > < stop
offset = ".973"
stop - color = "#905CFB" > < / stop > < / linearGradient > < linearGradient
id = "upsource_upsource_svg__b"
x1 = "15.714"
x2 = "20.142"
y1 = "34.846"
y2 = "10.126"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#0CB0F2" > < / stop > < stop
offset = ".973"
stop - color = "#905CFB" > < / stop > < / linearGradient > < linearGradient
id = "upsource_upsource_svg__c"
x1 = "58.422"
x2 = "27.024"
y1 = "53.741"
y2 = "38.414"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#0CB0F2" > < / stop > < stop
offset = ".973"
stop - color = "#905CFB" > < / stop > < / linearGradient > < linearGradient
id = "upsource_upsource_svg__d"
x1 = "60.768"
x2 = "7.377"
y1 = "56.136"
y2 = "36.95"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#0CB0F2" > < / stop > < stop
offset = ".973"
stop - color = "#905CFB" > < / stop > < / linearGradient > < linearGradient
id = "upsource_upsource_svg__e"
x1 = "64.288"
x2 = "18.549"
y1 = "5.933"
y2 = "42.779"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#FF8200" > < / stop > < stop
offset = ".973"
stop - color = "#905CFB" > < / stop > < / linearGradient > < linearGradient
id = "upsource_upsource_svg__f"
x1 = "30.505"
x2 = "2.287"
y1 = "49.31"
y2 = "39.287"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#0CB0F2" > < / stop > < stop
offset = ".973"
stop - color = "#905CFB" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#upsource_upsource_svg__a)"
d = "M60.59 24.027 9.633 26.93l-.3-19.53L55.283.188l5.306 23.838Z" > < / path > < path
fill = "url(#upsource_upsource_svg__b)"
d = "m20.345 43.258 16.418-20.834-17.82-12.22C15.84 7.4 11.135 6.2 6.33 8.203a9.843 9.843 0 0 0-5.306 5.308c-2.102 5.008-.8 9.916 2.403 12.92l16.919 16.828Z" > < / path > < path
fill = "url(#upsource_upsource_svg__c)"
d = "m20.345 43.258 25.228 24.94L61.29 38.85 36.763 22.424 20.345 43.258Z" > < / path > < path
fill = "url(#upsource_upsource_svg__d)"
d = "m53.982 36.647-41.946-2.003c-1.602-.3-3.404-.2-5.306.6-1.802.802-3.204 2.104-3.905 3.907-2.102 4.908.4 9.615 4.505 11.218l37.542 17.728c.5.3 3.004 1.002 3.004 1.002 2.002.6 4.204.901 6.206.901 2.503 0 5.306-.701 8.11-2.103 2.602-1.302 4.204-3.406 5.606-6.01C69.499 58.882 70 56.077 70 53.273c-.1-8.713-7.308-16.025-16.018-16.626Z" > < / path > < path
fill = "url(#upsource_upsource_svg__e)"
d = "M52.18 1.09c-.7.3-1.401.701-2.002 1.102L26.952 19.72l11.513 16.827 25.228-14.123c1.902-.901 3.404-2.504 4.305-4.307C73.604 7.3 63.192-3.517 52.18 1.09Z" > < / path > < path
fill = "#905CFB"
d = "m14.538 49.868 23.927-13.321L26.952 19.72 4.928 36.246l9.61 13.622Z" > < / path > < path
fill = "url(#upsource_upsource_svg__f)"
d = "M20.445 56.479V35.045l-8.41-.401c-1.601-.3-3.403-.2-5.305.6-1.802.802-3.204 2.104-3.905 3.907-2.102 4.908.4 9.615 4.505 11.218h.1l13.015 6.11Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM19 27.99V19h3.462v8.9c0 2.564 1.281 3.89 3.394 3.89 2.113 0 3.394-1.281 3.394-3.777V19h3.461v8.878c0 4.766-2.674 7.103-6.9 7.103-4.225 0-6.81-2.36-6.81-6.99ZM35.908 19h6.428c3.753 0 6.024 2.226 6.024 5.44v.045c0 3.641-2.832 5.529-6.36 5.529h-2.63v4.72h-3.462V19Zm6.203 7.935c1.732 0 2.743-1.034 2.743-2.383v-.045c0-1.55-1.08-2.383-2.81-2.383H39.37v4.811h2.742Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "teamcity" > < defs > < linearGradient
id = "teamcity_teamcity_svg__a"
x1 = "1.774"
x2 = "40.157"
y1 = "31.349"
y2 = "31.349"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#905CFB" > < / stop > < stop
offset = ".068"
stop - color = "#776CF9" > < / stop > < stop
offset = ".173"
stop - color = "#5681F7" > < / stop > < stop
offset = ".286"
stop - color = "#3B92F5" > < / stop > < stop
offset = ".41"
stop - color = "#269FF4" > < / stop > < stop
offset = ".547"
stop - color = "#17A9F3" > < / stop > < stop
offset = ".711"
stop - color = "#0FAEF2" > < / stop > < stop
offset = ".968"
stop - color = "#0CB0F2" > < / stop > < / linearGradient > < linearGradient
id = "teamcity_teamcity_svg__b"
x1 = "5.31"
x2 = "69.206"
y1 = "9.754"
y2 = "43.948"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#905CFB" > < / stop > < stop
offset = ".068"
stop - color = "#776CF9" > < / stop > < stop
offset = ".173"
stop - color = "#5681F7" > < / stop > < stop
offset = ".286"
stop - color = "#3B92F5" > < / stop > < stop
offset = ".41"
stop - color = "#269FF4" > < / stop > < stop
offset = ".547"
stop - color = "#17A9F3" > < / stop > < stop
offset = ".711"
stop - color = "#0FAEF2" > < / stop > < stop
offset = ".968"
stop - color = "#0CB0F2" > < / stop > < / linearGradient > < linearGradient
id = "teamcity_teamcity_svg__c"
x1 = "-19.279"
x2 = "55.965"
y1 = "70.878"
y2 = "33.248"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#3BEA62" > < / stop > < stop
offset = ".117"
stop - color = "#31DE80" > < / stop > < stop
offset = ".302"
stop - color = "#24CEA8" > < / stop > < stop
offset = ".484"
stop - color = "#1AC1C9" > < / stop > < stop
offset = ".659"
stop - color = "#12B7DF" > < / stop > < stop
offset = ".824"
stop - color = "#0EB2ED" > < / stop > < stop
offset = ".968"
stop - color = "#0CB0F2" > < / stop > < / linearGradient > < linearGradient
id = "teamcity_teamcity_svg__d"
x1 = "38.935"
x2 = "5.434"
y1 = "5.937"
y2 = "77.57"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#3BEA62" > < / stop > < stop
offset = ".094"
stop - color = "#2FDB87" > < / stop > < stop
offset = ".196"
stop - color = "#24CEA8" > < / stop > < stop
offset = ".306"
stop - color = "#1BC3C3" > < / stop > < stop
offset = ".426"
stop - color = "#14BAD8" > < / stop > < stop
offset = ".56"
stop - color = "#10B5E7" > < / stop > < stop
offset = ".719"
stop - color = "#0DB1EF" > < / stop > < stop
offset = ".968"
stop - color = "#0CB0F2" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#teamcity_teamcity_svg__a)"
d = "m39.691 47.968-6.098-33.985c-.4-2.399-1.2-4.797-2.7-7.096-2-3.199-5.199-5.398-8.798-6.298C7.898-2.809-2.599 11.385 3.6 23.98l14.797 31.686c.4 1 1 2 1.7 2.899 1.2 1.6 2.799 2.798 4.699 3.398 9.597 2.999 17.296-5.497 14.896-13.994Z" > < / path > < path
fill = "url(#teamcity_teamcity_svg__b)"
d = "M67.385 26.578a12.86 12.86 0 0 0-5.699-4.898L25.495 1.789c-1-.5-2.1-1-3.3-1.3C6.7-3.109-4.399 13.883 5.5 27.078c1.5 1.999 3.6 3.598 5.999 4.498l36.491 16.392c.8.5 1.6.8 2.5 1.1 13.997 4.398 24.594-10.395 16.896-22.49Z" > < / path > < path
fill = "url(#teamcity_teamcity_svg__c)"
d = "M67.385 26.578c-1.8-2.799-4.599-4.798-7.898-5.598-3.5-.8-6.799-.5-9.598.7L11.398 36.173s-.2.1-.6.4C.9 40.472-3.999 53.366 4 64.061c1.8 2.4 4.299 4.198 7.098 4.998 5.299 1.6 10.098 1 13.997-1.1h.1l37.591-20.09.1-.1c6.599-3.799 9.698-13.095 4.5-21.191Z" > < / path > < path
fill = "url(#teamcity_teamcity_svg__d)"
d = "M50.289 12.884c1.2-2.699 1.1-5.997-.9-8.996-1.1-1.8-2.9-2.999-4.899-3.499-4.499-1.1-8.298 1-10.098 4.199L3.5 42.07v.1c-4.4 5.797-5.1 14.394.5 21.89 1.8 2.4 4.298 4.198 7.098 4.998 10.497 3.299 19.295-2.499 22.095-10.795l17.096-45.38Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM23.783 22.19H19v-3.188h13.024v3.189h-4.783v12.53h-3.458V22.19ZM33.324 26.906v-.044a7.99 7.99 0 0 1 8.196-8.13c2.964 0 4.738.989 6.198 2.425l-2.201 2.538c-1.213-1.1-2.447-1.774-4.02-1.774-2.649 0-4.558 2.201-4.558 4.896v.044c0 2.695 1.864 4.94 4.558 4.94 1.797 0 2.897-.718 4.132-1.84l2.2 2.223a8.036 8.036 0 0 1-6.444 2.807 7.932 7.932 0 0 1-8.061-8.085" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
viewBox = "0 0 60 60"
id = "space" > < linearGradient
id = "space_space_svg__a"
x1 = "27.048"
x2 = "33.312"
y1 = "62.824"
y2 = "3.448"
gradientTransform = "matrix(1 0 0 -1 0 62)"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#fcf84a" > < / stop > < stop
offset = ".32"
stop - color = "#abe682" > < / stop > < stop
offset = ".79"
stop - color = "#36cdd2" > < / stop > < stop
offset = "1"
stop - color = "#07c3f2" > < / stop > < / linearGradient > < linearGradient
id = "space_space_svg__b"
x1 = "4.068"
x2 = "60.246"
y1 = "61.892"
y2 = "35.243"
gradientTransform = "matrix(1 0 0 -1 0 62)"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#3bea62" > < / stop > < stop
offset = "1"
stop - color = "#087cfa" > < / stop > < / linearGradient > < linearGradient
id = "space_space_svg__c"
x1 = "9.217"
x2 = "65.779"
y1 = "3.879"
y2 = "43.473"
gradientTransform = "matrix(1 0 0 -1 0 62)"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#009ae5" > < / stop > < stop
offset = ".18"
stop - color = "#0490dd" > < / stop > < stop
offset = ".49"
stop - color = "#1073c6" > < / stop > < stop
offset = ".89"
stop - color = "#2346a1" > < / stop > < stop
offset = "1"
stop - color = "#293896" > < / stop > < / linearGradient > < g
fill - rule = "evenodd" > < path
fill = "url(#space_space_svg__a)"
d = "M10.862 60A59.955 59.955 0 0 0 60 25.6 60.003 60.003 0 0 0 10.862 0C9.118 0 7.366.072 5.614.232A59.998 59.998 0 0 0 10.862 60z" > < / path > < path
fill = "url(#space_space_svg__b)"
d = "M5.67.232A70.659 70.659 0 0 1 37.239 25.6H60A59.811 59.811 0 0 0 10.926 0Q8.31 0 5.67.232z" > < / path > < path
fill = "url(#space_space_svg__c)"
d = "M37.247 25.6C34.503 43.704 10.862 60 10.862 60 32.35 57.96 51.2 45.08 60 25.6z" > < / path > < / g > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
viewBox = "0 0 32 32"
id = "toolbox" > < defs > < linearGradient
id = "toolbox_toolbox_svg__a"
x1 = "2.18"
x2 = "30.041"
y1 = "23.255"
y2 = "8.782"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".043"
stop - color = "#ff8618" > < / stop > < stop
offset = ".382"
stop - color = "#ff246e" > < / stop > < stop
offset = ".989"
stop - color = "#af1df5" > < / stop > < / linearGradient > < / defs > < path
fill = "#fff"
d = "m26 22.471-6.83 3.831v-3.044L26 19.427v3.044Z" > < / path > < path
fill = "#000001"
d = "m16 32.076 14-8.011V8.057l-14 8.01v16.009z" > < / path > < path
fill = "#fff"
d = "M18.925 24.641v2.4l6.101-3.491v-2.4l-6.101 3.491z" > < / path > < path
fill = "url(#toolbox_toolbox_svg__a)"
d = "M16 .076 2 8.057v16.008l14 8.011V16.067l14-8.01L16 .076z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "pycharm-edu" > < defs > < linearGradient
id = "pycharm-edu_pycharm-edu_svg__a"
x1 = "63.27"
x2 = "-9.065"
y1 = "63.27"
y2 = "-9.063"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".482"
stop - color = "#21D789" > < / stop > < stop
offset = ".726"
stop - color = "#FCF84A" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#pycharm-edu_pycharm-edu_svg__a)"
d = "M64 6H6v58h58V6Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M19.133 19.133h6.417c3.733 0 6.067 2.217 6.067 5.484 0 3.616-2.8 5.483-6.417 5.483h-2.683v4.667h-3.5V19.133h.116Zm6.184 8.05c1.75 0 2.683-1.166 2.683-2.45 0-1.516-1.05-2.333-2.8-2.333h-2.683v4.783h2.8ZM45.792 19.13v3.07H37.42v3.21h7.466v3.07H37.42v3.21h8.583v3.07H34V19.13h11.792ZM34.417 48.65h-15.75v2.683h15.75V48.65Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "intellij-idea-edu" > < defs > < linearGradient
id = "intellij-idea-edu_intellij-idea-edu_svg__a"
x1 = "70.506"
x2 = "-11.423"
y1 = "70.462"
y2 = "-11.466"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".347"
stop - color = "#087CFA" > < / stop > < stop
offset = ".856"
stop - color = "#FE2857" > < / stop > < stop
offset = "1"
stop - color = "#FE2857" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#intellij-idea-edu_intellij-idea-edu_svg__a)"
d = "M64 6H6v58h58V6Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M27.137 22.143V19.25h-7.864v2.893h2.194v9.964h-2.194v2.87h7.864v-2.87H24.92v-9.964h2.217ZM43.868 19.25v3.09H35.44v3.23h7.514v3.09H35.44v3.23h8.637v3.09H32V19.25h11.868ZM34.417 48.65h-15.75v2.683h15.75V48.65Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
xmlns: xlink = "http://www.w3.org/1999/xlink"
viewBox = "0 0 140 140"
id = "mps" > < defs > < linearGradient
id = "mps_mps_svg__a"
x1 = "105.979"
x2 = "-27.244"
y1 = "186.085"
y2 = "15.44"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".091"
stop - color = "#0b8fff" > < / stop > < stop
offset = ".208"
stop - color = "#0d94f6" > < / stop > < stop
offset = ".396"
stop - color = "#11a3de" > < / stop > < stop
offset = ".633"
stop - color = "#18bbb7" > < / stop > < stop
offset = ".871"
stop - color = "#21d789" > < / stop > < / linearGradient > < linearGradient
xlink: href = "#mps_mps_svg__a"
id = "mps_mps_svg__b"
x1 = "178.605"
x2 = "45.382"
y1 = "129.386"
y2 = "-41.259" > < / linearGradient > < linearGradient
id = "mps_mps_svg__c"
x1 = "78.586"
x2 = "126.297"
y1 = "105.516"
y2 = "-22.788"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".123"
stop - color = "#21d789" > < / stop > < stop
offset = ".132"
stop - color = "#27d788" > < / stop > < stop
offset = ".216"
stop - color = "#59d87b" > < / stop > < stop
offset = ".303"
stop - color = "#85d970" > < / stop > < stop
offset = ".394"
stop - color = "#abda67" > < / stop > < stop
offset = ".487"
stop - color = "#cadb5f" > < / stop > < stop
offset = ".585"
stop - color = "#e1db59" > < / stop > < stop
offset = ".688"
stop - color = "#f2dc55" > < / stop > < stop
offset = ".802"
stop - color = "#fcdc53" > < / stop > < stop
offset = ".946"
stop - color = "#ffdc52" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#mps_mps_svg__a)"
d = "M0 140h140L70 70 0 0v140z" > < / path > < path
fill = "url(#mps_mps_svg__b)"
d = "M140 140 70 70l70-70v140z" > < / path > < path
fill = "url(#mps_mps_svg__c)"
d = "M102 102 70 70l70-70-38 102z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "hub" > < defs > < linearGradient
id = "hub_hub_svg__a"
x1 = "29.736"
x2 = "37.755"
y1 = "21.074"
y2 = "40.961"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".146"
stop - color = "#07C3F2" > < / stop > < stop
offset = "1"
stop - color = "#6B57FF" > < / stop > < / linearGradient > < linearGradient
id = "hub_hub_svg__b"
x1 = "24.848"
x2 = "33.188"
y1 = "59.999"
y2 = "17.335"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".092"
stop - color = "#FCF84A" > < / stop > < stop
offset = ".456"
stop - color = "#6B57FF" > < / stop > < stop
offset = ".761"
stop - color = "#6B57FF" > < / stop > < stop
offset = ".833"
stop - color = "#5074FC" > < / stop > < stop
offset = ".989"
stop - color = "#0CBDF3" > < / stop > < stop
offset = "1"
stop - color = "#07C3F2" > < / stop > < / linearGradient > < linearGradient
id = "hub_hub_svg__c"
x1 = "64.215"
x2 = "2.576"
y1 = "49.204"
y2 = "56.588"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#FCF84A" > < / stop > < stop
offset = ".5"
stop - color = "#6B57FF" > < / stop > < stop
offset = "1"
stop - color = "#07C3F2" > < / stop > < / linearGradient > < / defs > < path
fill = "#FCF84A"
d = "M67.79 55.645 56.221 67.868a6.732 6.732 0 0 1-9.81-.035 6.72 6.72 0 0 1-.645-8.364l9.459-13.916a8.09 8.09 0 0 1 11.06-2.258 8.077 8.077 0 0 1 1.503 12.35Z" > < / path > < path
fill = "#07C3F2"
d = "m56.822 25.866-46.449-.835a10.544 10.544 0 0 1-9.927-7.564A10.539 10.539 0 0 1 9.668 3.994L55.956.054a12.939 12.939 0 0 1 13.627 9.65 12.933 12.933 0 0 1-12.761 16.162Z" > < / path > < path
fill = "url(#hub_hub_svg__a)"
d = "M6.066 66.995a14.711 14.711 0 0 1-1.351-22.553L48.177 3.52a12.943 12.943 0 0 1 16.634-.933 12.921 12.921 0 0 1 1.658 19.202L25.54 65.242a14.736 14.736 0 0 1-19.475 1.753Z" > < / path > < path
fill = "url(#hub_hub_svg__b)"
d = "M46.414 67.887 2.867 21.667a10.53 10.53 0 0 1 .787-15.198A10.548 10.548 0 0 1 19.03 8.194L56.72 59.296a6.715 6.715 0 0 1-.528 8.602 6.726 6.726 0 0 1-9.78-.011Z" > < / path > < path
fill = "url(#hub_hub_svg__c)"
d = "M63.855 58.048 18.44 69.421A14.755 14.755 0 0 1 .177 53.553a14.755 14.755 0 0 1 15.212-13.175l46.789 1.703a8.11 8.11 0 0 1 7.818 8.083 8.109 8.109 0 0 1-6.141 7.884Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM19 19h3.46v6.224h6.382V19h3.461v15.73h-3.46v-6.314H22.46v6.314H19V19ZM35.687 19h7.303c1.797 0 3.213.494 4.112 1.393a3.606 3.606 0 0 1 1.079 2.674v.045a3.658 3.658 0 0 1-2.067 3.393c1.82.697 2.943 1.753 2.943 3.865v.045c0 2.877-2.337 4.315-5.887 4.315h-7.483V19Zm9.056 4.652c0-1.034-.81-1.619-2.27-1.619h-3.416v3.326h3.191c1.528 0 2.495-.494 2.495-1.662v-.045Zm-1.686 4.584h-4v3.46h4.113c1.528 0 2.449-.539 2.449-1.708v-.045c0-1.056-.787-1.707-2.562-1.707Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "dottrace" > < defs > < linearGradient
id = "dottrace_dottrace_svg__a"
x1 = "-1.332"
x2 = "67.042"
y1 = "43.737"
y2 = "26.097"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".123"
stop - color = "#6B57FF" > < / stop > < stop
offset = ".538"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".854"
stop - color = "#DD1265" > < / stop > < / linearGradient > < linearGradient
id = "dottrace_dottrace_svg__b"
x1 = "45.915"
x2 = "67.658"
y1 = "38.91"
y2 = "9.099"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".192"
stop - color = "#DD1265" > < / stop > < stop
offset = ".295"
stop - color = "#DE146A" > < / stop > < stop
offset = ".411"
stop - color = "#E21977" > < / stop > < stop
offset = ".533"
stop - color = "#E7218E" > < / stop > < stop
offset = ".659"
stop - color = "#EF2DAD" > < / stop > < stop
offset = ".788"
stop - color = "#F93CD5" > < / stop > < stop
offset = ".853"
stop - color = "#FF45ED" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#dottrace_dottrace_svg__a)"
d = "M67.306 16.027 43.746 0 0 31.07 11.085 70l47.816-9.696 8.405-44.277Z" > < / path > < path
fill = "url(#dottrace_dottrace_svg__b)"
d = "M67.307 16.027 43.747 0 37.95 15.72v32.05H70l-2.693-31.743Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM19 19.002h6.134c4.943 0 8.358 3.392 8.358 7.818v.045c0 4.427-3.415 7.864-8.358 7.864H19V19.002Zm3.46 3.123v9.481h2.674c2.83 0 4.74-1.91 4.74-4.696v-.045a4.519 4.519 0 0 0-4.74-4.74H22.46ZM39.983 22.174h-4.79V18.98h13.044v3.194h-4.79v12.55h-3.465v-12.55Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "dotpeek" > < defs > < linearGradient
id = "dotpeek_dotpeek_svg__a"
x1 = "7.045"
x2 = "40.658"
y1 = "35.829"
y2 = "70.142"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".097"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".113"
stop - color = "#F846EE" > < / stop > < stop
offset = ".284"
stop - color = "#AC4FF7" > < / stop > < stop
offset = ".406"
stop - color = "#7D55FD" > < / stop > < stop
offset = ".466"
stop - color = "#6B57FF" > < / stop > < stop
offset = ".48"
stop - color = "#655DFE" > < / stop > < stop
offset = ".572"
stop - color = "#4482FA" > < / stop > < stop
offset = ".664"
stop - color = "#299EF6" > < / stop > < stop
offset = ".756"
stop - color = "#16B3F4" > < / stop > < stop
offset = ".847"
stop - color = "#0BBFF2" > < / stop > < stop
offset = ".935"
stop - color = "#07C3F2" > < / stop > < / linearGradient > < linearGradient
id = "dotpeek_dotpeek_svg__b"
x1 = "9.563"
x2 = "34.109"
y1 = "55.827"
y2 = "35.372"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".043"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".046"
stop - color = "#FE45ED" > < / stop > < stop
offset = ".201"
stop - color = "#D14BF3" > < / stop > < stop
offset = ".357"
stop - color = "#AC4FF7" > < / stop > < stop
offset = ".512"
stop - color = "#9053FB" > < / stop > < stop
offset = ".666"
stop - color = "#7B55FD" > < / stop > < stop
offset = ".818"
stop - color = "#6F57FF" > < / stop > < stop
offset = ".968"
stop - color = "#6B57FF" > < / stop > < / linearGradient > < linearGradient
id = "dotpeek_dotpeek_svg__c"
x1 = "39.855"
x2 = "56.355"
y1 = "16.927"
y2 = "50.653"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".199"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".286"
stop - color = "#F646EE" > < / stop > < stop
offset = ".429"
stop - color = "#DD49F1" > < / stop > < stop
offset = ".609"
stop - color = "#B64EF6" > < / stop > < stop
offset = ".818"
stop - color = "#7F55FD" > < / stop > < stop
offset = ".887"
stop - color = "#6B57FF" > < / stop > < / linearGradient > < linearGradient
id = "dotpeek_dotpeek_svg__d"
x1 = "19.875"
x2 = "61.328"
y1 = "18.305"
y2 = "8.256"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".097"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".17"
stop - color = "#F64AED" > < / stop > < stop
offset = ".29"
stop - color = "#DD56EE" > < / stop > < stop
offset = ".441"
stop - color = "#B56AEE" > < / stop > < stop
offset = ".618"
stop - color = "#7E87F0" > < / stop > < stop
offset = ".814"
stop - color = "#38AAF1" > < / stop > < stop
offset = ".941"
stop - color = "#07C3F2" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#dotpeek_dotpeek_svg__a)"
d = "M47.696 50.342 0 40.808 14.085 70l35.187-6.134-1.576-13.524Z" > < / path > < path
fill = "url(#dotpeek_dotpeek_svg__b)"
d = "M70 31.33 50.68 11.409.004 22.09 0 40.808l62.61 12.515L70 31.33Z" > < / path > < path
fill = "url(#dotpeek_dotpeek_svg__c)"
d = "M70 31.33 39.617 0l-23.81 7.21 7.797 23.71L62.61 53.324 70 31.33Z" > < / path > < path
fill = "url(#dotpeek_dotpeek_svg__d)"
d = "M64.536 19.575 61.78 0H39.617l-23.81 7.21 7.797 23.71 40.932-11.345Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM19 19h6.132c4.942 0 8.356 3.392 8.356 7.817v.045c0 4.425-3.414 7.861-8.356 7.861H19V19Zm3.46 3.122v9.48h2.672c2.83 0 4.74-1.91 4.74-4.695v-.045a4.516 4.516 0 0 0-4.74-4.74H22.46ZM36.027 19h6.443c3.761 0 6.037 2.23 6.037 5.451v.045c0 3.65-2.839 5.542-6.375 5.542h-2.636v4.73h-3.47V19Zm6.217 7.952c1.735 0 2.748-1.036 2.748-2.388v-.045c0-1.554-1.08-2.388-2.816-2.388h-2.68v4.82h2.748Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "dotmemory" > < defs > < linearGradient
id = "dotmemory_dotmemory_svg__a"
x1 = "18.757"
x2 = "30.724"
y1 = "19.283"
y2 = "69.379"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#6B57FF" > < / stop > < stop
offset = ".13"
stop - color = "#9A51F9" > < / stop > < stop
offset = ".268"
stop - color = "#C64CF4" > < / stop > < stop
offset = ".392"
stop - color = "#E548F0" > < / stop > < stop
offset = ".497"
stop - color = "#F846EE" > < / stop > < stop
offset = ".57"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".633"
stop - color = "#FF57C9" > < / stop > < stop
offset = ".814"
stop - color = "#FE8A65" > < / stop > < stop
offset = ".941"
stop - color = "#FDAA26" > < / stop > < stop
offset = "1"
stop - color = "#FDB60D" > < / stop > < / linearGradient > < linearGradient
id = "dotmemory_dotmemory_svg__b"
x1 = "51.758"
x2 = "39.877"
y1 = "35.768"
y2 = "1.731"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#6B57FF" > < / stop > < stop
offset = ".138"
stop - color = "#8953FB" > < / stop > < stop
offset = ".437"
stop - color = "#D64AF2" > < / stop > < stop
offset = ".588"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".968"
stop - color = "#FDB60D" > < / stop > < / linearGradient > < linearGradient
id = "dotmemory_dotmemory_svg__c"
x1 = "26.353"
x2 = "36.21"
y1 = "53.604"
y2 = "30.222"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".118"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".197"
stop - color = "#DF49F1" > < / stop > < stop
offset = ".304"
stop - color = "#BC4DF5" > < / stop > < stop
offset = ".416"
stop - color = "#9E51F9" > < / stop > < stop
offset = ".535"
stop - color = "#8854FC" > < / stop > < stop
offset = ".663"
stop - color = "#7855FD" > < / stop > < stop
offset = ".807"
stop - color = "#6E57FF" > < / stop > < stop
offset = "1"
stop - color = "#6B57FF" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#dotmemory_dotmemory_svg__a)"
d = "M7.975 65.148 0 37.65l49.553 13.658L44.266 70l-36.29-4.852Z" > < / path > < path
fill = "url(#dotmemory_dotmemory_svg__b)"
d = "M23.477.09 42.12 5.422 63.173 0l4.176 28.878-47.394-15.753L23.477.09Z" > < / path > < path
fill = "url(#dotmemory_dotmemory_svg__c)"
d = "m70 46.114-2.65-17.236-42.88-14.252L.09 19.858 0 37.651l49.553 13.658L70 46.114Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM19 19h6.13c4.941 0 8.355 3.391 8.355 7.815v.045c0 4.424-3.414 7.86-8.354 7.86H19V19Zm3.458 3.122v9.476h2.673c2.83 0 4.738-1.909 4.738-4.693v-.045a4.516 4.516 0 0 0-4.738-4.738h-2.673ZM34.693 19.01h3.728l4.134 6.647 4.131-6.647h3.728v15.72h-3.438l.001-10.261-4.422 6.714h-.093l-4.377-6.648-.001 10.195h-3.392V19.01Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "dotcover" > < defs > < linearGradient
id = "dotcover_dotcover_svg__a"
x1 = "37.049"
x2 = "23.558"
y1 = "55.637"
y2 = "5.422"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".048"
stop - color = "#6B57FF" > < / stop > < stop
offset = ".12"
stop - color = "#7556FE" > < / stop > < stop
offset = ".241"
stop - color = "#8F53FB" > < / stop > < stop
offset = ".395"
stop - color = "#BA4DF5" > < / stop > < stop
offset = ".576"
stop - color = "#F446EE" > < / stop > < stop
offset = ".608"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".69"
stop - color = "#FF3BBE" > < / stop > < stop
offset = ".771"
stop - color = "#FF318C" > < / stop > < stop
offset = ".995"
stop - color = "#FC801D" > < / stop > < / linearGradient > < linearGradient
id = "dotcover_dotcover_svg__b"
x1 = "67.819"
x2 = "41.488"
y1 = "48.799"
y2 = "40.13"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".027"
stop - color = "#6B57FF" > < / stop > < stop
offset = ".388"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".487"
stop - color = "#FF4DD1" > < / stop > < stop
offset = ".702"
stop - color = "#FE6189" > < / stop > < stop
offset = "1"
stop - color = "#FC801D" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#dotcover_dotcover_svg__a)"
d = "M42.798 0 .003 4.816 0 26.828l10.733 35.725 53.819-13.64L42.798 0Z" > < / path > < path
fill = "url(#dotcover_dotcover_svg__b)"
d = "m65.943 22.209-16.859-8.075L25.42 56.726l6.43 8.727L48.24 70l15.78-9.955L70 41.31 65.943 22.21Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM19 19h6.148c4.955 0 8.379 3.4 8.379 7.838v.045c0 4.437-3.424 7.883-8.379 7.883H19V19Zm3.468 3.13v9.505h2.68c2.838 0 4.753-1.915 4.753-4.707v-.045a4.528 4.528 0 0 0-4.752-4.752h-2.68ZM35.185 27.003v-.046a8.053 8.053 0 0 1 8.263-8.194c2.987 0 4.776.996 6.247 2.444l-2.218 2.559c-1.223-1.11-2.467-1.789-4.052-1.789-2.671 0-4.596 2.22-4.596 4.935v.046c0 2.716 1.879 4.98 4.596 4.98 1.81 0 2.92-.725 4.165-1.856l2.219 2.241a8.103 8.103 0 0 1-6.498 2.83 7.997 7.997 0 0 1-8.126-8.15" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 160 160"
id = "code-with-me" > < path
fill = "url(#code-with-me_code-with-me_svg__a)"
d = "M16 16v96h49.067l24-96H16Zm39.733 80H32V80h27.467l-3.734 16Zm39.2-48-24 96H144V48H94.933ZM128 128H91.467l3.733-16H128v16Z" > < / path > < defs > < linearGradient
id = "code-with-me_code-with-me_svg__a"
x1 = "17.195"
x2 = "123.504"
y1 = "9.783"
y2 = "128.638"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".055"
stop - color = "#3BEA62" > < / stop > < stop
offset = "1"
stop - color = "#6B57FF" > < / stop > < / linearGradient > < / defs > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "projector" > < path
fill = "url(#projector_projector_svg__a)"
d = "M68.897 53.413 70 23.054 50.712 18.68 34.277 29.674l7.647 22.56 26.973 1.179Z" > < / path > < path
fill = "url(#projector_projector_svg__b)"
d = "M64.598 37.13 70 23.054l-18.984-8.37-16.739 14.99 30.32 7.456Z" > < / path > < path
fill = "url(#projector_projector_svg__c)"
d = "m44.777 70 24.12-16.587-57.979-25.755L0 58.7 44.777 70Z" > < / path > < path
fill = "url(#projector_projector_svg__d)"
d = "m0 26.745 38.576 29.407L64.598 37.13 35.038 4.337 9.283 0 0 26.745Z" > < / path > < path
fill = "#010101"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#fff"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM19 19h6.183c5.017 0 8.4 3.354 8.4 7.75 0 4.395-3.383 7.864-8.4 7.864L19 34.73V19Zm3.5 3.123v9.484h2.683c2.8 0 4.784-1.85 4.784-4.626 0-2.776-1.867-4.743-4.784-4.743l-2.683-.115ZM34.97 32.36 37 29.91c1.4 1.19 2.94 1.89 4.69 1.89 1.4 0 2.31-.56 2.31-1.47v-.07c0-.91-.56-1.33-3.15-2.03-3.22-.77-5.25-1.68-5.25-4.83v-.07c0-2.87 2.31-4.76 5.53-4.76 2.31 0 4.27.7 5.88 2.03l-1.82 2.59c-1.4-.98-2.8-1.54-4.13-1.54s-2.03.63-2.03 1.4v.07c0 1.05.7 1.4 3.43 2.1 3.22.84 5.04 1.96 5.04 4.76v.07c0 3.15-2.38 4.9-5.81 4.9-2.38-.07-4.83-.91-6.72-2.59Z" > < / path > < path
fill = "#010101"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#fff"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM35.333 35.21c-1.236 0-2.263-.233-3.08-.7a7.356 7.356 0 0 1-2.053-1.657l2.17-2.426c.443.49.91.886 1.353 1.166.467.28.957.42 1.517.42.653 0 1.167-.21 1.54-.63.373-.42.56-1.073.56-1.983V19.273h3.547v10.29c0 .934-.117 1.75-.374 2.45-.256.7-.63 1.284-1.096 1.75-.49.49-1.074.84-1.774 1.097-.7.233-1.47.35-2.31.35ZM19.25 19.25h6.44c3.78 0 6.02 2.24 6.02 5.46v.07c0 3.64-2.8 5.53-6.37 5.53h-2.66V35h-3.43V19.25Zm6.23 7.91c1.75 0 2.73-1.05 2.73-2.38v-.07c0-1.54-1.05-2.38-2.8-2.38h-2.66v4.83h2.73Z" > < / path > < defs > < linearGradient
id = "projector_projector_svg__a"
x1 = "59.78"
x2 = "49.639"
y1 = "48.666"
y2 = "19.368"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".001"
stop - color = "#FF318C" > < / stop > < stop
offset = "1"
stop - color = "#FE6C54" > < / stop > < / linearGradient > < linearGradient
id = "projector_projector_svg__b"
x1 = "62.419"
x2 = "53.52"
y1 = "16.94"
y2 = "28.242"
gradientUnits = "userSpaceOnUse" > < stop
stop - color = "#FF546A" > < / stop > < stop
offset = ".781"
stop - color = "#FE764A" > < / stop > < / linearGradient > < linearGradient
id = "projector_projector_svg__c"
x1 = "58.735"
x2 = "7.661"
y1 = "62.409"
y2 = "43.981"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".017"
stop - color = "#FF318C" > < / stop > < stop
offset = ".811"
stop - color = "#6B57FF" > < / stop > < / linearGradient > < linearGradient
id = "projector_projector_svg__d"
x1 = "19.82"
x2 = "41.54"
y1 = "48.841"
y2 = "10.476"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".331"
stop - color = "#FF318C" > < / stop > < stop
offset = ".942"
stop - color = "#FDB60D" > < / stop > < / linearGradient > < / defs > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "gateway" > < linearGradient
id = "gateway_gateway_svg__a"
x1 = "20.068"
x2 = "64.396"
y1 = "14.563"
y2 = "58.891"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#fdb60d" > < / stop > < stop
offset = ".548"
stop - color = "#ff318c" > < / stop > < stop
offset = ".888"
stop - color = "#6b57ff" > < / stop > < / linearGradient > < linearGradient
id = "gateway_gateway_svg__b"
x1 = "28.59"
x2 = "31.451"
y1 = "31.067"
y2 = "26.112"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#fff"
stop - opacity = ".6" > < / stop > < stop
offset = ".081"
stop - color = "#ffc524"
stop - opacity = ".4" > < / stop > < stop
offset = ".705"
stop - color = "#ffc524"
stop - opacity = "0" > < / stop > < / linearGradient > < linearGradient
id = "gateway_gateway_svg__c"
x1 = "28.433"
x2 = "32.696"
y1 = "8.59"
y2 = "15.974"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#f9ed32"
stop - opacity = ".6" > < / stop > < stop
offset = ".198"
stop - color = "#ffc524"
stop - opacity = ".4" > < / stop > < stop
offset = ".705"
stop - color = "#ffc524"
stop - opacity = "0" > < / stop > < / linearGradient > < linearGradient
id = "gateway_gateway_svg__d"
x1 = "41.913"
x2 = "40.014"
y1 = "7.991"
y2 = "11.28"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#fdb60d"
stop - opacity = ".6" > < / stop > < stop
offset = ".234"
stop - color = "#fdb60d"
stop - opacity = ".4" > < / stop > < stop
offset = ".518"
stop - color = "#ff318c"
stop - opacity = "0" > < / stop > < / linearGradient > < linearGradient
id = "gateway_gateway_svg__e"
x1 = "9.026"
x2 = "51.277"
y1 = "34.972"
y2 = "34.972"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".015" > < / stop > < stop
offset = ".193" > < / stop > < stop
offset = ".572"
stop - color = "#6b57ff" > < / stop > < stop
offset = ".826"
stop - color = "#ff318c" > < / stop > < / linearGradient > < linearGradient
id = "gateway_gateway_svg__f"
x1 = "35"
x2 = "41.997"
y1 = "42.482"
y2 = "42.482"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#ffb2ff"
stop - opacity = ".6" > < / stop > < stop
offset = ".081"
stop - color = "#d828ff"
stop - opacity = ".4" > < / stop > < stop
offset = ".705"
stop - color = "#ff318c"
stop - opacity = "0" > < / stop > < / linearGradient > < linearGradient
id = "gateway_gateway_svg__g"
x1 = "61.081"
x2 = "53.935"
y1 = "42.482"
y2 = "42.482"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#64f"
stop - opacity = ".8" > < / stop > < stop
offset = ".097"
stop - color = "#6b57ff"
stop - opacity = ".4" > < / stop > < stop
offset = ".705"
stop - color = "#ff318c"
stop - opacity = "0" > < / stop > < / linearGradient > < linearGradient
id = "gateway_gateway_svg__h"
x1 = "54.865"
x2 = "52.809"
y1 = "54.396"
y2 = "50.834"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".006"
stop - color = "#ff318c" > < / stop > < stop
offset = ".469"
stop - color = "#6b57ff"
stop - opacity = "0" > < / stop > < / linearGradient > < linearGradient
id = "gateway_gateway_svg__i"
x1 = "22.013"
x2 = "22.013"
y1 = "5.936"
y2 = "23.543"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".239"
stop - color = "#ff5592"
stop - opacity = ".65" > < / stop > < stop
offset = ".829"
stop - color = "#ff57e4"
stop - opacity = "0" > < / stop > < / linearGradient > < linearGradient
id = "gateway_gateway_svg__j"
x1 = "28.237"
x2 = "21.774"
y1 = "22.192"
y2 = "58.846"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".047"
stop - color = "#fff"
stop - opacity = ".86" > < / stop > < stop
offset = ".767"
stop - color = "#cbcaa4"
stop - opacity = "0" > < / stop > < / linearGradient > < path
fill = "url(#gateway_gateway_svg__a)"
d = "m35 65 25.974-15.02V19.964L35 5 9.026 19.963v.002-.001L35 34.985z" > < / path > < path
fill = "url(#gateway_gateway_svg__b)"
d = "M60.974 19.963 35 5 9.026 19.963v.002-.001L35 34.985z" > < / path > < path
fill = "url(#gateway_gateway_svg__c)"
d = "M60.974 19.963 35 5 9.026 19.963v.002-.001L35 34.985z" > < / path > < path
fill = "url(#gateway_gateway_svg__d)"
d = "M60.974 19.963 35 5 9.026 19.963v.002-.001L35 34.985z" > < / path > < path
fill = "url(#gateway_gateway_svg__e)"
d = "M9.026 49.98V19.965L35 34.984z" > < / path > < path
fill = "url(#gateway_gateway_svg__f)"
d = "m35 65 25.974-15.02V19.965L35 34.984z" > < / path > < path
fill = "url(#gateway_gateway_svg__g)"
d = "m35 65 25.974-15.02V19.965L35 34.984z" > < / path > < path
fill = "url(#gateway_gateway_svg__h)"
d = "m35 65 25.974-15.02V19.965L35 34.984z" > < / path > < path
fill = "url(#gateway_gateway_svg__i)"
d = "M28.035 30.944 35 34.971V5L9.026 19.957z"
opacity = ".8" > < / path > < path
fill = "url(#gateway_gateway_svg__j)"
d = "M35 34.984 9.026 49.98 35 65z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "mono" > < path
fill = "#1A1B1E"
d = "M29.206 12.143H15.873a4.444 4.444 0 0 0-4.444 4.444v36.825a4.444 4.444 0 0 0 4.444 4.445h13.333a4.445 4.445 0 0 0 4.445-4.445V16.587a4.444 4.444 0 0 0-4.445-4.444Z" > < / path > < path
fill = "#515151"
d = "M33.65 47.825H11.43v-.889H33.65v.89ZM33.65 54.174H11.43v-.889H33.65v.889ZM33.65 28.778H11.43v-.89H33.65v.89ZM33.65 22.428H11.43v-.889H33.65v.889Z" > < / path > < path
fill = "#FFF"
d = "M14.404 47.698V21.742h4.48l2.703 8.356c.237.782.438 1.54.604 2.275.19.711.332 1.257.427 1.636.07-.38.19-.925.355-1.636.19-.734.403-1.505.64-2.31l2.596-8.32h4.48v25.955H27.31V35.787c0-2.181.083-4.29.249-6.33.19-2.062.415-4.017.675-5.866l-4.053 12.764h-3.271l-4.089-12.693c.237 1.754.45 3.615.64 5.582.213 1.968.32 4.148.32 6.543v11.91h-3.378Z" > < / path > < path
fill = "#1A1B1E"
d = "M52.698 12.143H39.365a4.444 4.444 0 0 0-4.444 4.444v36.825a4.445 4.445 0 0 0 4.444 4.445h13.333a4.444 4.444 0 0 0 4.445-4.445V16.587a4.444 4.444 0 0 0-4.445-4.444Z" > < / path > < path
fill = "#515151"
d = "M57.143 47.825H34.92v-.889h22.222v.89ZM57.143 54.174H34.92v-.889h22.222v.889ZM57.143 28.778H34.92v-.89h22.222v.89ZM57.143 22.428H34.92v-.889h22.222v.889Z" > < / path > < path
fill = "#FFF"
d = "M46.039 47.983c-2.394 0-4.29-.664-5.69-1.991-1.398-1.351-2.097-3.188-2.097-5.511v-5.12c0-2.323.7-4.148 2.098-5.476 1.398-1.351 3.295-2.027 5.689-2.027s4.29.676 5.688 2.027c1.4 1.327 2.098 3.14 2.098 5.44v5.156c0 2.323-.699 4.16-2.098 5.51-1.398 1.328-3.294 1.992-5.688 1.992Zm0-3.093c1.327 0 2.37-.368 3.128-1.103.76-.758 1.138-1.86 1.138-3.306v-5.12c0-1.446-.379-2.537-1.138-3.271-.758-.759-1.8-1.138-3.128-1.138s-2.37.379-3.13 1.137c-.758.735-1.137 1.826-1.137 3.272v5.12c0 1.445.38 2.548 1.138 3.306.758.735 1.801 1.102 3.129 1.102Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "qodana" > < defs > < linearGradient
id = "qodana_qodana_svg__a"
x1 = "-1.355"
x2 = "55.71"
y1 = "54.971"
y2 = "46.772"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".176"
stop - color = "#FC7A26" > < / stop > < stop
offset = ".634"
stop - color = "#FF318C" > < / stop > < / linearGradient > < linearGradient
id = "qodana_qodana_svg__b"
x1 = "-9.742"
x2 = "71.493"
y1 = "-.856"
y2 = "59.512"
gradientUnits = "userSpaceOnUse" > < stop
stop - color = "#FF318C" > < / stop > < stop
offset = ".399"
stop - color = "#B544C6" > < / stop > < stop
offset = ".874"
stop - color = "#FF318C" > < / stop > < / linearGradient > < linearGradient
id = "qodana_qodana_svg__c"
x1 = "-19.21"
x2 = "71.098"
y1 = "25.887"
y2 = "4.645"
gradientUnits = "userSpaceOnUse" > < stop
stop - color = "#FF318C" > < / stop > < stop
offset = ".2"
stop - color = "#D73BAB" > < / stop > < stop
offset = ".515"
stop - color = "#9D4AD8" > < / stop > < stop
offset = ".748"
stop - color = "#7953F4" > < / stop > < stop
offset = ".872"
stop - color = "#6B57FF" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#qodana_qodana_svg__a)"
d = "M47.002 30.496 13.34 37.541c-.87.145-1.742.29-2.613.582-2.682.797-5.002 2.396-6.744 4.646C-6.1 55.842 4.305 72.94 20.16 69.567L56 64.424c5.269-1.086 8.412-3.426 10.661-6.766 9.576-14.307-2.831-32.1-19.659-27.162Z" > < / path > < path
fill = "url(#qodana_qodana_svg__b)"
d = "M28.478 4.43C24.342.652 18.242-1.16 11.343.797a14.338 14.338 0 0 0-7.188 5.012c-6.898 8.93-4.572 19.675 2.326 25.195l36.883 30.785c3.702 2.469 8.493 3.559 13.793 2.398 3.92-.87 7.261-3.195 9.512-6.535 5.663-8.496 3.632-18.297-2.54-23.742L28.478 4.43Z" > < / path > < path
fill = "url(#qodana_qodana_svg__c)"
d = "M16.128.074c-1.818.145-3.422.363-4.732.797-2.842.8-5.389 2.543-7.212 4.938-10.777 13.941.803 32.093 17.26 28.46l44.337-16.581c1.299-.53 2.345-1.059 3.07-2.223 2.767-4.137.228-8.676-4.321-9.185L17.948 0c-.656 0-1.235 0-1.82.074Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#fff"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM32.733 35.192l-1.73-1.55a8.566 8.566 0 0 1-4.67 1.348C21.48 34.99 18 31.374 18 26.905v-.045c0-4.47 3.526-8.13 8.377-8.13 4.85 0 8.332 3.615 8.332 8.085v.045a8.064 8.064 0 0 1-1.392 4.514l1.617 1.37-2.201 2.448Zm-4.29-3.818-2.56-2.179 2.2-2.47 2.584 2.335a5.51 5.51 0 0 0 .426-2.155v-.045a4.777 4.777 0 0 0-4.76-4.941c-2.786 0-4.717 2.2-4.717 4.896v.045a4.775 4.775 0 0 0 4.761 4.94 4.722 4.722 0 0 0 2.066-.426ZM37.395 18.999h5.923c4.941 0 8.355 3.391 8.355 7.816v.045c0 4.424-3.414 7.86-8.355 7.86h-5.923V18.999Zm3.458 3.122v9.477h2.465c2.83 0 4.74-1.908 4.74-4.693v-.045a4.515 4.515 0 0 0-4.74-4.739h-2.465Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "edutools" > < defs > < linearGradient
id = "edutools_edutools_svg__a"
x1 = "58.655"
x2 = "11.146"
y1 = "58.655"
y2 = "11.146"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".038"
stop - color = "#21D789" > < / stop > < stop
offset = ".895"
stop - color = "#AF1DF5" > < / stop > < stop
offset = "1"
stop - color = "#AF1DF5" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#edutools_edutools_svg__a)"
d = "M6 58.925V6h52.925L6 58.925ZM11.075 64H64V11.075L11.075 64Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "fleet" > < defs > < radialGradient
id = "fleet_fleet_svg__a"
cx = "0"
cy = "0"
r = "1"
gradientTransform = "matrix(22.35433 -20.58122 27.17129 29.51214 38.648 42.538)"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".771"
stop - color = "#001AFF" > < / stop > < stop
offset = "1"
stop - color = "#8ACEFF" > < / stop > < / radialGradient > < radialGradient
id = "fleet_fleet_svg__b"
cx = "0"
cy = "0"
r = "1"
gradientTransform = "rotate(-30.543 79.837 -70.068) scale(16.777 22.1489)"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".719"
stop - color = "#FA00FF"
stop - opacity = "0" > < / stop > < stop
offset = "1"
stop - color = "#FF00D6"
stop - opacity = ".44" > < / stop > < / radialGradient > < radialGradient
id = "fleet_fleet_svg__c"
cx = "0"
cy = "0"
r = "1"
gradientTransform = "rotate(49.385 -19.814 41.858) scale(47.8852)"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".026"
stop - color = "#8DFDFD" > < / stop > < stop
offset = ".271"
stop - color = "#87FBFB" > < / stop > < stop
offset = ".484"
stop - color = "#74D6F4" > < / stop > < stop
offset = ".932"
stop - color = "#0038FF" > < / stop > < / radialGradient > < radialGradient
id = "fleet_fleet_svg__d"
cx = "0"
cy = "0"
r = "1"
gradientTransform = "rotate(137.237 9.434 23.195) scale(32.8316)"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".267"
stop - color = "#0500FF"
stop - opacity = "0" > < / stop > < stop
offset = "1"
stop - color = "#0500FF"
stop - opacity = ".15" > < / stop > < / radialGradient > < radialGradient
id = "fleet_fleet_svg__e"
cx = "0"
cy = "0"
r = "1"
gradientTransform = "rotate(75.198 -4.629 32.631) scale(51.1484)"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".42"
stop - color = "#FF00E5"
stop - opacity = "0" > < / stop > < stop
offset = ".774"
stop - color = "#FF00F5"
stop - opacity = ".64" > < / stop > < stop
offset = ".899"
stop - color = "#BE46FF"
stop - opacity = ".87" > < / stop > < / radialGradient > < radialGradient
id = "fleet_fleet_svg__g"
cx = "0"
cy = "0"
r = "1"
gradientTransform = "matrix(2.73484 22.75837 -34.39872 4.13365 29.458 35.276)"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#00B2FF" > < / stop > < stop
offset = ".571"
stop - color = "#74C5FF" > < / stop > < stop
offset = ".979"
stop - color = "#9FD7FF" > < / stop > < / radialGradient > < linearGradient
id = "fleet_fleet_svg__f"
x1 = "11.644"
x2 = "82.363"
y1 = "42.432"
y2 = "43.401"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".432"
stop - color = "#FE62EE"
stop - opacity = "0" > < / stop > < stop
offset = ".818"
stop - color = "#FD3AF5"
stop - opacity = ".47" > < / stop > < / linearGradient > < linearGradient
id = "fleet_fleet_svg__h"
x1 = "33.054"
x2 = "37.35"
y1 = "23.191"
y2 = "49.344"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".042"
stop - color = "#0038FF" > < / stop > < stop
offset = ".724"
stop - color = "#48BFF1"
stop - opacity = ".59" > < / stop > < stop
offset = "1"
stop - color = "#74C5FF"
stop - opacity = "0" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#fleet_fleet_svg__a)"
d = "M65.153 30.85c0 9.496-10.163 17.194-22.7 17.194-12.536 0-22.699-7.698-22.699-17.194 0-9.496 10.163-17.194 22.7-17.194 12.536 0 22.699 7.698 22.699 17.194z" > < / path > < path
fill = "url(#fleet_fleet_svg__b)"
d = "M65.153 30.85c0 9.496-10.163 17.194-22.7 17.194-12.536 0-22.699-7.698-22.699-17.194 0-9.496 10.163-17.194 22.7-17.194 12.536 0 22.699 7.698 22.699 17.194z" > < / path > < path
fill = "url(#fleet_fleet_svg__c)"
d = "M66 35c0 17.12-13.88 31-31 31C17.88 66 4 52.12 4 35 4 17.88 17.88 4 35 4c8.046 3.642 16.464 17.194 19.99 21.429 3.524 4.235 12.648 9.571 8.176-1.623C65.073 26.832 66 31.852 66 35z" > < / path > < path
fill = "url(#fleet_fleet_svg__d)"
d = "M66 35c0 17.12-13.88 31-31 31C17.88 66 4 52.12 4 35 4 17.88 17.88 4 35 4c8.046 3.642 16.464 17.194 19.99 21.429 3.524 4.235 12.648 9.571 8.176-1.623C65.073 26.832 66 31.852 66 35z" > < / path > < path
fill = "url(#fleet_fleet_svg__e)"
d = "M66 35c0 17.12-13.88 31-31 31C17.88 66 4 52.12 4 35 4 17.88 17.88 4 35 4c8.046 3.642 16.464 17.194 19.99 21.429 3.524 4.235 12.648 9.571 8.176-1.623C65.073 26.832 66 31.852 66 35z" > < / path > < path
fill = "url(#fleet_fleet_svg__f)"
d = "M66 35c0 17.12-13.88 31-31 31C17.88 66 4 52.12 4 35 4 17.88 17.88 4 35 4c8.046 3.642 16.464 17.194 19.99 21.429 3.524 4.235 12.648 9.571 8.176-1.623C65.073 26.832 66 31.852 66 35z" > < / path > < path
fill = "url(#fleet_fleet_svg__g)"
d = "M56.651 39.682c1.658 7.764-6.511 16.089-18.246 18.594-11.734 2.505-22.59-1.757-24.248-9.52-1.658-7.764 6.511-16.089 18.246-18.594 11.734-2.506 22.59 1.757 24.248 9.52z" > < / path > < path
fill = "url(#fleet_fleet_svg__h)"
d = "M56.651 39.682c1.658 7.764-6.511 16.089-18.246 18.594-11.734 2.505-22.59-1.757-24.248-9.52-1.658-7.764 6.511-16.089 18.246-18.594 11.734-2.506 22.59 1.757 24.248 9.52z" > < / path > < path
fill = "#D6F8F8"
fill - opacity = ".19"
fill - rule = "evenodd"
d = "M51.462 49.883c3.074-3.133 4.386-6.66 3.698-9.882-.688-3.223-3.326-5.907-7.411-7.51-4.073-1.6-9.412-2.037-15.028-.838-5.616 1.199-10.31 3.779-13.375 6.901-3.074 3.133-4.386 6.66-3.698 9.883.688 3.223 3.326 5.906 7.412 7.51 4.072 1.6 9.41 2.037 15.027.838 5.616-1.2 10.31-3.779 13.375-6.902zm-13.057 8.393c11.735-2.505 19.904-10.83 18.246-18.594-1.658-7.763-12.514-12.026-24.248-9.52-11.735 2.505-19.904 10.83-18.246 18.593 1.658 7.764 12.514 12.026 24.248 9.521z"
clip - rule = "evenodd" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "marketplace" > < defs > < linearGradient
id = "marketplace_marketplace_svg__a"
x1 = "18.931"
x2 = "53.991"
y1 = "19.64"
y2 = "53.153"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".043"
stop - color = "#FC801D" > < / stop > < stop
offset = ".448"
stop - color = "#FE2857" > < / stop > < stop
offset = ".895"
stop - color = "#AF1DF5" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#marketplace_marketplace_svg__a)"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#fff"
d = "M35 48.125H19.25v2.625H35v-2.625ZM19.234 19.232h3.672l4.073 6.628 4.07-6.628h3.672v15.676h-3.383V24.673l-4.36 6.697h-.089l-4.313-6.628v10.166h-3.342V19.232Zm18.646 0h6.326c3.695 0 5.93 2.218 5.93 5.42v.044c0 3.628-2.789 5.51-6.262 5.51h-2.588v4.702H37.88V19.232Zm6.105 7.905c1.702 0 2.698-1.03 2.698-2.374v-.044c0-1.546-1.06-2.374-2.765-2.374h-2.632v4.792h2.699Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "riderflow" > < defs > < linearGradient
id = "riderflow_riderflow_svg__a"
x1 = "16.844"
x2 = "38.664"
y1 = "41.53"
y2 = "64.22"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".01"
stop - color = "#087CFA" > < / stop > < stop
offset = ".49"
stop - color = "#903ACA" > < / stop > < stop
offset = ".93"
stop - color = "#DD1265" > < / stop > < / linearGradient > < linearGradient
id = "riderflow_riderflow_svg__b"
x1 = "42.219"
x2 = "57.684"
y1 = "36.165"
y2 = "8.898"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".59"
stop - color = "#087CFA" > < / stop > < stop
offset = ".99"
stop - color = "#0093FF" > < / stop > < / linearGradient > < linearGradient
id = "riderflow_riderflow_svg__c"
x1 = "30.258"
x2 = "41.726"
y1 = "-.027"
y2 = "22.717"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".21"
stop - color = "#087CFA" > < / stop > < stop
offset = ".7"
stop - color = "#DD1265" > < / stop > < / linearGradient > < linearGradient
id = "riderflow_riderflow_svg__d"
x1 = "15.176"
x2 = "25.577"
y1 = "3.073"
y2 = "38.511"
gradientUnits = "userSpaceOnUse" > < stop
stop - color = "#087CFA" > < / stop > < stop
offset = ".33"
stop - color = "#903ACA" > < / stop > < stop
offset = ".6"
stop - color = "#DD1265" > < / stop > < / linearGradient > < linearGradient
id = "riderflow_riderflow_svg__e"
x1 = "81.61"
x2 = "49.892"
y1 = "16.549"
y2 = "52.675"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".21"
stop - color = "#087CFA" > < / stop > < stop
offset = ".56"
stop - color = "#903ACA" > < / stop > < stop
offset = ".84"
stop - color = "#DD1265" > < / stop > < / linearGradient > < linearGradient
id = "riderflow_riderflow_svg__f"
x1 = "58.751"
x2 = "38.795"
y1 = "72.133"
y2 = "45.434"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".31"
stop - color = "#FDB60D" > < / stop > < stop
offset = "1"
stop - color = "#DD1265" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#riderflow_riderflow_svg__a)"
d = "M50.198 56.033 24.396 70 0 55.716l44.844-16.757 5.354 17.074Z" > < / path > < path
fill = "url(#riderflow_riderflow_svg__b)"
d = "M39.971 0 25.95 41.595l-13.956-7.793L0 55.715l22.395-3.576 28.415-5.015L70 42.826V16.723L39.971 0Z" > < / path > < path
fill = "#087CFA"
d = "m31.719 24.248-18.681-5.375L11.484 0l15.718 6.606L39.977 0l-8.258 24.248Z" > < / path > < path
fill = "url(#riderflow_riderflow_svg__c)"
d = "M32.266 23.155 27.2 6.606 39.976 0l-7.71 23.155Z" > < / path > < path
fill = "url(#riderflow_riderflow_svg__d)"
d = "M48.174 40.65 11.501 0 0 26.217 32.38 54.19l15.794-13.54Z" > < / path > < path
fill = "url(#riderflow_riderflow_svg__e)"
d = "m70 42.826-21.328 4.922.815-3.517L70 16.724v26.102Z" > < / path > < path
fill = "url(#riderflow_riderflow_svg__f)"
d = "M58.794 70 32.38 54.196l15.794-13.547L58.794 70Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#fff"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM19.27 19.25h7.208c2.007 0 3.562.562 4.597 1.576a4.964 4.964 0 0 1 1.356 3.604v.074a4.902 4.902 0 0 1-3.384 4.891l3.857 5.616h-4.062l-3.383-5.049h-2.721v5.05H19.27V19.25Zm6.982 7.639c1.692 0 2.659-.904 2.659-2.233v-.042c0-1.487-1.051-2.254-2.722-2.254h-3.451v4.529h3.514ZM35.567 19.25h12.01v3.152H39.04v3.357h7.523v3.153H39.04v6.1h-3.473V19.25Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "license-vault" > < defs > < linearGradient
id = "license-vault_license-vault_svg__a"
x1 = "2.851"
x2 = "67.964"
y1 = "2.851"
y2 = "67.964"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".168"
stop - color = "#FF45ED" > < / stop > < stop
offset = ".602"
stop - color = "#B74AF7" > < / stop > < stop
offset = "1"
stop - color = "#009AE5" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#license-vault_license-vault_svg__a)"
d = "M0 70h70V0H0v70Z" > < / path > < path
fill = "#000"
d = "M0 70V0l35 26v44H0Z" > < / path > < path
fill = "#fff"
d = "M8.725 61.25h17.407v-3.86H8.725v3.86Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 41 48"
id = "android-studio" > < g
clip - path = "url(#android-studio_android-studio_svg__a)" > < path
fill = "#073042"
d = "M15.066 6.055H4.036C1.817 6.055 0 7.847 0 10.045c0 2.186 1.68 3.978 3.898 3.978h11.248l-.08-7.968Z" > < / path > < path
fill = "#4285F4"
d = "M40.145 41.509H4.035C1.818 41.509 0 39.717 0 37.53V10.032s-.012 3.99 4.298 3.99h29.95s5.898-.497 5.898 3.831V41.51Z" > < / path > < path
fill = "#4285F4"
d = "M23.298 27.422a3.565 3.565 0 0 0 1.418-2.84c0-1.939-1.566-3.516-3.51-3.584.046 0 .08-.011.126-.011.217 0 .435.022.64.056v-2.276a.688.688 0 0 0-.697-.688.688.688 0 0 0-.697.688v2.254c-1.772.247-3.132 1.735-3.132 3.55 0 1.205.605 2.276 1.543 2.918l-6.653 14.009h4.344l3.075-6.48c.571-1.195 2.286-1.195 2.857-.011l3.167 6.49h4.39l-6.87-14.075Zm-2.217-.631c-1.235 0-2.24-.992-2.24-2.209s1.005-2.209 2.24-2.209c1.234 0 2.24.992 2.24 2.209s-1.006 2.209-2.24 2.209Z" > < / path > < path
fill = "#073042"
d = "M19.878 22.373c1.235 0 2.24.992 2.24 2.21 0 1.216-1.005 2.208-2.24 2.208-1.234 0-2.24-.992-2.24-2.209 0-1.228 1.006-2.209 2.24-2.209Zm.892-1.33v-2.276a.688.688 0 0 0-.697-.688.688.688 0 0 0-.698.688v2.254c-1.771.248-3.143 1.747-3.143 3.561 0 1.206.606 2.277 1.543 2.919L9.373 45.15c-.606 1.284.343 2.772 1.795 2.772a1.992 1.992 0 0 0 1.795-1.127l5.59-11.777c.57-1.195 2.286-1.195 2.857-.011l5.716 11.71a1.974 1.974 0 0 0 1.771 1.104c1.452 0 2.412-1.5 1.772-2.784l-8.573-17.615a3.565 3.565 0 0 0 1.417-2.84c0-1.679-1.166-3.076-2.743-3.471" > < / path > < path
fill = "#fff"
d = "M28.13 8.016H12.677V10.8H28.13V8.017Z" > < / path > < path
fill = "#3DDC84"
d = "M25.88 10.473a1.041 1.041 0 0 1-1.052-1.037c0-.575.469-1.037 1.052-1.037.583 0 1.051.462 1.051 1.037s-.468 1.037-1.051 1.037Zm-11.614 0a1.041 1.041 0 0 1-1.052-1.037c0-.575.469-1.037 1.052-1.037.583 0 1.052.462 1.052 1.037s-.47 1.037-1.052 1.037ZM26.257 4.24 28.36.657A.422.422 0 0 0 28.2.07a.435.435 0 0 0-.594.157l-2.126 3.63a12.969 12.969 0 0 0-5.407-1.15c-1.943 0-3.772.405-5.407 1.138L12.55.217a.438.438 0 0 0-.594-.158c-.206.124-.286.383-.16.586L13.9 4.23a12.254 12.254 0 0 0-6.447 9.793h25.24a12.21 12.21 0 0 0-6.436-9.782Z" > < / path > < path
fill = "#073042"
d = "M36.51 21.652h-1.669a.2.2 0 0 0-.145.059.205.205 0 0 0-.06.144l-.046 25.808a.204.204 0 0 0 .206.203l1.703.011c2 0 3.635-1.611 3.635-3.584V18.069c.011 1.973-1.623 3.584-3.624 3.584Z" > < / path > < / g > < defs > < clipPath
id = "android-studio_android-studio_svg__a" > < path
fill = "#fff"
d = "M0 0h40.145v48H0z" > < / path > < / clipPath > < / defs > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "dataspell" > < defs > < linearGradient
id = "dataspell_dataspell_svg__a"
x1 = "51.915"
x2 = "5.515"
y1 = "21.235"
y2 = "21.235"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#21D789" > < / stop > < stop
offset = ".917"
stop - color = "#FCF84A" > < / stop > < / linearGradient > < linearGradient
id = "dataspell_dataspell_svg__b"
x1 = "53.765"
x2 = "53.765"
y1 = "20.208"
y2 = "78.116"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#21D789" > < / stop > < stop
offset = "1"
stop - color = "#087CFA" > < / stop > < / linearGradient > < linearGradient
id = "dataspell_dataspell_svg__c"
x1 = "92.069"
x2 = "23.619"
y1 = "72.972"
y2 = "17.191"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".105"
stop - color = "#21D789" > < / stop > < stop
offset = ".967"
stop - color = "#087CFA" > < / stop > < / linearGradient > < linearGradient
id = "dataspell_dataspell_svg__d"
x1 = "60.521"
x2 = "12.274"
y1 = "-5.388"
y2 = "49.291"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".235"
stop - color = "#21D789" > < / stop > < stop
offset = ".74"
stop - color = "#087CFA" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#dataspell_dataspell_svg__a)"
d = "m44.99 0 1.385 28.438-35.438 14L0 14.145 44.99 0Z" > < / path > < path
fill = "#21D789"
d = "m70 16.625-30.625 13.27L44.99 0 70 16.625Z" > < / path > < path
fill = "url(#dataspell_dataspell_svg__b)"
d = "M37.552 23.187 70 16.625v30.698l-22.313 8.385-9.114-8.312-1.02-24.209Z" > < / path > < path
fill = "url(#dataspell_dataspell_svg__c)"
d = "m24.063 14.219 22.387 3.463L70 47.05l-22.605 8.731-8.723-8.659-14.61-32.903Z" > < / path > < path
fill = "url(#dataspell_dataspell_svg__d)"
d = "m14.438 0 31.937 17.646L35.365 70H16.77L.656 53.375 14.437 0Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#FFF"
d = "M34.417 48.65h-15.75v2.683h15.75V48.65ZM19 19h6.183c5.017 0 8.4 3.354 8.4 7.75 0 4.395-3.383 7.864-8.4 7.864L19 34.73V19Zm3.5 3.123v9.484h2.683c2.8 0 4.784-1.85 4.784-4.626 0-2.776-1.867-4.743-4.784-4.743l-2.683-.115ZM34.97 32.36 37 29.91c1.4 1.19 2.94 1.89 4.69 1.89 1.4 0 2.31-.56 2.31-1.47v-.07c0-.91-.56-1.33-3.15-2.03-3.22-.77-5.25-1.68-5.25-4.83v-.07c0-2.87 2.31-4.76 5.53-4.76 2.31 0 4.27.7 5.88 2.03l-1.82 2.59c-1.4-.98-2.8-1.54-4.13-1.54s-2.03.63-2.03 1.4v.07c0 1.05.7 1.4 3.43 2.1 3.22.84 5.04 1.96 5.04 4.76v.07c0 3.15-2.38 4.9-5.81 4.9-2.38-.07-4.83-.91-6.72-2.59Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 70 70"
id = "aqua" > < defs > < linearGradient
id = "aqua_aqua_svg__a"
x1 = "25.657"
x2 = "16.44"
y1 = "58.53"
y2 = "25.272"
gradientUnits = "userSpaceOnUse" > < stop
stop - color = "#087CFA" > < / stop > < stop
offset = "1"
stop - color = "#6B57FF" > < / stop > < / linearGradient > < linearGradient
id = "aqua_aqua_svg__b"
x1 = "13.002"
x2 = "47.315"
y1 = "63.483"
y2 = "14.124"
gradientUnits = "userSpaceOnUse" > < stop
stop - color = "#087CFA" > < / stop > < stop
offset = ".387"
stop - color = "#097FF6" > < / stop > < stop
offset = ".96"
stop - color = "#3BEA62" > < / stop > < / linearGradient > < / defs > < path
fill = "url(#aqua_aqua_svg__a)"
d = "M33.084 25.14 3.479 17.906 0 26.136l10.672 34.135L39.026 70l-5.942-44.86Z" > < / path > < path
fill = "url(#aqua_aqua_svg__b)"
d = "M70 20.024 62.885 6.092 26.58 0 10.672 60.27 39.026 70l1.52-2.493L70 20.024Z" > < / path > < path
fill = "#000"
d = "M56 14H14v42h42V14Z" > < / path > < path
fill = "#fff"
d = "M34.416 48.65h-15.75v2.683h15.75v-2.684ZM42.306 19.256h3.169l6.694 15.73h-3.593l-1.428-3.502h-6.604l-1.428 3.503h-3.504l6.694-15.731Zm3.615 9.193-2.075-5.065-2.075 5.065h4.15ZM32.884 35.456l-1.718-1.54c-1.317.849-2.9 1.34-4.641 1.34-4.82 0-8.278-3.593-8.278-8.033v-.045c0-4.44 3.503-8.077 8.322-8.077 4.82 0 8.278 3.592 8.278 8.032v.045c0 1.651-.513 3.19-1.383 4.485l1.607 1.361-2.187 2.432Zm-4.262-3.793-2.544-2.164 2.187-2.455 2.566 2.32a5.472 5.472 0 0 0 .424-2.141v-.045c0-2.678-1.963-4.909-4.73-4.909-2.767 0-4.686 2.187-4.686 4.864v.045c0 2.678 1.964 4.909 4.73 4.909.759 0 1.45-.134 2.053-.424Z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
viewBox = "0 0 70 70"
id = "jetbrains-academy" > < linearGradient
id = "jetbrains-academy_jetbrains-academy_svg__a"
x1 = "41.286"
x2 = "13.839"
y1 = "41.286"
y2 = "13.839"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".233"
stop - color = "#21d789" > < / stop > < stop
offset = ".89"
stop - color = "#af1df5" > < / stop > < / linearGradient > < path
d = "M56 14v42H14z" > < / path > < path
fill = "#fff"
d = "M50.765 50.75H40.252v-2.316h10.513Z" > < / path > < path
fill = "url(#jetbrains-academy_jetbrains-academy_svg__a)"
d = "M14 56V14h42z" > < / path > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 64 64"
id = "jetbrains-academy-square-64" > < defs > < linearGradient
id = "jetbrains-academy-square-64_jetbrains-academy-square-64_svg__b"
x1 = "41.578"
x2 = "-.245"
y1 = "41.579"
y2 = "-.245"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".233"
stop - color = "#21D789" > < / stop > < stop
offset = ".89"
stop - color = "#AF1DF5" > < / stop > < / linearGradient > < clipPath
id = "jetbrains-academy-square-64_jetbrains-academy-square-64_svg__a" > < path
fill = "#fff"
d = "M0 0h64v64H0z" > < / path > < / clipPath > < / defs > < g
clip - path = "url(#jetbrains-academy-square-64_jetbrains-academy-square-64_svg__a)" > < path
fill = "#000"
d = "M64 0v64H0L64 0Z" > < / path > < path
fill = "#fff"
d = "M40 56h16v-4H40v4Z" > < / path > < path
fill = "url(#jetbrains-academy-square-64_jetbrains-academy-square-64_svg__b)"
d = "M0 64V0h64L0 64Z" > < / path > < / g > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
fill = "none"
viewBox = "0 0 96 96"
id = "jetbrains-academy-square-96" > < defs > < linearGradient
id = "jetbrains-academy-square-96_jetbrains-academy-square-96_svg__b"
x1 = "62.368"
x2 = "-.368"
y1 = "62.368"
y2 = "-.368"
gradientUnits = "userSpaceOnUse" > < stop
offset = ".233"
stop - color = "#21D789" > < / stop > < stop
offset = ".89"
stop - color = "#AF1DF5" > < / stop > < / linearGradient > < clipPath
id = "jetbrains-academy-square-96_jetbrains-academy-square-96_svg__a" > < path
fill = "#fff"
d = "M0 0h96v96H0z" > < / path > < / clipPath > < / defs > < g
clip - path = "url(#jetbrains-academy-square-96_jetbrains-academy-square-96_svg__a)" > < path
fill = "#000"
d = "M96 0v96H0L96 0Z" > < / path > < path
fill = "#fff"
d = "M60 84h24v-6H60v6Z" > < / path > < path
fill = "url(#jetbrains-academy-square-96_jetbrains-academy-square-96_svg__b)"
d = "M0 96V0h96L0 96Z" > < / path > < / g > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
viewBox = "0 0 273 75"
id = "space-text-white" > < linearGradient
id = "space-text-white_space-text-white_svg__a"
x1 = "33.813"
x2 = "41.643"
y1 = "-102.99"
y2 = "-177.21"
gradientTransform = "matrix(1 0 0 -1 0 -104)"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#fcf84a" > < / stop > < stop
offset = ".32"
stop - color = "#abe682" > < / stop > < stop
offset = ".79"
stop - color = "#36cdd2" > < / stop > < stop
offset = "1"
stop - color = "#07c3f2" > < / stop > < / linearGradient > < linearGradient
id = "space-text-white_space-text-white_svg__b"
x1 = "5.095"
x2 = "75.305"
y1 = "-104.136"
y2 = "-137.446"
gradientTransform = "matrix(1 0 0 -1 0 -104)"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#3bea62" > < / stop > < stop
offset = "1"
stop - color = "#087cfa" > < / stop > < / linearGradient > < linearGradient
id = "space-text-white_space-text-white_svg__c"
x1 = "11.52"
x2 = "82.22"
y1 = "-176.65"
y2 = "-127.17"
gradientTransform = "matrix(1 0 0 -1 0 -104)"
gradientUnits = "userSpaceOnUse" > < stop
offset = "0"
stop - color = "#009ae5" > < / stop > < stop
offset = ".18"
stop - color = "#0490dd" > < / stop > < stop
offset = ".49"
stop - color = "#1073c6" > < / stop > < stop
offset = ".89"
stop - color = "#2346a1" > < / stop > < stop
offset = "1"
stop - color = "#293896" > < / stop > < / linearGradient > < path
fill = "#fff"
d = "m89.663 50.28 5.74-7c4 3.32 8.14 5.43 13.19 5.43 4 0 6.37-1.6 6.37-4.22v-.09c0-2.49-1.52-3.77-8.9-5.69-8.89-2.3-14.63-4.79-14.63-13.67v-.13c0-8.11 6.43-13.48 15.45-13.48a25.3 25.3 0 0 1 16.4 5.69l-5 7.41c-3.91-2.75-7.76-4.41-11.48-4.41s-5.68 1.72-5.68 3.9v.12c0 2.94 1.89 3.9 9.52 5.88 9 2.37 14 5.63 14 13.42v.13c0 8.88-6.69 13.87-16.21 13.87a27.91 27.91 0 0 1-18.74-7.16M156.403 39.74v-.13c0-5.69-3.78-9.46-8.26-9.46s-8.2 3.77-8.2 9.46v.13c0 5.68 3.72 9.45 8.2 9.45s8.26-3.7 8.26-9.45m-25.93-17.19h9.59v4.92a12.37 12.37 0 0 1 10.54-5.56c7.88 0 15.39 6.26 15.39 17.7v.13c0 11.44-7.38 17.7-15.39 17.7a13 13 0 0 1-10.54-5.11V67h-9.59zM191.473 44.72V43a14.64 14.64 0 0 0-6.12-1.28c-4.1 0-6.62 1.66-6.62 4.73v.12c0 2.62 2.14 4.16 5.23 4.16 4.48 0 7.51-2.49 7.51-6M169.463 47v-.13c0-7.48 5.61-10.93 13.62-10.93a23.69 23.69 0 0 1 8.26 1.41v-.58c0-4-2.46-6.26-7.25-6.26a24.56 24.56 0 0 0-9.33 1.85l-2.4-7.41a29.52 29.52 0 0 1 13.12-2.75c5.23 0 9 1.41 11.42 3.84s3.65 6.32 3.65 10.93V56.8h-9.27v-3.71a12.92 12.92 0 0 1-10.22 4.35c-6.37 0-11.6-3.71-11.6-10.48M205.603 39.86v-.12a17.47 17.47 0 0 1 17.104-17.828q.313-.007.626-.002c6.37 0 10.34 2.17 13.49 5.75l-5.86 6.39c-2.15-2.3-4.29-3.77-7.7-3.77-4.79 0-8.2 4.28-8.2 9.33v.13c0 5.24 3.35 9.45 8.58 9.45 3.22 0 5.43-1.4 7.76-3.64l5.61 5.75c-3.28 3.65-7.06 6.27-13.81 6.27A17.38 17.38 0 0 1 205.6 40.415q-.004-.278.002-.555M262.943 37c-.57-4.35-3.09-7.29-7.13-7.29s-6.56 2.88-7.32 7.29zm-23.84 2.87v-.12c0-9.78 6.87-17.83 16.71-17.83 11.29 0 16.47 8.88 16.47 18.59 0 .77-.07 1.67-.13 2.56h-23.53a7.883 7.883 0 0 0 8.26 6.71c3.22 0 5.55-1 8.2-3.52l5.49 4.93a16.81 16.81 0 0 1-13.81 6.39c-10.16 0-17.66-7.23-17.66-17.71" > < / path > < g
fill - rule = "evenodd" > < path
fill = "url(#space-text-white_space-text-white_svg__a)"
d = "M13.583 75a75 75 0 0 0 61.42-43 75 75 0 0 0-61.42-32q-3.27 0-6.57.29A75 75 0 0 0 13.583 75z" > < / path > < path
fill = "url(#space-text-white_space-text-white_svg__b)"
d = "M7.093.3A88.3 88.3 0 0 1 46.553 32h28.45a74.76 74.76 0 0 0-61.35-32q-3.27 0-6.56.3z" > < / path > < path
fill = "url(#space-text-white_space-text-white_svg__c)"
d = "M46.553 32c-3.43 22.67-33 43-33 43 26.89-2.54 50.46-18.64 61.45-43z" > < / path > < / g > < / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
preserveAspectRatio = "xMidYMid"
viewBox = "0 0 20 16"
id = "hamburger" >
< path
d = "M-0.000,16.000 L-0.000,14.000 L20.000,14.000 L20.000,16.000 L-0.000,16.000 ZM-0.000,7.000 L20.000,7.000 L20.000,9.000 L-0.000,9.000 L-0.000,7.000 ZM-0.000,-0.000 L20.000,-0.000 L20.000,2.000 L-0.000,2.000 L-0.000,-0.000 Z" > < / path >
< / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
xmlns: xlink = "http://www.w3.org/1999/xlink"
viewBox = "0 0 18.414 18.415"
id = "close" >
< g >
< path
d = "M1.414,18.415L0,17L17,0l1.414,1.415L1.414,18.415z" > < / path >
< path
d = "M17,18.415L18.414,17l-17-17L0,1.415L17,18.415z" > < / path >
< / g >
< / symbol > < symbol
xmlns = "http://www.w3.org/2000/svg"
viewBox = "0 0 24 24"
id = "more_24" > < circle
cx = "12"
cy = "19"
r = "2" > < / circle > < circle
cx = "12"
cy = "12"
r = "2" > < / circle > < circle
cx = "12"
cy = "5"
r = "2" > < / circle > < / symbol > < / svg >

< !-- Google
Tag
Manager(noscript) -->
< noscript > < iframe
src = "https://www.googletagmanager.com/ns.html?id=GTM-5P98"
height = "0"
width = "0"
style = "display:none;visibility:hidden" > < / iframe > < / noscript >
< !-- End
Google
Tag
Manager(noscript) -->
< script >
/ * ! modernizr
3.2
.0(Custom
Build) | MIT *
*http: // modernizr.com / download /?-flexbox - flexboxtweener ! * /
!function(e, n, t)
{function
r(e, n)
{
return typeof
e == = n}function
o()
{var
e, n, t, o, i, s, l; for (var f in v) if (v.hasOwnProperty(f))
{ if (e
      =[], n=v[f], n.name & & (e.push(n.name.toLowerCase()), n.options & & n.options.aliases & & n.options.aliases.length))for (
t=0;t < n.options.aliases.length;t++)e.push(
    n.options.aliases[t].toLowerCase()); for (o=r(n.fn, "function")?n.fn():n.fn, i = 0;i < e.length;i + +)s = e[
    i], l = s.split("."), 1 == = l.length?Modernizr[l[0]] = o:(
    !Modernizr[l[0]] | | Modernizr[l[0]]instanceof Boolean | | (Modernizr[l[0]]=new Boolean(Modernizr[l[0]])),
Modernizr[l[0]][l[1]] = o), C.push((o?"":"no-") + l.join("-"))}}function
i(e, n)
{
return!!~("" + e).indexOf(n)}function
s(e)
{
return e.replace( / ([a - z]) - ([a - z]) / g, function(e, n, t)
{
return n + t.toUpperCase()}).replace( / ^ - /, "")}function
l(e, n)
{
return function()
{
return e.apply(n, arguments)}}function
f(e, n, t)
{var
o; for (var i in e) if (e[i] in n)
return t ===!1?e[i]: (o=n[e[i]], r(o, "function")?l(o, t | | n): o);return!1}function
a(e)
{
return e.replace( / ([A - Z]) / g, function(e, n)
{
return "-" + n.toLowerCase()}).replace( / ^ ms - /, "-ms-")}function
u()
{
return "function" != typeof
n.createElement?n.createElement(arguments[0]): b?n.createElementNS.call(n, "http://www.w3.org/2000/svg",
                                                                        arguments[0]): n.createElement.apply(n,
                                                                                                             arguments)}function
d()
{var
e = n.body;
return e | | (e=u(b?"svg":"body"), e.fake=!0), e}function
p(e, t, r, o)
{var
i, s, l, f, a = "modernizr", p = u("div"), c = d(); if (parseInt(r, 10))
for (;r--;)l=u("div"), l.id=o?o[r]:a + (r + 1), p.appendChild(l);return i=u(
    "style"), i.type = "text/css", i.id = "s" + a, (c.fake?c:p).appendChild(i), c.appendChild(
    p), i.styleSheet?i.styleSheet.cssText = e:i.appendChild(n.createTextNode(e)), p.id = a, c.fake & & (
    c.style.background
    ="", c.style.overflow="hidden", f=_.style.overflow, _.style.overflow="hidden", _.appendChild(c)), s = t(p,
                                                                                                            e), c.fake?(
c.parentNode.removeChild(c), _.style.overflow=f, _.offsetHeight): p.parentNode.removeChild(p), !!s}function
c(n, r)
{var
o = n.length; if ("CSS" in e & & "supports" in e.CSS)
{
for (;o--;)if (e.CSS.supports(a(n[o]), r))
return!0;
return!1}if (
        "CSSSupportsRule" in e){for (var i=[];o--;)i.push("("+a(n[o])+":"+r+")"); return i=i.join(" or "), p("@supports ("+i+") { #modernizr { position: absolute; } }", function(e){
return "absolute" == getComputedStyle(e, null).position})}return t}function
m(e, n, o, l)
{function
f()
{d & & (delete E.style, delete E.modElem)} if (l=r(l, "undefined")?!1: l, !r(o, "undefined")){var
a = c(e, o); if (!r(a, "undefined"))return a}for (var
d, p, m, h, y, v=["modernizr", "tspan"];!E.style;)d=!0, E.modElem=u(v.shift()), E.style=E.modElem.style; for (m=e.length, p=0;m > p;p++) if (h=e[p], y=E.style[h], i(h, "-") & & (h=s(h)), E.style[h] != =t){if (l | | r(o, "undefined")) return f(), "pfx" == n?h:!
    0;try{E.style[h] = o}catch(g)
{} if (E.style[h] != y)
return f(), "pfx" == n?h:!0}return f(),!1}function
h(e, n, t, o, i)
{var
s = e.charAt(0).toUpperCase() + e.slice(1), l = (e + " " + x.join(s + " ") + s).split(" ");
return r(n, "string") | | r(n, "undefined")?m(l, n, o, i): (l=(e+" "+S.join(s+" ") + s).split(" "), f(l, n, t))}function
y(e, n, r)
{
return h(e, t, t, n, r)}var
v = [], g = {_version: "3.2.0",
             _config: {classPrefix: "", enableClasses:!0, enableJSClass:!0, usePrefixes:!0}, _q: [], on: function(e, n)
{var
t = this;
setTimeout(function()
{n(t[e])}, 0)}, addTest: function(e, n, t)
{v.push({name: e, fn: n, options: t})}, addAsyncTest: function(e)
{v.push({name: null, fn: e})}}, Modernizr = function()
{};
Modernizr.prototype = g, Modernizr = new
Modernizr;
var
C = [], w = "Moz O ms Webkit", x = g._config.usePrefixes?w.split(" "): [];
g._cssomPrefixes = x;
var
S = g._config.usePrefixes?w.toLowerCase().split(" "): [];
g._domPrefixes = S;
var
_ = n.documentElement, b = "svg" == = _.nodeName.toLowerCase(), z = {elem: u("modernizr")};
Modernizr._q.push(function()
{delete
z.elem});var
E = {style: z.elem.style};
Modernizr._q.unshift(function()
{delete
E.style}), g.testAllProps = h, g.testAllProps = y, Modernizr.addTest("flexbox",
                                                                     y("flexBasis", "1px",!0)), Modernizr.addTest(
    "flexboxtweener", y("flexAlign", "end",!0)), o(), delete
g.addTest, delete
g.addAsyncTest; for (var P=0;P < Modernizr._q.length;P++)
Modernizr._q[P]();
e.Modernizr = Modernizr}(window, document);

if (!Modernizr.flexbox & & !Modernizr.flexboxtweener)
{

    var $body = $('body');

var
nodesClasses = {
wrapper: 'not-supported-browser',
container: 'not-supported-browser__container',

title: 'not-supported-browser__title',
content: 'not-supported-browser__content',
logo: 'not-supported-browser__logo'
};

var
nodes = {
wrapper: $('<div class="' + nodesClasses.wrapper + '"></div>'),
title: $('<div class="' + nodesClasses.title + '">Sorry, your browser is not fully supported</div>'),
content: $(
            '<div class="' + nodesClasses.content + '">There may be some issues with pages layout in your current browser.<br/>Please use an alternate browser until we resolve the issues.<br/>Thank you.</div>'),
container: $('<div class="' + nodesClasses.container + '"></div>'),
logo: $(
            '<div class="' + nodesClasses.logo + '"><svg class="sprite-img _jetbrains" xmlns:xlink="http://www.w3.org/1999/xlink"><use xlink:href="#jetbrains"></use></svg></div>')
};

$body.addClass('overflow-hidden');

nodes.content \
    .prepend(nodes.title) \
    .prepend(nodes.logo);

nodes.container \
    .append(nodes.content);

nodes.wrapper
.append(nodes.container)
.appendTo($body);
}
< / script >
    < div


class ="page" >

< div


class ="page__header" >

< div


class ="page__header-language-suggestion" id="language-suggest-bar" > < /div >

< div


class ="page__header-country-suggestion" id="country-suggest-bar" > < /div >

< div


class ="site-header-container" id="js-site-header-container" > < header class ="_siteHeader_m01hi _siteHeaderAdaptive_w40zt _siteHeaderAdaptive_vxxm8 _siteHeaderAdaptive_c8m2ji _siteHeaderAdaptive_5vczf" id="wt-site-header" data-test="site-header" > < div class ="wt-container _siteHeader__contentContainer_lml0p" > < div class ="_siteHeader__inner_mlgw3j _siteHeader__inner_ztf7y _siteHeader__inner_33kd3" > < div class ="_siteHeader__mobileMainMenuExtra_yvnu6 _siteHeader__mobileMainMenuExtra_f2byd" > < button data-test="site-header-close-mobile-main-menu-action" aria-label="Close main menu" type="button" class ="_main_1dh718a_17 _modeClear_1dh718a_478 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _siteHeaderAction_tgwyh _siteHeader__closeMobileMainMenu_souanj" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _siteHeaderAction__icon_qg4ev _siteHeaderAction__icon_vh845f _icon_1dh718a_569" > < path d="M19.707 5.707l-1.414-1.414L12 10.586 5.707 4.293 4.293 5.707 10.586 12l-6.293 6.293 1.414 1.414L12 13.414l6.293 6.293 1.414-1.414L13.414 12l6.293-6.293z" > < /path > < /svg > < /button > < /div > < div class ="wt-row wt-row_align-items_center wt-row_size_0" > < a href="/" class ="_siteLogo_q88txh _siteLogo_ickiz _siteLogo_27by3 _siteLogo_r3sih _siteLogoAdaptive_fz0qqg _siteLogoAdaptive_ggbkhg wt-col-inline _siteHeader__logo_wsxuj _siteHeader__logo_7oske" aria-label="Navigate to main page" data-test="site-logo" > < svg viewBox="0 0 700 700" class ="_siteLogo__image_7g479 _siteLogo__image_ebx71" > < path d="m0 0h700v700h-700z" fill="#000" > < /path > < path d="m60.379 568.75h262.5v43.75h-262.5z" fill="#fff" > < /path > < path d="m57.428 184.315 20.372-19.232c5.542 6.682 10.758 10.594 17.929 10.594 7.823 0 12.877-5.378 12.877-15.972v-72.205h31.457v72.367c0 14.343-3.586 24.448-11.246 32.109-7.5 7.5-18.254 11.572-31.294 11.572-19.885 0-31.946-8.312-40.095-19.233z" fill="#fff" > < /path > < path d="m147.394 87.5h91.762v26.73h-60.468v17.44h54.763v24.937h-54.763v18.092h61.283v26.893h-92.577z" fill="#fff" > < /path > < path d="m280.491 115.208h-34.064v-27.708h99.911v27.708h-34.227v86.384h-31.62z" fill="#fff" > < /path > < path d="m139.736 282.7c10.106-4.4 17.6-12.224 17.6-25.426v-.326a25.675 25.675 0 0 0 -7.336-18.584c-6.682-6.52-16.788-10.106-31.131-10.106h-58.507v114.092h58.838c27.218 0 43.191-11.9 43.191-31.457v-.326c.001-15.484-8.8-23.307-22.655-27.867zm-48.57-29.011h20.7c9.29 0 14.343 3.422 14.343 9.779v.326c0 6.682-5.542 9.942-15.158 9.942h-19.885v-20.051zm39.607 52.808c0 6.682-5.379 10.431-15.158 10.431h-24.449v-21.028h24.123c10.594 0 15.484 4.075 15.484 10.269v.326z" fill="#fff" > < /path > < path d="m335.8 227.444h-30.475l-42.63 101.193-17.833-26.056c14.18-6.031 23.469-17.6 23.469-35.205v-.326c0-11.246-3.422-19.885-10.1-26.567-7.661-7.661-19.722-12.224-37.162-12.224h-53.953v114.091h31.619v-34.55h14.017l22.981 34.553h54.267l8.15-20.536h44.169l8.149 20.536h33.9zm-99.093 42.05c0 8.312-6.357 13.529-16.951 13.529h-21.02v-27.546h20.864c10.432 0 17.114 4.564 17.114 13.692v.325zm70.737 27.706 12.877-32.271 12.712 32.271z" fill="#fff" > < /path > < path d="m388.119 228.258h31.619v114.092h-31.619z" fill="#fff" > < /path > < path d="m427.56 228.258h29.501l46.94 60.306v-60.306h31.294v114.092h-27.545l-48.896-62.587v62.587h-31.294z" fill="#fff" > < /path > < path d="m537.277 325.4 17.6-21.025c11.409 8.964 23.8 13.691 37 13.691 8.638 0 13.2-2.934 13.2-7.824v-.325c0-4.89-3.749-7.335-19.4-11.084-24.286-5.541-43.03-12.387-43.03-35.694v-.326c0-21.188 16.788-36.509 44.17-36.509 19.4 0 34.553 5.216 46.94 15.158l-15.801 22.328c-10.431-7.5-21.84-11.246-31.946-11.246-7.66 0-11.409 3.1-11.409 7.334v.322c0 5.216 3.912 7.5 19.885 11.083 26.078 5.7 42.377 14.18 42.377 35.531v.326c0 23.307-18.418 37.161-46.126 37.161-20.211.005-39.28-6.351-53.46-18.901z" fill="#fff" > < /path > < /svg > < /a > < div class ="wt-col-auto-fill wt-col_align-self_stretch _siteHeader__contentPart_932t4 _siteHeader__desktopContentPart_57b1y _siteHeader__desktopContentPart_87cuc" > < div class ="wt-row wt-row_size_0 wt-row_justify_end _siteHeader__contentPartRow_tkflnh" > < nav class ="_mainMenu_u71uq wt-col-inline" data-test="main-menu" > < div class ="_mainMenuItem_29v65" data-test="main-menu-item" data-test-marker="Developer Tools" > < button type="button" class ="_mainMenuItem__action_6msel _mainMenuItem__action_e0rkwf _mainMenuItem__action_d84ml _mainMenuItem__action_aa1l9 _mainMenuItem__action_a0n8y _mainMenuItem__action_dngujh _mainMenuItem__action_28j9v _mainMenuItem__action_v73y8i _mainMenuItem__action_42uf2 _mainMenuItem__action_07kd4" aria-label="Developer Tools: Open submenu" data-test="main-menu-item-action" > Developer Tools < /button > < div class ="_mainMenuItem__submenuWrapper_dxbj7 _mainMenuItem__submenuWrapper_11ave _mainMenuItem__submenuWrapper_9pejb" > < div class ="_mainMenuItem__submenu_y1dd2 _mainMenuItem__submenu_i0lmy" data-test="main-submenu" > < div class ="_mainSubmenu__body_tph6v _mainSubmenu__body_nnhk5" > < div class ="_mainSubmenu__content_xyg62 _mainSubmenu__content_aflg" > < div class ="_mainSubmenu__columnsWrapper_e7cwuk" > < div class ="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--auto-fill_bybeq" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title" > IDEs < /h5 > < div class ="wt-offset-top-12" > < div class ="_mainSubmenuSubColumns__inner_7pa49h" > < div class ="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--6_watp9g" > < div class ="" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/objc/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > AppCode < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__2" x1="30.221" x2="69.796" y1="63.074" y2="63.074" gradientUnits="userSpaceOnUse" > < stop offset="0.194" stop-color="#07C3F2" > < /stop > < stop offset="0.903" stop-color="#087CFA" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__1" x1="1.274" x2="38.41" y1="16.036" y2="16.036" gradientUnits="userSpaceOnUse" > < stop offset="0.194" stop-color="#07C3F2" > < /stop > < stop offset="0.903" stop-color="#087CFA" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__0" x1="45.876" x2="11.197" y1="72.222" y2="23.824" gradientUnits="userSpaceOnUse" > < stop offset="0.091" stop-color="#21D789" > < /stop > < stop offset="0.484" stop-color="#07C3F2" > < /stop > < stop offset="0.903" stop-color="#087CFA" > < /stop > < /linearGradient > < /defs > < path fill="#087CFA" d="M53.5207 70L69.9999 26.3229L41.5625 19.6875L53.5207 70Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__2)" d="M69.7812 56.1458L53.5208 70L30.1874 64.0208L42 54.5L69.7812 56.1458Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__1)" d="M8.7501 32.0833L1.23969 10.7917L38.4272 0L29.5 21.5L8.7501 32.0833Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__0)" d="M61.1042 40.5417L50.6771 22.75L50.8229 22.6042L38.4271 0L0 41.4896V70L69.7812 56.1458L61.1042 40.5417Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4167 48.65H18.6667V51.3333H34.4167V48.65Z" > < /path > < g fill="#FFF" > < path d="M24.7993 19.13H27.9253L34.5941 34.76H31.0513L29.662 31.2867H23.0627L21.6733 34.76H18.2L24.7993 19.13ZM28.3421 28.2301L26.2581 23.1591L24.1741 28.2301H28.3421Z" > < /path > < path d="M34.6 27.0667C34.6 22.6333 37.8666 18.9 42.7666 18.9C45.8 18.9 47.4333 19.8333 49.0666 21.2333L46.9666 23.8C45.8 22.6333 44.6333 21.9333 43 21.9333C40.4333 21.9333 38.3333 24.0333 38.3333 26.8333C38.3333 29.6333 40.2 31.7333 43 31.7333C44.8666 31.7333 45.8 31.0333 47.2 29.8667L49.3 32.2C47.4333 34.0667 45.5666 35 42.5333 35C37.8666 35 34.6 31.5 34.6 27.0667Z" > < /path > < /g > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/aqua/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > Aqua < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__4" x1="25.657" x2="16.44" y1="58.53" y2="25.272" gradientUnits="userSpaceOnUse" > < stop stop-color="#087CFA" > < /stop > < stop offset="1" stop-color="#6B57FF" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__3" x1="13.002" x2="47.315" y1="63.483" y2="14.124" gradientUnits="userSpaceOnUse" > < stop stop-color="#087CFA" > < /stop > < stop offset="0.387" stop-color="#097FF6" > < /stop > < stop offset="0.96" stop-color="#3BEA62" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__4)" d="M33.084 25.1406L3.47891 17.9053L0 26.1363L10.6717 60.2709L39.0261 70.0002L33.084 25.1406Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__3)" d="M70.0002 20.0238L62.8851 6.09226L26.579 0L10.6719 60.2707L39.0262 70L40.5453 67.5065L70.0002 20.0238Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#fff" d="M34.4165 48.6494H18.6665V51.3327H34.4165V48.6494Z" > < /path > < path fill="#fff" d="M42.3063 19.2559H45.4747L52.1688 34.9866H48.5763L47.1482 31.4835H40.5436L39.1155 34.9866H35.6123L42.3063 19.2559ZM45.921 28.4489L43.8459 23.3837L41.7708 28.4489H45.921V28.4489Z" > < /path > < path fill="#fff" d="M32.884 35.4562L31.1659 33.9166C29.8494 34.7645 28.2652 35.2553 26.5247 35.2553C21.7051 35.2553 18.2466 31.6629 18.2466 27.2227V27.178C18.2466 22.7377 21.7497 19.1006 26.5694 19.1006C31.389 19.1006 34.8475 22.6931 34.8475 27.1334V27.178C34.8475 28.8291 34.3343 30.3688 33.4642 31.6629L35.0707 33.0241L32.884 35.4562V35.4562ZM28.6222 31.6629L26.0785 29.4986L28.2652 27.0441L30.8312 29.3647C31.099 28.74 31.2551 28.0036 31.2551 27.2227V27.178C31.2551 24.5004 29.2916 22.2691 26.5247 22.2691C23.7579 22.2691 21.839 24.4558 21.839 27.1334V27.178C21.839 29.8556 23.8026 32.0869 26.5694 32.0869C27.328 32.0869 28.0197 31.953 28.6222 31.6629V31.6629Z" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/clion/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > CLion < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__8" x1="25.161" x2="45.217" y1="13.686" y2="13.686" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#FF318C" > < /stop > < stop offset="0.149" stop-color="#FB348C" > < /stop > < stop offset="0.285" stop-color="#F03C8C" > < /stop > < stop offset="0.416" stop-color="#DE4A8C" > < /stop > < stop offset="0.543" stop-color="#C45D8B" > < /stop > < stop offset="0.669" stop-color="#A2778B" > < /stop > < stop offset="0.793" stop-color="#79958A" > < /stop > < stop offset="0.913" stop-color="#49B98A" > < /stop > < stop offset="1" stop-color="#21D789" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__7" x1="17.131" x2="6.836" y1="8.883" y2="77.965" gradientUnits="userSpaceOnUse" > < stop offset="0.091" stop-color="#21D789" > < /stop > < stop offset="0.903" stop-color="#009AE5" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__6" x1="63.836" x2="-6.583" y1="6.492" y2="80.865" gradientUnits="userSpaceOnUse" > < stop offset="0.091" stop-color="#21D789" > < /stop > < stop offset="0.903" stop-color="#009AE5" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__5" x1="42.791" x2="66.875" y1="51.126" y2="54.551" gradientUnits="userSpaceOnUse" > < stop offset="0.091" stop-color="#21D789" > < /stop > < stop offset="0.903" stop-color="#009AE5" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__8)" d="M20 41.5L26.6875 0L42.5833 8.82292L20 41.5Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__7)" d="M26.6875 39V0L6.48958 12.7604L0 51.4792L26.6875 39Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__6)" d="M68.6146 21L59.5729 2.69789L42.5833 8.82289L25.1563 27.3437L0 51.4791L22.6771 67.9583L51.2604 42.2187L68.6146 21Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__5)" d="M56.8748 40.1042L45.9373 35L26.7969 55.2344L41.4894 66.2083L58.9894 70L69.9998 45.0625L56.8748 40.1042Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4167 48.65H18.6667V51.3333H34.4167V48.65Z" > < /path > < g fill="#FFF" > < path d="M36 19.13H39.458V31.8553H46.3047V34.76H36V19.13Z" > < /path > < path d="M18 27.0667C18 22.6333 21.2667 18.9 26.1667 18.9C29.2 18.9 30.8333 19.8333 32.4667 21.2333L30.3667 23.8C29.2 22.6333 28.0333 21.9333 26.4 21.9333C23.8333 21.9333 21.7333 24.0333 21.7333 26.8333C21.7333 29.6333 23.6 31.7333 26.4 31.7333C28.2667 31.7333 29.2 31.0333 30.6 29.8667L32.7 32.2C30.8333 34.0667 28.9667 35 25.9333 35C21.2667 35 18 31.5 18 27.0667Z" > < /path > < /g > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/datagrip/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > DataGrip < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__13" x1="64.084" x2="66.131" y1="26.335" y2="44.156" gradientUnits="userSpaceOnUse" > < stop offset="0.16" stop-color="#21D789" > < /stop > < stop offset="0.54" stop-color="#419FBC" > < /stop > < stop offset="1" stop-color="#6B57FF" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__12" x1="45.467" x2="50.644" y1="18.684" y2="5.439" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#6B57FF" > < /stop > < stop offset="0.952" stop-color="#21D789" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__11" x1="16.86" x2="21.888" y1="35.34" y2="57.248" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#6B57FF" > < /stop > < stop offset="0.022" stop-color="#685CFB" > < /stop > < stop offset="0.281" stop-color="#4A91CA" > < /stop > < stop offset="0.506" stop-color="#34B7A7" > < /stop > < stop offset="0.685" stop-color="#26CE91" > < /stop > < stop offset="0.797" stop-color="#21D789" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__10" x1="4.36" x2="65.7" y1="35.008" y2="68.875" gradientUnits="userSpaceOnUse" > < stop offset="0.075" stop-color="#21D789" > < /stop > < stop offset="0.887" stop-color="#6B57FF" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__9" x1="4.735" x2="66.381" y1="26.84" y2="26.84" gradientUnits="userSpaceOnUse" > < stop offset="0.309" stop-color="#21D789" > < /stop > < stop offset="0.487" stop-color="#59A3B2" > < /stop > < stop offset="0.767" stop-color="#B74AF7" > < /stop > < stop offset="1" stop-color="#FF45ED" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__13)" d="M65.5521 10.8646L70 39.5208L61.7604 44.3333L56.5 26.5L65.5521 10.8646Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__12)" d="M65.5521 10.8646L40.4687 0L33.4688 5.83333L45 17L65.5521 10.8646Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__11)" d="M47.3229 70L11 30.5L0.583313 62.4896L47.3229 70Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__10)" d="M54.5 45L0 32.3021L47.3229 70L54.5 45Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__9)" d="M0 0.510406V32.3021L60.7396 53.1562L65.5521 10.8646L0 0.510406Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3333H34.4166V48.6499Z" > < /path > < path fill="#FFF" d="M35.8 27.224C35.8 22.6811 39.3191 18.97 44.118 18.97C46.9973 18.97 48.6608 19.7378 50.3244 21.1455L48.149 23.8328C46.9333 22.8091 45.8455 22.2332 43.99 22.2332C41.4306 22.2332 39.4471 24.4727 39.4471 27.16V27.224C39.4471 30.1033 41.4306 32.2148 44.2459 32.2148C45.5256 32.2148 46.6133 31.8948 47.5091 31.255V29.0155H43.99V26.0083H50.8363V32.8546C49.3007 34.2623 47.0612 35.35 44.1819 35.35C39.1912 35.35 35.8 31.8948 35.8 27.224Z" > < /path > < path fill="#FFF" d="M18.5 19.1334H24.6833C29.7 19.1334 33.0833 22.4876 33.0833 26.8828C33.0833 31.2779 29.7 34.7478 24.6833 34.7478L18.5 34.8634V19.1334ZM22 22.2563V31.7406H24.6833C27.4833 31.7406 29.4667 29.89 29.4667 27.1141C29.4667 24.3382 27.6 22.372 24.6833 22.372L22 22.2563Z" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/dataspell/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > DataSpell < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__17" x1="51.915" x2="5.515" y1="21.235" y2="21.235" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#21D789" > < /stop > < stop offset="0.917" stop-color="#FCF84A" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__16" x1="53.765" x2="53.765" y1="20.208" y2="78.116" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#21D789" > < /stop > < stop offset="1" stop-color="#087CFA" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__15" x1="92.069" x2="23.619" y1="72.972" y2="17.191" gradientUnits="userSpaceOnUse" > < stop offset="0.105" stop-color="#21D789" > < /stop > < stop offset="0.967" stop-color="#087CFA" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__14" x1="60.521" x2="12.274" y1="-5.388" y2="49.291" gradientUnits="userSpaceOnUse" > < stop offset="0.235" stop-color="#21D789" > < /stop > < stop offset="0.74" stop-color="#087CFA" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__17)" d="M44.9896 0L46.375 28.4375L10.9375 42.4375L-1.50998e-07 14.1458L44.9896 0Z" > < /path > < path fill="#21D789" d="M70 16.625L39.375 29.8958L44.9896 0L70 16.625Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__16)" d="M37.5521 23.1874L70 16.6249V47.3229L47.6875 55.7083L38.5729 47.3958L37.5521 23.1874Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__15)" d="M24.0625 14.2188L46.4498 17.6823L70 47.0502L47.3947 55.7812L38.6724 47.1224L24.0625 14.2188Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__14)" d="M14.4375 0L46.375 17.6458L35.3646 70H16.7708L0.656255 53.375L14.4375 0Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.65H18.6666V51.3333H34.4166V48.65Z" > < /path > < path fill="#FFF" d="M19 19H25.1833C30.2 19 33.5833 22.3542 33.5833 26.7493C33.5833 31.1445 30.2 34.6143 25.1833 34.6143L19 34.73V19ZM22.5 22.1229V31.6071H25.1833C27.9833 31.6071 29.9667 29.7565 29.9667 26.9807C29.9667 24.2048 28.1 22.2385 25.1833 22.2385L22.5 22.1229Z" > < /path > < path fill="#FFF" d="M34.97 32.36L37 29.91C38.4 31.1 39.94 31.8 41.69 31.8C43.09 31.8 44 31.24 44 30.33V30.26C44 29.35 43.44 28.93 40.85 28.23C37.63 27.46 35.6 26.55 35.6 23.4V23.33C35.6 20.46 37.91 18.57 41.13 18.57C43.44 18.57 45.4 19.27 47.01 20.6L45.19 23.19C43.79 22.21 42.39 21.65 41.06 21.65C39.73 21.65 39.03 22.28 39.03 23.05V23.12C39.03 24.17 39.73 24.52 42.46 25.22C45.68 26.06 47.5 27.18 47.5 29.98V30.05C47.5 33.2 45.12 34.95 41.69 34.95C39.31 34.88 36.86 34.04 34.97 32.36Z" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/fleet/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > Fleet < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < radialGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__25" cx="0" cy="0" r="1" gradientTransform="matrix(22.35433 -20.58122 27.17129 29.51214 38.648 42.538)" gradientUnits="userSpaceOnUse" > < stop offset="0.771" stop-color="#001AFF" > < /stop > < stop offset="1" stop-color="#8ACEFF" > < /stop > < /radialGradient > < radialGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__24" cx="0" cy="0" r="1" gradientTransform="rotate(-30.543 79.837 -70.068) scale(16.777 22.1489)" gradientUnits="userSpaceOnUse" > < stop offset="0.719" stop-color="#FA00FF" stop-opacity="0" > < /stop > < stop offset="1" stop-color="#FF00D6" stop-opacity="0.44" > < /stop > < /radialGradient > < radialGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__23" cx="0" cy="0" r="1" gradientTransform="rotate(49.385 -19.814 41.858) scale(47.8852)" gradientUnits="userSpaceOnUse" > < stop offset="0.026" stop-color="#8DFDFD" > < /stop > < stop offset="0.271" stop-color="#87FBFB" > < /stop > < stop offset="0.484" stop-color="#74D6F4" > < /stop > < stop offset="0.932" stop-color="#0038FF" > < /stop > < /radialGradient > < radialGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__22" cx="0" cy="0" r="1" gradientTransform="rotate(137.237 9.434 23.195) scale(32.8316)" gradientUnits="userSpaceOnUse" > < stop offset="0.267" stop-color="#0500FF" stop-opacity="0" > < /stop > < stop offset="1" stop-color="#0500FF" stop-opacity="0.15" > < /stop > < /radialGradient > < radialGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__21" cx="0" cy="0" r="1" gradientTransform="rotate(75.198 -4.629 32.631) scale(51.1484)" gradientUnits="userSpaceOnUse" > < stop offset="0.42" stop-color="#FF00E5" stop-opacity="0" > < /stop > < stop offset="0.774" stop-color="#FF00F5" stop-opacity="0.64" > < /stop > < stop offset="0.899" stop-color="#BE46FF" stop-opacity="0.87" > < /stop > < /radialGradient > < radialGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__20" cx="0" cy="0" r="1" gradientTransform="matrix(2.73484 22.75837 -34.39872 4.13365 29.458 35.276)" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#00B2FF" > < /stop > < stop offset="0.571" stop-color="#74C5FF" > < /stop > < stop offset="0.979" stop-color="#9FD7FF" > < /stop > < /radialGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__19" x1="11.644" x2="82.363" y1="42.432" y2="43.401" gradientUnits="userSpaceOnUse" > < stop offset="0.432" stop-color="#FE62EE" stop-opacity="0" > < /stop > < stop offset="0.818" stop-color="#FD3AF5" stop-opacity="0.47" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__18" x1="33.054" x2="37.35" y1="23.191" y2="49.344" gradientUnits="userSpaceOnUse" > < stop offset="0.042" stop-color="#0038FF" > < /stop > < stop offset="0.724" stop-color="#48BFF1" stop-opacity="0.59" > < /stop > < stop offset="1" stop-color="#74C5FF" stop-opacity="0" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__25)" d="M65.153 30.85c0 9.496-10.163 17.194-22.7 17.194-12.536 0-22.699-7.698-22.699-17.194 0-9.496 10.163-17.194 22.7-17.194 12.536 0 22.699 7.698 22.699 17.194z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__24)" d="M65.153 30.85c0 9.496-10.163 17.194-22.7 17.194-12.536 0-22.699-7.698-22.699-17.194 0-9.496 10.163-17.194 22.7-17.194 12.536 0 22.699 7.698 22.699 17.194z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__23)" d="M66 35c0 17.12-13.88 31-31 31C17.88 66 4 52.12 4 35 4 17.88 17.88 4 35 4c8.046 3.642 16.464 17.194 19.99 21.429 3.524 4.235 12.648 9.571 8.176-1.623C65.073 26.832 66 31.852 66 35z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__22)" d="M66 35c0 17.12-13.88 31-31 31C17.88 66 4 52.12 4 35 4 17.88 17.88 4 35 4c8.046 3.642 16.464 17.194 19.99 21.429 3.524 4.235 12.648 9.571 8.176-1.623C65.073 26.832 66 31.852 66 35z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__21)" d="M66 35c0 17.12-13.88 31-31 31C17.88 66 4 52.12 4 35 4 17.88 17.88 4 35 4c8.046 3.642 16.464 17.194 19.99 21.429 3.524 4.235 12.648 9.571 8.176-1.623C65.073 26.832 66 31.852 66 35z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__19)" d="M66 35c0 17.12-13.88 31-31 31C17.88 66 4 52.12 4 35 4 17.88 17.88 4 35 4c8.046 3.642 16.464 17.194 19.99 21.429 3.524 4.235 12.648 9.571 8.176-1.623C65.073 26.832 66 31.852 66 35z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__20)" d="M56.651 39.682c1.658 7.764-6.511 16.089-18.246 18.594-11.734 2.505-22.59-1.757-24.248-9.52-1.658-7.764 6.511-16.089 18.246-18.594 11.734-2.506 22.59 1.757 24.248 9.52z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__18)" d="M56.651 39.682c1.658 7.764-6.511 16.089-18.246 18.594-11.734 2.505-22.59-1.757-24.248-9.52-1.658-7.764 6.511-16.089 18.246-18.594 11.734-2.506 22.59 1.757 24.248 9.52z" > < /path > < path fill="#D6F8F8" fill-opacity="0.19" fill-rule="evenodd" d="M51.462 49.883c3.074-3.133 4.386-6.66 3.698-9.882-.688-3.223-3.326-5.907-7.411-7.51-4.073-1.6-9.412-2.037-15.028-.838-5.616 1.199-10.31 3.779-13.375 6.901-3.074 3.133-4.386 6.66-3.698 9.883.688 3.223 3.326 5.906 7.412 7.51 4.072 1.6 9.41 2.037 15.027.838 5.616-1.2 10.31-3.779 13.375-6.902zm-13.057 8.393c11.735-2.505 19.904-10.83 18.246-18.594-1.658-7.763-12.514-12.026-24.248-9.52-11.735 2.505-19.904 10.83-18.246 18.593 1.658 7.764 12.514 12.026 24.248 9.521z" clip-rule="evenodd" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/go/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > GoLand < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__28" x1="68.929" x2="41.588" y1="39.874" y2="63.009" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#087CFA" > < /stop > < stop offset="0.023" stop-color="#0D7BFA" > < /stop > < stop offset="0.373" stop-color="#5566F9" > < /stop > < stop offset="0.663" stop-color="#8A57F8" > < /stop > < stop offset="0.881" stop-color="#AB4EF7" > < /stop > < stop offset="1" stop-color="#B74AF7" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__27" x1="24.089" x2="40.706" y1="21.699" y2="2.794" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#087CFA" > < /stop > < stop offset="0.023" stop-color="#0D7BFA" > < /stop > < stop offset="0.373" stop-color="#5566F9" > < /stop > < stop offset="0.663" stop-color="#8A57F8" > < /stop > < stop offset="0.881" stop-color="#AB4EF7" > < /stop > < stop offset="1" stop-color="#B74AF7" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__26" x1="9.725" x2="60.22" y1="61.15" y2="28.702" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#087CFA" > < /stop > < stop offset="0.102" stop-color="#1598D3" > < /stop > < stop offset="0.225" stop-color="#23B6AA" > < /stop > < stop offset="0.345" stop-color="#2DCC8B" > < /stop > < stop offset="0.462" stop-color="#35DD74" > < /stop > < stop offset="0.572" stop-color="#39E767" > < /stop > < stop offset="0.67" stop-color="#3BEA62" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__28)" d="M61.6875 27.0521L70 45.5729L55.7083 70L38.5 42L61.6875 27.0521Z" > < /path > < path fill="#B74AF7" d="M44.5 44L55.7083 70L33.6146 62.4167L44.5 44Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__27)" d="M49.2917 19.7604L44.7708 0H19.6146L0 30.0417L5.6875 43.8229L0 56.4375L49.2917 37V19.7604Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__26)" d="M70 14.875L40.6146 21.8021L0 56.4375L26.25 70L46.9583 48.6354L70 14.875Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z" > < /path > < path fill="#FFF" d="M18 27.224C18 22.6811 21.5191 18.97 26.318 18.97C29.1973 18.97 30.8609 19.7378 32.5244 21.1454L30.349 23.8328C29.1333 22.809 28.0455 22.2332 26.19 22.2332C23.6306 22.2332 21.6471 24.4726 21.6471 27.16V27.224C21.6471 30.1033 23.6306 32.2147 26.4459 32.2147C27.7256 32.2147 28.8134 31.8948 29.7091 31.255V29.0155H26.19V26.0083H33.0363V32.8546C31.5007 34.2622 29.2612 35.35 26.382 35.35C21.3912 35.35 18 31.8948 18 27.224Z" > < /path > < path fill="#FFF" d="M34.572 27.224C34.572 22.6811 38.0911 18.97 43.0179 18.97C47.8807 18.97 51.3998 22.6171 51.3998 27.096V27.16C51.3998 31.6389 47.8807 35.35 42.9539 35.35C38.0911 35.35 34.572 31.7029 34.572 27.224ZM47.7527 27.224C47.7527 24.4726 45.7692 22.2332 42.9539 22.2332C40.1386 22.2332 38.2191 24.4726 38.2191 27.16V27.224C38.2191 29.9113 40.2026 32.2147 43.0179 32.2147C45.8332 32.1508 47.7527 29.9753 47.7527 27.224Z" > < /path > < /svg > < /span > < /a > < /div > < /div > < /div > < div class ="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--6_watp9g" > < div class ="" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/idea/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > IntelliJ & nbsp;IDEA < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__31" x1="5.174" x2="40.014" y1="39.889" y2="38.123" gradientUnits="userSpaceOnUse" > < stop offset="0.091" stop-color="#FC801D" > < /stop > < stop offset="0.231" stop-color="#B07F61" > < /stop > < stop offset="0.409" stop-color="#577DB3" > < /stop > < stop offset="0.533" stop-color="#1E7CE6" > < /stop > < stop offset="0.593" stop-color="#087CFA" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__30" x1="61.991" x2="50.158" y1="36.915" y2="1.557" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#FE2857" > < /stop > < stop offset="0.078" stop-color="#CB3979" > < /stop > < stop offset="0.16" stop-color="#9E4997" > < /stop > < stop offset="0.247" stop-color="#7557B2" > < /stop > < stop offset="0.339" stop-color="#5362C8" > < /stop > < stop offset="0.436" stop-color="#386CDA" > < /stop > < stop offset="0.541" stop-color="#2373E8" > < /stop > < stop offset="0.658" stop-color="#1478F2" > < /stop > < stop offset="0.794" stop-color="#0B7BF8" > < /stop > < stop offset="1" stop-color="#087CFA" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__29" x1="10.066" x2="53.876" y1="16.495" y2="88.96" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#FE2857" > < /stop > < stop offset="0.08" stop-color="#FE295F" > < /stop > < stop offset="0.206" stop-color="#FF2D76" > < /stop > < stop offset="0.303" stop-color="#FF318C" > < /stop > < stop offset="0.385" stop-color="#EA3896" > < /stop > < stop offset="0.553" stop-color="#B248AE" > < /stop > < stop offset="0.792" stop-color="#5A63D6" > < /stop > < stop offset="1" stop-color="#087CFA" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__31)" d="M11.2 49.4668L0.699951 41.3001L9 26L18.5 33.5L11.2 49.4668Z" > < /path > < path fill="#087CFA" d="M69.9999 18.6666L68.8333 59.2666L41.7666 70L27.0666 60.4333L41.7666 37.5L69.9999 18.6666Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__30)" d="M70 18.6666L55.5 33L37 15L48.0666 1.16663L70 18.6666Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__29)" d="M27.0667 60.4333L5.6 68.3667L10.0333 52.5L15.8667 33.1333L0 27.7667L10.0333 0L33.1333 2.8L54.5 31L55.5 33L27.0667 60.4333Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < g fill="#FFF" > < path d="M27.1366 22.1433V19.25H19.2733V22.1433H21.4666V32.1067H19.2733V34.9767H27.1366V32.1067H24.92V22.1433H27.1366Z" > < /path > < path d="M34.6967 35.21C33.46 35.21 32.4334 34.9767 31.6167 34.51C30.7767 34.0433 30.1 33.4833 29.5634 32.8533L31.7334 30.4267C32.1767 30.9167 32.6434 31.3133 33.0867 31.5933C33.5534 31.8733 34.0434 32.0133 34.6034 32.0133C35.2567 32.0133 35.77 31.8033 36.1434 31.3833C36.5167 30.9633 36.7034 30.31 36.7034 29.4V19.2733H40.25V29.5633C40.25 30.4967 40.1334 31.3133 39.8767 32.0133C39.62 32.7133 39.2467 33.2967 38.78 33.7633C38.29 34.2533 37.7067 34.6033 37.0067 34.86C36.3067 35.0933 35.5367 35.21 34.6967 35.21Z" > < /path > < path d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z" > < /path > < /g > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/phpstorm/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > PhpStorm < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__35" x1="17.617" x2="23.56" y1="21.533" y2="9.655" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#AF1DF5" > < /stop > < stop offset="0.21" stop-color="#BC20E4" > < /stop > < stop offset="0.63" stop-color="#DD29B8" > < /stop > < stop offset="1" stop-color="#FF318C" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__34" x1="2.258" x2="31.498" y1="48.027" y2="9.401" gradientUnits="userSpaceOnUse" > < stop offset="0.02" stop-color="#6B57FF" > < /stop > < stop offset="0.42" stop-color="#B74AF7" > < /stop > < stop offset="0.75" stop-color="#FF318C" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__33" x1="53.04" x2="35.657" y1="47.667" y2="6.426" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#293896" > < /stop > < stop offset="0.08" stop-color="#3B3AA2" > < /stop > < stop offset="0.29" stop-color="#6740C0" > < /stop > < stop offset="0.49" stop-color="#8A44D8" > < /stop > < stop offset="0.68" stop-color="#A347E9" > < /stop > < stop offset="0.86" stop-color="#B249F3" > < /stop > < stop offset="1" stop-color="#B74AF7" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__32" x1="50.044" x2="23.634" y1="61.283" y2="22.588" gradientUnits="userSpaceOnUse" > < stop offset="0.02" stop-color="#6B57FF" > < /stop > < stop offset="0.78" stop-color="#B74AF7" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__35)" d="M38.6458 12.3228L36.3125 5.24996L11.9583 0L0 13.4895L13.125 20.1978L34.9271 30.0415L38.6458 12.3228Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__34)" d="M26.9792 20.489L0 13.489L6.63542 53.5929L26.4687 53.52L26.9792 20.489Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__33)" d="M18.9582 25.6665L34.0519 12.2499L43.2394 4.15625L60.8853 7.43748L69.9999 30.0415L56.8749 43.0935L18.9582 25.6665Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__32)" d="M49.9479 17.0628L14.2188 16.917L19.25 56.073L20.1979 61.7604L43.8958 70L70 54.323L49.9479 17.0628Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z" > < /path > < path fill="#FFF" d="M32.97 32.76L35 30.31C36.4 31.5 37.94 32.2 39.69 32.2C41.09 32.2 42 31.64 42 30.73V30.66C42 29.75 41.44 29.33 38.85 28.63C35.63 27.86 33.6 26.95 33.6 23.8V23.73C33.6 20.86 35.91 18.97 39.13 18.97C41.44 18.97 43.4 19.67 45.01 21L43.19 23.59C41.79 22.61 40.39 22.05 39.06 22.05C37.73 22.05 37.03 22.68 37.03 23.45V23.52C37.03 24.57 37.73 24.92 40.46 25.62C43.68 26.46 45.5 27.58 45.5 30.38V30.45C45.5 33.6 43.12 35.35 39.69 35.35C37.31 35.28 34.86 34.44 32.97 32.76Z" > < /path > < path fill="#FFF" d="M19.25 19.25H25.69C29.47 19.25 31.71 21.49 31.71 24.71V24.78C31.71 28.42 28.91 30.31 25.34 30.31H22.68V35H19.25V19.25ZM25.48 27.16C27.23 27.16 28.21 26.11 28.21 24.78V24.71C28.21 23.17 27.16 22.33 25.41 22.33H22.75V27.16H25.48Z" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/pycharm/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > PyCharm < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__40" x1="24.999" x2="66.656" y1="27.046" y2="27.046" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#21D789" > < /stop > < stop offset="1" stop-color="#07C3F2" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__39" x1="-24.559" x2="61.22" y1="59.081" y2="-4.241" gradientUnits="userSpaceOnUse" > < stop offset="0.011" stop-color="#FCF84A" > < /stop > < stop offset="0.112" stop-color="#A7EB62" > < /stop > < stop offset="0.206" stop-color="#5FE077" > < /stop > < stop offset="0.273" stop-color="#32DA84" > < /stop > < stop offset="0.306" stop-color="#21D789" > < /stop > < stop offset="0.577" stop-color="#21D789" > < /stop > < stop offset="0.597" stop-color="#21D789" > < /stop > < stop offset="0.686" stop-color="#20D68C" > < /stop > < stop offset="0.763" stop-color="#1ED497" > < /stop > < stop offset="0.835" stop-color="#19D1A9" > < /stop > < stop offset="0.904" stop-color="#13CCC2" > < /stop > < stop offset="0.971" stop-color="#0BC6E1" > < /stop > < stop offset="1" stop-color="#07C3F2" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__38" x1="9.33" x2="23.637" y1="77.654" y2="32.76" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#21D789" > < /stop > < stop offset="0.16" stop-color="#24D888" > < /stop > < stop offset="0.298" stop-color="#2FD985" > < /stop > < stop offset="0.427" stop-color="#41DC80" > < /stop > < stop offset="0.552" stop-color="#5AE079" > < /stop > < stop offset="0.673" stop-color="#7AE46F" > < /stop > < stop offset="0.791" stop-color="#A1EA64" > < /stop > < stop offset="0.904" stop-color="#CFF157" > < /stop > < stop offset="1" stop-color="#FCF84A" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__37" x1="28.275" x2="59.409" y1="38.623" y2="-3.236" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#21D789" > < /stop > < stop offset="0.093" stop-color="#23D986" > < /stop > < stop offset="0.172" stop-color="#2ADE7B" > < /stop > < stop offset="0.247" stop-color="#36E669" > < /stop > < stop offset="0.271" stop-color="#3BEA62" > < /stop > < stop offset="0.35" stop-color="#47EB61" > < /stop > < stop offset="0.494" stop-color="#67ED5D" > < /stop > < stop offset="0.686" stop-color="#9AF156" > < /stop > < stop offset="0.915" stop-color="#E0F64D" > < /stop > < stop offset="1" stop-color="#FCF84A" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__36" x1="75.889" x2="13.158" y1="43.95" y2="43.369" gradientUnits="userSpaceOnUse" > < stop offset="0.387" stop-color="#FCF84A" > < /stop > < stop offset="0.463" stop-color="#ECF74C" > < /stop > < stop offset="0.611" stop-color="#C1F451" > < /stop > < stop offset="0.815" stop-color="#7EEF5A" > < /stop > < stop offset="1" stop-color="#3BEA62" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__40)" d="M49 10.9668L69.5333 28.0001L62.0666 42.9335L49.9333 39.6668H39.2L49 10.9668Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__39)" d="M28.4667 22.1667L24.5 42.9333L24.0333 50.1667L14.2333 54.6L0 56L4.2 10.7333L29.8667 0L45.7333 10.2667L28.4667 22.1667Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__38)" d="M28.4667 22.1667L30.3333 62.5334L24.0333 70.0001L0 56.0001L19.6 26.6001L28.4667 22.1667Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__37)" d="M54.8333 19.1333H30.5666L52.0333 0L54.8333 19.1333Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__36)" d="M70 62.5333L48.5334 69.7667L20.3 61.8333L28.4667 22.1667L31.7334 19.1333L49 17.5L47.6 35L61.3667 29.6333L70 62.5333Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M19.1333 19.1333H25.55C29.2833 19.1333 31.6167 21.35 31.6167 24.6166C31.6167 28.2333 28.8167 30.1 25.2 30.1H22.5167V34.7666H19.0167V19.1333H19.1333ZM25.3167 27.1833C27.0667 27.1833 28 26.0166 28 24.7333C28 23.2166 26.95 22.4 25.2 22.4H22.5167V27.1833H25.3167Z" > < /path > < path fill="#FFF" d="M33.6 27.0666C33.6 22.6332 36.8667 18.8999 41.7667 18.8999C44.8 18.8999 46.4334 19.8332 48.0667 21.2332L45.9667 23.7999C44.8 22.6332 43.6334 21.9332 42 21.9332C39.4334 21.9332 37.3334 24.0332 37.3334 26.8332C37.3334 29.6332 39.2 31.7332 42 31.7332C43.8667 31.7332 44.8 31.0332 46.2 29.8666L48.3 32.1999C46.4334 34.0666 44.5667 34.9999 41.5334 34.9999C36.8667 34.9999 33.6 31.4999 33.6 27.0666Z" > < /path > < path fill="#FFF" d="M34.4167 48.6499H18.6667V51.3332H34.4167V48.6499Z" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/rider/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > Rider < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__43" x1="65.5" x2="11.542" y1="40.101" y2="9.137" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#DD1265" > < /stop > < stop offset="0.483" stop-color="#DD1265" > < /stop > < stop offset="0.942" stop-color="#FDB60D" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__42" x1="33.416" x2="54.805" y1="6.112" y2="65.175" gradientUnits="userSpaceOnUse" > < stop offset="0.139" stop-color="#087CFA" > < /stop > < stop offset="0.476" stop-color="#DD1265" > < /stop > < stop offset="0.958" stop-color="#087CFA" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__41" x1="17.395" x2="33.194" y1="7.934" y2="64.079" gradientUnits="userSpaceOnUse" > < stop offset="0.278" stop-color="#DD1265" > < /stop > < stop offset="0.968" stop-color="#FDB60D" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__43)" d="M70 27.2708L20.9272 0L53.8125 48.8542L60.5209 44.4063L70 27.2708Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__42)" d="M50.4583 16.1146L44.2604 1.09375L30.6979 14.5104L36.2395 63.0729L49.4374 70L69.9999 57.9688L50.4583 16.1146Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__41)" d="M20.927 0L0 14.0729L7.80207 62.1979L27.8541 69.8542L53.8124 48.8542L20.927 0Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z" > < /path > < path fill="#FFF" d="M35.5 19.25H41.6833C46.7 19.25 50.0833 22.6042 50.0833 26.9993C50.0833 31.3945 46.7 34.8643 41.6833 34.8643L35.5 34.98V19.25ZM39 22.3729V31.8571H41.6833C44.4833 31.8571 46.4667 30.0065 46.4667 27.2307C46.4667 24.4548 44.6 22.4885 41.6833 22.4885L39 22.3729Z" > < /path > < path fill="#FFF" d="M19.3399 19.25H26.5408C28.5682 19.25 30.0363 19.8093 31.1549 20.858C32.0638 21.7668 32.4832 22.9553 32.4832 24.4234V24.4933C32.4832 25.7517 32.2036 26.8004 31.5744 27.6393C30.9452 28.4084 30.1062 29.0376 29.1275 29.3871L32.9726 34.98H28.9178L25.6319 30.1561H22.7656V34.98H19.27V19.25H19.3399ZM26.331 26.8703C27.17 26.8703 27.8691 26.6606 28.2886 26.2411C28.7779 25.8216 28.9877 25.2624 28.9877 24.6332V24.5632C28.9877 23.7942 28.7779 23.2349 28.2886 22.8854C27.7992 22.5358 27.17 22.3261 26.2611 22.3261H22.8355V26.8703H26.331Z" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/ruby/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > RubyMine < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__46" x1="44.877" x2="36.032" y1="40.487" y2="17.268" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#FE2857" > < /stop > < stop offset="0.056" stop-color="#FE3052" > < /stop > < stop offset="0.325" stop-color="#FD533B" > < /stop > < stop offset="0.58" stop-color="#FC6C2A" > < /stop > < stop offset="0.811" stop-color="#FC7B20" > < /stop > < stop offset="1" stop-color="#FC801D" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__45" x1="28.02" x2="41.687" y1="7.252" y2="19.779" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#6B57FF" > < /stop > < stop offset="1" stop-color="#FE2857" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__44" x1="0.306" x2="45.3" y1="11.212" y2="68.408" gradientUnits="userSpaceOnUse" > < stop offset="0.001" stop-color="#6B57FF" > < /stop > < stop offset="0.297" stop-color="#FE2857" > < /stop > < stop offset="0.629" stop-color="#FE2857" > < /stop > < stop offset="0.641" stop-color="#FE3052" > < /stop > < stop offset="0.701" stop-color="#FD533B" > < /stop > < stop offset="0.757" stop-color="#FC6C2A" > < /stop > < stop offset="0.808" stop-color="#FC7B20" > < /stop > < stop offset="0.85" stop-color="#FC801D" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__46)" d="M58.1875 0L38.2083 7.14583L22.3854 0L17.2084 13.125H13.8542V51.7708L62.4166 52.2083L70 13.7083L58.1875 0Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__45)" d="M57.6042 25.1563L25.6667 6.125L57.6042 43.6771V25.1563Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__44)" d="M29.1666 68.1771L55.2708 64.6771L51.2604 56.875L48.8541 51.7709L51.2604 47.5782L55.2708 39.3751L25.5937 6.125L0 12.3958V49.1458L14.7292 70L29.0208 68.1771H29.0937H29.1666Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z" > < /path > < path fill="#FFF" d="M34.8601 19.25H38.6353L42.7601 25.8916L46.8848 19.25H50.66V34.98H47.1645V24.7031L42.7601 31.4145H42.6902L38.2857 24.773V34.98H34.8601V19.25Z" > < /path > < path fill="#FFF" d="M19.3399 19.25H26.5408C28.5682 19.25 30.0363 19.8093 31.1549 20.858C32.0638 21.7668 32.4832 22.9553 32.4832 24.4234V24.4933C32.4832 25.7517 32.2036 26.8004 31.5744 27.6393C30.9452 28.4084 30.1062 29.0376 29.1275 29.3871L32.9726 34.98H28.9178L25.6319 30.1561H22.7656V34.98H19.27V19.25H19.3399ZM26.331 26.8703C27.17 26.8703 27.8691 26.6606 28.2886 26.2411C28.7779 25.8216 28.9877 25.2624 28.9877 24.6332V24.5632C28.9877 23.7942 28.7779 23.2349 28.2886 22.8854C27.7992 22.5358 27.17 22.3261 26.2611 22.3261H22.8355V26.8703H26.331Z" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/webstorm/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > WebStorm < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__49" x1="25.068" x2="43.183" y1="1.46" y2="66.675" gradientUnits="userSpaceOnUse" > < stop offset="0.285" stop-color="#07C3F2" > < /stop > < stop offset="0.941" stop-color="#087CFA" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__48" x1="30.72" x2="61.365" y1="9.734" y2="54.671" gradientUnits="userSpaceOnUse" > < stop offset="0.14" stop-color="#FCF84A" > < /stop > < stop offset="0.366" stop-color="#07C3F2" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__47" x1="61.082" x2="65.106" y1="15.29" y2="29.544" gradientUnits="userSpaceOnUse" > < stop offset="0.285" stop-color="#07C3F2" > < /stop > < stop offset="0.941" stop-color="#087CFA" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__49)" d="M9.40625 63.2918L0 7.36466L17.4271 0.072998L28.5833 6.70841L38.7917 1.23966L60.0833 9.40633L48.125 70.0001L9.40625 63.2918Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__48)" d="M69.9999 23.6979L60.9582 1.38542L44.552 0L19.2499 24.2813L26.104 55.6354L38.7915 64.5313L69.9999 46.0104L62.3436 31.7188L69.9999 23.6979Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__47)" d="M55.9999 20.3438L62.3436 31.7188L69.9999 23.6979L64.3853 9.84375L55.9999 20.3438Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z" > < /path > < path fill="#FFF" d="M34.16 19.25L31.78 28.42L29.12 19.25H26.46L23.8 28.42L21.42 19.25H17.78L22.26 35H25.2L27.79 25.9L30.31 35H33.32L37.8 19.25H34.16Z" > < /path > < path fill="#FFF" d="M38.5 32.76L40.53 30.31C41.93 31.5 43.47 32.2 45.22 32.2C46.62 32.2 47.53 31.64 47.53 30.73V30.66C47.53 29.75 46.97 29.33 44.38 28.63C41.23 27.79 39.13 26.95 39.13 23.8V23.73C39.13 20.86 41.44 18.97 44.66 18.97C46.97 18.97 48.93 19.67 50.54 21L48.72 23.59C47.32 22.61 45.92 22.05 44.59 22.05C43.26 22.05 42.56 22.68 42.56 23.45V23.52C42.56 24.57 43.26 24.92 45.99 25.62C49.21 26.46 51.03 27.58 51.03 30.38V30.45C51.03 33.6 48.65 35.35 45.22 35.35C42.77 35.28 40.39 34.44 38.5 32.76Z" > < /path > < /svg > < /span > < /a > < /div > < /div > < /div > < /div > < /div > < /div > < div class ="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--inline_hper7" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title" > PLUGINS & amp; SERVICES < /h5 > < div class ="wt-offset-top-12" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://plugins.jetbrains.com/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > All Plugins < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://plugins.jetbrains.com/search?tags=Theme" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > IDE Themes < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://plugins.jetbrains.com/plugin/12494-big-data-tools" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Big Data Tools < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/code-with-me/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Code With Me < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/riderflow/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > RiderFlow < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/rust/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Rust < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://plugins.jetbrains.com/plugin/1347-scala" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Scala < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/toolbox-app/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Toolbox App < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/toolbox-enterprise/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Toolbox Enterprise < /span > < /span > < /a > < /div > < /div > < /div > < div class ="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--inline_hper7 _mainSubmenu__columnSeparated_fyc7bf" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title" >.NET & amp; VISUAL STUDIO < /h5 > < div class ="wt-offset-top-12" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/rider/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > Rider < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__52" x1="65.5" x2="11.542" y1="40.101" y2="9.137" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#DD1265" > < /stop > < stop offset="0.483" stop-color="#DD1265" > < /stop > < stop offset="0.942" stop-color="#FDB60D" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__51" x1="33.416" x2="54.805" y1="6.112" y2="65.175" gradientUnits="userSpaceOnUse" > < stop offset="0.139" stop-color="#087CFA" > < /stop > < stop offset="0.476" stop-color="#DD1265" > < /stop > < stop offset="0.958" stop-color="#087CFA" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__50" x1="17.395" x2="33.194" y1="7.934" y2="64.079" gradientUnits="userSpaceOnUse" > < stop offset="0.278" stop-color="#DD1265" > < /stop > < stop offset="0.968" stop-color="#FDB60D" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__52)" d="M70 27.2708L20.9272 0L53.8125 48.8542L60.5209 44.4063L70 27.2708Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__51)" d="M50.4583 16.1146L44.2604 1.09375L30.6979 14.5104L36.2395 63.0729L49.4374 70L69.9999 57.9688L50.4583 16.1146Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__50)" d="M20.927 0L0 14.0729L7.80207 62.1979L27.8541 69.8542L53.8124 48.8542L20.927 0Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z" > < /path > < path fill="#FFF" d="M35.5 19.25H41.6833C46.7 19.25 50.0833 22.6042 50.0833 26.9993C50.0833 31.3945 46.7 34.8643 41.6833 34.8643L35.5 34.98V19.25ZM39 22.3729V31.8571H41.6833C44.4833 31.8571 46.4667 30.0065 46.4667 27.2307C46.4667 24.4548 44.6 22.4885 41.6833 22.4885L39 22.3729Z" > < /path > < path fill="#FFF" d="M19.3399 19.25H26.5408C28.5682 19.25 30.0363 19.8093 31.1549 20.858C32.0638 21.7668 32.4832 22.9553 32.4832 24.4234V24.4933C32.4832 25.7517 32.2036 26.8004 31.5744 27.6393C30.9452 28.4084 30.1062 29.0376 29.1275 29.3871L32.9726 34.98H28.9178L25.6319 30.1561H22.7656V34.98H19.27V19.25H19.3399ZM26.331 26.8703C27.17 26.8703 27.8691 26.6606 28.2886 26.2411C28.7779 25.8216 28.9877 25.2624 28.9877 24.6332V24.5632C28.9877 23.7942 28.7779 23.2349 28.2886 22.8854C27.7992 22.5358 27.17 22.3261 26.2611 22.3261H22.8355V26.8703H26.331Z" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/resharper/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > ReSharper < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__55" x1="34.448" x2="64.631" y1="70.146" y2="26.155" gradientUnits="userSpaceOnUse" > < stop offset="0.016" stop-color="#FF45ED" > < /stop > < stop offset="0.4" stop-color="#DD1265" > < /stop > < stop offset="1" stop-color="#FDB60D" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__54" x1="1.828" x2="48.825" y1="53.428" y2="9.226" gradientUnits="userSpaceOnUse" > < stop offset="0.016" stop-color="#FF45ED" > < /stop > < stop offset="0.661" stop-color="#DD1265" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__53" x1="47.598" x2="48.08" y1="-1.658" y2="26.117" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#DD1265" > < /stop > < stop offset="0.055" stop-color="#DF1961" > < /stop > < stop offset="0.701" stop-color="#F46330" > < /stop > < stop offset="1" stop-color="#FC801D" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__55)" d="M51.1974 15.7209L26.3802 47.0706L20.7823 70H58.4484L70 23.0666L51.1974 15.7209Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__54)" d="M48.9858 0H11.6129L0 47.0707H55.6073L48.9858 0Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__53)" d="M50.9338 13.3164L48.9858 0L44.782 13.3164H50.9338Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z" > < /path > < path fill="#FFF" d="M36.0781 31.3592L34.3704 31.3592L34.3703 28.4832L36.5725 28.4832L37.1343 25.1573L35.1567 25.1573L35.1566 22.2812L37.6288 22.2813L38.19 19.0007L41.1567 19.0008L40.5949 22.2814L43.8536 22.2815L44.4147 19.0009L47.3814 19.001L46.8196 22.2816L48.5273 22.2816L48.5274 25.1577L46.3252 25.1576L45.7634 28.4835L47.741 28.4835L47.7411 31.3596L45.2696 31.3595L44.6852 34.73L41.7191 34.7299L42.3029 31.3594L39.0448 31.3593L38.4604 34.7299L35.4943 34.7298L36.0781 31.3592ZM42.7973 28.4834L43.3591 25.1575L40.1004 25.1574L39.5387 28.4833L42.7973 28.4834Z" > < /path > < path fill="#FFF" d="M19 19L26.1868 19.0002C28.1783 19.0003 29.7056 19.5316 30.7688 20.5941C31.2255 21.0702 31.5805 21.6344 31.8121 22.2521C32.0437 22.8699 32.1471 23.5284 32.116 24.1874V24.2327C32.1656 25.3452 31.837 26.4416 31.1836 27.3434C30.5549 28.1499 29.7101 28.7613 28.7474 29.1063L32.5883 34.7207L28.5456 34.7206L25.2918 29.8921L22.4396 29.892L22.4593 34.7204L19.0005 34.7203L19 19ZM25.9625 26.6354C26.6701 26.6828 27.3702 26.4668 27.9281 26.0289C28.1546 25.8268 28.3335 25.5769 28.4519 25.2973C28.5703 25.0177 28.6252 24.7153 28.6126 24.4119V24.3673C28.6348 24.0496 28.5812 23.7312 28.4561 23.4383C28.3311 23.1455 28.1382 22.8865 27.8934 22.6829C27.3089 22.2772 26.6052 22.0796 25.895 22.1216L22.4589 22.1215L22.459 26.6353L25.9625 26.6354Z" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/resharper-cpp/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > ReSharper C++ < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__58" x1="5.126" x2="26.323" y1="17.302" y2="70.918" gradientUnits="userSpaceOnUse" > < stop offset="0.22" stop-color="#DD1265" > < /stop > < stop offset="0.736" stop-color="#FF45ED" > < /stop > < stop offset="1" stop-color="#FDB60D" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__57" x1="52.282" x2="0.445" y1="73.292" y2="18.152" gradientUnits="userSpaceOnUse" > < stop offset="0.113" stop-color="#FDB60D" > < /stop > < stop offset="0.509" stop-color="#FF45ED" > < /stop > < stop offset="0.765" stop-color="#FF45ED" > < /stop > < stop offset="1" stop-color="#FDB60D" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__56" x1="25.5" x2="69.96" y1="-1.93" y2="51.168" gradientUnits="userSpaceOnUse" > < stop offset="0.175" stop-color="#FDB60D" > < /stop > < stop offset="0.49" stop-color="#FF45ED" > < /stop > < stop offset="0.819" stop-color="#DD1265" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__58)" d="M18.894 15.6855L16.8323 52.3261L11.5517 70L0 23.0667L18.894 15.6855Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__57)" d="M18.8942 15.6854L21.0145 0L49.2185 69.9999H11.5519L16.8325 52.326L18.8942 15.6854Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__56)" d="M35.2592 47.0706H70L58.3871 0H21.0142L35.2592 47.0706Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z" > < /path > < path fill="#FFF" d="M19 19L26.2892 19.0002C28.309 19.0003 29.8581 19.5391 30.9364 20.6168C31.3996 21.0997 31.7597 21.6719 31.9946 22.2985C32.2295 22.925 32.3344 23.5929 32.3029 24.2613V24.3073C32.3532 25.4356 32.0198 26.5476 31.3572 27.4622C30.7195 28.2803 29.8626 28.9003 28.8862 29.2503L32.7818 34.9446L28.6816 34.9445L25.3814 30.0472L22.4886 30.0472L22.5085 34.9443L19.0005 34.9442L19 19ZM26.0616 26.7442C26.7793 26.7923 27.4894 26.5732 28.0552 26.1291C28.285 25.924 28.4665 25.6706 28.5865 25.387C28.7066 25.1034 28.7622 24.7967 28.7495 24.489V24.4437C28.772 24.1215 28.7177 23.7986 28.5908 23.5016C28.464 23.2045 28.2683 22.9419 28.02 22.7354C27.4272 22.3239 26.7135 22.1234 25.9932 22.1661L22.5081 22.166L22.5083 26.7441L26.0616 26.7442Z" > < /path > < path fill="#FFF" d="M43.872 24.2626H40.2574V21.0512H43.872V17.46H47.1766V21.0512H50.7912V24.2626H47.1766V27.8539H43.872V24.2626Z" > < /path > < path fill="#FFF" d="M36.9551 32.9623H33.3406V29.7509H36.9551V26.1597H40.2598V29.7509H43.8743V32.9623H40.2598V36.5536H36.9551V32.9623Z" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/dotcover/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > dotCover < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__60" x1="37.049" x2="23.558" y1="55.637" y2="5.422" gradientUnits="userSpaceOnUse" > < stop offset="0.048" stop-color="#6B57FF" > < /stop > < stop offset="0.12" stop-color="#7556FE" > < /stop > < stop offset="0.241" stop-color="#8F53FB" > < /stop > < stop offset="0.395" stop-color="#BA4DF5" > < /stop > < stop offset="0.576" stop-color="#F446EE" > < /stop > < stop offset="0.608" stop-color="#FF45ED" > < /stop > < stop offset="0.69" stop-color="#FF3BBE" > < /stop > < stop offset="0.771" stop-color="#FF318C" > < /stop > < stop offset="0.995" stop-color="#FC801D" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__59" x1="67.819" x2="41.488" y1="48.799" y2="40.13" gradientUnits="userSpaceOnUse" > < stop offset="0.027" stop-color="#6B57FF" > < /stop > < stop offset="0.388" stop-color="#FF45ED" > < /stop > < stop offset="0.487" stop-color="#FF4DD1" > < /stop > < stop offset="0.702" stop-color="#FE6189" > < /stop > < stop offset="1" stop-color="#FC801D" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__60)" d="M42.7984 0L0.00328125 4.81631L0 26.8279L10.7335 62.553L64.552 48.9134L42.7984 0Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__59)" d="M65.9427 22.2088L49.0842 14.1337L25.4188 56.7263L31.8489 65.4527L48.2409 70L64.0216 60.0453L70 41.3105L65.9427 22.2088Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.65H18.6666V51.3333H34.4166V48.65Z" > < /path > < path fill="#FFF" d="M19 19H25.1485C30.1034 19 33.5267 22.4009 33.5267 26.8377V26.8828C33.5267 31.3196 30.1034 34.7655 25.1485 34.7655H19V19ZM22.4684 22.1307V31.635H25.1486C27.9864 31.635 29.9007 29.7205 29.9007 26.9279V26.8828C29.9329 26.2503 29.832 25.618 29.6046 25.0269C29.3772 24.4357 29.0283 23.8989 28.5804 23.451C28.1325 23.0032 27.5957 22.6542 27.0045 22.4268C26.4134 22.1994 25.7811 22.0985 25.1486 22.1307H22.4684Z" > < /path > < path fill="#FFF" d="M35.1846 27.0028V26.9575C35.1652 25.8703 35.3662 24.7903 35.7755 23.7828C36.1848 22.7753 36.7938 21.8611 37.566 21.0953C38.3381 20.3296 39.2573 19.7281 40.2682 19.3273C41.2791 18.9264 42.3607 18.7343 43.4478 18.7628C46.4355 18.7628 48.2242 19.7587 49.6954 21.2073L47.4767 23.7656C46.2544 22.6565 45.0096 21.9774 43.4246 21.9774C40.7537 21.9774 38.8293 24.1962 38.8293 26.9123V26.9576C38.8293 29.6743 40.7079 31.9377 43.4246 31.9377C45.2359 31.9377 46.345 31.2134 47.5899 30.0817L49.8086 32.3231C49.0108 33.2562 48.0114 33.9958 46.8858 34.4861C45.7603 34.9763 44.538 35.2043 43.3114 35.1529C42.2374 35.1703 41.1709 34.9712 40.1755 34.5674C39.1802 34.1637 38.2763 33.5636 37.5178 32.803C36.7594 32.0424 36.1619 31.1368 35.761 30.1403C35.3602 29.1438 35.1641 28.0767 35.1846 27.0028" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/dotmemory/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > dotMemory < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__63" x1="18.757" x2="30.724" y1="19.283" y2="69.379" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#6B57FF" > < /stop > < stop offset="0.13" stop-color="#9A51F9" > < /stop > < stop offset="0.268" stop-color="#C64CF4" > < /stop > < stop offset="0.392" stop-color="#E548F0" > < /stop > < stop offset="0.497" stop-color="#F846EE" > < /stop > < stop offset="0.57" stop-color="#FF45ED" > < /stop > < stop offset="0.633" stop-color="#FF57C9" > < /stop > < stop offset="0.814" stop-color="#FE8A65" > < /stop > < stop offset="0.941" stop-color="#FDAA26" > < /stop > < stop offset="1" stop-color="#FDB60D" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__62" x1="51.758" x2="39.877" y1="35.768" y2="1.731" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#6B57FF" > < /stop > < stop offset="0.138" stop-color="#8953FB" > < /stop > < stop offset="0.437" stop-color="#D64AF2" > < /stop > < stop offset="0.588" stop-color="#FF45ED" > < /stop > < stop offset="0.968" stop-color="#FDB60D" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__61" x1="26.353" x2="36.21" y1="53.604" y2="30.222" gradientUnits="userSpaceOnUse" > < stop offset="0.118" stop-color="#FF45ED" > < /stop > < stop offset="0.197" stop-color="#DF49F1" > < /stop > < stop offset="0.304" stop-color="#BC4DF5" > < /stop > < stop offset="0.416" stop-color="#9E51F9" > < /stop > < stop offset="0.535" stop-color="#8854FC" > < /stop > < stop offset="0.663" stop-color="#7855FD" > < /stop > < stop offset="0.807" stop-color="#6E57FF" > < /stop > < stop offset="1" stop-color="#6B57FF" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__63)" d="M7.97508 65.1476L0 37.6507L49.5529 51.3095L44.2657 70L7.97508 65.1476Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__62)" d="M23.4774 0.0896876L42.1193 5.42172L63.1729 0L67.3493 28.8778L19.955 13.125L23.4774 0.0896876Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__61)" d="M70 46.1135L67.3493 28.8776L24.4705 14.6255L0.0896875 19.8585L0 37.6506L49.5529 51.3093L70 46.1135Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.65H18.6666V51.3333H34.4166V48.65Z" > < /path > < path fill="#FFF" d="M19 19H25.1307C30.0712 19 33.4846 22.3911 33.4846 26.8149V26.86C33.4846 31.2839 30.0712 34.7198 25.1307 34.7198H19V19ZM22.4584 22.1216V31.5984H25.1307C27.9603 31.5984 29.8691 29.6894 29.8691 26.9049V26.86C29.9012 26.2293 29.8006 25.5988 29.5739 25.0094C29.3471 24.42 28.9992 23.8847 28.5526 23.4381C28.1061 22.9916 27.5708 22.6437 26.9813 22.4169C26.3919 22.1901 25.7615 22.0895 25.1307 22.1216H22.4584Z" > < /path > < path fill="#FFF" d="M34.6927 19.0094L38.4209 19.0099L42.5551 25.6573L46.6861 19.0099L50.4138 19.0104L50.4133 34.73H46.9765L46.977 24.4688L42.5545 31.183H42.4621L38.085 24.5352L38.084 34.7295H34.6921L34.6927 19.0094Z" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/decompiler/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > dotPeek < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__67" x1="7.045" x2="40.658" y1="35.829" y2="70.142" gradientUnits="userSpaceOnUse" > < stop offset="0.097" stop-color="#FF45ED" > < /stop > < stop offset="0.113" stop-color="#F846EE" > < /stop > < stop offset="0.284" stop-color="#AC4FF7" > < /stop > < stop offset="0.406" stop-color="#7D55FD" > < /stop > < stop offset="0.466" stop-color="#6B57FF" > < /stop > < stop offset="0.48" stop-color="#655DFE" > < /stop > < stop offset="0.572" stop-color="#4482FA" > < /stop > < stop offset="0.664" stop-color="#299EF6" > < /stop > < stop offset="0.756" stop-color="#16B3F4" > < /stop > < stop offset="0.847" stop-color="#0BBFF2" > < /stop > < stop offset="0.935" stop-color="#07C3F2" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__66" x1="9.563" x2="34.109" y1="55.827" y2="35.372" gradientUnits="userSpaceOnUse" > < stop offset="0.043" stop-color="#FF45ED" > < /stop > < stop offset="0.046" stop-color="#FE45ED" > < /stop > < stop offset="0.201" stop-color="#D14BF3" > < /stop > < stop offset="0.357" stop-color="#AC4FF7" > < /stop > < stop offset="0.512" stop-color="#9053FB" > < /stop > < stop offset="0.666" stop-color="#7B55FD" > < /stop > < stop offset="0.818" stop-color="#6F57FF" > < /stop > < stop offset="0.968" stop-color="#6B57FF" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__65" x1="39.855" x2="56.355" y1="16.927" y2="50.653" gradientUnits="userSpaceOnUse" > < stop offset="0.199" stop-color="#FF45ED" > < /stop > < stop offset="0.286" stop-color="#F646EE" > < /stop > < stop offset="0.429" stop-color="#DD49F1" > < /stop > < stop offset="0.609" stop-color="#B64EF6" > < /stop > < stop offset="0.818" stop-color="#7F55FD" > < /stop > < stop offset="0.887" stop-color="#6B57FF" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__64" x1="19.875" x2="61.328" y1="18.305" y2="8.256" gradientUnits="userSpaceOnUse" > < stop offset="0.097" stop-color="#FF45ED" > < /stop > < stop offset="0.17" stop-color="#F64AED" > < /stop > < stop offset="0.29" stop-color="#DD56EE" > < /stop > < stop offset="0.441" stop-color="#B56AEE" > < /stop > < stop offset="0.618" stop-color="#7E87F0" > < /stop > < stop offset="0.814" stop-color="#38AAF1" > < /stop > < stop offset="0.941" stop-color="#07C3F2" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__67)" d="M47.6963 50.342L0 40.8083L14.0848 70L49.2718 63.8662L47.6963 50.342Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__66)" d="M70 31.3298L50.6805 11.4088L0.00328125 22.0914L0 40.8082L62.6101 53.3229L70 31.3298Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__65)" d="M69.9999 31.3299L39.6167 0L15.8063 7.20945L23.6036 30.9208L62.61 53.323L69.9999 31.3299Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__64)" d="M64.5356 19.5754L61.7804 0H51.3373H39.6167L15.8063 7.20945L23.6036 30.9208L64.5356 19.5754Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.65H18.6666V51.3333H34.4166V48.65Z" > < /path > < path fill="#FFF" d="M19 19H25.1321C30.0736 19 33.4878 22.3918 33.4878 26.8167V26.8617C33.4878 31.2866 30.0736 34.7233 25.1321 34.7233H19V19ZM22.4592 22.1223V31.6011H25.1321C27.9623 31.6011 29.8715 29.6918 29.8715 26.9066V26.8617C29.9036 26.2309 29.803 25.6003 29.5762 25.0107C29.3494 24.4212 29.0014 23.8858 28.5547 23.4391C28.1081 22.9924 27.5727 22.6445 26.9831 22.4176C26.3935 22.1908 25.763 22.0902 25.1321 22.1223H22.4592Z" > < /path > < path fill="#FFF" d="M36.0267 19H42.4699C46.2312 19 48.5066 21.2303 48.5066 24.4511V24.4961C48.5066 28.1454 45.6681 30.0379 42.1315 30.0379H39.4958V34.7682H36.0267V19ZM42.2441 26.9517C43.9789 26.9517 44.9924 25.9157 44.9924 24.5637V24.5187C44.9924 22.9646 43.9114 22.1312 42.1765 22.1312H39.4958V26.9517H42.2441Z" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/profiler/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6" > dotTrace < /span > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__69" x1="-1.332" x2="67.042" y1="43.737" y2="26.097" gradientUnits="userSpaceOnUse" > < stop offset="0.123" stop-color="#6B57FF" > < /stop > < stop offset="0.538" stop-color="#FF45ED" > < /stop > < stop offset="0.854" stop-color="#DD1265" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__68" x1="45.915" x2="67.658" y1="38.91" y2="9.099" gradientUnits="userSpaceOnUse" > < stop offset="0.192" stop-color="#DD1265" > < /stop > < stop offset="0.295" stop-color="#DE146A" > < /stop > < stop offset="0.411" stop-color="#E21977" > < /stop > < stop offset="0.533" stop-color="#E7218E" > < /stop > < stop offset="0.659" stop-color="#EF2DAD" > < /stop > < stop offset="0.788" stop-color="#F93CD5" > < /stop > < stop offset="0.853" stop-color="#FF45ED" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__69)" d="M67.3065 16.0267L43.7466 0L0 31.0707L11.0851 70L58.9005 60.3039L67.3065 16.0267Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__68)" d="M67.3066 16.0267L43.7468 0L37.9504 15.7199V47.7701H70L67.3066 16.0267Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z" > < /path > < path fill="#FFF" d="M19 19.0016H25.1337C30.0767 19.0016 33.4917 22.3943 33.4917 26.8204V26.8654C33.4917 31.2915 30.0767 34.7291 25.1337 34.7291H19V19.0016ZM22.4601 22.1248V31.6061H25.1338C27.9647 31.6061 29.8745 29.6962 29.8745 26.9103V26.8654C29.9066 26.2344 29.8059 25.6037 29.5791 25.0139C29.3522 24.4242 29.0041 23.8887 28.5573 23.4419C28.1105 22.9951 27.575 22.647 26.9853 22.4201C26.3956 22.1933 25.7648 22.0926 25.1338 22.1248H22.4601Z" > < /path > < path fill="#FFF" d="M39.9826 22.1738H35.1921V18.98L48.2367 18.9805V22.1738H43.4461V34.7235H39.9821L39.9826 22.1738Z" > < /path > < /svg > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://plugins.jetbrains.com/search?isFeaturedSearch=true&amp;products=resharper&amp;products=rider" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" >.NET Tools Plugins < /span > < /span > < /a > < /div > < /div > < /div > < div class ="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--inline_hper7 _mainSubmenu__columnSeparated_fyc7bf" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title" > LANGUAGES & amp; FRAMEWORKS < /h5 > < div class ="wt-offset-top-12" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://kotlinlang.org/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Kotlin < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://ktor.io/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Ktor < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/mps/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > MPS < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/lp/compose-multiplatform/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Compose Multiplatform < /span > < /span > < /a > < /div > < /div > < /div > < /div > < div data-test="main-submenu-suggestions" > < div class ="_mainSubmenuSuggestion_ihmj1 _mainSubmenuSuggestionAdaptive_2gp4l" data-test="main-submenu-suggestion" > < div class ="wt-row wt-row_align-items_center wt-row_size_m wt-row-sm_wrap" > < div class ="wt-col-auto-fill wt-col-sm-12" > < h5 class ="rs-text-2 rs-text-2_hardness_hard rs-text-2_theme_light" data-test="suggestion-title" > Not sure which tool is best for you? < /h5 > < p class ="rs-text-2 rs-text-2_theme_light" data-test="suggestion-description" > Whichever technologies you use, there's a JetBrains tool to match</p></div><div class="wt-col-inline wt-offset-top-sm-12"><a data-test="suggestion-action" href="/products/" type="button" class="_main_1dh718a_17 _modeRock_1dh718a_241 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _light_1dh718a_59">Find your tool</a></div></div><a href="/products/" class="_mainSubmenuSuggestion__link_knoa4 _mainSubmenuSuggestion__link_9ek20g" aria-label="Find your tool" data-test="suggestion-link"></a></div></div></div><div class="main-submenu-banners _mainSubmenuBanners_332p1 _mainSubmenuBanners_j4vgp _mainSubmenuBannersAdaptive_aj1vpj _mainSubmenuBannersAdaptive_ei08o _mainSubmenu__banners_hdl8 _mainSubmenu__banners_l5zvm" data-test="main-submenu-banners"><div class="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner"><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(117.63deg, rgb(8, 89, 255) -0.78%, rgb(0, 154, 231) 55.03%, rgb(221, 255, 84) 111.19%); background-color: rgb(22, 125, 255);"></div><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(117.63deg, rgb(8, 89, 255) -0.78%, rgb(0, 154, 231) 55.03%, rgb(221, 255, 84) 111.19%); background-color: rgb(22, 125, 255);"></div><div class="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl"><svg viewBox="0 0 60 60" class="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c" data-test="banner-logo-image"><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__72" gradientTransform="matrix(1 0 0 -1 0 62)" gradientUnits="userSpaceOnUse" x1="27.048" x2="33.312" y1="62.824" y2="3.448"><stop offset="0" stop-color="#fcf84a"></stop><stop offset="0.32" stop-color="#abe682"></stop><stop offset="0.79" stop-color="#36cdd2"></stop><stop offset="1" stop-color="#07c3f2"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__71" gradientTransform="matrix(1 0 0 -1 0 62)" gradientUnits="userSpaceOnUse" x1="4.068" x2="60.246" y1="61.892" y2="35.243"><stop offset="0" stop-color="#3bea62"></stop><stop offset="1" stop-color="#087cfa"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__70" gradientTransform="matrix(1 0 0 -1 0 62)" gradientUnits="userSpaceOnUse" x1="9.217" x2="65.779" y1="3.879" y2="43.473"><stop offset="0" stop-color="#009ae5"></stop><stop offset="0.18" stop-color="#0490dd"></stop><stop offset="0.49" stop-color="#1073c6"></stop><stop offset="0.89" stop-color="#2346a1"></stop><stop offset="1" stop-color="#293896"></stop></linearGradient><g fill-rule="evenodd"><path d="m10.8618 60a59.95462 59.95462 0 0 0 49.1382-34.4 60.00348 60.00348 0 0 0 -49.1382-25.6c-1.74408 0-3.49616.072-5.24824.232a59.99772 59.99772 0 0 0 5.24824 59.768z" fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__72)"></path><path d="m5.66956.232a70.65854 70.65854 0 0 1 31.56944 25.368h22.761a59.81147 59.81147 0 0 0 -49.0742-25.6q-2.61612 0-5.25624.232z" fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__71)"></path><path d="m37.247 25.6c-2.74414 18.104-26.3852 34.4-26.3852 34.4 21.48896-2.04 40.33781-14.92 49.1382-34.4z" fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__70)"></path></g></svg><div class="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12"><div class="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p"><h3 class="rs-h3 rs-h3_theme_dark" data-test="banner-title">Space</h3><p class="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description">A complete software development platform</p></div><a data-test="banner-action" aria-label="Explore Space" href="/space/" type="button" class="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569"><path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z"></path></svg></a></div></div><a href="/space/" class="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Explore Space" data-test="banner-link"></a></div><div class="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner"><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(130.93deg, rgb(105, 2, 154) 0%, rgb(135, 1, 199) 32.33%, rgb(107, 87, 255) 97.76%); background-color: rgb(135, 1, 199);"></div><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(130.93deg, rgb(105, 2, 154) 0%, rgb(135, 1, 199) 32.33%, rgb(107, 87, 255) 97.76%); background-color: rgb(135, 1, 199);"></div><div class="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl"><div class="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c _productLogo_img_5cqf5" data-test="banner-logo-image" style="background-image: url(&quot;/img/banners-menu-main/fleet.png&quot;);"></div><div class="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12"><div class="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p"><h3 class="rs-h3 rs-h3_theme_dark" data-test="banner-title">Fleet</h3><p class="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description">Next-generation IDE by JetBrains</p></div><a data-test="banner-action" aria-label="Learn more" href="/fleet/" type="button" class="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569"><path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z"></path></svg></a></div></div><a href="/fleet/" class="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Learn more" data-test="banner-link"></a></div></div></div></div></div></div><div class="_mainMenuItem_29v65" data-test="main-menu-item" data-test-marker="Team Tools"><button type="button" class="_mainMenuItem__action_6msel _mainMenuItem__action_e0rkwf _mainMenuItem__action_d84ml _mainMenuItem__action_aa1l9 _mainMenuItem__action_a0n8y _mainMenuItem__action_dngujh _mainMenuItem__action_28j9v _mainMenuItem__action_v73y8i _mainMenuItem__action_42uf2 _mainMenuItem__action_07kd4" aria-label="Team Tools: Open submenu" data-test="main-menu-item-action">Team Tools</button><div class="_mainMenuItem__submenuWrapper_dxbj7 _mainMenuItem__submenuWrapper_11ave _mainMenuItem__submenuWrapper_9pejb"><div class="_mainMenuItem__submenu_y1dd2 _mainMenuItem__submenu_i0lmy" data-test="main-submenu"><div class="_mainSubmenu__body_tph6v _mainSubmenu__body_nnhk5"><div class="_mainSubmenu__content_xyg62 _mainSubmenu__content_aflg"><div class="_mainSubmenu__columnsWrapper_e7cwuk"><div class="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--8_19zk4"><h5 class="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title">IN-CLOUD AND ON-PREMISES SOLUTIONS</h5><div class="wt-offset-top-12"><div class="_mainSubmenuSubColumns__inner_7pa49h"><div class="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--6_watp9g"><div class=""><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/datalore/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Datalore</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">A collaborative data science platform</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/space/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Space</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">A complete software development platform</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/teamcity/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">TeamCity</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Powerful Continuous Integration out of the box</span></a></div></div></div><div class="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--6_watp9g"><div class=""><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/youtrack/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">YouTrack</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Powerful project management for all your teams</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/qodana/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Qodana</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">The code quality platform for your favorite CI</span></a></div></div></div></div></div></div><div class="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--4_s32so _mainSubmenu__columnSeparated_fyc7bf"><h5 class="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title">EXTENSIONS</h5><div class="wt-offset-top-12"><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://plugins.jetbrains.com/teamcity/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">TeamCity Plugins</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://plugins.jetbrains.com/youtrack/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">YouTrack Extensions</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/hub/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">JetBrains Hub</span></span></a></div></div></div></div></div><div class="main-submenu-banners _mainSubmenuBanners_332p1 _mainSubmenuBanners_j4vgp _mainSubmenuBannersAdaptive_aj1vpj _mainSubmenuBannersAdaptive_ei08o _mainSubmenu__banners_hdl8 _mainSubmenu__banners_l5zvm" data-test="main-submenu-banners"><div class="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner"><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(120.81deg, rgb(0, 51, 150) 11.31%, rgb(0, 156, 244) 95.37%); background-color: rgb(0, 92, 209);"></div><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(120.81deg, rgb(0, 51, 150) 11.31%, rgb(0, 156, 244) 95.37%); background-color: rgb(0, 92, 209);"></div><div class="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl"><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c" data-test="banner-logo-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__76" x1="21.41" x2="63.882" y1="17.36" y2="25.844" gradientUnits="userSpaceOnUse"><stop offset="0.242" stop-color="#3BEA62"></stop><stop offset="0.857" stop-color="#FCF84A"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__75" x1="16.862" x2="57.518" y1="4.912" y2="66.891" gradientUnits="userSpaceOnUse"><stop offset="0.018" stop-color="#3BEA62"></stop><stop offset="0.786" stop-color="#087CFA"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__74" x1="16.295" x2="67.926" y1="39.35" y2="58.041" gradientUnits="userSpaceOnUse"><stop offset="0.121" stop-color="#1FAEB5"></stop><stop offset="0.975" stop-color="#087CFA"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__73" x1="1.435" x2="68.11" y1="42.252" y2="12.633" gradientUnits="userSpaceOnUse"><stop offset="0.121" stop-color="#1FAEB5"></stop><stop offset="0.856" stop-color="#FCF84A"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__76)" d="M64.9765 8.29965C64.1745 7.86318 63.0808 7.49945 62.2058 7.35395C61.6225 7.35395 24.3642 0.224872 22.3956 0.0793808C21.4477 0.00663505 20.4269 0.0793808 19.4791 0.224872C2.19877 2.77097 -2.17598 23.7945 12.1149 32.5967C15.4689 34.6336 19.4791 35.3611 23.3434 34.4881C30.1243 33.0332 60.6018 25.5404 62.5704 25.1039C71.0283 23.2853 72.8511 12.4462 64.9765 8.29965Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__75)" d="M65.3411 40.6714C63.8829 38.9982 37.4885 9.09972 31.8742 4.22575C30.7805 3.28006 29.4681 2.40711 28.0099 1.60691C25.385 0.224739 22.3956 -0.284481 19.4791 0.151993C3.8758 2.5526 -1.22808 19.9388 8.46929 29.7595C9.49007 30.8507 38.5093 63.0043 38.8009 63.368C40.1134 64.9684 41.7174 66.4961 43.759 67.7328C47.113 69.8424 51.1961 70.4971 55.1333 69.6242C69.4242 66.4234 74.0177 50.3465 65.3411 40.6714Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__74)" d="M59.7998 36.4521C59.2165 36.1611 58.6332 35.8701 57.977 35.6519C57.4666 35.5064 18.2396 23.1396 17.3647 22.9214C15.9064 22.5576 14.3752 22.4849 12.917 22.7031C-1.08223 24.74 -4.65495 41.8353 6.93815 49.0371C9.63592 50.7103 45.436 68.6057 46.3839 68.9694C49.1545 69.9879 52.144 70.2061 55.0605 69.5514C71.8304 65.9141 75.2572 44.5269 59.7998 36.4521Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__73)" d="M64.9766 8.29953C63.6642 7.57207 62.133 7.35383 60.6018 7.57207C59.7998 7.71756 59.0707 7.86305 58.3416 8.15404C54.9147 9.5362 10.0005 23.2852 8.76099 23.8671C-1.66551 28.3774 -3.3425 42.6355 6.93817 49.0372C9.63594 50.7103 12.917 51.2923 16.1252 50.5648C17.3647 50.2738 18.6042 49.9101 19.625 49.4009C25.1663 46.782 64.612 24.5218 65.4141 24.0854C71.32 20.6663 71.8304 11.9368 64.9766 8.29953Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4167 48.65H18.6667V51.3334H34.4167V48.65Z"></path><g fill="#FFF"><path d="M36.0001 19.13H39.458V31.8553H46.3048V34.76H36.0001V19.13Z"></path><path d="M18.67 19.13H24.7561C29.6664 19.13 33.0552 22.5188 33.0552 26.8758V26.945C33.0552 31.3712 29.6664 34.76 24.7561 34.76H18.67V19.13ZM22.128 22.2422V31.6478H24.7561C27.5916 31.6478 29.4589 29.7805 29.4589 27.0142V26.945C29.4589 24.1786 27.5916 22.2422 24.7561 22.2422H22.128V22.2422Z"></path></g></svg><div class="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12"><div class="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p"><h3 class="rs-h3 rs-h3_theme_dark" data-test="banner-title">Datalore</h3><p class="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description">A collaborative data science platform. Available online and on-premises</p></div><a data-test="banner-action" aria-label="Learn more" href="/datalore/" type="button" class="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569"><path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z"></path></svg></a></div></div><a href="/datalore/" class="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Learn more" data-test="banner-link"></a></div><div class="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner"><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(141.09deg, rgb(216, 6, 99) -21.81%, rgb(131, 76, 239) 33.98%, rgb(0, 181, 226) 100.21%); background-color: rgb(107, 87, 255);"></div><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(141.09deg, rgb(216, 6, 99) -21.81%, rgb(131, 76, 239) 33.98%, rgb(0, 181, 226) 100.21%); background-color: rgb(107, 87, 255);"></div><div class="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl"><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c" data-test="banner-logo-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__79" x1="7.088" x2="64.122" y1="54.736" y2="28.739" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#905CFB"></stop><stop offset="0.165" stop-color="#6677F8"></stop><stop offset="0.378" stop-color="#3596F5"></stop><stop offset="0.54" stop-color="#17A9F3"></stop><stop offset="0.632" stop-color="#0CB0F2"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__78" x1="30.319" x2="1.071" y1="28.108" y2="2.276" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#905CFB"></stop><stop offset="0.072" stop-color="#A554E6"></stop><stop offset="0.252" stop-color="#D641B5"></stop><stop offset="0.39" stop-color="#F43597"></stop><stop offset="0.468" stop-color="#FF318C"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__77" x1="4.988" x2="74.041" y1="58.67" y2="15.161" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#905CFB"></stop><stop offset="0.165" stop-color="#6677F8"></stop><stop offset="0.378" stop-color="#3596F5"></stop><stop offset="0.54" stop-color="#17A9F3"></stop><stop offset="0.632" stop-color="#0CB0F2"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__79)" d="M66.916 47.482C66.716 47.282 53.8136 34.8792 53.8136 34.8792C53.8136 34.8792 63.6154 24.4769 66.2159 21.8763C66.7408 21.3513 67.6261 20.2758 68.2162 19.2757C71.8169 13.1743 69.7165 5.3726 63.6154 1.7718C59.1146 -0.828787 53.5136 -0.428697 49.5128 2.57197C48.8127 3.07209 48.2126 3.5722 47.6125 4.17233C47.3124 4.57242 33.71 16.9752 21.9078 27.7776L44.0118 41.7807L20.8076 67.8866C19.4074 68.8868 18.0071 69.487 16.5068 69.787C16.8069 69.787 17.7071 69.8869 18.0072 69.7868C22.608 69.0867 61.215 62.3854 63.1153 61.9853C65.4157 61.5852 67.5161 60.1849 68.8163 58.0844C71.0167 54.4836 70.0166 49.9826 66.916 47.482Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__78)" d="M45.9121 30.4781C45.512 27.7775 44.1118 25.577 42.1114 23.9767C40.011 22.3763 23.8081 5.57256 22.0078 3.67213C19.2073 0.971525 15.2065 -0.528811 11.1058 0.171346C4.10453 1.17157 -0.796361 7.77305 0.303839 14.7746C0.80393 18.2754 2.80429 21.2761 5.40476 23.1765C8.00524 25.1769 28.4089 39.1801 29.7092 40.1803C31.8096 41.7807 34.6101 42.6809 37.4106 42.1808C42.9116 41.1805 46.8123 35.9794 45.9121 30.4781Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__77)" d="M23.0079 67.7866C23.108 67.7866 46.3122 41.6808 46.3122 41.6808L22.9079 26.8774C14.6064 34.4791 6.90502 41.3807 5.10469 43.0811C4.00449 44.0813 2.90429 45.3816 2.10415 46.7819C-2.19664 54.1836 0.303819 63.5857 7.70516 67.8866C10.7057 69.587 17.5069 71.6875 23.0079 67.7866Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4167 48.6499H18.6667V51.3332H34.4167V48.6499Z"></path><path fill="#FFF" d="M24.7737 34.73H28.2342V28.4607L34.2795 19H30.3463L26.5265 25.3144L22.7736 19H18.73L24.7737 28.5276L24.7737 34.73ZM36.4142 19.0006V22.1905H41.1998V34.729H44.6603V22.1905H49.4458V19.0006H36.4142Z"></path></svg><div class="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12"><div class="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p"><h3 class="rs-h3 rs-h3_theme_dark" data-test="banner-title">YouTrack</h3><p class="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description">Powerful project management for all your teams</p></div><a data-test="banner-action" aria-label="Learn more" href="/youtrack/" type="button" class="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569"><path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z"></path></svg></a></div></div><a href="/youtrack/" class="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Learn more" data-test="banner-link"></a></div></div></div></div></div></div><div class="_mainMenuItem_29v65" data-test="main-menu-item" data-test-marker="Education"><button type="button" class="_mainMenuItem__action_6msel _mainMenuItem__action_e0rkwf _mainMenuItem__action_d84ml _mainMenuItem__action_aa1l9 _mainMenuItem__action_a0n8y _mainMenuItem__action_dngujh _mainMenuItem__action_28j9v _mainMenuItem__action_v73y8i _mainMenuItem__action_42uf2 _mainMenuItem__action_07kd4" aria-label="Education: Open submenu" data-test="main-menu-item-action">Education</button><div class="_mainMenuItem__submenuWrapper_dxbj7 _mainMenuItem__submenuWrapper_11ave _mainMenuItem__submenuWrapper_9pejb"><div class="_mainMenuItem__submenu_y1dd2 _mainMenuItem__submenu_i0lmy" data-test="main-submenu"><div class="_mainSubmenu__body_tph6v _mainSubmenu__body_nnhk5"><div class="_mainSubmenu__content_xyg62 _mainSubmenu__content_aflg"><div class="_mainSubmenu__columnsWrapper_e7cwuk"><div class="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--4_s32so"><h5 class="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title">FOR LEARNERS</h5><div class="wt-offset-top-12"><div class="_mainSubmenuSubColumns__inner_7pa49h"><div class="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--11_535vd"><div class=""><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/academy/#learn" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Programming languages</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Select a language and try different approaches to learning it</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/academy/#careers" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Career fields</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Explore careers and see where programming could take you</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/education/university-relations/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">University relations</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Study offline with academic programs</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/careers/internships/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Internships</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Apply for internships and flexible jobs for students<br></span></a></div></div></div></div></div></div><div class="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--4_s32so"><h5 class="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title">FOR EDUCATORS</h5><div class="wt-offset-top-12"><div class="_mainSubmenuSubColumns__inner_7pa49h"><div class="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--11_535vd"><div class=""><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/pages/academy/teaching/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Teaching with JetBrains IDEs</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Create courses and share your knowledge</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="https://kotlinlang.org/education/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Kotlin for education</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Teach a wide range of Kotlin courses</span></a></div></div></div><div class="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--11_535vd"><h5 class="rs-h5 rs-h5_theme_light wt-offset-top-24" data-test="main-submenu-sub-column-title">FOR TEAMS</h5><div class="wt-offset-top-12"><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="https://lp.jetbrains.com/academy/for-organizations" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Professional development</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Ensure your team has up-to-date technical skills</span></a></div></div></div></div></div></div><div class="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--4_s32so _mainSubmenu__columnSeparated_fyc7bf"><h5 class="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title">FREE LICENSES</h5><div class="wt-offset-top-12"><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/community/education/#students/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">For students and teachers</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">JetBrains IDEs for individual academic use</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/community/education/#classrooms" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">For educational institutions</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">JetBrains IDEs and team tools for classroom use</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/community/education/#courses" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">For bootcamps and courses</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">JetBrains IDEs for your students</span></a></div></div></div></div></div><div class="main-submenu-banners _mainSubmenuBanners_332p1 _mainSubmenuBanners_j4vgp _mainSubmenuBannersAdaptive_aj1vpj _mainSubmenuBannersAdaptive_ei08o _mainSubmenu__banners_hdl8 _mainSubmenu__banners_l5zvm" data-test="main-submenu-banners"><div class="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner"><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(335.07deg, rgb(99, 108, 234) 0%, rgb(131, 76, 239) 40.63%, rgb(119, 31, 137) 100%); background-color: rgb(176, 29, 246);"></div><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(335.07deg, rgb(99, 108, 234) 0%, rgb(131, 76, 239) 40.63%, rgb(119, 31, 137) 100%); background-color: rgb(176, 29, 246);"></div><div class="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl"><div class="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c _productLogo_img_5cqf5" data-test="banner-logo-image" style="background-image: url(&quot;/img/banners-menu-main/academy-logo.svg&quot;);"></div><div class="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12"><div class="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p"><h3 class="rs-h3 rs-h3_theme_dark" data-test="banner-title">JetBrains Academy</h3><p class="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description">Find your way in learning or teaching computer science</p></div><a data-test="banner-action" aria-label="Discover more" href="/academy" type="button" class="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569"><path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z"></path></svg></a></div></div><a href="/academy" class="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Discover more" data-test="banner-link"></a></div></div></div></div></div></div><div class="_mainMenuItem_29v65" data-test="main-menu-item" data-test-marker="Solutions"><button type="button" class="_mainMenuItem__action_6msel _mainMenuItem__action_e0rkwf _mainMenuItem__action_d84ml _mainMenuItem__action_aa1l9 _mainMenuItem__action_a0n8y _mainMenuItem__action_dngujh _mainMenuItem__action_28j9v _mainMenuItem__action_v73y8i _mainMenuItem__action_42uf2 _mainMenuItem__action_07kd4" aria-label="Solutions: Open submenu" data-test="main-menu-item-action">Solutions</button><div class="_mainMenuItem__submenuWrapper_dxbj7 _mainMenuItem__submenuWrapper_11ave _mainMenuItem__submenuWrapper_9pejb"><div class="_mainMenuItem__submenu_y1dd2 _mainMenuItem__submenu_i0lmy" data-test="main-submenu"><div class="_mainSubmenu__body_tph6v _mainSubmenu__body_nnhk5"><div class="_mainSubmenu__content_xyg62 _mainSubmenu__content_aflg"><div class="_mainSubmenu__columnsWrapper_e7cwuk"><div class="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--8_19zk4"><h5 class="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title">BY INDUSTRY &amp; TECHNOLOGY</h5><div class="wt-offset-top-12"><div class="_mainSubmenuSubColumns__inner_7pa49h"><div class="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--6_watp9g"><div class=""><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/remote-development/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Remote Development</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Tools for remote development for you and your team</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/gamedev/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Game Development</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Tools for game development for any platform</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/devops/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">DevOps</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Tools and integrations for any infrastructure</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/quality-assurance-solutions/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Quality Assurance</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Tools for Quality Assurance and Test Automation</span></a></div></div></div><div class="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--6_watp9g"><div class=""><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/cpp/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">C++ Tools</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Tools for C/C++ development for any platform</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/data-tools/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Data Tools</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Tools for Big Data and Data Science</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/space/solutions/software-teams/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Software Development</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">All-in-one solution for software projects and teams</span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item"><a href="/license-vault/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">License Vault</span></span><span class="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description">Efficient management of JetBrains licenses</span></a></div></div></div></div></div></div><div class="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--4_s32so _mainSubmenu__columnSeparated_fyc7bf"><h5 class="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title">RECOMMENDED</h5><div class="wt-offset-top-12"><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/all/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">All Products Pack</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/dotnet/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">.NET Tools</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/education/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">JetBrains for Education</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/products/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">All JetBrains Products</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://plugins.jetbrains.com/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">JetBrains Marketplace</span></span></a></div></div></div></div></div><div class="main-submenu-banners _mainSubmenuBanners_332p1 _mainSubmenuBanners_j4vgp _mainSubmenuBannersAdaptive_aj1vpj _mainSubmenuBannersAdaptive_ei08o _mainSubmenu__banners_hdl8 _mainSubmenu__banners_l5zvm" data-test="main-submenu-banners"><div class="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner"><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(246.1deg, rgb(0, 224, 214) 1.67%, rgb(126, 27, 253) 92.48%); background-color: rgb(107, 87, 255);"></div><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(246.1deg, rgb(0, 224, 214) 1.67%, rgb(126, 27, 253) 92.48%); background-color: rgb(107, 87, 255);"></div><div class="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl"><div class="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c _productLogo_img_5cqf5" data-test="banner-logo-image" style="background-image: url(&quot;/img/banners-menu-main/containers.svg&quot;);"></div><div class="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12"><div class="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p"><h3 class="rs-h3 rs-h3_theme_dark" data-test="banner-title">Developer Tools for Your Business</h3><p class="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description">Professional tools for productive development</p></div><a data-test="banner-action" aria-label="Learn more" href="/store/business/" type="button" class="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569"><path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z"></path></svg></a></div></div><a href="/store/business/" class="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Learn more" data-test="banner-link"></a></div><div class="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner"><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(240.88deg, rgb(45, 243, 136) 0%, rgb(5, 191, 135) 37.75%, rgb(2, 116, 116) 98.39%); background-color: rgb(45, 243, 136);"></div><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(240.88deg, rgb(45, 243, 136) 0%, rgb(5, 191, 135) 37.75%, rgb(2, 116, 116) 98.39%); background-color: rgb(45, 243, 136);"></div><div class="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl"><div class="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9"><div class="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p"><h3 class="rs-h3 rs-h3_theme_dark" data-test="banner-title">Remote Development</h3><p class="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description">Connect to remote dev environments from anywhere in seconds</p></div><a data-test="banner-action" aria-label="Discover more" href="/remote-development/" type="button" class="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569"><path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z"></path></svg></a></div></div><a href="/remote-development/" class="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Discover more" data-test="banner-link"></a></div></div></div></div></div></div><div class="_mainMenuItem_29v65" data-test="main-menu-item" data-test-marker="Support"><button type="button" class="_mainMenuItem__action_6msel _mainMenuItem__action_e0rkwf _mainMenuItem__action_d84ml _mainMenuItem__action_aa1l9 _mainMenuItem__action_a0n8y _mainMenuItem__action_dngujh _mainMenuItem__action_28j9v _mainMenuItem__action_v73y8i _mainMenuItem__action_42uf2 _mainMenuItem__action_07kd4" aria-label="Support: Open submenu" data-test="main-menu-item-action">Support</button><div class="_mainMenuItem__submenuWrapper_dxbj7 _mainMenuItem__submenuWrapper_11ave _mainMenuItem__submenuWrapper_9pejb"><div class="_mainMenuItem__submenu_y1dd2 _mainMenuItem__submenu_i0lmy" data-test="main-submenu"><div class="_mainSubmenu__body_tph6v _mainSubmenu__body_nnhk5"><div class="_mainSubmenu__content_xyg62 _mainSubmenu__content_aflg"><div class="_mainSubmenu__columnsWrapper_e7cwuk"><div class="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--6_teoqhk"><h5 class="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title">PRODUCT &amp; TECHNICAL SUPPORT</h5><div class="wt-offset-top-12"><div class="_mainSubmenuSubColumns__inner_7pa49h"><div class="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--12_w1dwk"><div class=""><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/support/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Support Center</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/help/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Product Documentation</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/company/webinars/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Webinars</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/resources/newsletters/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Newsletters</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/resources/eap/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Early Access</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://blog.jetbrains.com/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Blog</span></span></a></div></div></div></div></div></div><div class="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--6_teoqhk _mainSubmenu__columnSeparated_fyc7bf"><h5 class="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title">FREQUENT TASKS</h5><div class="wt-offset-top-12"><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://account.jetbrains.com/profile-details" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Manage your account</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://account.jetbrains.com/licenses" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Manage your licenses</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/support/sales/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Contact Sales</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://sales.jetbrains.com/hc/en-gb/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Licensing FAQ</span></span></a></div></div></div></div></div><div class="main-submenu-banners _mainSubmenuBanners_332p1 _mainSubmenuBanners_j4vgp _mainSubmenuBannersAdaptive_aj1vpj _mainSubmenuBannersAdaptive_ei08o _mainSubmenu__banners_hdl8 _mainSubmenu__banners_l5zvm" data-test="main-submenu-banners"><div class="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner"><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(294.91deg, rgb(255, 49, 140) -50.1%, rgb(107, 87, 255) 97.43%); background-color: rgb(107, 87, 255);"></div><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(294.91deg, rgb(255, 49, 140) -50.1%, rgb(107, 87, 255) 97.43%); background-color: rgb(107, 87, 255);"></div><div class="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl"><div class="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c _productLogo_img_5cqf5" data-test="banner-logo-image" style="background-image: url(&quot;/img/banners-menu-main/download.svg&quot;);"></div><div class="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12"><div class="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p"><h3 class="rs-h3 rs-h3_theme_dark" data-test="banner-title">Download and Install</h3></div><a data-test="banner-action" aria-label="Download and Install" href="/products/" type="button" class="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569"><path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z"></path></svg></a></div></div><a href="/products/" class="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Download and Install" data-test="banner-link"></a></div><div class="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner"><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(283.8deg, rgb(8, 124, 250) 5.73%, rgb(33, 215, 137) 100%); background-color: rgb(33, 215, 137);"></div><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(283.8deg, rgb(8, 124, 250) 5.73%, rgb(33, 215, 137) 100%); background-color: rgb(33, 215, 137);"></div><div class="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl"><div class="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c _productLogo_img_5cqf5" data-test="banner-logo-image" style="background-image: url(&quot;/img/banners-menu-main/test-review.svg&quot;);"></div><div class="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12"><div class="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p"><h3 class="rs-h3 rs-h3_theme_dark" data-test="banner-title">Contact us</h3></div><a data-test="banner-action" aria-label="Contact us" href="/company/contacts/" type="button" class="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569"><path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z"></path></svg></a></div></div><a href="/company/contacts/" class="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Contact us" data-test="banner-link"></a></div></div></div></div></div></div><div class="_mainMenuItem_29v65" data-test="main-menu-item" data-test-marker="Store"><button type="button" class="_mainMenuItem__action_6msel _mainMenuItem__action_e0rkwf _mainMenuItem__action_d84ml _mainMenuItem__action_aa1l9 _mainMenuItem__action_a0n8y _mainMenuItem__action_dngujh _mainMenuItem__action_28j9v _mainMenuItem__action_v73y8i _mainMenuItem__action_42uf2 _mainMenuItem__action_07kd4" aria-label="Store: Open submenu" data-test="main-menu-item-action">Store</button><div class="_mainMenuItem__submenuWrapper_dxbj7 _mainMenuItem__submenuWrapper_11ave _mainMenuItem__submenuWrapper_9pejb"><div class="_mainMenuItem__submenu_y1dd2 _mainMenuItem__submenu_i0lmy" data-test="main-submenu"><div class="_mainSubmenu__body_tph6v _mainSubmenu__body_nnhk5"><div class="_mainSubmenu__content_xyg62 _mainSubmenu__content_aflg"><div class="_mainSubmenu__columnsWrapper_e7cwuk"><div class="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--4_s32so"><h5 class="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title">DEVELOPER TOOLS</h5><div class="wt-offset-top-12"><div class="_mainSubmenuSubColumns__inner_7pa49h"><div class="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--12_w1dwk"><div class=""><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/store/#personal" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">For Individual Use</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/store/#commercial" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">For Teams and Organizations</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/store/#discounts" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Special offers &amp; programs</span></span></a></div></div></div><div class="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--12_w1dwk"><h5 class="rs-h5 rs-h5_theme_light wt-offset-top-24" data-test="main-submenu-sub-column-title">SERVICES &amp; PLUGINS</h5><div class="wt-offset-top-12"><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/store/plugins/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Marketplace</span></span></a></div></div></div><div class="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--12_w1dwk"><h5 class="rs-h5 rs-h5_theme_light wt-offset-top-24" data-test="main-submenu-sub-column-title">LEARNING TOOLS</h5><div class="wt-offset-top-12"><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/academy/buy/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">JetBrains Academy</span></span></a></div></div></div></div></div></div><div class="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--4_s32so"><h5 class="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title">TEAM TOOLS</h5><div class="wt-offset-top-12"><div class="_mainSubmenuSubColumns__inner_7pa49h"><div class="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--12_w1dwk"><div class=""><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/store/teamware#space-store-section" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Space</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/store/teamware#teamcity-store-section" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">TeamCity</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/store/teamware#youtrack-store-section" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">YouTrack</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/datalore/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Datalore</span></span></a></div></div></div><div class="_mainSubmenuSubColumns__column_nujyrk _mainSubmenuSubColumns__column--12_w1dwk"><h5 class="rs-h5 rs-h5_theme_light wt-offset-top-24" data-test="main-submenu-sub-column-title">COLLABORATIVE DEVELOPMENT</h5><div class="wt-offset-top-12"><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/code-with-me/buy/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Code With Me</span></span></a></div></div></div></div></div></div><div class="main-submenu__column _mainSubmenu__column_dl3zs _mainSubmenu__column--4_s32so _mainSubmenu__columnSeparated_fyc7bf"><h5 class="rs-h5 rs-h5_theme_light" data-test="main-submenu-column-title">SALES SUPPORT</h5><div class="wt-offset-top-12"><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/support/sales/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Contact Sales</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/legal/docs/store/terms/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Purchase Terms</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://sales.jetbrains.com/hc/en-gb/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">FAQ</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/company/partners/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Partners and Resellers</span></span></a></div></div></div></div></div><div class="main-submenu-banners _mainSubmenuBanners_332p1 _mainSubmenuBanners_j4vgp _mainSubmenuBannersAdaptive_aj1vpj _mainSubmenuBannersAdaptive_ei08o _mainSubmenu__banners_hdl8 _mainSubmenu__banners_l5zvm" data-test="main-submenu-banners"><div class="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner"><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(293.2deg, rgb(253, 13, 122) 13.45%, rgb(252, 100, 67) 73.57%, rgb(248, 158, 7) 100%); background-color: rgb(255, 49, 140);"></div><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(293.2deg, rgb(253, 13, 122) 13.45%, rgb(252, 100, 67) 73.57%, rgb(248, 158, 7) 100%); background-color: rgb(255, 49, 140);"></div><div class="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl"><div class="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c _productLogo_img_5cqf5" data-test="banner-logo-image" style="background-image: url(&quot;/img/banners-menu-main/discount.svg&quot;);"></div><div class="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12"><div class="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p"><h3 class="rs-h3 rs-h3_theme_dark" data-test="banner-title">All Products Pack</h3><p class="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description">Get all JetBrains desktop tools including 10&nbsp;IDEs,<br>2&nbsp;profilers, and 3&nbsp;extensions</p></div><a data-test="banner-action" aria-label="Learn more" href="/all/" type="button" class="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569"><path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z"></path></svg></a></div></div><a href="/all/" class="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Learn more" data-test="banner-link"></a></div><div class="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner"><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(304.12deg, rgb(8, 124, 250) -14.07%, rgb(53, 53, 53) 109.22%); background-color: rgb(107, 87, 255);"></div><div class="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(304.12deg, rgb(8, 124, 250) -14.07%, rgb(53, 53, 53) 109.22%); background-color: rgb(107, 87, 255);"></div><div class="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl"><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c" data-test="banner-logo-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__82" x1="5.174" x2="40.014" y1="39.889" y2="38.123" gradientUnits="userSpaceOnUse"><stop offset="0.091" stop-color="#FC801D"></stop><stop offset="0.231" stop-color="#B07F61"></stop><stop offset="0.409" stop-color="#577DB3"></stop><stop offset="0.533" stop-color="#1E7CE6"></stop><stop offset="0.593" stop-color="#087CFA"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__81" x1="61.991" x2="50.158" y1="36.915" y2="1.557" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FE2857"></stop><stop offset="0.078" stop-color="#CB3979"></stop><stop offset="0.16" stop-color="#9E4997"></stop><stop offset="0.247" stop-color="#7557B2"></stop><stop offset="0.339" stop-color="#5362C8"></stop><stop offset="0.436" stop-color="#386CDA"></stop><stop offset="0.541" stop-color="#2373E8"></stop><stop offset="0.658" stop-color="#1478F2"></stop><stop offset="0.794" stop-color="#0B7BF8"></stop><stop offset="1" stop-color="#087CFA"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__80" x1="10.066" x2="53.876" y1="16.495" y2="88.96" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FE2857"></stop><stop offset="0.08" stop-color="#FE295F"></stop><stop offset="0.206" stop-color="#FF2D76"></stop><stop offset="0.303" stop-color="#FF318C"></stop><stop offset="0.385" stop-color="#EA3896"></stop><stop offset="0.553" stop-color="#B248AE"></stop><stop offset="0.792" stop-color="#5A63D6"></stop><stop offset="1" stop-color="#087CFA"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__82)" d="M11.2 49.4668L0.699951 41.3001L9 26L18.5 33.5L11.2 49.4668Z"></path><path fill="#087CFA" d="M69.9999 18.6666L68.8333 59.2666L41.7666 70L27.0666 60.4333L41.7666 37.5L69.9999 18.6666Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__81)" d="M70 18.6666L55.5 33L37 15L48.0666 1.16663L70 18.6666Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__80)" d="M27.0667 60.4333L5.6 68.3667L10.0333 52.5L15.8667 33.1333L0 27.7667L10.0333 0L33.1333 2.8L54.5 31L55.5 33L27.0667 60.4333Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><g fill="#FFF"><path d="M27.1366 22.1433V19.25H19.2733V22.1433H21.4666V32.1067H19.2733V34.9767H27.1366V32.1067H24.92V22.1433H27.1366Z"></path><path d="M34.6967 35.21C33.46 35.21 32.4334 34.9767 31.6167 34.51C30.7767 34.0433 30.1 33.4833 29.5634 32.8533L31.7334 30.4267C32.1767 30.9167 32.6434 31.3133 33.0867 31.5933C33.5534 31.8733 34.0434 32.0133 34.6034 32.0133C35.2567 32.0133 35.77 31.8033 36.1434 31.3833C36.5167 30.9633 36.7034 30.31 36.7034 29.4V19.2733H40.25V29.5633C40.25 30.4967 40.1334 31.3133 39.8767 32.0133C39.62 32.7133 39.2467 33.2967 38.78 33.7633C38.29 34.2533 37.7067 34.6033 37.0067 34.86C36.3067 35.0933 35.5367 35.21 34.6967 35.21Z"></path><path d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z"></path></g></svg><div class="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12"><div class="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p"><h3 class="rs-h3 rs-h3_theme_dark" data-test="banner-title">The Total Economic Impact™ of IntelliJ&nbsp;IDEA study</h3><p class="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description">Commissioned TEI research conducted by Forrester Consulting</p></div><a data-test="banner-action" aria-label="Learn more" href="/lp/intellijidea-forrester-tei/" type="button" class="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569"><path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z"></path></svg></a></div></div><a href="/lp/intellijidea-forrester-tei/" class="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Learn more" data-test="banner-link"></a></div></div></div></div></div></div></nav><div class="wt-col-inline wt-col_align-self_center _siteHeader__actions_4tval" data-test="desktop-side-header-actions"><div class="_siteHeaderActions__row_dnkmi"><div class="_siteHeaderActions__action_r5cvz _siteHeaderActions__action_izukp"><button data-test="site-header-search-action" aria-label="Open search" type="button" class="_main_1dh718a_17 _modeClear_1dh718a_478 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _siteHeaderAction_tgwyh"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _siteHeaderAction__icon_qg4ev _siteHeaderAction__icon_vh845f _icon_1dh718a_569"><path d="M2.293 10a6.99 6.99 0 0 0 11.187 5.6l6.106 6.107L21 20.293l-6.106-6.106A6.997 6.997 0 1 0 2.293 10zm2 0a5 5 0 1 1 5 5 5 5 0 0 1-5-5z"></path></svg></button></div><div class="_siteHeaderActions__action_r5cvz _siteHeaderActions__action_izukp"><a data-test="site-header-profile-action" aria-label="Navigate to profile" href="https://account.jetbrains.com/" type="button" class="_main_1dh718a_17 _modeClear_1dh718a_478 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _siteHeaderAction_tgwyh"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _siteHeaderAction__icon_qg4ev _siteHeaderAction__icon_vh845f _icon_1dh718a_569"><circle cx="12" cy="5.5" r="2.5"></circle><path d="M15 10H9a4 4 0 0 0-4 4v7h14v-7a4 4 0 0 0-4-4z"></path></svg></a></div><div class="_siteHeaderActions__action_r5cvz _siteHeaderActions__action_izukp"><a data-test="site-header-cart-action" aria-label="Navigate to Store" href="/store/" type="button" class="_main_1dh718a_17 _modeClear_1dh718a_478 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _siteHeaderAction_tgwyh"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _siteHeaderAction__icon_qg4ev _siteHeaderAction__icon_vh845f _icon_1dh718a_569"><circle cx="6" cy="19" r="2"></circle><circle cx="16" cy="19" r="2"></circle><path d="M19.997 7H7.13l-.885-2.352A1 1 0 0 0 5.308 4H2v2h2.628L5 7l2.368 7.103a2 2 0 0 0 2.53 1.265l8.734-2.912A2 2 0 0 0 20 10.557z"></path></svg></a></div><div class="_siteHeaderActions__action_r5cvz _siteHeaderActions__action_izukp"><span data-test="dropdown-trigger" class="_triggerWrapper_1t4sa2o_55"><button data-test="language-picker" aria-label="Open language selection" type="button" class="_main_1dh718a_17 _modeClear_1dh718a_478 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _desktopSiteHeaderActions__languagePicker_bdprm _desktopSiteHeaderActions__languagePicker_6fayc"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569"><path d="m11.62965 16.61452c-1.13922-.692-3.111-2.36313-3.153-2.32718a28.32942 28.32942 0 0 1 -3.30095 2.26177c-.68823.39708-1.38892.49615-1.82064-.09139a.992.992 0 0 1 .26656-1.40406c.00852-.00391 2.44665-1.594 3.25973-2.29678a11.64387 11.64387 0 0 1 -2.23281-3.53521 1.07774 1.07774 0 0 1 .52716-1.36835c.52715-.22205 1.049-.12664 1.48663.61989a10.33341 10.33341 0 0 0 1.8143 2.89517 10.853 10.853 0 0 0 2.1563-4.3469l-7.63293-.02148v-2.00685h4.8124v-.99406a.98574.98574 0 1 1 1.9713 0v.99406h5.1703v2.00685h-2.08646a17.03869 17.03869 0 0 1 -2.64065 5.75689 15.88157 15.88157 0 0 0 2.30149 1.66068l2.3092-5.66617a1.162 1.162 0 0 1 2.1802.01591l3.01041 7.389 1.85638 4.385h-2.47393l-1.08252-2.53924h-4.84082l-.888 2.53924h-2.5993l.287-.69166zm4.31307-5.16715-1.67531 4.55419h3.35059z"></path></svg></button></span></div></div></div></div></div><div class="wt-col-auto-fill wt-col_align-self_stretch _siteHeader__contentPart_932t4 _siteHeader__mobileContentPart_j250y _siteHeader__mobileContentPart_8vd8s _siteHeader__mobileContentPart_4521jk"><div class="wt-row wt-row_size_0 wt-row_justify_end _siteHeader__contentPartRow_tkflnh"><div class="_siteHeaderActiveSitePart_uwmy6 wt-col-auto-fill _siteHeader__activeSitePart_zpimg" data-test="site-header-active-site-part"><div class="_siteHeaderActiveSitePart__textWrapper_dk3sb _siteHeaderActiveSitePart__textWrapper_lnsw1"><div class="rs-h4 rs-h4_theme_dark _siteHeaderActiveSitePart__text_2zas4" data-test="text-part">PyCharm</div></div></div><div class="wt-col-auto-fill _siteHeader__mobileMainMenuWrapper_3k2otf _siteHeader__mobileMainMenuWrapper_xw82d"><nav class="_mobileMainMenu_t6q" data-test="mobile-main-menu"><div class="_mobileMainMenu__inner_8raok"><div class="wt-row wt-row_size_0"><div class="wt-col-inline" data-test="mobile-main-menu-item" data-test-marker="Developer Tools"><button class="_mobileMainMenuItem__action_5guvc _mobileMainMenuItem__action_aia9hh _mobileMainMenuItem__action_zczl4 _mobileMainMenuItem__action_jh6aw _mobileMainMenuItem__action_lfuz6" type="button" aria-label="Developer Tools: Open submenu" data-test="mobile-main-menu-item-action">Developer Tools</button><div class="_mobileMainSubmenu_5p4gw _mobileMainMenuItem__submenu_v3gfo wt-display-none" data-test="mobile-main-submenu"><div class="_mobileMainSubmenu__columnsWrapper_5r3czi"><div class="_mobileMainSubmenu__column_osm81 _mobileMainSubmenu__column--full-size_niturg wt-offset-top-24 wt-offset-top-sm-48"><h5 class="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title">IDEs</h5><div class="wt-offset-top-12"><div class="_mobileMainSubmenuSubColumns__columnsWrapper_zt0m2"><div class="_mobileMainSubmenuSubColumns__column_gnsze _mobileMainSubmenuSubColumns__columnHalfSize_oo8jwi"><div class=""><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/objc/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">AppCode</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__85" x1="30.221" x2="69.796" y1="63.074" y2="63.074" gradientUnits="userSpaceOnUse"><stop offset="0.194" stop-color="#07C3F2"></stop><stop offset="0.903" stop-color="#087CFA"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__84" x1="1.274" x2="38.41" y1="16.036" y2="16.036" gradientUnits="userSpaceOnUse"><stop offset="0.194" stop-color="#07C3F2"></stop><stop offset="0.903" stop-color="#087CFA"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__83" x1="45.876" x2="11.197" y1="72.222" y2="23.824" gradientUnits="userSpaceOnUse"><stop offset="0.091" stop-color="#21D789"></stop><stop offset="0.484" stop-color="#07C3F2"></stop><stop offset="0.903" stop-color="#087CFA"></stop></linearGradient></defs><path fill="#087CFA" d="M53.5207 70L69.9999 26.3229L41.5625 19.6875L53.5207 70Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__85)" d="M69.7812 56.1458L53.5208 70L30.1874 64.0208L42 54.5L69.7812 56.1458Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__84)" d="M8.7501 32.0833L1.23969 10.7917L38.4272 0L29.5 21.5L8.7501 32.0833Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__83)" d="M61.1042 40.5417L50.6771 22.75L50.8229 22.6042L38.4271 0L0 41.4896V70L69.7812 56.1458L61.1042 40.5417Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4167 48.65H18.6667V51.3333H34.4167V48.65Z"></path><g fill="#FFF"><path d="M24.7993 19.13H27.9253L34.5941 34.76H31.0513L29.662 31.2867H23.0627L21.6733 34.76H18.2L24.7993 19.13ZM28.3421 28.2301L26.2581 23.1591L24.1741 28.2301H28.3421Z"></path><path d="M34.6 27.0667C34.6 22.6333 37.8666 18.9 42.7666 18.9C45.8 18.9 47.4333 19.8333 49.0666 21.2333L46.9666 23.8C45.8 22.6333 44.6333 21.9333 43 21.9333C40.4333 21.9333 38.3333 24.0333 38.3333 26.8333C38.3333 29.6333 40.2 31.7333 43 31.7333C44.8666 31.7333 45.8 31.0333 47.2 29.8667L49.3 32.2C47.4333 34.0667 45.5666 35 42.5333 35C37.8666 35 34.6 31.5 34.6 27.0667Z"></path></g></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/aqua/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">Aqua</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__87" x1="25.657" x2="16.44" y1="58.53" y2="25.272" gradientUnits="userSpaceOnUse"><stop stop-color="#087CFA"></stop><stop offset="1" stop-color="#6B57FF"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__86" x1="13.002" x2="47.315" y1="63.483" y2="14.124" gradientUnits="userSpaceOnUse"><stop stop-color="#087CFA"></stop><stop offset="0.387" stop-color="#097FF6"></stop><stop offset="0.96" stop-color="#3BEA62"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__87)" d="M33.084 25.1406L3.47891 17.9053L0 26.1363L10.6717 60.2709L39.0261 70.0002L33.084 25.1406Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__86)" d="M70.0002 20.0238L62.8851 6.09226L26.579 0L10.6719 60.2707L39.0262 70L40.5453 67.5065L70.0002 20.0238Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#fff" d="M34.4165 48.6494H18.6665V51.3327H34.4165V48.6494Z"></path><path fill="#fff" d="M42.3063 19.2559H45.4747L52.1688 34.9866H48.5763L47.1482 31.4835H40.5436L39.1155 34.9866H35.6123L42.3063 19.2559ZM45.921 28.4489L43.8459 23.3837L41.7708 28.4489H45.921V28.4489Z"></path><path fill="#fff" d="M32.884 35.4562L31.1659 33.9166C29.8494 34.7645 28.2652 35.2553 26.5247 35.2553C21.7051 35.2553 18.2466 31.6629 18.2466 27.2227V27.178C18.2466 22.7377 21.7497 19.1006 26.5694 19.1006C31.389 19.1006 34.8475 22.6931 34.8475 27.1334V27.178C34.8475 28.8291 34.3343 30.3688 33.4642 31.6629L35.0707 33.0241L32.884 35.4562V35.4562ZM28.6222 31.6629L26.0785 29.4986L28.2652 27.0441L30.8312 29.3647C31.099 28.74 31.2551 28.0036 31.2551 27.2227V27.178C31.2551 24.5004 29.2916 22.2691 26.5247 22.2691C23.7579 22.2691 21.839 24.4558 21.839 27.1334V27.178C21.839 29.8556 23.8026 32.0869 26.5694 32.0869C27.328 32.0869 28.0197 31.953 28.6222 31.6629V31.6629Z"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/clion/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">CLion</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__91" x1="25.161" x2="45.217" y1="13.686" y2="13.686" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FF318C"></stop><stop offset="0.149" stop-color="#FB348C"></stop><stop offset="0.285" stop-color="#F03C8C"></stop><stop offset="0.416" stop-color="#DE4A8C"></stop><stop offset="0.543" stop-color="#C45D8B"></stop><stop offset="0.669" stop-color="#A2778B"></stop><stop offset="0.793" stop-color="#79958A"></stop><stop offset="0.913" stop-color="#49B98A"></stop><stop offset="1" stop-color="#21D789"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__90" x1="17.131" x2="6.836" y1="8.883" y2="77.965" gradientUnits="userSpaceOnUse"><stop offset="0.091" stop-color="#21D789"></stop><stop offset="0.903" stop-color="#009AE5"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__89" x1="63.836" x2="-6.583" y1="6.492" y2="80.865" gradientUnits="userSpaceOnUse"><stop offset="0.091" stop-color="#21D789"></stop><stop offset="0.903" stop-color="#009AE5"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__88" x1="42.791" x2="66.875" y1="51.126" y2="54.551" gradientUnits="userSpaceOnUse"><stop offset="0.091" stop-color="#21D789"></stop><stop offset="0.903" stop-color="#009AE5"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__91)" d="M20 41.5L26.6875 0L42.5833 8.82292L20 41.5Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__90)" d="M26.6875 39V0L6.48958 12.7604L0 51.4792L26.6875 39Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__89)" d="M68.6146 21L59.5729 2.69789L42.5833 8.82289L25.1563 27.3437L0 51.4791L22.6771 67.9583L51.2604 42.2187L68.6146 21Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__88)" d="M56.8748 40.1042L45.9373 35L26.7969 55.2344L41.4894 66.2083L58.9894 70L69.9998 45.0625L56.8748 40.1042Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4167 48.65H18.6667V51.3333H34.4167V48.65Z"></path><g fill="#FFF"><path d="M36 19.13H39.458V31.8553H46.3047V34.76H36V19.13Z"></path><path d="M18 27.0667C18 22.6333 21.2667 18.9 26.1667 18.9C29.2 18.9 30.8333 19.8333 32.4667 21.2333L30.3667 23.8C29.2 22.6333 28.0333 21.9333 26.4 21.9333C23.8333 21.9333 21.7333 24.0333 21.7333 26.8333C21.7333 29.6333 23.6 31.7333 26.4 31.7333C28.2667 31.7333 29.2 31.0333 30.6 29.8667L32.7 32.2C30.8333 34.0667 28.9667 35 25.9333 35C21.2667 35 18 31.5 18 27.0667Z"></path></g></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/datagrip/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">DataGrip</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__96" x1="64.084" x2="66.131" y1="26.335" y2="44.156" gradientUnits="userSpaceOnUse"><stop offset="0.16" stop-color="#21D789"></stop><stop offset="0.54" stop-color="#419FBC"></stop><stop offset="1" stop-color="#6B57FF"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__95" x1="45.467" x2="50.644" y1="18.684" y2="5.439" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6B57FF"></stop><stop offset="0.952" stop-color="#21D789"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__94" x1="16.86" x2="21.888" y1="35.34" y2="57.248" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6B57FF"></stop><stop offset="0.022" stop-color="#685CFB"></stop><stop offset="0.281" stop-color="#4A91CA"></stop><stop offset="0.506" stop-color="#34B7A7"></stop><stop offset="0.685" stop-color="#26CE91"></stop><stop offset="0.797" stop-color="#21D789"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__93" x1="4.36" x2="65.7" y1="35.008" y2="68.875" gradientUnits="userSpaceOnUse"><stop offset="0.075" stop-color="#21D789"></stop><stop offset="0.887" stop-color="#6B57FF"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__92" x1="4.735" x2="66.381" y1="26.84" y2="26.84" gradientUnits="userSpaceOnUse"><stop offset="0.309" stop-color="#21D789"></stop><stop offset="0.487" stop-color="#59A3B2"></stop><stop offset="0.767" stop-color="#B74AF7"></stop><stop offset="1" stop-color="#FF45ED"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__96)" d="M65.5521 10.8646L70 39.5208L61.7604 44.3333L56.5 26.5L65.5521 10.8646Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__95)" d="M65.5521 10.8646L40.4687 0L33.4688 5.83333L45 17L65.5521 10.8646Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__94)" d="M47.3229 70L11 30.5L0.583313 62.4896L47.3229 70Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__93)" d="M54.5 45L0 32.3021L47.3229 70L54.5 45Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__92)" d="M0 0.510406V32.3021L60.7396 53.1562L65.5521 10.8646L0 0.510406Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3333H34.4166V48.6499Z"></path><path fill="#FFF" d="M35.8 27.224C35.8 22.6811 39.3191 18.97 44.118 18.97C46.9973 18.97 48.6608 19.7378 50.3244 21.1455L48.149 23.8328C46.9333 22.8091 45.8455 22.2332 43.99 22.2332C41.4306 22.2332 39.4471 24.4727 39.4471 27.16V27.224C39.4471 30.1033 41.4306 32.2148 44.2459 32.2148C45.5256 32.2148 46.6133 31.8948 47.5091 31.255V29.0155H43.99V26.0083H50.8363V32.8546C49.3007 34.2623 47.0612 35.35 44.1819 35.35C39.1912 35.35 35.8 31.8948 35.8 27.224Z"></path><path fill="#FFF" d="M18.5 19.1334H24.6833C29.7 19.1334 33.0833 22.4876 33.0833 26.8828C33.0833 31.2779 29.7 34.7478 24.6833 34.7478L18.5 34.8634V19.1334ZM22 22.2563V31.7406H24.6833C27.4833 31.7406 29.4667 29.89 29.4667 27.1141C29.4667 24.3382 27.6 22.372 24.6833 22.372L22 22.2563Z"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/dataspell/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">DataSpell</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__100" x1="51.915" x2="5.515" y1="21.235" y2="21.235" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#21D789"></stop><stop offset="0.917" stop-color="#FCF84A"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__99" x1="53.765" x2="53.765" y1="20.208" y2="78.116" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#21D789"></stop><stop offset="1" stop-color="#087CFA"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__98" x1="92.069" x2="23.619" y1="72.972" y2="17.191" gradientUnits="userSpaceOnUse"><stop offset="0.105" stop-color="#21D789"></stop><stop offset="0.967" stop-color="#087CFA"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__97" x1="60.521" x2="12.274" y1="-5.388" y2="49.291" gradientUnits="userSpaceOnUse"><stop offset="0.235" stop-color="#21D789"></stop><stop offset="0.74" stop-color="#087CFA"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__100)" d="M44.9896 0L46.375 28.4375L10.9375 42.4375L-1.50998e-07 14.1458L44.9896 0Z"></path><path fill="#21D789" d="M70 16.625L39.375 29.8958L44.9896 0L70 16.625Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__99)" d="M37.5521 23.1874L70 16.6249V47.3229L47.6875 55.7083L38.5729 47.3958L37.5521 23.1874Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__98)" d="M24.0625 14.2188L46.4498 17.6823L70 47.0502L47.3947 55.7812L38.6724 47.1224L24.0625 14.2188Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__97)" d="M14.4375 0L46.375 17.6458L35.3646 70H16.7708L0.656255 53.375L14.4375 0Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.65H18.6666V51.3333H34.4166V48.65Z"></path><path fill="#FFF" d="M19 19H25.1833C30.2 19 33.5833 22.3542 33.5833 26.7493C33.5833 31.1445 30.2 34.6143 25.1833 34.6143L19 34.73V19ZM22.5 22.1229V31.6071H25.1833C27.9833 31.6071 29.9667 29.7565 29.9667 26.9807C29.9667 24.2048 28.1 22.2385 25.1833 22.2385L22.5 22.1229Z"></path><path fill="#FFF" d="M34.97 32.36L37 29.91C38.4 31.1 39.94 31.8 41.69 31.8C43.09 31.8 44 31.24 44 30.33V30.26C44 29.35 43.44 28.93 40.85 28.23C37.63 27.46 35.6 26.55 35.6 23.4V23.33C35.6 20.46 37.91 18.57 41.13 18.57C43.44 18.57 45.4 19.27 47.01 20.6L45.19 23.19C43.79 22.21 42.39 21.65 41.06 21.65C39.73 21.65 39.03 22.28 39.03 23.05V23.12C39.03 24.17 39.73 24.52 42.46 25.22C45.68 26.06 47.5 27.18 47.5 29.98V30.05C47.5 33.2 45.12 34.95 41.69 34.95C39.31 34.88 36.86 34.04 34.97 32.36Z"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/fleet/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">Fleet</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><radialGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__108" cx="0" cy="0" r="1" gradientTransform="matrix(22.35433 -20.58122 27.17129 29.51214 38.648 42.538)" gradientUnits="userSpaceOnUse"><stop offset="0.771" stop-color="#001AFF"></stop><stop offset="1" stop-color="#8ACEFF"></stop></radialGradient><radialGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__107" cx="0" cy="0" r="1" gradientTransform="rotate(-30.543 79.837 -70.068) scale(16.777 22.1489)" gradientUnits="userSpaceOnUse"><stop offset="0.719" stop-color="#FA00FF" stop-opacity="0"></stop><stop offset="1" stop-color="#FF00D6" stop-opacity="0.44"></stop></radialGradient><radialGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__106" cx="0" cy="0" r="1" gradientTransform="rotate(49.385 -19.814 41.858) scale(47.8852)" gradientUnits="userSpaceOnUse"><stop offset="0.026" stop-color="#8DFDFD"></stop><stop offset="0.271" stop-color="#87FBFB"></stop><stop offset="0.484" stop-color="#74D6F4"></stop><stop offset="0.932" stop-color="#0038FF"></stop></radialGradient><radialGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__105" cx="0" cy="0" r="1" gradientTransform="rotate(137.237 9.434 23.195) scale(32.8316)" gradientUnits="userSpaceOnUse"><stop offset="0.267" stop-color="#0500FF" stop-opacity="0"></stop><stop offset="1" stop-color="#0500FF" stop-opacity="0.15"></stop></radialGradient><radialGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__104" cx="0" cy="0" r="1" gradientTransform="rotate(75.198 -4.629 32.631) scale(51.1484)" gradientUnits="userSpaceOnUse"><stop offset="0.42" stop-color="#FF00E5" stop-opacity="0"></stop><stop offset="0.774" stop-color="#FF00F5" stop-opacity="0.64"></stop><stop offset="0.899" stop-color="#BE46FF" stop-opacity="0.87"></stop></radialGradient><radialGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__103" cx="0" cy="0" r="1" gradientTransform="matrix(2.73484 22.75837 -34.39872 4.13365 29.458 35.276)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#00B2FF"></stop><stop offset="0.571" stop-color="#74C5FF"></stop><stop offset="0.979" stop-color="#9FD7FF"></stop></radialGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__102" x1="11.644" x2="82.363" y1="42.432" y2="43.401" gradientUnits="userSpaceOnUse"><stop offset="0.432" stop-color="#FE62EE" stop-opacity="0"></stop><stop offset="0.818" stop-color="#FD3AF5" stop-opacity="0.47"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__101" x1="33.054" x2="37.35" y1="23.191" y2="49.344" gradientUnits="userSpaceOnUse"><stop offset="0.042" stop-color="#0038FF"></stop><stop offset="0.724" stop-color="#48BFF1" stop-opacity="0.59"></stop><stop offset="1" stop-color="#74C5FF" stop-opacity="0"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__108)" d="M65.153 30.85c0 9.496-10.163 17.194-22.7 17.194-12.536 0-22.699-7.698-22.699-17.194 0-9.496 10.163-17.194 22.7-17.194 12.536 0 22.699 7.698 22.699 17.194z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__107)" d="M65.153 30.85c0 9.496-10.163 17.194-22.7 17.194-12.536 0-22.699-7.698-22.699-17.194 0-9.496 10.163-17.194 22.7-17.194 12.536 0 22.699 7.698 22.699 17.194z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__106)" d="M66 35c0 17.12-13.88 31-31 31C17.88 66 4 52.12 4 35 4 17.88 17.88 4 35 4c8.046 3.642 16.464 17.194 19.99 21.429 3.524 4.235 12.648 9.571 8.176-1.623C65.073 26.832 66 31.852 66 35z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__105)" d="M66 35c0 17.12-13.88 31-31 31C17.88 66 4 52.12 4 35 4 17.88 17.88 4 35 4c8.046 3.642 16.464 17.194 19.99 21.429 3.524 4.235 12.648 9.571 8.176-1.623C65.073 26.832 66 31.852 66 35z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__104)" d="M66 35c0 17.12-13.88 31-31 31C17.88 66 4 52.12 4 35 4 17.88 17.88 4 35 4c8.046 3.642 16.464 17.194 19.99 21.429 3.524 4.235 12.648 9.571 8.176-1.623C65.073 26.832 66 31.852 66 35z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__102)" d="M66 35c0 17.12-13.88 31-31 31C17.88 66 4 52.12 4 35 4 17.88 17.88 4 35 4c8.046 3.642 16.464 17.194 19.99 21.429 3.524 4.235 12.648 9.571 8.176-1.623C65.073 26.832 66 31.852 66 35z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__103)" d="M56.651 39.682c1.658 7.764-6.511 16.089-18.246 18.594-11.734 2.505-22.59-1.757-24.248-9.52-1.658-7.764 6.511-16.089 18.246-18.594 11.734-2.506 22.59 1.757 24.248 9.52z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__101)" d="M56.651 39.682c1.658 7.764-6.511 16.089-18.246 18.594-11.734 2.505-22.59-1.757-24.248-9.52-1.658-7.764 6.511-16.089 18.246-18.594 11.734-2.506 22.59 1.757 24.248 9.52z"></path><path fill="#D6F8F8" fill-opacity="0.19" fill-rule="evenodd" d="M51.462 49.883c3.074-3.133 4.386-6.66 3.698-9.882-.688-3.223-3.326-5.907-7.411-7.51-4.073-1.6-9.412-2.037-15.028-.838-5.616 1.199-10.31 3.779-13.375 6.901-3.074 3.133-4.386 6.66-3.698 9.883.688 3.223 3.326 5.906 7.412 7.51 4.072 1.6 9.41 2.037 15.027.838 5.616-1.2 10.31-3.779 13.375-6.902zm-13.057 8.393c11.735-2.505 19.904-10.83 18.246-18.594-1.658-7.763-12.514-12.026-24.248-9.52-11.735 2.505-19.904 10.83-18.246 18.593 1.658 7.764 12.514 12.026 24.248 9.521z" clip-rule="evenodd"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/go/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">GoLand</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__111" x1="68.929" x2="41.588" y1="39.874" y2="63.009" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#087CFA"></stop><stop offset="0.023" stop-color="#0D7BFA"></stop><stop offset="0.373" stop-color="#5566F9"></stop><stop offset="0.663" stop-color="#8A57F8"></stop><stop offset="0.881" stop-color="#AB4EF7"></stop><stop offset="1" stop-color="#B74AF7"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__110" x1="24.089" x2="40.706" y1="21.699" y2="2.794" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#087CFA"></stop><stop offset="0.023" stop-color="#0D7BFA"></stop><stop offset="0.373" stop-color="#5566F9"></stop><stop offset="0.663" stop-color="#8A57F8"></stop><stop offset="0.881" stop-color="#AB4EF7"></stop><stop offset="1" stop-color="#B74AF7"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__109" x1="9.725" x2="60.22" y1="61.15" y2="28.702" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#087CFA"></stop><stop offset="0.102" stop-color="#1598D3"></stop><stop offset="0.225" stop-color="#23B6AA"></stop><stop offset="0.345" stop-color="#2DCC8B"></stop><stop offset="0.462" stop-color="#35DD74"></stop><stop offset="0.572" stop-color="#39E767"></stop><stop offset="0.67" stop-color="#3BEA62"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__111)" d="M61.6875 27.0521L70 45.5729L55.7083 70L38.5 42L61.6875 27.0521Z"></path><path fill="#B74AF7" d="M44.5 44L55.7083 70L33.6146 62.4167L44.5 44Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__110)" d="M49.2917 19.7604L44.7708 0H19.6146L0 30.0417L5.6875 43.8229L0 56.4375L49.2917 37V19.7604Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__109)" d="M70 14.875L40.6146 21.8021L0 56.4375L26.25 70L46.9583 48.6354L70 14.875Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z"></path><path fill="#FFF" d="M18 27.224C18 22.6811 21.5191 18.97 26.318 18.97C29.1973 18.97 30.8609 19.7378 32.5244 21.1454L30.349 23.8328C29.1333 22.809 28.0455 22.2332 26.19 22.2332C23.6306 22.2332 21.6471 24.4726 21.6471 27.16V27.224C21.6471 30.1033 23.6306 32.2147 26.4459 32.2147C27.7256 32.2147 28.8134 31.8948 29.7091 31.255V29.0155H26.19V26.0083H33.0363V32.8546C31.5007 34.2622 29.2612 35.35 26.382 35.35C21.3912 35.35 18 31.8948 18 27.224Z"></path><path fill="#FFF" d="M34.572 27.224C34.572 22.6811 38.0911 18.97 43.0179 18.97C47.8807 18.97 51.3998 22.6171 51.3998 27.096V27.16C51.3998 31.6389 47.8807 35.35 42.9539 35.35C38.0911 35.35 34.572 31.7029 34.572 27.224ZM47.7527 27.224C47.7527 24.4726 45.7692 22.2332 42.9539 22.2332C40.1386 22.2332 38.2191 24.4726 38.2191 27.16V27.224C38.2191 29.9113 40.2026 32.2147 43.0179 32.2147C45.8332 32.1508 47.7527 29.9753 47.7527 27.224Z"></path></svg></span></a></div></div></div><div class="_mobileMainSubmenuSubColumns__column_gnsze _mobileMainSubmenuSubColumns__columnHalfSize_oo8jwi"><div class=""><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/idea/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">IntelliJ&nbsp;IDEA</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__114" x1="5.174" x2="40.014" y1="39.889" y2="38.123" gradientUnits="userSpaceOnUse"><stop offset="0.091" stop-color="#FC801D"></stop><stop offset="0.231" stop-color="#B07F61"></stop><stop offset="0.409" stop-color="#577DB3"></stop><stop offset="0.533" stop-color="#1E7CE6"></stop><stop offset="0.593" stop-color="#087CFA"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__113" x1="61.991" x2="50.158" y1="36.915" y2="1.557" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FE2857"></stop><stop offset="0.078" stop-color="#CB3979"></stop><stop offset="0.16" stop-color="#9E4997"></stop><stop offset="0.247" stop-color="#7557B2"></stop><stop offset="0.339" stop-color="#5362C8"></stop><stop offset="0.436" stop-color="#386CDA"></stop><stop offset="0.541" stop-color="#2373E8"></stop><stop offset="0.658" stop-color="#1478F2"></stop><stop offset="0.794" stop-color="#0B7BF8"></stop><stop offset="1" stop-color="#087CFA"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__112" x1="10.066" x2="53.876" y1="16.495" y2="88.96" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FE2857"></stop><stop offset="0.08" stop-color="#FE295F"></stop><stop offset="0.206" stop-color="#FF2D76"></stop><stop offset="0.303" stop-color="#FF318C"></stop><stop offset="0.385" stop-color="#EA3896"></stop><stop offset="0.553" stop-color="#B248AE"></stop><stop offset="0.792" stop-color="#5A63D6"></stop><stop offset="1" stop-color="#087CFA"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__114)" d="M11.2 49.4668L0.699951 41.3001L9 26L18.5 33.5L11.2 49.4668Z"></path><path fill="#087CFA" d="M69.9999 18.6666L68.8333 59.2666L41.7666 70L27.0666 60.4333L41.7666 37.5L69.9999 18.6666Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__113)" d="M70 18.6666L55.5 33L37 15L48.0666 1.16663L70 18.6666Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__112)" d="M27.0667 60.4333L5.6 68.3667L10.0333 52.5L15.8667 33.1333L0 27.7667L10.0333 0L33.1333 2.8L54.5 31L55.5 33L27.0667 60.4333Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><g fill="#FFF"><path d="M27.1366 22.1433V19.25H19.2733V22.1433H21.4666V32.1067H19.2733V34.9767H27.1366V32.1067H24.92V22.1433H27.1366Z"></path><path d="M34.6967 35.21C33.46 35.21 32.4334 34.9767 31.6167 34.51C30.7767 34.0433 30.1 33.4833 29.5634 32.8533L31.7334 30.4267C32.1767 30.9167 32.6434 31.3133 33.0867 31.5933C33.5534 31.8733 34.0434 32.0133 34.6034 32.0133C35.2567 32.0133 35.77 31.8033 36.1434 31.3833C36.5167 30.9633 36.7034 30.31 36.7034 29.4V19.2733H40.25V29.5633C40.25 30.4967 40.1334 31.3133 39.8767 32.0133C39.62 32.7133 39.2467 33.2967 38.78 33.7633C38.29 34.2533 37.7067 34.6033 37.0067 34.86C36.3067 35.0933 35.5367 35.21 34.6967 35.21Z"></path><path d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z"></path></g></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/phpstorm/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">PhpStorm</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__118" x1="17.617" x2="23.56" y1="21.533" y2="9.655" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#AF1DF5"></stop><stop offset="0.21" stop-color="#BC20E4"></stop><stop offset="0.63" stop-color="#DD29B8"></stop><stop offset="1" stop-color="#FF318C"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__117" x1="2.258" x2="31.498" y1="48.027" y2="9.401" gradientUnits="userSpaceOnUse"><stop offset="0.02" stop-color="#6B57FF"></stop><stop offset="0.42" stop-color="#B74AF7"></stop><stop offset="0.75" stop-color="#FF318C"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__116" x1="53.04" x2="35.657" y1="47.667" y2="6.426" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#293896"></stop><stop offset="0.08" stop-color="#3B3AA2"></stop><stop offset="0.29" stop-color="#6740C0"></stop><stop offset="0.49" stop-color="#8A44D8"></stop><stop offset="0.68" stop-color="#A347E9"></stop><stop offset="0.86" stop-color="#B249F3"></stop><stop offset="1" stop-color="#B74AF7"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__115" x1="50.044" x2="23.634" y1="61.283" y2="22.588" gradientUnits="userSpaceOnUse"><stop offset="0.02" stop-color="#6B57FF"></stop><stop offset="0.78" stop-color="#B74AF7"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__118)" d="M38.6458 12.3228L36.3125 5.24996L11.9583 0L0 13.4895L13.125 20.1978L34.9271 30.0415L38.6458 12.3228Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__117)" d="M26.9792 20.489L0 13.489L6.63542 53.5929L26.4687 53.52L26.9792 20.489Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__116)" d="M18.9582 25.6665L34.0519 12.2499L43.2394 4.15625L60.8853 7.43748L69.9999 30.0415L56.8749 43.0935L18.9582 25.6665Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__115)" d="M49.9479 17.0628L14.2188 16.917L19.25 56.073L20.1979 61.7604L43.8958 70L70 54.323L49.9479 17.0628Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z"></path><path fill="#FFF" d="M32.97 32.76L35 30.31C36.4 31.5 37.94 32.2 39.69 32.2C41.09 32.2 42 31.64 42 30.73V30.66C42 29.75 41.44 29.33 38.85 28.63C35.63 27.86 33.6 26.95 33.6 23.8V23.73C33.6 20.86 35.91 18.97 39.13 18.97C41.44 18.97 43.4 19.67 45.01 21L43.19 23.59C41.79 22.61 40.39 22.05 39.06 22.05C37.73 22.05 37.03 22.68 37.03 23.45V23.52C37.03 24.57 37.73 24.92 40.46 25.62C43.68 26.46 45.5 27.58 45.5 30.38V30.45C45.5 33.6 43.12 35.35 39.69 35.35C37.31 35.28 34.86 34.44 32.97 32.76Z"></path><path fill="#FFF" d="M19.25 19.25H25.69C29.47 19.25 31.71 21.49 31.71 24.71V24.78C31.71 28.42 28.91 30.31 25.34 30.31H22.68V35H19.25V19.25ZM25.48 27.16C27.23 27.16 28.21 26.11 28.21 24.78V24.71C28.21 23.17 27.16 22.33 25.41 22.33H22.75V27.16H25.48Z"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/pycharm/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">PyCharm</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__123" x1="24.999" x2="66.656" y1="27.046" y2="27.046" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#21D789"></stop><stop offset="1" stop-color="#07C3F2"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__122" x1="-24.559" x2="61.22" y1="59.081" y2="-4.241" gradientUnits="userSpaceOnUse"><stop offset="0.011" stop-color="#FCF84A"></stop><stop offset="0.112" stop-color="#A7EB62"></stop><stop offset="0.206" stop-color="#5FE077"></stop><stop offset="0.273" stop-color="#32DA84"></stop><stop offset="0.306" stop-color="#21D789"></stop><stop offset="0.577" stop-color="#21D789"></stop><stop offset="0.597" stop-color="#21D789"></stop><stop offset="0.686" stop-color="#20D68C"></stop><stop offset="0.763" stop-color="#1ED497"></stop><stop offset="0.835" stop-color="#19D1A9"></stop><stop offset="0.904" stop-color="#13CCC2"></stop><stop offset="0.971" stop-color="#0BC6E1"></stop><stop offset="1" stop-color="#07C3F2"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__121" x1="9.33" x2="23.637" y1="77.654" y2="32.76" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#21D789"></stop><stop offset="0.16" stop-color="#24D888"></stop><stop offset="0.298" stop-color="#2FD985"></stop><stop offset="0.427" stop-color="#41DC80"></stop><stop offset="0.552" stop-color="#5AE079"></stop><stop offset="0.673" stop-color="#7AE46F"></stop><stop offset="0.791" stop-color="#A1EA64"></stop><stop offset="0.904" stop-color="#CFF157"></stop><stop offset="1" stop-color="#FCF84A"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__120" x1="28.275" x2="59.409" y1="38.623" y2="-3.236" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#21D789"></stop><stop offset="0.093" stop-color="#23D986"></stop><stop offset="0.172" stop-color="#2ADE7B"></stop><stop offset="0.247" stop-color="#36E669"></stop><stop offset="0.271" stop-color="#3BEA62"></stop><stop offset="0.35" stop-color="#47EB61"></stop><stop offset="0.494" stop-color="#67ED5D"></stop><stop offset="0.686" stop-color="#9AF156"></stop><stop offset="0.915" stop-color="#E0F64D"></stop><stop offset="1" stop-color="#FCF84A"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__119" x1="75.889" x2="13.158" y1="43.95" y2="43.369" gradientUnits="userSpaceOnUse"><stop offset="0.387" stop-color="#FCF84A"></stop><stop offset="0.463" stop-color="#ECF74C"></stop><stop offset="0.611" stop-color="#C1F451"></stop><stop offset="0.815" stop-color="#7EEF5A"></stop><stop offset="1" stop-color="#3BEA62"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__123)" d="M49 10.9668L69.5333 28.0001L62.0666 42.9335L49.9333 39.6668H39.2L49 10.9668Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__122)" d="M28.4667 22.1667L24.5 42.9333L24.0333 50.1667L14.2333 54.6L0 56L4.2 10.7333L29.8667 0L45.7333 10.2667L28.4667 22.1667Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__121)" d="M28.4667 22.1667L30.3333 62.5334L24.0333 70.0001L0 56.0001L19.6 26.6001L28.4667 22.1667Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__120)" d="M54.8333 19.1333H30.5666L52.0333 0L54.8333 19.1333Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__119)" d="M70 62.5333L48.5334 69.7667L20.3 61.8333L28.4667 22.1667L31.7334 19.1333L49 17.5L47.6 35L61.3667 29.6333L70 62.5333Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M19.1333 19.1333H25.55C29.2833 19.1333 31.6167 21.35 31.6167 24.6166C31.6167 28.2333 28.8167 30.1 25.2 30.1H22.5167V34.7666H19.0167V19.1333H19.1333ZM25.3167 27.1833C27.0667 27.1833 28 26.0166 28 24.7333C28 23.2166 26.95 22.4 25.2 22.4H22.5167V27.1833H25.3167Z"></path><path fill="#FFF" d="M33.6 27.0666C33.6 22.6332 36.8667 18.8999 41.7667 18.8999C44.8 18.8999 46.4334 19.8332 48.0667 21.2332L45.9667 23.7999C44.8 22.6332 43.6334 21.9332 42 21.9332C39.4334 21.9332 37.3334 24.0332 37.3334 26.8332C37.3334 29.6332 39.2 31.7332 42 31.7332C43.8667 31.7332 44.8 31.0332 46.2 29.8666L48.3 32.1999C46.4334 34.0666 44.5667 34.9999 41.5334 34.9999C36.8667 34.9999 33.6 31.4999 33.6 27.0666Z"></path><path fill="#FFF" d="M34.4167 48.6499H18.6667V51.3332H34.4167V48.6499Z"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/rider/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">Rider</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__126" x1="65.5" x2="11.542" y1="40.101" y2="9.137" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#DD1265"></stop><stop offset="0.483" stop-color="#DD1265"></stop><stop offset="0.942" stop-color="#FDB60D"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__125" x1="33.416" x2="54.805" y1="6.112" y2="65.175" gradientUnits="userSpaceOnUse"><stop offset="0.139" stop-color="#087CFA"></stop><stop offset="0.476" stop-color="#DD1265"></stop><stop offset="0.958" stop-color="#087CFA"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__124" x1="17.395" x2="33.194" y1="7.934" y2="64.079" gradientUnits="userSpaceOnUse"><stop offset="0.278" stop-color="#DD1265"></stop><stop offset="0.968" stop-color="#FDB60D"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__126)" d="M70 27.2708L20.9272 0L53.8125 48.8542L60.5209 44.4063L70 27.2708Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__125)" d="M50.4583 16.1146L44.2604 1.09375L30.6979 14.5104L36.2395 63.0729L49.4374 70L69.9999 57.9688L50.4583 16.1146Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__124)" d="M20.927 0L0 14.0729L7.80207 62.1979L27.8541 69.8542L53.8124 48.8542L20.927 0Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z"></path><path fill="#FFF" d="M35.5 19.25H41.6833C46.7 19.25 50.0833 22.6042 50.0833 26.9993C50.0833 31.3945 46.7 34.8643 41.6833 34.8643L35.5 34.98V19.25ZM39 22.3729V31.8571H41.6833C44.4833 31.8571 46.4667 30.0065 46.4667 27.2307C46.4667 24.4548 44.6 22.4885 41.6833 22.4885L39 22.3729Z"></path><path fill="#FFF" d="M19.3399 19.25H26.5408C28.5682 19.25 30.0363 19.8093 31.1549 20.858C32.0638 21.7668 32.4832 22.9553 32.4832 24.4234V24.4933C32.4832 25.7517 32.2036 26.8004 31.5744 27.6393C30.9452 28.4084 30.1062 29.0376 29.1275 29.3871L32.9726 34.98H28.9178L25.6319 30.1561H22.7656V34.98H19.27V19.25H19.3399ZM26.331 26.8703C27.17 26.8703 27.8691 26.6606 28.2886 26.2411C28.7779 25.8216 28.9877 25.2624 28.9877 24.6332V24.5632C28.9877 23.7942 28.7779 23.2349 28.2886 22.8854C27.7992 22.5358 27.17 22.3261 26.2611 22.3261H22.8355V26.8703H26.331Z"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/ruby/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">RubyMine</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__129" x1="44.877" x2="36.032" y1="40.487" y2="17.268" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FE2857"></stop><stop offset="0.056" stop-color="#FE3052"></stop><stop offset="0.325" stop-color="#FD533B"></stop><stop offset="0.58" stop-color="#FC6C2A"></stop><stop offset="0.811" stop-color="#FC7B20"></stop><stop offset="1" stop-color="#FC801D"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__128" x1="28.02" x2="41.687" y1="7.252" y2="19.779" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6B57FF"></stop><stop offset="1" stop-color="#FE2857"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__127" x1="0.306" x2="45.3" y1="11.212" y2="68.408" gradientUnits="userSpaceOnUse"><stop offset="0.001" stop-color="#6B57FF"></stop><stop offset="0.297" stop-color="#FE2857"></stop><stop offset="0.629" stop-color="#FE2857"></stop><stop offset="0.641" stop-color="#FE3052"></stop><stop offset="0.701" stop-color="#FD533B"></stop><stop offset="0.757" stop-color="#FC6C2A"></stop><stop offset="0.808" stop-color="#FC7B20"></stop><stop offset="0.85" stop-color="#FC801D"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__129)" d="M58.1875 0L38.2083 7.14583L22.3854 0L17.2084 13.125H13.8542V51.7708L62.4166 52.2083L70 13.7083L58.1875 0Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__128)" d="M57.6042 25.1563L25.6667 6.125L57.6042 43.6771V25.1563Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__127)" d="M29.1666 68.1771L55.2708 64.6771L51.2604 56.875L48.8541 51.7709L51.2604 47.5782L55.2708 39.3751L25.5937 6.125L0 12.3958V49.1458L14.7292 70L29.0208 68.1771H29.0937H29.1666Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z"></path><path fill="#FFF" d="M34.8601 19.25H38.6353L42.7601 25.8916L46.8848 19.25H50.66V34.98H47.1645V24.7031L42.7601 31.4145H42.6902L38.2857 24.773V34.98H34.8601V19.25Z"></path><path fill="#FFF" d="M19.3399 19.25H26.5408C28.5682 19.25 30.0363 19.8093 31.1549 20.858C32.0638 21.7668 32.4832 22.9553 32.4832 24.4234V24.4933C32.4832 25.7517 32.2036 26.8004 31.5744 27.6393C30.9452 28.4084 30.1062 29.0376 29.1275 29.3871L32.9726 34.98H28.9178L25.6319 30.1561H22.7656V34.98H19.27V19.25H19.3399ZM26.331 26.8703C27.17 26.8703 27.8691 26.6606 28.2886 26.2411C28.7779 25.8216 28.9877 25.2624 28.9877 24.6332V24.5632C28.9877 23.7942 28.7779 23.2349 28.2886 22.8854C27.7992 22.5358 27.17 22.3261 26.2611 22.3261H22.8355V26.8703H26.331Z"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/webstorm/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">WebStorm</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__132" x1="25.068" x2="43.183" y1="1.46" y2="66.675" gradientUnits="userSpaceOnUse"><stop offset="0.285" stop-color="#07C3F2"></stop><stop offset="0.941" stop-color="#087CFA"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__131" x1="30.72" x2="61.365" y1="9.734" y2="54.671" gradientUnits="userSpaceOnUse"><stop offset="0.14" stop-color="#FCF84A"></stop><stop offset="0.366" stop-color="#07C3F2"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__130" x1="61.082" x2="65.106" y1="15.29" y2="29.544" gradientUnits="userSpaceOnUse"><stop offset="0.285" stop-color="#07C3F2"></stop><stop offset="0.941" stop-color="#087CFA"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__132)" d="M9.40625 63.2918L0 7.36466L17.4271 0.072998L28.5833 6.70841L38.7917 1.23966L60.0833 9.40633L48.125 70.0001L9.40625 63.2918Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__131)" d="M69.9999 23.6979L60.9582 1.38542L44.552 0L19.2499 24.2813L26.104 55.6354L38.7915 64.5313L69.9999 46.0104L62.3436 31.7188L69.9999 23.6979Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__130)" d="M55.9999 20.3438L62.3436 31.7188L69.9999 23.6979L64.3853 9.84375L55.9999 20.3438Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z"></path><path fill="#FFF" d="M34.16 19.25L31.78 28.42L29.12 19.25H26.46L23.8 28.42L21.42 19.25H17.78L22.26 35H25.2L27.79 25.9L30.31 35H33.32L37.8 19.25H34.16Z"></path><path fill="#FFF" d="M38.5 32.76L40.53 30.31C41.93 31.5 43.47 32.2 45.22 32.2C46.62 32.2 47.53 31.64 47.53 30.73V30.66C47.53 29.75 46.97 29.33 44.38 28.63C41.23 27.79 39.13 26.95 39.13 23.8V23.73C39.13 20.86 41.44 18.97 44.66 18.97C46.97 18.97 48.93 19.67 50.54 21L48.72 23.59C47.32 22.61 45.92 22.05 44.59 22.05C43.26 22.05 42.56 22.68 42.56 23.45V23.52C42.56 24.57 43.26 24.92 45.99 25.62C49.21 26.46 51.03 27.58 51.03 30.38V30.45C51.03 33.6 48.65 35.35 45.22 35.35C42.77 35.28 40.39 34.44 38.5 32.76Z"></path></svg></span></a></div></div></div></div></div></div><div class="_mobileMainSubmenu__column_osm81 _mobileMainSubmenu__column--full-size_niturg wt-offset-top-24 wt-offset-top-sm-48"><h5 class="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title">PLUGINS &amp; SERVICES</h5><div class="wt-offset-top-12"><div class="_mobileMainSubmenuSubColumns__columnsWrapper_zt0m2"><div class="_mobileMainSubmenuSubColumns__column_gnsze _mobileMainSubmenuSubColumns__columnHalfSize_oo8jwi"><div class=""><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://plugins.jetbrains.com/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">All Plugins</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://plugins.jetbrains.com/search?tags=Theme" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">IDE Themes</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://plugins.jetbrains.com/plugin/12494-big-data-tools" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Big Data Tools</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/code-with-me/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Code With Me</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/riderflow/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">RiderFlow</span></span></a></div></div></div><div class="_mobileMainSubmenuSubColumns__column_gnsze _mobileMainSubmenuSubColumns__columnHalfSize_oo8jwi"><div class=""><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/rust/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Rust</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://plugins.jetbrains.com/plugin/1347-scala" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Scala</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/toolbox-app/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Toolbox App</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/toolbox-enterprise/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Toolbox Enterprise</span></span></a></div></div></div></div></div></div><div class="_mobileMainSubmenu__column_osm81 wt-offset-top-24 wt-offset-top-sm-48"><h5 class="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title">.NET &amp; VISUAL STUDIO</h5><div class="wt-offset-top-12"><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/rider/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">Rider</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__135" x1="65.5" x2="11.542" y1="40.101" y2="9.137" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#DD1265"></stop><stop offset="0.483" stop-color="#DD1265"></stop><stop offset="0.942" stop-color="#FDB60D"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__134" x1="33.416" x2="54.805" y1="6.112" y2="65.175" gradientUnits="userSpaceOnUse"><stop offset="0.139" stop-color="#087CFA"></stop><stop offset="0.476" stop-color="#DD1265"></stop><stop offset="0.958" stop-color="#087CFA"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__133" x1="17.395" x2="33.194" y1="7.934" y2="64.079" gradientUnits="userSpaceOnUse"><stop offset="0.278" stop-color="#DD1265"></stop><stop offset="0.968" stop-color="#FDB60D"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__135)" d="M70 27.2708L20.9272 0L53.8125 48.8542L60.5209 44.4063L70 27.2708Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__134)" d="M50.4583 16.1146L44.2604 1.09375L30.6979 14.5104L36.2395 63.0729L49.4374 70L69.9999 57.9688L50.4583 16.1146Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__133)" d="M20.927 0L0 14.0729L7.80207 62.1979L27.8541 69.8542L53.8124 48.8542L20.927 0Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z"></path><path fill="#FFF" d="M35.5 19.25H41.6833C46.7 19.25 50.0833 22.6042 50.0833 26.9993C50.0833 31.3945 46.7 34.8643 41.6833 34.8643L35.5 34.98V19.25ZM39 22.3729V31.8571H41.6833C44.4833 31.8571 46.4667 30.0065 46.4667 27.2307C46.4667 24.4548 44.6 22.4885 41.6833 22.4885L39 22.3729Z"></path><path fill="#FFF" d="M19.3399 19.25H26.5408C28.5682 19.25 30.0363 19.8093 31.1549 20.858C32.0638 21.7668 32.4832 22.9553 32.4832 24.4234V24.4933C32.4832 25.7517 32.2036 26.8004 31.5744 27.6393C30.9452 28.4084 30.1062 29.0376 29.1275 29.3871L32.9726 34.98H28.9178L25.6319 30.1561H22.7656V34.98H19.27V19.25H19.3399ZM26.331 26.8703C27.17 26.8703 27.8691 26.6606 28.2886 26.2411C28.7779 25.8216 28.9877 25.2624 28.9877 24.6332V24.5632C28.9877 23.7942 28.7779 23.2349 28.2886 22.8854C27.7992 22.5358 27.17 22.3261 26.2611 22.3261H22.8355V26.8703H26.331Z"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/resharper/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">ReSharper</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__138" x1="34.448" x2="64.631" y1="70.146" y2="26.155" gradientUnits="userSpaceOnUse"><stop offset="0.016" stop-color="#FF45ED"></stop><stop offset="0.4" stop-color="#DD1265"></stop><stop offset="1" stop-color="#FDB60D"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__137" x1="1.828" x2="48.825" y1="53.428" y2="9.226" gradientUnits="userSpaceOnUse"><stop offset="0.016" stop-color="#FF45ED"></stop><stop offset="0.661" stop-color="#DD1265"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__136" x1="47.598" x2="48.08" y1="-1.658" y2="26.117" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#DD1265"></stop><stop offset="0.055" stop-color="#DF1961"></stop><stop offset="0.701" stop-color="#F46330"></stop><stop offset="1" stop-color="#FC801D"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__138)" d="M51.1974 15.7209L26.3802 47.0706L20.7823 70H58.4484L70 23.0666L51.1974 15.7209Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__137)" d="M48.9858 0H11.6129L0 47.0707H55.6073L48.9858 0Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__136)" d="M50.9338 13.3164L48.9858 0L44.782 13.3164H50.9338Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z"></path><path fill="#FFF" d="M36.0781 31.3592L34.3704 31.3592L34.3703 28.4832L36.5725 28.4832L37.1343 25.1573L35.1567 25.1573L35.1566 22.2812L37.6288 22.2813L38.19 19.0007L41.1567 19.0008L40.5949 22.2814L43.8536 22.2815L44.4147 19.0009L47.3814 19.001L46.8196 22.2816L48.5273 22.2816L48.5274 25.1577L46.3252 25.1576L45.7634 28.4835L47.741 28.4835L47.7411 31.3596L45.2696 31.3595L44.6852 34.73L41.7191 34.7299L42.3029 31.3594L39.0448 31.3593L38.4604 34.7299L35.4943 34.7298L36.0781 31.3592ZM42.7973 28.4834L43.3591 25.1575L40.1004 25.1574L39.5387 28.4833L42.7973 28.4834Z"></path><path fill="#FFF" d="M19 19L26.1868 19.0002C28.1783 19.0003 29.7056 19.5316 30.7688 20.5941C31.2255 21.0702 31.5805 21.6344 31.8121 22.2521C32.0437 22.8699 32.1471 23.5284 32.116 24.1874V24.2327C32.1656 25.3452 31.837 26.4416 31.1836 27.3434C30.5549 28.1499 29.7101 28.7613 28.7474 29.1063L32.5883 34.7207L28.5456 34.7206L25.2918 29.8921L22.4396 29.892L22.4593 34.7204L19.0005 34.7203L19 19ZM25.9625 26.6354C26.6701 26.6828 27.3702 26.4668 27.9281 26.0289C28.1546 25.8268 28.3335 25.5769 28.4519 25.2973C28.5703 25.0177 28.6252 24.7153 28.6126 24.4119V24.3673C28.6348 24.0496 28.5812 23.7312 28.4561 23.4383C28.3311 23.1455 28.1382 22.8865 27.8934 22.6829C27.3089 22.2772 26.6052 22.0796 25.895 22.1216L22.4589 22.1215L22.459 26.6353L25.9625 26.6354Z"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/resharper-cpp/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">ReSharper C++</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__141" x1="5.126" x2="26.323" y1="17.302" y2="70.918" gradientUnits="userSpaceOnUse"><stop offset="0.22" stop-color="#DD1265"></stop><stop offset="0.736" stop-color="#FF45ED"></stop><stop offset="1" stop-color="#FDB60D"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__140" x1="52.282" x2="0.445" y1="73.292" y2="18.152" gradientUnits="userSpaceOnUse"><stop offset="0.113" stop-color="#FDB60D"></stop><stop offset="0.509" stop-color="#FF45ED"></stop><stop offset="0.765" stop-color="#FF45ED"></stop><stop offset="1" stop-color="#FDB60D"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__139" x1="25.5" x2="69.96" y1="-1.93" y2="51.168" gradientUnits="userSpaceOnUse"><stop offset="0.175" stop-color="#FDB60D"></stop><stop offset="0.49" stop-color="#FF45ED"></stop><stop offset="0.819" stop-color="#DD1265"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__141)" d="M18.894 15.6855L16.8323 52.3261L11.5517 70L0 23.0667L18.894 15.6855Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__140)" d="M18.8942 15.6854L21.0145 0L49.2185 69.9999H11.5519L16.8325 52.326L18.8942 15.6854Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__139)" d="M35.2592 47.0706H70L58.3871 0H21.0142L35.2592 47.0706Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z"></path><path fill="#FFF" d="M19 19L26.2892 19.0002C28.309 19.0003 29.8581 19.5391 30.9364 20.6168C31.3996 21.0997 31.7597 21.6719 31.9946 22.2985C32.2295 22.925 32.3344 23.5929 32.3029 24.2613V24.3073C32.3532 25.4356 32.0198 26.5476 31.3572 27.4622C30.7195 28.2803 29.8626 28.9003 28.8862 29.2503L32.7818 34.9446L28.6816 34.9445L25.3814 30.0472L22.4886 30.0472L22.5085 34.9443L19.0005 34.9442L19 19ZM26.0616 26.7442C26.7793 26.7923 27.4894 26.5732 28.0552 26.1291C28.285 25.924 28.4665 25.6706 28.5865 25.387C28.7066 25.1034 28.7622 24.7967 28.7495 24.489V24.4437C28.772 24.1215 28.7177 23.7986 28.5908 23.5016C28.464 23.2045 28.2683 22.9419 28.02 22.7354C27.4272 22.3239 26.7135 22.1234 25.9932 22.1661L22.5081 22.166L22.5083 26.7441L26.0616 26.7442Z"></path><path fill="#FFF" d="M43.872 24.2626H40.2574V21.0512H43.872V17.46H47.1766V21.0512H50.7912V24.2626H47.1766V27.8539H43.872V24.2626Z"></path><path fill="#FFF" d="M36.9551 32.9623H33.3406V29.7509H36.9551V26.1597H40.2598V29.7509H43.8743V32.9623H40.2598V36.5536H36.9551V32.9623Z"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/dotcover/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">dotCover</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__143" x1="37.049" x2="23.558" y1="55.637" y2="5.422" gradientUnits="userSpaceOnUse"><stop offset="0.048" stop-color="#6B57FF"></stop><stop offset="0.12" stop-color="#7556FE"></stop><stop offset="0.241" stop-color="#8F53FB"></stop><stop offset="0.395" stop-color="#BA4DF5"></stop><stop offset="0.576" stop-color="#F446EE"></stop><stop offset="0.608" stop-color="#FF45ED"></stop><stop offset="0.69" stop-color="#FF3BBE"></stop><stop offset="0.771" stop-color="#FF318C"></stop><stop offset="0.995" stop-color="#FC801D"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__142" x1="67.819" x2="41.488" y1="48.799" y2="40.13" gradientUnits="userSpaceOnUse"><stop offset="0.027" stop-color="#6B57FF"></stop><stop offset="0.388" stop-color="#FF45ED"></stop><stop offset="0.487" stop-color="#FF4DD1"></stop><stop offset="0.702" stop-color="#FE6189"></stop><stop offset="1" stop-color="#FC801D"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__143)" d="M42.7984 0L0.00328125 4.81631L0 26.8279L10.7335 62.553L64.552 48.9134L42.7984 0Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__142)" d="M65.9427 22.2088L49.0842 14.1337L25.4188 56.7263L31.8489 65.4527L48.2409 70L64.0216 60.0453L70 41.3105L65.9427 22.2088Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.65H18.6666V51.3333H34.4166V48.65Z"></path><path fill="#FFF" d="M19 19H25.1485C30.1034 19 33.5267 22.4009 33.5267 26.8377V26.8828C33.5267 31.3196 30.1034 34.7655 25.1485 34.7655H19V19ZM22.4684 22.1307V31.635H25.1486C27.9864 31.635 29.9007 29.7205 29.9007 26.9279V26.8828C29.9329 26.2503 29.832 25.618 29.6046 25.0269C29.3772 24.4357 29.0283 23.8989 28.5804 23.451C28.1325 23.0032 27.5957 22.6542 27.0045 22.4268C26.4134 22.1994 25.7811 22.0985 25.1486 22.1307H22.4684Z"></path><path fill="#FFF" d="M35.1846 27.0028V26.9575C35.1652 25.8703 35.3662 24.7903 35.7755 23.7828C36.1848 22.7753 36.7938 21.8611 37.566 21.0953C38.3381 20.3296 39.2573 19.7281 40.2682 19.3273C41.2791 18.9264 42.3607 18.7343 43.4478 18.7628C46.4355 18.7628 48.2242 19.7587 49.6954 21.2073L47.4767 23.7656C46.2544 22.6565 45.0096 21.9774 43.4246 21.9774C40.7537 21.9774 38.8293 24.1962 38.8293 26.9123V26.9576C38.8293 29.6743 40.7079 31.9377 43.4246 31.9377C45.2359 31.9377 46.345 31.2134 47.5899 30.0817L49.8086 32.3231C49.0108 33.2562 48.0114 33.9958 46.8858 34.4861C45.7603 34.9763 44.538 35.2043 43.3114 35.1529C42.2374 35.1703 41.1709 34.9712 40.1755 34.5674C39.1802 34.1637 38.2763 33.5636 37.5178 32.803C36.7594 32.0424 36.1619 31.1368 35.761 30.1403C35.3602 29.1438 35.1641 28.0767 35.1846 27.0028"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/dotmemory/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">dotMemory</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__146" x1="18.757" x2="30.724" y1="19.283" y2="69.379" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6B57FF"></stop><stop offset="0.13" stop-color="#9A51F9"></stop><stop offset="0.268" stop-color="#C64CF4"></stop><stop offset="0.392" stop-color="#E548F0"></stop><stop offset="0.497" stop-color="#F846EE"></stop><stop offset="0.57" stop-color="#FF45ED"></stop><stop offset="0.633" stop-color="#FF57C9"></stop><stop offset="0.814" stop-color="#FE8A65"></stop><stop offset="0.941" stop-color="#FDAA26"></stop><stop offset="1" stop-color="#FDB60D"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__145" x1="51.758" x2="39.877" y1="35.768" y2="1.731" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6B57FF"></stop><stop offset="0.138" stop-color="#8953FB"></stop><stop offset="0.437" stop-color="#D64AF2"></stop><stop offset="0.588" stop-color="#FF45ED"></stop><stop offset="0.968" stop-color="#FDB60D"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__144" x1="26.353" x2="36.21" y1="53.604" y2="30.222" gradientUnits="userSpaceOnUse"><stop offset="0.118" stop-color="#FF45ED"></stop><stop offset="0.197" stop-color="#DF49F1"></stop><stop offset="0.304" stop-color="#BC4DF5"></stop><stop offset="0.416" stop-color="#9E51F9"></stop><stop offset="0.535" stop-color="#8854FC"></stop><stop offset="0.663" stop-color="#7855FD"></stop><stop offset="0.807" stop-color="#6E57FF"></stop><stop offset="1" stop-color="#6B57FF"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__146)" d="M7.97508 65.1476L0 37.6507L49.5529 51.3095L44.2657 70L7.97508 65.1476Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__145)" d="M23.4774 0.0896876L42.1193 5.42172L63.1729 0L67.3493 28.8778L19.955 13.125L23.4774 0.0896876Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__144)" d="M70 46.1135L67.3493 28.8776L24.4705 14.6255L0.0896875 19.8585L0 37.6506L49.5529 51.3093L70 46.1135Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.65H18.6666V51.3333H34.4166V48.65Z"></path><path fill="#FFF" d="M19 19H25.1307C30.0712 19 33.4846 22.3911 33.4846 26.8149V26.86C33.4846 31.2839 30.0712 34.7198 25.1307 34.7198H19V19ZM22.4584 22.1216V31.5984H25.1307C27.9603 31.5984 29.8691 29.6894 29.8691 26.9049V26.86C29.9012 26.2293 29.8006 25.5988 29.5739 25.0094C29.3471 24.42 28.9992 23.8847 28.5526 23.4381C28.1061 22.9916 27.5708 22.6437 26.9813 22.4169C26.3919 22.1901 25.7615 22.0895 25.1307 22.1216H22.4584Z"></path><path fill="#FFF" d="M34.6927 19.0094L38.4209 19.0099L42.5551 25.6573L46.6861 19.0099L50.4138 19.0104L50.4133 34.73H46.9765L46.977 24.4688L42.5545 31.183H42.4621L38.085 24.5352L38.084 34.7295H34.6921L34.6927 19.0094Z"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/decompiler/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">dotPeek</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__150" x1="7.045" x2="40.658" y1="35.829" y2="70.142" gradientUnits="userSpaceOnUse"><stop offset="0.097" stop-color="#FF45ED"></stop><stop offset="0.113" stop-color="#F846EE"></stop><stop offset="0.284" stop-color="#AC4FF7"></stop><stop offset="0.406" stop-color="#7D55FD"></stop><stop offset="0.466" stop-color="#6B57FF"></stop><stop offset="0.48" stop-color="#655DFE"></stop><stop offset="0.572" stop-color="#4482FA"></stop><stop offset="0.664" stop-color="#299EF6"></stop><stop offset="0.756" stop-color="#16B3F4"></stop><stop offset="0.847" stop-color="#0BBFF2"></stop><stop offset="0.935" stop-color="#07C3F2"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__149" x1="9.563" x2="34.109" y1="55.827" y2="35.372" gradientUnits="userSpaceOnUse"><stop offset="0.043" stop-color="#FF45ED"></stop><stop offset="0.046" stop-color="#FE45ED"></stop><stop offset="0.201" stop-color="#D14BF3"></stop><stop offset="0.357" stop-color="#AC4FF7"></stop><stop offset="0.512" stop-color="#9053FB"></stop><stop offset="0.666" stop-color="#7B55FD"></stop><stop offset="0.818" stop-color="#6F57FF"></stop><stop offset="0.968" stop-color="#6B57FF"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__148" x1="39.855" x2="56.355" y1="16.927" y2="50.653" gradientUnits="userSpaceOnUse"><stop offset="0.199" stop-color="#FF45ED"></stop><stop offset="0.286" stop-color="#F646EE"></stop><stop offset="0.429" stop-color="#DD49F1"></stop><stop offset="0.609" stop-color="#B64EF6"></stop><stop offset="0.818" stop-color="#7F55FD"></stop><stop offset="0.887" stop-color="#6B57FF"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__147" x1="19.875" x2="61.328" y1="18.305" y2="8.256" gradientUnits="userSpaceOnUse"><stop offset="0.097" stop-color="#FF45ED"></stop><stop offset="0.17" stop-color="#F64AED"></stop><stop offset="0.29" stop-color="#DD56EE"></stop><stop offset="0.441" stop-color="#B56AEE"></stop><stop offset="0.618" stop-color="#7E87F0"></stop><stop offset="0.814" stop-color="#38AAF1"></stop><stop offset="0.941" stop-color="#07C3F2"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__150)" d="M47.6963 50.342L0 40.8083L14.0848 70L49.2718 63.8662L47.6963 50.342Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__149)" d="M70 31.3298L50.6805 11.4088L0.00328125 22.0914L0 40.8082L62.6101 53.3229L70 31.3298Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__148)" d="M69.9999 31.3299L39.6167 0L15.8063 7.20945L23.6036 30.9208L62.61 53.323L69.9999 31.3299Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__147)" d="M64.5356 19.5754L61.7804 0H51.3373H39.6167L15.8063 7.20945L23.6036 30.9208L64.5356 19.5754Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.65H18.6666V51.3333H34.4166V48.65Z"></path><path fill="#FFF" d="M19 19H25.1321C30.0736 19 33.4878 22.3918 33.4878 26.8167V26.8617C33.4878 31.2866 30.0736 34.7233 25.1321 34.7233H19V19ZM22.4592 22.1223V31.6011H25.1321C27.9623 31.6011 29.8715 29.6918 29.8715 26.9066V26.8617C29.9036 26.2309 29.803 25.6003 29.5762 25.0107C29.3494 24.4212 29.0014 23.8858 28.5547 23.4391C28.1081 22.9924 27.5727 22.6445 26.9831 22.4176C26.3935 22.1908 25.763 22.0902 25.1321 22.1223H22.4592Z"></path><path fill="#FFF" d="M36.0267 19H42.4699C46.2312 19 48.5066 21.2303 48.5066 24.4511V24.4961C48.5066 28.1454 45.6681 30.0379 42.1315 30.0379H39.4958V34.7682H36.0267V19ZM42.2441 26.9517C43.9789 26.9517 44.9924 25.9157 44.9924 24.5637V24.5187C44.9924 22.9646 43.9114 22.1312 42.1765 22.1312H39.4958V26.9517H42.2441Z"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/profiler/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq _mainSubmenuItem__linkWithLogo_adk6a" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5 _mainSubmenuItem__titleWithLogo_91fk6">dotTrace</span><svg fill="none" viewBox="0 0 70 70" class="_productLogo_uqxhs _mainSubmenuItem__logo_pt7wt _mainSubmenuItem__logo_2t0w _mainSubmenuItem__logo_mxmgi _mainSubmenuItem__logo_hqkim" data-test="main-submenu-item-image"><defs><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__152" x1="-1.332" x2="67.042" y1="43.737" y2="26.097" gradientUnits="userSpaceOnUse"><stop offset="0.123" stop-color="#6B57FF"></stop><stop offset="0.538" stop-color="#FF45ED"></stop><stop offset="0.854" stop-color="#DD1265"></stop></linearGradient><linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__151" x1="45.915" x2="67.658" y1="38.91" y2="9.099" gradientUnits="userSpaceOnUse"><stop offset="0.192" stop-color="#DD1265"></stop><stop offset="0.295" stop-color="#DE146A"></stop><stop offset="0.411" stop-color="#E21977"></stop><stop offset="0.533" stop-color="#E7218E"></stop><stop offset="0.659" stop-color="#EF2DAD"></stop><stop offset="0.788" stop-color="#F93CD5"></stop><stop offset="0.853" stop-color="#FF45ED"></stop></linearGradient></defs><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__152)" d="M67.3065 16.0267L43.7466 0L0 31.0707L11.0851 70L58.9005 60.3039L67.3065 16.0267Z"></path><path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__151)" d="M67.3066 16.0267L43.7468 0L37.9504 15.7199V47.7701H70L67.3066 16.0267Z"></path><path fill="#000" d="M56 14H14V56H56V14Z"></path><path fill="#FFF" d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z"></path><path fill="#FFF" d="M19 19.0016H25.1337C30.0767 19.0016 33.4917 22.3943 33.4917 26.8204V26.8654C33.4917 31.2915 30.0767 34.7291 25.1337 34.7291H19V19.0016ZM22.4601 22.1248V31.6061H25.1338C27.9647 31.6061 29.8745 29.6962 29.8745 26.9103V26.8654C29.9066 26.2344 29.8059 25.6037 29.5791 25.0139C29.3522 24.4242 29.0041 23.8887 28.5573 23.4419C28.1105 22.9951 27.575 22.647 26.9853 22.4201C26.3956 22.1933 25.7648 22.0926 25.1338 22.1248H22.4601Z"></path><path fill="#FFF" d="M39.9826 22.1738H35.1921V18.98L48.2367 18.9805V22.1738H43.4461V34.7235H39.9821L39.9826 22.1738Z"></path></svg></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://plugins.jetbrains.com/search?isFeaturedSearch=true&amp;products=resharper&amp;products=rider" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">.NET Tools Plugins</span></span></a></div></div></div><div class="_mobileMainSubmenu__column_osm81 wt-offset-top-24 wt-offset-top-sm-48"><h5 class="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title">LANGUAGES &amp; FRAMEWORKS</h5><div class="wt-offset-top-12"><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://kotlinlang.org/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Kotlin</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="https://ktor.io/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Ktor</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/mps/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">MPS</span></span></a></div><div class="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item"><a href="/lp/compose-multiplatform/" class="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link"><span class="_mainSubmenuItem__titlePart_cflex"><span class="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5">Compose Multiplatform</span></span></a></div></div></div></div><div data-test="main-submenu-suggestions"><div class="_mainSubmenuSuggestion_ihmj1 _mainSubmenuSuggestionAdaptive_2gp4l" data-test="main-submenu-suggestion"><div class="wt-row wt-row_align-items_center wt-row_size_m wt-row-sm_wrap"><div class="wt-col-auto-fill wt-col-sm-12"><h5 class="rs-text-2 rs-text-2_hardness_hard rs-text-2_theme_light" data-test="suggestion-title">Not sure which tool is best for you?</h5><p class="rs-text-2 rs-text-2_theme_light" data-test="suggestion-description">Whichever technologies you use, there's a JetBrains tool to match < /p > < /div > < div class ="wt-col-inline wt-offset-top-sm-12" > < a data-test="suggestion-action" href="/products/" type="button" class ="_main_1dh718a_17 _modeRock_1dh718a_241 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _light_1dh718a_59" > Find your tool < /a > < /div > < /div > < a href="/products/" class ="_mainSubmenuSuggestion__link_knoa4 _mainSubmenuSuggestion__link_9ek20g" aria-label="Find your tool" data-test="suggestion-link" > < /a > < /div > < /div > < div class ="main-submenu-banners _mainSubmenuBanners_332p1 _mainSubmenuBanners_j4vgp _mainSubmenuBannersAdaptive_aj1vpj _mainSubmenuBannersAdaptive_ei08o" data-test="main-submenu-banners" > < div class ="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner" > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(117.63deg, rgb(8, 89, 255) -0.78%, rgb(0, 154, 231) 55.03%, rgb(221, 255, 84) 111.19%); background-color: rgb(22, 125, 255);" > < /div > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(117.63deg, rgb(8, 89, 255) -0.78%, rgb(0, 154, 231) 55.03%, rgb(221, 255, 84) 111.19%); background-color: rgb(22, 125, 255);" > < /div > < div class ="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl" > < svg viewBox="0 0 60 60" class ="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c" data-test="banner-logo-image" > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__155" gradientTransform="matrix(1 0 0 -1 0 62)" gradientUnits="userSpaceOnUse" x1="27.048" x2="33.312" y1="62.824" y2="3.448" > < stop offset="0" stop-color="#fcf84a" > < /stop > < stop offset="0.32" stop-color="#abe682" > < /stop > < stop offset="0.79" stop-color="#36cdd2" > < /stop > < stop offset="1" stop-color="#07c3f2" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__154" gradientTransform="matrix(1 0 0 -1 0 62)" gradientUnits="userSpaceOnUse" x1="4.068" x2="60.246" y1="61.892" y2="35.243" > < stop offset="0" stop-color="#3bea62" > < /stop > < stop offset="1" stop-color="#087cfa" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__153" gradientTransform="matrix(1 0 0 -1 0 62)" gradientUnits="userSpaceOnUse" x1="9.217" x2="65.779" y1="3.879" y2="43.473" > < stop offset="0" stop-color="#009ae5" > < /stop > < stop offset="0.18" stop-color="#0490dd" > < /stop > < stop offset="0.49" stop-color="#1073c6" > < /stop > < stop offset="0.89" stop-color="#2346a1" > < /stop > < stop offset="1" stop-color="#293896" > < /stop > < /linearGradient > < g fill-rule="evenodd" > < path d="m10.8618 60a59.95462 59.95462 0 0 0 49.1382-34.4 60.00348 60.00348 0 0 0 -49.1382-25.6c-1.74408 0-3.49616.072-5.24824.232a59.99772 59.99772 0 0 0 5.24824 59.768z" fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__155)" > < /path > < path d="m5.66956.232a70.65854 70.65854 0 0 1 31.56944 25.368h22.761a59.81147 59.81147 0 0 0 -49.0742-25.6q-2.61612 0-5.25624.232z" fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__154)" > < /path > < path d="m37.247 25.6c-2.74414 18.104-26.3852 34.4-26.3852 34.4 21.48896-2.04 40.33781-14.92 49.1382-34.4z" fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__153)" > < /path > < /g > < /svg > < div class ="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12" > < div class ="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p" > < h3 class ="rs-h3 rs-h3_theme_dark" data-test="banner-title" > Space < /h3 > < p class ="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description" > A complete software development platform < /p > < /div > < a data-test="banner-action" aria-label="Explore Space" href="/space/" type="button" class ="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569" > < path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z" > < /path > < /svg > < /a > < /div > < /div > < a href="/space/" class ="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Explore Space" data-test="banner-link" > < /a > < /div > < div class ="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner" > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(130.93deg, rgb(105, 2, 154) 0%, rgb(135, 1, 199) 32.33%, rgb(107, 87, 255) 97.76%); background-color: rgb(135, 1, 199);" > < /div > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(130.93deg, rgb(105, 2, 154) 0%, rgb(135, 1, 199) 32.33%, rgb(107, 87, 255) 97.76%); background-color: rgb(135, 1, 199);" > < /div > < div class ="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl" > < div class ="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c _productLogo_img_5cqf5" data-test="banner-logo-image" style="background-image: url(&quot;/img/banners-menu-main/fleet.png&quot;);" > < /div > < div class ="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12" > < div class ="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p" > < h3 class ="rs-h3 rs-h3_theme_dark" data-test="banner-title" > Fleet < /h3 > < p class ="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description" > Next-generation IDE by JetBrains < /p > < /div > < a data-test="banner-action" aria-label="Learn more" href="/fleet/" type="button" class ="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569" > < path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z" > < /path > < /svg > < /a > < /div > < /div > < a href="/fleet/" class ="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Learn more" data-test="banner-link" > < /a > < /div > < /div > < /div > < /div > < div class ="wt-col-inline" data-test="mobile-main-menu-item" data-test-marker="Team Tools" > < button class ="_mobileMainMenuItem__action_5guvc _mobileMainMenuItem__action_aia9hh _mobileMainMenuItem__action_zczl4 _mobileMainMenuItem__action_jh6aw _mobileMainMenuItem__action_lfuz6" type="button" aria-label="Team Tools: Open submenu" data-test="mobile-main-menu-item-action" > Team Tools < /button > < div class ="_mobileMainSubmenu_5p4gw _mobileMainMenuItem__submenu_v3gfo wt-display-none" data-test="mobile-main-submenu" > < div class ="_mobileMainSubmenu__columnsWrapper_5r3czi" > < div class ="_mobileMainSubmenu__column_osm81 _mobileMainSubmenu__column--full-size_niturg wt-offset-top-24 wt-offset-top-sm-48" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title" > IN-CLOUD AND ON-PREMISES SOLUTIONS < /h5 > < div class ="wt-offset-top-12" > < div class ="_mobileMainSubmenuSubColumns__columnsWrapper_zt0m2" > < div class ="_mobileMainSubmenuSubColumns__column_gnsze" > < div class ="" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/datalore/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Datalore < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > A collaborative data science platform < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/space/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Space < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > A complete software development platform < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/teamcity/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > TeamCity < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Powerful Continuous Integration out of the box < /span > < /a > < /div > < /div > < /div > < div class ="_mobileMainSubmenuSubColumns__column_gnsze" > < div class ="" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/youtrack/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > YouTrack < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Powerful project management for all your teams < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/qodana/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Qodana < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > The code quality platform for your favorite CI < /span > < /a > < /div > < /div > < /div > < /div > < /div > < /div > < div class ="_mobileMainSubmenu__column_osm81 _mobileMainSubmenu__column--full-size_niturg wt-offset-top-24 wt-offset-top-sm-48" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title" > EXTENSIONS < /h5 > < div class ="wt-offset-top-12" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://plugins.jetbrains.com/teamcity/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > TeamCity Plugins < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://plugins.jetbrains.com/youtrack/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > YouTrack Extensions < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/hub/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > JetBrains Hub < /span > < /span > < /a > < /div > < /div > < /div > < /div > < div class ="main-submenu-banners _mainSubmenuBanners_332p1 _mainSubmenuBanners_j4vgp _mainSubmenuBannersAdaptive_aj1vpj _mainSubmenuBannersAdaptive_ei08o" data-test="main-submenu-banners" > < div class ="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner" > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(120.81deg, rgb(0, 51, 150) 11.31%, rgb(0, 156, 244) 95.37%); background-color: rgb(0, 92, 209);" > < /div > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(120.81deg, rgb(0, 51, 150) 11.31%, rgb(0, 156, 244) 95.37%); background-color: rgb(0, 92, 209);" > < /div > < div class ="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl" > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c" data-test="banner-logo-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__159" x1="21.41" x2="63.882" y1="17.36" y2="25.844" gradientUnits="userSpaceOnUse" > < stop offset="0.242" stop-color="#3BEA62" > < /stop > < stop offset="0.857" stop-color="#FCF84A" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__158" x1="16.862" x2="57.518" y1="4.912" y2="66.891" gradientUnits="userSpaceOnUse" > < stop offset="0.018" stop-color="#3BEA62" > < /stop > < stop offset="0.786" stop-color="#087CFA" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__157" x1="16.295" x2="67.926" y1="39.35" y2="58.041" gradientUnits="userSpaceOnUse" > < stop offset="0.121" stop-color="#1FAEB5" > < /stop > < stop offset="0.975" stop-color="#087CFA" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__156" x1="1.435" x2="68.11" y1="42.252" y2="12.633" gradientUnits="userSpaceOnUse" > < stop offset="0.121" stop-color="#1FAEB5" > < /stop > < stop offset="0.856" stop-color="#FCF84A" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__159)" d="M64.9765 8.29965C64.1745 7.86318 63.0808 7.49945 62.2058 7.35395C61.6225 7.35395 24.3642 0.224872 22.3956 0.0793808C21.4477 0.00663505 20.4269 0.0793808 19.4791 0.224872C2.19877 2.77097 -2.17598 23.7945 12.1149 32.5967C15.4689 34.6336 19.4791 35.3611 23.3434 34.4881C30.1243 33.0332 60.6018 25.5404 62.5704 25.1039C71.0283 23.2853 72.8511 12.4462 64.9765 8.29965Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__158)" d="M65.3411 40.6714C63.8829 38.9982 37.4885 9.09972 31.8742 4.22575C30.7805 3.28006 29.4681 2.40711 28.0099 1.60691C25.385 0.224739 22.3956 -0.284481 19.4791 0.151993C3.8758 2.5526 -1.22808 19.9388 8.46929 29.7595C9.49007 30.8507 38.5093 63.0043 38.8009 63.368C40.1134 64.9684 41.7174 66.4961 43.759 67.7328C47.113 69.8424 51.1961 70.4971 55.1333 69.6242C69.4242 66.4234 74.0177 50.3465 65.3411 40.6714Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__157)" d="M59.7998 36.4521C59.2165 36.1611 58.6332 35.8701 57.977 35.6519C57.4666 35.5064 18.2396 23.1396 17.3647 22.9214C15.9064 22.5576 14.3752 22.4849 12.917 22.7031C-1.08223 24.74 -4.65495 41.8353 6.93815 49.0371C9.63592 50.7103 45.436 68.6057 46.3839 68.9694C49.1545 69.9879 52.144 70.2061 55.0605 69.5514C71.8304 65.9141 75.2572 44.5269 59.7998 36.4521Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__156)" d="M64.9766 8.29953C63.6642 7.57207 62.133 7.35383 60.6018 7.57207C59.7998 7.71756 59.0707 7.86305 58.3416 8.15404C54.9147 9.5362 10.0005 23.2852 8.76099 23.8671C-1.66551 28.3774 -3.3425 42.6355 6.93817 49.0372C9.63594 50.7103 12.917 51.2923 16.1252 50.5648C17.3647 50.2738 18.6042 49.9101 19.625 49.4009C25.1663 46.782 64.612 24.5218 65.4141 24.0854C71.32 20.6663 71.8304 11.9368 64.9766 8.29953Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4167 48.65H18.6667V51.3334H34.4167V48.65Z" > < /path > < g fill="#FFF" > < path d="M36.0001 19.13H39.458V31.8553H46.3048V34.76H36.0001V19.13Z" > < /path > < path d="M18.67 19.13H24.7561C29.6664 19.13 33.0552 22.5188 33.0552 26.8758V26.945C33.0552 31.3712 29.6664 34.76 24.7561 34.76H18.67V19.13ZM22.128 22.2422V31.6478H24.7561C27.5916 31.6478 29.4589 29.7805 29.4589 27.0142V26.945C29.4589 24.1786 27.5916 22.2422 24.7561 22.2422H22.128V22.2422Z" > < /path > < /g > < /svg > < div class ="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12" > < div class ="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p" > < h3 class ="rs-h3 rs-h3_theme_dark" data-test="banner-title" > Datalore < /h3 > < p class ="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description" > A collaborative data science platform.Available online and on-premises < /p > < /div > < a data-test="banner-action" aria-label="Learn more" href="/datalore/" type="button" class ="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569" > < path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z" > < /path > < /svg > < /a > < /div > < /div > < a href="/datalore/" class ="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Learn more" data-test="banner-link" > < /a > < /div > < div class ="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner" > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(141.09deg, rgb(216, 6, 99) -21.81%, rgb(131, 76, 239) 33.98%, rgb(0, 181, 226) 100.21%); background-color: rgb(107, 87, 255);" > < /div > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(141.09deg, rgb(216, 6, 99) -21.81%, rgb(131, 76, 239) 33.98%, rgb(0, 181, 226) 100.21%); background-color: rgb(107, 87, 255);" > < /div > < div class ="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl" > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c" data-test="banner-logo-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__162" x1="7.088" x2="64.122" y1="54.736" y2="28.739" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#905CFB" > < /stop > < stop offset="0.165" stop-color="#6677F8" > < /stop > < stop offset="0.378" stop-color="#3596F5" > < /stop > < stop offset="0.54" stop-color="#17A9F3" > < /stop > < stop offset="0.632" stop-color="#0CB0F2" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__161" x1="30.319" x2="1.071" y1="28.108" y2="2.276" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#905CFB" > < /stop > < stop offset="0.072" stop-color="#A554E6" > < /stop > < stop offset="0.252" stop-color="#D641B5" > < /stop > < stop offset="0.39" stop-color="#F43597" > < /stop > < stop offset="0.468" stop-color="#FF318C" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__160" x1="4.988" x2="74.041" y1="58.67" y2="15.161" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#905CFB" > < /stop > < stop offset="0.165" stop-color="#6677F8" > < /stop > < stop offset="0.378" stop-color="#3596F5" > < /stop > < stop offset="0.54" stop-color="#17A9F3" > < /stop > < stop offset="0.632" stop-color="#0CB0F2" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__162)" d="M66.916 47.482C66.716 47.282 53.8136 34.8792 53.8136 34.8792C53.8136 34.8792 63.6154 24.4769 66.2159 21.8763C66.7408 21.3513 67.6261 20.2758 68.2162 19.2757C71.8169 13.1743 69.7165 5.3726 63.6154 1.7718C59.1146 -0.828787 53.5136 -0.428697 49.5128 2.57197C48.8127 3.07209 48.2126 3.5722 47.6125 4.17233C47.3124 4.57242 33.71 16.9752 21.9078 27.7776L44.0118 41.7807L20.8076 67.8866C19.4074 68.8868 18.0071 69.487 16.5068 69.787C16.8069 69.787 17.7071 69.8869 18.0072 69.7868C22.608 69.0867 61.215 62.3854 63.1153 61.9853C65.4157 61.5852 67.5161 60.1849 68.8163 58.0844C71.0167 54.4836 70.0166 49.9826 66.916 47.482Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__161)" d="M45.9121 30.4781C45.512 27.7775 44.1118 25.577 42.1114 23.9767C40.011 22.3763 23.8081 5.57256 22.0078 3.67213C19.2073 0.971525 15.2065 -0.528811 11.1058 0.171346C4.10453 1.17157 -0.796361 7.77305 0.303839 14.7746C0.80393 18.2754 2.80429 21.2761 5.40476 23.1765C8.00524 25.1769 28.4089 39.1801 29.7092 40.1803C31.8096 41.7807 34.6101 42.6809 37.4106 42.1808C42.9116 41.1805 46.8123 35.9794 45.9121 30.4781Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__160)" d="M23.0079 67.7866C23.108 67.7866 46.3122 41.6808 46.3122 41.6808L22.9079 26.8774C14.6064 34.4791 6.90502 41.3807 5.10469 43.0811C4.00449 44.0813 2.90429 45.3816 2.10415 46.7819C-2.19664 54.1836 0.303819 63.5857 7.70516 67.8866C10.7057 69.587 17.5069 71.6875 23.0079 67.7866Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < path fill="#FFF" d="M34.4167 48.6499H18.6667V51.3332H34.4167V48.6499Z" > < /path > < path fill="#FFF" d="M24.7737 34.73H28.2342V28.4607L34.2795 19H30.3463L26.5265 25.3144L22.7736 19H18.73L24.7737 28.5276L24.7737 34.73ZM36.4142 19.0006V22.1905H41.1998V34.729H44.6603V22.1905H49.4458V19.0006H36.4142Z" > < /path > < /svg > < div class ="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12" > < div class ="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p" > < h3 class ="rs-h3 rs-h3_theme_dark" data-test="banner-title" > YouTrack < /h3 > < p class ="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description" > Powerful project management for all your teams < /p > < /div > < a data-test="banner-action" aria-label="Learn more" href="/youtrack/" type="button" class ="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569" > < path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z" > < /path > < /svg > < /a > < /div > < /div > < a href="/youtrack/" class ="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Learn more" data-test="banner-link" > < /a > < /div > < /div > < /div > < /div > < div class ="wt-col-inline" data-test="mobile-main-menu-item" data-test-marker="Education" > < button class ="_mobileMainMenuItem__action_5guvc _mobileMainMenuItem__action_aia9hh _mobileMainMenuItem__action_zczl4 _mobileMainMenuItem__action_jh6aw _mobileMainMenuItem__action_lfuz6" type="button" aria-label="Education: Open submenu" data-test="mobile-main-menu-item-action" > Education < /button > < div class ="_mobileMainSubmenu_5p4gw _mobileMainMenuItem__submenu_v3gfo wt-display-none" data-test="mobile-main-submenu" > < div class ="_mobileMainSubmenu__columnsWrapper_5r3czi" > < div class ="_mobileMainSubmenu__column_osm81 _mobileMainSubmenu__column--full-size_niturg wt-offset-top-24 wt-offset-top-sm-48" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title" > FOR LEARNERS < /h5 > < div class ="wt-offset-top-12" > < div class ="_mobileMainSubmenuSubColumns__columnsWrapper_zt0m2" > < div class ="_mobileMainSubmenuSubColumns__column_gnsze" > < div class ="" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/academy/#learn" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Programming languages < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Select a language and try different approaches to learning it < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/academy/#careers" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Career fields < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Explore careers and see where programming could take you < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/education/university-relations/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > University relations < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Study offline with academic programs < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/careers/internships/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Internships < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Apply for internships and flexible jobs for students < br > < /span > < /a > < /div > < /div > < /div > < /div > < /div > < /div > < div class ="_mobileMainSubmenu__column_osm81 _mobileMainSubmenu__column--full-size_niturg wt-offset-top-24 wt-offset-top-sm-48" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title" > FOR EDUCATORS < /h5 > < div class ="wt-offset-top-12" > < div class ="_mobileMainSubmenuSubColumns__columnsWrapper_zt0m2" > < div class ="_mobileMainSubmenuSubColumns__column_gnsze" > < div class ="" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/pages/academy/teaching/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Teaching with JetBrains IDEs < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Create courses and share your knowledge < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="https://kotlinlang.org/education/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Kotlin for education < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Teach a wide range of Kotlin courses < /span > < /a > < /div > < /div > < /div > < div class ="_mobileMainSubmenuSubColumns__column_gnsze" > < h5 class ="rs-h5 rs-h5_theme_light wt-offset-top-24 wt-offset-top-sm-48" data-test="mobile-main-menu-sub-column-title" > FOR TEAMS < /h5 > < div class ="wt-offset-top-12" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="https://lp.jetbrains.com/academy/for-organizations" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Professional development < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Ensure your team has up-to-date technical skills < /span > < /a > < /div > < /div > < /div > < /div > < /div > < /div > < div class ="_mobileMainSubmenu__column_osm81 _mobileMainSubmenu__column--full-size_niturg wt-offset-top-24 wt-offset-top-sm-48" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title" > FREE LICENSES < /h5 > < div class ="wt-offset-top-12" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/community/education/#students/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > For students and teachers < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > JetBrains IDEs for individual academic use < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/community/education/#classrooms" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > For educational institutions < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > JetBrains IDEs and team tools for classroom use < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/community/education/#courses" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > For bootcamps and courses < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > JetBrains IDEs for your students < /span > < /a > < /div > < /div > < /div > < /div > < div class ="main-submenu-banners _mainSubmenuBanners_332p1 _mainSubmenuBanners_j4vgp _mainSubmenuBannersAdaptive_aj1vpj _mainSubmenuBannersAdaptive_ei08o" data-test="main-submenu-banners" > < div class ="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner" > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(335.07deg, rgb(99, 108, 234) 0%, rgb(131, 76, 239) 40.63%, rgb(119, 31, 137) 100%); background-color: rgb(176, 29, 246);" > < /div > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(335.07deg, rgb(99, 108, 234) 0%, rgb(131, 76, 239) 40.63%, rgb(119, 31, 137) 100%); background-color: rgb(176, 29, 246);" > < /div > < div class ="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl" > < div class ="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c _productLogo_img_5cqf5" data-test="banner-logo-image" style="background-image: url(&quot;/img/banners-menu-main/academy-logo.svg&quot;);" > < /div > < div class ="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12" > < div class ="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p" > < h3 class ="rs-h3 rs-h3_theme_dark" data-test="banner-title" > JetBrains Academy < /h3 > < p class ="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description" > Find your way in learning or teaching computer science < /p > < /div > < a data-test="banner-action" aria-label="Discover more" href="/academy" type="button" class ="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569" > < path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z" > < /path > < /svg > < /a > < /div > < /div > < a href="/academy" class ="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Discover more" data-test="banner-link" > < /a > < /div > < /div > < /div > < /div > < div class ="wt-col-inline" data-test="mobile-main-menu-item" data-test-marker="Solutions" > < button class ="_mobileMainMenuItem__action_5guvc _mobileMainMenuItem__action_aia9hh _mobileMainMenuItem__action_zczl4 _mobileMainMenuItem__action_jh6aw _mobileMainMenuItem__action_lfuz6" type="button" aria-label="Solutions: Open submenu" data-test="mobile-main-menu-item-action" > Solutions < /button > < div class ="_mobileMainSubmenu_5p4gw _mobileMainMenuItem__submenu_v3gfo wt-display-none" data-test="mobile-main-submenu" > < div class ="_mobileMainSubmenu__columnsWrapper_5r3czi" > < div class ="_mobileMainSubmenu__column_osm81 _mobileMainSubmenu__column--full-size_niturg wt-offset-top-24 wt-offset-top-sm-48" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title" > BY INDUSTRY & amp; TECHNOLOGY < /h5 > < div class ="wt-offset-top-12" > < div class ="_mobileMainSubmenuSubColumns__columnsWrapper_zt0m2" > < div class ="_mobileMainSubmenuSubColumns__column_gnsze" > < div class ="" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/remote-development/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Remote Development < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Tools for remote development for you and your team < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/gamedev/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Game Development < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Tools for game development for any platform < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/devops/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > DevOps < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Tools and integrations for any infrastructure < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/quality-assurance-solutions/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Quality Assurance < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Tools for Quality Assurance and Test Automation < /span > < /a > < /div > < /div > < /div > < div class ="_mobileMainSubmenuSubColumns__column_gnsze" > < div class ="" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/cpp/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > C++ Tools < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Tools for C/C++ development for any platform < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/data-tools/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Data Tools < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Tools for Big Data and Data Science < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/space/solutions/software-teams/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Software Development < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > All- in -one solution for software projects and teams < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas _mainSubmenuItemWithDescription_3zbb6" data-test="main-submenu-item" > < a href="/license-vault/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > License Vault < /span > < /span > < span class ="rs-text-2 rs-text-2_hardness_pale rs-text-2_theme_light _mainSubmenuItem__description_jdne7 _mainSubmenuItem__description_0l3ta" data-test="main-submenu-item-description" > Efficient management of JetBrains licenses < /span > < /a > < /div > < /div > < /div > < /div > < /div > < /div > < div class ="_mobileMainSubmenu__column_osm81 _mobileMainSubmenu__column--full-size_niturg wt-offset-top-24 wt-offset-top-sm-48" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title" > RECOMMENDED < /h5 > < div class ="wt-offset-top-12" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/all/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > All Products Pack < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/dotnet/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" >.NET Tools < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/education/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > JetBrains for Education < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/products/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > All JetBrains Products < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://plugins.jetbrains.com/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > JetBrains Marketplace < /span > < /span > < /a > < /div > < /div > < /div > < /div > < div class ="main-submenu-banners _mainSubmenuBanners_332p1 _mainSubmenuBanners_j4vgp _mainSubmenuBannersAdaptive_aj1vpj _mainSubmenuBannersAdaptive_ei08o" data-test="main-submenu-banners" > < div class ="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner" > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(246.1deg, rgb(0, 224, 214) 1.67%, rgb(126, 27, 253) 92.48%); background-color: rgb(107, 87, 255);" > < /div > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(246.1deg, rgb(0, 224, 214) 1.67%, rgb(126, 27, 253) 92.48%); background-color: rgb(107, 87, 255);" > < /div > < div class ="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl" > < div class ="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c _productLogo_img_5cqf5" data-test="banner-logo-image" style="background-image: url(&quot;/img/banners-menu-main/containers.svg&quot;);" > < /div > < div class ="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12" > < div class ="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p" > < h3 class ="rs-h3 rs-h3_theme_dark" data-test="banner-title" > Developer Tools for Your Business < /h3 > < p class ="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description" > Professional tools for productive development < /p > < /div > < a data-test="banner-action" aria-label="Learn more" href="/store/business/" type="button" class ="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569" > < path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z" > < /path > < /svg > < /a > < /div > < /div > < a href="/store/business/" class ="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Learn more" data-test="banner-link" > < /a > < /div > < div class ="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner" > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(240.88deg, rgb(45, 243, 136) 0%, rgb(5, 191, 135) 37.75%, rgb(2, 116, 116) 98.39%); background-color: rgb(45, 243, 136);" > < /div > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(240.88deg, rgb(45, 243, 136) 0%, rgb(5, 191, 135) 37.75%, rgb(2, 116, 116) 98.39%); background-color: rgb(45, 243, 136);" > < /div > < div class ="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl" > < div class ="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9" > < div class ="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p" > < h3 class ="rs-h3 rs-h3_theme_dark" data-test="banner-title" > Remote Development < /h3 > < p class ="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description" > Connect to remote dev environments from anywhere in seconds < /p > < /div > < a data-test="banner-action" aria-label="Discover more" href="/remote-development/" type="button" class ="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569" > < path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z" > < /path > < /svg > < /a > < /div > < /div > < a href="/remote-development/" class ="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Discover more" data-test="banner-link" > < /a > < /div > < /div > < /div > < /div > < div class ="wt-col-inline" data-test="mobile-main-menu-item" data-test-marker="Support" > < button class ="_mobileMainMenuItem__action_5guvc _mobileMainMenuItem__action_aia9hh _mobileMainMenuItem__action_zczl4 _mobileMainMenuItem__action_jh6aw _mobileMainMenuItem__action_lfuz6" type="button" aria-label="Support: Open submenu" data-test="mobile-main-menu-item-action" > Support < /button > < div class ="_mobileMainSubmenu_5p4gw _mobileMainMenuItem__submenu_v3gfo wt-display-none" data-test="mobile-main-submenu" > < div class ="_mobileMainSubmenu__columnsWrapper_5r3czi" > < div class ="_mobileMainSubmenu__column_osm81 wt-offset-top-24 wt-offset-top-sm-48" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title" > PRODUCT & amp; TECHNICAL SUPPORT < /h5 > < div class ="wt-offset-top-12" > < div class ="_mobileMainSubmenuSubColumns__columnsWrapper_zt0m2" > < div class ="_mobileMainSubmenuSubColumns__column_gnsze" > < div class ="" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/support/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Support Center < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/help/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Product Documentation < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/company/webinars/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Webinars < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/resources/newsletters/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Newsletters < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/resources/eap/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Early Access < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://blog.jetbrains.com/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Blog < /span > < /span > < /a > < /div > < /div > < /div > < /div > < /div > < /div > < div class ="_mobileMainSubmenu__column_osm81 wt-offset-top-24 wt-offset-top-sm-48" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title" > FREQUENT TASKS < /h5 > < div class ="wt-offset-top-12" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://account.jetbrains.com/profile-details" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Manage your account < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://account.jetbrains.com/licenses" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Manage your licenses < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/support/sales/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Contact Sales < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://sales.jetbrains.com/hc/en-gb/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Licensing FAQ < /span > < /span > < /a > < /div > < /div > < /div > < /div > < div class ="main-submenu-banners _mainSubmenuBanners_332p1 _mainSubmenuBanners_j4vgp _mainSubmenuBannersAdaptive_aj1vpj _mainSubmenuBannersAdaptive_ei08o" data-test="main-submenu-banners" > < div class ="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner" > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(294.91deg, rgb(255, 49, 140) -50.1%, rgb(107, 87, 255) 97.43%); background-color: rgb(107, 87, 255);" > < /div > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(294.91deg, rgb(255, 49, 140) -50.1%, rgb(107, 87, 255) 97.43%); background-color: rgb(107, 87, 255);" > < /div > < div class ="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl" > < div class ="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c _productLogo_img_5cqf5" data-test="banner-logo-image" style="background-image: url(&quot;/img/banners-menu-main/download.svg&quot;);" > < /div > < div class ="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12" > < div class ="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p" > < h3 class ="rs-h3 rs-h3_theme_dark" data-test="banner-title" > Download and Install < /h3 > < /div > < a data-test="banner-action" aria-label="Download and Install" href="/products/" type="button" class ="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569" > < path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z" > < /path > < /svg > < /a > < /div > < /div > < a href="/products/" class ="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Download and Install" data-test="banner-link" > < /a > < /div > < div class ="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner" > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(283.8deg, rgb(8, 124, 250) 5.73%, rgb(33, 215, 137) 100%); background-color: rgb(33, 215, 137);" > < /div > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(283.8deg, rgb(8, 124, 250) 5.73%, rgb(33, 215, 137) 100%); background-color: rgb(33, 215, 137);" > < /div > < div class ="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl" > < div class ="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c _productLogo_img_5cqf5" data-test="banner-logo-image" style="background-image: url(&quot;/img/banners-menu-main/test-review.svg&quot;);" > < /div > < div class ="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12" > < div class ="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p" > < h3 class ="rs-h3 rs-h3_theme_dark" data-test="banner-title" > Contact us < /h3 > < /div > < a data-test="banner-action" aria-label="Contact us" href="/company/contacts/" type="button" class ="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569" > < path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z" > < /path > < /svg > < /a > < /div > < /div > < a href="/company/contacts/" class ="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Contact us" data-test="banner-link" > < /a > < /div > < /div > < /div > < /div > < div class ="wt-col-inline" data-test="mobile-main-menu-item" data-test-marker="Store" > < button class ="_mobileMainMenuItem__action_5guvc _mobileMainMenuItem__action_aia9hh _mobileMainMenuItem__action_zczl4 _mobileMainMenuItem__action_jh6aw _mobileMainMenuItem__action_lfuz6" type="button" aria-label="Store: Open submenu" data-test="mobile-main-menu-item-action" > Store < /button > < div class ="_mobileMainSubmenu_5p4gw _mobileMainMenuItem__submenu_v3gfo wt-display-none" data-test="mobile-main-submenu" > < div class ="_mobileMainSubmenu__columnsWrapper_5r3czi" > < div class ="_mobileMainSubmenu__column_osm81 wt-offset-top-24 wt-offset-top-sm-48" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title" > DEVELOPER TOOLS < /h5 > < div class ="wt-offset-top-12" > < div class ="_mobileMainSubmenuSubColumns__columnsWrapper_zt0m2" > < div class ="_mobileMainSubmenuSubColumns__column_gnsze" > < div class ="" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/store/#personal" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > For Individual Use < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/store/#commercial" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > For Teams and Organizations < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/store/#discounts" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Special offers & amp; programs < /span > < /span > < /a > < /div > < /div > < /div > < div class ="_mobileMainSubmenuSubColumns__column_gnsze" > < h5 class ="rs-h5 rs-h5_theme_light wt-offset-top-24 wt-offset-top-sm-48" data-test="mobile-main-menu-sub-column-title" > SERVICES & amp; PLUGINS < /h5 > < div class ="wt-offset-top-12" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/store/plugins/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Marketplace < /span > < /span > < /a > < /div > < /div > < /div > < div class ="_mobileMainSubmenuSubColumns__column_gnsze" > < h5 class ="rs-h5 rs-h5_theme_light wt-offset-top-24 wt-offset-top-sm-48" data-test="mobile-main-menu-sub-column-title" > LEARNING TOOLS < /h5 > < div class ="wt-offset-top-12" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/academy/buy/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > JetBrains Academy < /span > < /span > < /a > < /div > < /div > < /div > < /div > < /div > < /div > < div class ="_mobileMainSubmenu__column_osm81 wt-offset-top-24 wt-offset-top-sm-48" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title" > TEAM TOOLS < /h5 > < div class ="wt-offset-top-12" > < div class ="_mobileMainSubmenuSubColumns__columnsWrapper_zt0m2" > < div class ="_mobileMainSubmenuSubColumns__column_gnsze" > < div class ="" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/store/teamware#space-store-section" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Space < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/store/teamware#teamcity-store-section" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > TeamCity < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/store/teamware#youtrack-store-section" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > YouTrack < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/datalore/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Datalore < /span > < /span > < /a > < /div > < /div > < /div > < div class ="_mobileMainSubmenuSubColumns__column_gnsze" > < h5 class ="rs-h5 rs-h5_theme_light wt-offset-top-24 wt-offset-top-sm-48" data-test="mobile-main-menu-sub-column-title" > COLLABORATIVE DEVELOPMENT < /h5 > < div class ="wt-offset-top-12" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/code-with-me/buy/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Code With Me < /span > < /span > < /a > < /div > < /div > < /div > < /div > < /div > < /div > < div class ="_mobileMainSubmenu__column_osm81 _mobileMainSubmenu__column--full-size_niturg wt-offset-top-24 wt-offset-top-sm-48" > < h5 class ="rs-h5 rs-h5_theme_light" data-test="mobile-main-menu-column-title" > SALES SUPPORT < /h5 > < div class ="wt-offset-top-12" > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/support/sales/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Contact Sales < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/legal/docs/store/terms/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Purchase Terms < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="https://sales.jetbrains.com/hc/en-gb/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > FAQ < /span > < /span > < /a > < /div > < div class ="_mainSubmenuItem_v3ix5 _mainSubmenuItem_tzj91 _mainSubmenuItem_itkas" data-test="main-submenu-item" > < a href="/company/partners/" class ="_mainSubmenuItem__link_p3j8m _mainSubmenuItem__link_ekfw1h _mainSubmenuItem__link_pzevr _mainSubmenuItem__link_gwcytf _mainSubmenuItem__link_hmzggj _mainSubmenuItem__link_4t64w _mainSubmenuItem__link_n5r3x _mainSubmenuItem__link_pl7dq" data-test="main-submenu-item-link" > < span class ="_mainSubmenuItem__titlePart_cflex" > < span class ="rs-text-2 rs-text-2_theme_light _mainSubmenuItem__title_ccvp5" > Partners and Resellers < /span > < /span > < /a > < /div > < /div > < /div > < /div > < div class ="main-submenu-banners _mainSubmenuBanners_332p1 _mainSubmenuBanners_j4vgp _mainSubmenuBannersAdaptive_aj1vpj _mainSubmenuBannersAdaptive_ei08o" data-test="main-submenu-banners" > < div class ="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner" > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(293.2deg, rgb(253, 13, 122) 13.45%, rgb(252, 100, 67) 73.57%, rgb(248, 158, 7) 100%); background-color: rgb(255, 49, 140);" > < /div > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(293.2deg, rgb(253, 13, 122) 13.45%, rgb(252, 100, 67) 73.57%, rgb(248, 158, 7) 100%); background-color: rgb(255, 49, 140);" > < /div > < div class ="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl" > < div class ="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c _productLogo_img_5cqf5" data-test="banner-logo-image" style="background-image: url(&quot;/img/banners-menu-main/discount.svg&quot;);" > < /div > < div class ="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12" > < div class ="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p" > < h3 class ="rs-h3 rs-h3_theme_dark" data-test="banner-title" > All Products Pack < /h3 > < p class ="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description" > Get all JetBrains desktop tools including 10 & nbsp;IDEs, < br > 2 & nbsp;profilers, and 3 & nbsp;extensions < /p > < /div > < a data-test="banner-action" aria-label="Learn more" href="/all/" type="button" class ="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569" > < path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z" > < /path > < /svg > < /a > < /div > < /div > < a href="/all/" class ="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Learn more" data-test="banner-link" > < /a > < /div > < div class ="_mainSubmenuBanner_ebz8t _mainSubmenuBannerAdaptive_ui8nr _mainSubmenuBannerAdaptive_sl37t _mainSubmenuBanners__banner_jjws3k _mainSubmenuBanners__banner_mz6fx _mainSubmenuBanners__banner_xj7n7 _mainSubmenuBanners__banner_kmf4j" data-test="main-submenu-banner" > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageVertical_56jpu" style="background-image: linear-gradient(304.12deg, rgb(8, 124, 250) -14.07%, rgb(53, 53, 53) 109.22%); background-color: rgb(107, 87, 255);" > < /div > < div class ="_mainSubmenuBanner__image_ywo2j _mainSubmenuBanner__imageHorizontal_ounyn _mainSubmenuBanner__imageHorizontal_qqlfo" style="background-image: linear-gradient(304.12deg, rgb(8, 124, 250) -14.07%, rgb(53, 53, 53) 109.22%); background-color: rgb(107, 87, 255);" > < /div > < div class ="_mainSubmenuBanner__content_l9qzzl _mainSubmenuBanner__content_784gr _mainSubmenuBanner__content_0cnhhl _mainSubmenuBanner__content_u1hh9 _mainSubmenuBanner__content_skzqfl" > < svg fill="none" viewBox="0 0 70 70" class ="_productLogo_uqxhs _mainSubmenuBanner__logo_0iyk4 _mainSubmenuBanner__logo_oswk1 _mainSubmenuBanner__logo_la09c" data-test="banner-logo-image" > < defs > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__165" x1="5.174" x2="40.014" y1="39.889" y2="38.123" gradientUnits="userSpaceOnUse" > < stop offset="0.091" stop-color="#FC801D" > < /stop > < stop offset="0.231" stop-color="#B07F61" > < /stop > < stop offset="0.409" stop-color="#577DB3" > < /stop > < stop offset="0.533" stop-color="#1E7CE6" > < /stop > < stop offset="0.593" stop-color="#087CFA" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__164" x1="61.991" x2="50.158" y1="36.915" y2="1.557" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#FE2857" > < /stop > < stop offset="0.078" stop-color="#CB3979" > < /stop > < stop offset="0.16" stop-color="#9E4997" > < /stop > < stop offset="0.247" stop-color="#7557B2" > < /stop > < stop offset="0.339" stop-color="#5362C8" > < /stop > < stop offset="0.436" stop-color="#386CDA" > < /stop > < stop offset="0.541" stop-color="#2373E8" > < /stop > < stop offset="0.658" stop-color="#1478F2" > < /stop > < stop offset="0.794" stop-color="#0B7BF8" > < /stop > < stop offset="1" stop-color="#087CFA" > < /stop > < /linearGradient > < linearGradient id="__WEBTEAM_UI_SITE_HEADER_LOGO_ID__163" x1="10.066" x2="53.876" y1="16.495" y2="88.96" gradientUnits="userSpaceOnUse" > < stop offset="0" stop-color="#FE2857" > < /stop > < stop offset="0.08" stop-color="#FE295F" > < /stop > < stop offset="0.206" stop-color="#FF2D76" > < /stop > < stop offset="0.303" stop-color="#FF318C" > < /stop > < stop offset="0.385" stop-color="#EA3896" > < /stop > < stop offset="0.553" stop-color="#B248AE" > < /stop > < stop offset="0.792" stop-color="#5A63D6" > < /stop > < stop offset="1" stop-color="#087CFA" > < /stop > < /linearGradient > < /defs > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__165)" d="M11.2 49.4668L0.699951 41.3001L9 26L18.5 33.5L11.2 49.4668Z" > < /path > < path fill="#087CFA" d="M69.9999 18.6666L68.8333 59.2666L41.7666 70L27.0666 60.4333L41.7666 37.5L69.9999 18.6666Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__164)" d="M70 18.6666L55.5 33L37 15L48.0666 1.16663L70 18.6666Z" > < /path > < path fill="url(#__WEBTEAM_UI_SITE_HEADER_LOGO_ID__163)" d="M27.0667 60.4333L5.6 68.3667L10.0333 52.5L15.8667 33.1333L0 27.7667L10.0333 0L33.1333 2.8L54.5 31L55.5 33L27.0667 60.4333Z" > < /path > < path fill="#000" d="M56 14H14V56H56V14Z" > < /path > < g fill="#FFF" > < path d="M27.1366 22.1433V19.25H19.2733V22.1433H21.4666V32.1067H19.2733V34.9767H27.1366V32.1067H24.92V22.1433H27.1366Z" > < /path > < path d="M34.6967 35.21C33.46 35.21 32.4334 34.9767 31.6167 34.51C30.7767 34.0433 30.1 33.4833 29.5634 32.8533L31.7334 30.4267C32.1767 30.9167 32.6434 31.3133 33.0867 31.5933C33.5534 31.8733 34.0434 32.0133 34.6034 32.0133C35.2567 32.0133 35.77 31.8033 36.1434 31.3833C36.5167 30.9633 36.7034 30.31 36.7034 29.4V19.2733H40.25V29.5633C40.25 30.4967 40.1334 31.3133 39.8767 32.0133C39.62 32.7133 39.2467 33.2967 38.78 33.7633C38.29 34.2533 37.7067 34.6033 37.0067 34.86C36.3067 35.0933 35.5367 35.21 34.6967 35.21Z" > < /path > < path d="M34.4166 48.6499H18.6666V51.3332H34.4166V48.6499Z" > < /path > < /g > < /svg > < div class ="_mainSubmenuBanner__contentPart_l2uyh _mainSubmenuBanner__contentPart_ss1p9 wt-offset-top-lg-0 wt-offset-top-12" > < div class ="_mainSubmenuBanner__textContent_y5qkff _mainSubmenuBanner__textContent_cw50p" > < h3 class ="rs-h3 rs-h3_theme_dark" data-test="banner-title" > The Total Economic Impact™ of IntelliJ & nbsp;IDEA study < /h3 > < p class ="rs-text-2 rs-text-2_theme_dark _mainSubmenuBanner__description_abp0b" data-test="banner-description" > Commissioned TEI research conducted by Forrester Consulting < /p > < /div > < a data-test="banner-action" aria-label="Learn more" href="/lp/intellijidea-forrester-tei/" type="button" class ="_main_1dh718a_17 _modeOutline_1dh718a_389 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _mainSubmenuBanner__action_e4bdv _mainSubmenuBanner__action_j234b" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569" > < path d="M21 12l-8-6.857V11H2v2h11v5.857L21 12z" > < /path > < /svg > < /a > < /div > < /div > < a href="/lp/intellijidea-forrester-tei/" class ="_mainSubmenuBanner__bannerLink_gdfq6 _mainSubmenuBanner__bannerLink_nwlr2k" aria-label="Learn more" data-test="banner-link" > < /a > < /div > < /div > < /div > < /div > < div class ="wt-col-inline" data-test="mobile-main-menu-item" data-test-marker="Login" > < a href="https://account.jetbrains.com/" class ="_mobileMainMenuItem__action_5guvc _mobileMainMenuItem__action_aia9hh _mobileMainMenuItem__action_zczl4 _mobileMainMenuItem__action_jh6aw _mobileMainMenuItem__action_lfuz6" data-test="mobile-main-menu-item-action" > Login < /a > < /div > < /div > < /div > < /nav > < /div > < div class ="wt-col-inline wt-col_align-self_center _siteHeader__mobileActions_ysdb1" data-test="mobile-site-header-actions" > < div class ="_siteHeaderActions__row_dnkmi" > < div class ="_siteHeaderActions__action_r5cvz _siteHeaderActions__action_izukp" > < button data-test="site-header-mobile-search-action" aria-label="Open search" type="button" class ="_main_1dh718a_17 _modeClear_1dh718a_478 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _siteHeaderAction_tgwyh" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _siteHeaderAction__icon_qg4ev _siteHeaderAction__icon_vh845f _icon_1dh718a_569" > < path d="M2.293 10a6.99 6.99 0 0 0 11.187 5.6l6.106 6.107L21 20.293l-6.106-6.106A6.997 6.997 0 1 0 2.293 10zm2 0a5 5 0 1 1 5 5 5 5 0 0 1-5-5z" > < /path > < /svg > < /button > < /div > < div class ="_siteHeaderActions__action_r5cvz _siteHeaderActions__action_izukp" > < button data-test="site-header-open-mobile-main-menu-action" aria-label="Open main menu" type="button" class ="_main_1dh718a_17 _modeClear_1dh718a_478 _sizeS_1dh718a_92 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 _withoutText_1dh718a_138 _siteHeaderAction_tgwyh" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _siteHeaderAction__icon_qg4ev _siteHeaderAction__icon_vh845f _icon_1dh718a_569" > < path d="M4 5h16v2H4zm0 6h16v2H4zm0 6h16v2H4z" > < /path > < /svg > < /button > < /div > < /div > < /div > < /div > < /div > < /div > < /div > < /div > < /header > < /div >

< div


class ="menu-second _fixed" id="js-menu-second" data-test="menu-second" style="position: fixed; top: 0px; left: 0px; z-index: 1005; margin-top: 0px; margin-bottom: 0px; width: 320px;" >

< div


class ="wt-container" >

< div
id = "js-menu-second-mobile-wrapper"


class ="wt-display-none wt-display-md-block" >

< div
id = "js-menu-second-mobile" > < div


class ="wt-row wt-row_size_0 wt-row_wide wt-row_wrap menu-second-mobile wt-row_align-items_center wt-row_justify_between" > < button class ="wt-col-auto-fill wt-col_align-self_stretch menu-second-mobile__trigger" > < span class ="wt-list-item wt-list-item_placement_right wt-list-item_mode_nude wt-list-item_size_m wt-list-item_theme_light" data-test="list-item" > < span class ="wt-list-item__content" > Overview < /span > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd wt-list-item__icon wt-list-item__icon_placement_right" > < path d="M12 17L5 9h14l-7 8z" > < /path > < /svg > < /span > < /button > < a data-test="button" href="/pycharm/buy/" type="button" class ="wt-button wt-button_mode_primary wt-button_size_s wt-button_theme_light wt-button_align-icon_left wt-col-inline menu-second-mobile__download-button" > Pricing < /a > < /div > < /div >

< / div >

< div
id = "js-menu-second-desktop"


class ="menu-second-desktop


wt - row
wt - row_size_0
wt - row_align - items_center
"><div class="
wt - col - auto - fill
"><a class="
menu - second - title - box
" href=" / pycharm / "><span class="
menu - second - title - box__logo
jetbrains - logo
_pycharm
"><svg class="
_pycharm
sprite - img
" xmlns:xlink="
http: // www.w3.org / 1999 / xlink
"><use xlink:href="  # pycharm"></use></svg></span><span class="menu-second-title-box__title wt-h3">PyCharm</span></a></div><a href="/pycharm/nextversion/" class="wt-col-inline wt-text-2 menu-second__link wt-text-2_hardness_average menu-item">Coming in 2023.2 </a><a href="/pycharm/whatsnew/" class="wt-col-inline wt-text-2 menu-second__link wt-text-2_hardness_average menu-item">What's New </a><a href="/pycharm/features/" class="wt-col-inline wt-text-2 menu-second__link wt-text-2_hardness_average menu-item">Features </a><a href="/pycharm/learn/" class="wt-col-inline wt-text-2 menu-second__link wt-text-2_hardness_average menu-item">Learn </a><a href="/pycharm/buy/" class="wt-col-inline wt-button wt-button_size_s wt-button_mode_outline">Pricing</a><a href="/pycharm/download/" class="wt-col-inline menu-second__download-button wt-button wt-button_size_s wt-button_mode_primary">Download</a></div>

< / div >
< / div > < span


class ="fixer-placeholder" style="z-index: -1; float: none; clear: none; display: block; position: relative; top: 0px; margin: 0px; height: 73px; max-width: none;" > < /span >

< / div >

< div


class ="page__content " >

< div
id = "react-download-thanks" > < section


class ="wt-section wt-section_bg_white wt-section_theme_light wt-offset-top-96" > < div class ="wt-container" > < h1 class ="wt-h1 wt-h1_theme_light" > Thank you for downloading PyCharm! < /h1 > < h2 class ="wt-subtitle-1 wt-subtitle-1_theme_light wt-offset-top-24 download-thanks-direct-link-disclaimer" > Your download should start shortly.If it doesn't, please use the <a class="wt-link wt-link_theme_light" href="https://download.jetbrains.com/python/pycharm-community-2023.1.2.exe">direct link</a>.</h2><p class="wt-text-2 wt-text-2_theme_light wt-offset-top-24">Download and verify the file <a class="wt-link wt-link_theme_light" href="https://download.jetbrains.com/python/pycharm-community-2023.1.2.exe.sha256">SHA-256 checksum</a>.</p></div></section><section class="wt-section wt-section_bg_white wt-section_theme_light"><div class="wt-container"><div class="wt-row wt-row_direction_row wt-row_size_m wt-row-sm_direction_column"><div class="wt-col-5 wt-col-md-5 wt-col-sm-12"><form class="wt-row wt-row_size_m"><div class="wt-col-12"><h3 class="wt-h3 wt-h3_theme_light">Getting Started</h3><p class="wt-text-1 wt-text-1_hardness_hard wt-text-1_theme_light wt-offset-top-24">Send me helpful educational materials during my evaluation period</p></div><div class="wt-col-12"><label class="wt-input wt-input_theme_light wt-input_size_m wt-input_empty wt-input_icon-position_right wt-offset-top-24" data-test="input"><div class="wt-input__wrapper"><div class="wt-input__field"><input placeholder="Email address" autocomplete="on" name="Email" class="wt-input__inner" type="email" aria-invalid="false" value=""></div></div></label><span class="wt-privacy-notice wt-privacy-notice_theme_light wt-privacy-notice_size_xs wt-offset-top-24"><span class="wt-privacy-notice__message wt-privacy-notice__message_long">By submitting this form, I agree that my email address, name, and location may be used by JetBrains s.r.o. ("JetBrains") for the purposes outlined above. I agree that JetBrains may process said data using <a href="https://www.jetbrains.com/legal/privacy/third-parties.html" target="_blank">third-party services</a> for these purposes in accordance with the <a href="https://www.jetbrains.com/company/privacy.html" target="_blank">JetBrains Privacy Policy</a>. I understand that I can revoke this consent at any time in <a href="https://account.jetbrains.com/profile-details/privacy" target="_blank">my profile</a>. In addition, an unsubscribe link is included in each email.</span></span><button data-test="button" type="submit" class="wt-button wt-button_mode_primary wt-button_size_m wt-button_theme_light wt-button_align-icon_left wt-offset-top-24">Submit</button></div><div class="wt-col-12"></div></form></div><div class="wt-col-6 wt-col-sm-12 wt-offset-left-1 wt-offset-top-sm-96 wt-offset-left-sm-0"><h3 class="wt-h3 wt-h3_theme_light">New to PyCharm?</h3><div class="wt-row wt-row_size_0 wt-offset-top-24"><div class="wt-col-inline onboarding-icon-wrapper"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd"><path d="M8.29 20.25A11.59 11.59 0 0020 8.78v-.73a8.3 8.3 0 002-2.13 8.36 8.36 0 01-2.36.65 4.16 4.16 0 001.81-2.27 8.19 8.19 0 01-2.61 1 4.11 4.11 0 00-7 3.75 11.7 11.7 0 01-8.45-4.3 4.11 4.11 0 001.27 5.48 4.06 4.06 0 01-1.86-.52 4.11 4.11 0 003.29 4 4.13 4.13 0 01-1.85.07 4.12 4.12 0 003.83 2.85A8.25 8.25 0 013 18.47a7.929 7.929 0 01-1-.06 11.69 11.69 0 006.29 1.84"></path></svg></div><p class="wt-col-auto-fill wt-text-2 wt-text-2_theme_light"><a href="https://twitter.com/pycharm" class="wt-link wt-link_external">Follow us on Twitter</a></p></div><div class="wt-row wt-row_size_0 wt-offset-top-12"><div class="wt-col-inline onboarding-icon-wrapper"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd"><path d="M10 5h10v2H10zm0 6h10v2H10zm0 6h10v2H10z"></path><circle cx="6" cy="18" r="2"></circle><circle cx="6" cy="12" r="2"></circle><circle cx="6" cy="6" r="2"></circle></svg></div><p class="wt-col-auto-fill wt-text-2 wt-text-2_theme_light"><a href="https://www.jetbrains.com/help/pycharm/installation-guide.html" class="wt-link wt-link_external">Installation guide</a></p></div><div class="wt-row wt-row_size_0 wt-offset-top-12"><div class="wt-col-inline onboarding-icon-wrapper"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd"><path d="M9 5h10v10H9z"></path><path d="M7 9H5v10h10v-2H7V9z"></path></svg></div><p class="wt-col-auto-fill wt-text-2 wt-text-2_theme_light"><a href="/pycharm/learn/" class="wt-link">Learning center</a></p></div><div class="wt-row wt-row_size_0 wt-offset-top-12"><div class="wt-col-inline onboarding-icon-wrapper"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd"><circle cx="12.042" cy="4" r="2"></circle><path d="M18.339 7a6.982 6.982 0 0 0-6.3 4 6.982 6.982 0 0 0-6.3-4H3v10h2.739a6.983 6.983 0 0 1 6.3 4 6.582 6.582 0 0 1 6-4.033h2.994L21 7z"></path></svg></div><p class="wt-col-auto-fill wt-text-2 wt-text-2_theme_light"><a href="/pycharm/guide/" class="wt-link">PyCharm Guide</a></p></div><div class="wt-row wt-row_size_0 wt-offset-top-12"><div class="wt-col-inline onboarding-icon-wrapper"><svg viewBox="0 0 24 24" class="_wt-icon_bxtje _m_aq1fd"><path d="M21.79993,7.7356a4.80987,4.80987,0,0,0-.79456-2.1189,2.75914,2.75914,0,0,0-2.00378-.9021c-2.799-.217-6.9972-.217-6.9972-.217H11.995s-4.19812,0-6.99659.217a2.75983,2.75983,0,0,0-2.00378.9021,4.81806,4.81806,0,0,0-.79456,2.1189A34.36132,34.36132,0,0,0,2,11.18787v1.618a34.35272,34.35272,0,0,0,.20007,3.45288,4.8,4.8,0,0,0,.79456,2.11694,3.27043,3.27043,0,0,0,2.20508.91211C6.79956,19.45166,12,19.50232,12,19.50232s4.20264-.00745,7.00159-.22192a2.77147,2.77147,0,0,0,2.00378-.90406,4.80739,4.80739,0,0,0,.79456-2.11682A34.37352,34.37352,0,0,0,22,12.8064V11.18848A34.36535,34.36535,0,0,0,21.79993,7.7356ZM9.50232,15.75122V8.24878L15.75427,12Z"></path></svg></div><p class="wt-col-auto-fill wt-text-2 wt-text-2_theme_light"><a href="https://www.youtube.com/pycharmide?sub_confirmation=1" class="wt-link wt-link_external">Subscribe to our YouTube Channel</a></p></div></div></div></div></section><section class="wt-section wt-section_bg_white wt-section_theme_light"><div class="wt-container"><div class="wt-row wt-row_align-items_stretch wt-row_size_m"><div class="wt-col-6 wt-col-md-12 other-tools__card-wrapper wt-offset-top-24"><a data-test="card" href="/space/solutions/software-teams/" class="wt-card wt-card_theme_light wt-card_link other-tools__card"><div data-test="cardSection" class="wt-card__section"><div class="wt-row wt-row_align-items_center wt-row_size_m"><svg class="wt-col-inline other-tools__logo_small" data-test="svg-sprite-image" data-test-sprite-id="space"><use href="#space"></use></svg><h3 class="other-tools__logo-title">Space</h3></div><p class="rs-h2 rs-h2_theme_light wt-offset-top-24 other-tools__title">A complete software development platform</p><p class="rs-subtitle-2 rs-subtitle-2_theme_light wt-offset-top-24">Everything a modern team needs to build, deliver, and collaborate effectively</p><button data-test="button" type="button" class="_main_1e63mqc_17 _modeClassic_1e63mqc_135 _sizeM_1e63mqc_99 _alignIconLeft_1e63mqc_77 _light_1e63mqc_59 other-tools__button">Learn more</button></div></a></div><div class="wt-col-6 wt-col-md-12 other-tools__card-wrapper"><div class="wt-row wt-row_wrap wt-row_size_m"><div class="wt-col-6 wt-col-sm-12 other-tools__card-wrapper wt-offset-top-24"><a data-test="card" href="/idea" class="wt-card wt-card_theme_light wt-card_link other-tools__card"><div data-test="cardSection" class="wt-card__section"><svg class="other-tools__logo" data-test="svg-sprite-image" data-test-sprite-id="intellij-idea"><use href="#intellij-idea"></use></svg><h3 class="wt-h3 wt-offset-top-12">IntelliJ IDEA</h3><p class="wt-text-2 wt-text-2_hardness_average wt-offset-top-12">The most intelligent JVM IDE</p></div></a></div><div class="wt-col-6 wt-col-sm-12 other-tools__card-wrapper wt-offset-top-24"><a data-test="card" href="/datagrip" class="wt-card wt-card_theme_light wt-card_link other-tools__card"><div data-test="cardSection" class="wt-card__section"><svg class="other-tools__logo" data-test="svg-sprite-image" data-test-sprite-id="datagrip"><use href="#datagrip"></use></svg><h3 class="wt-h3 wt-offset-top-12">DataGrip</h3><p class="wt-text-2 wt-text-2_hardness_average wt-offset-top-12">Many databases, one tool</p></div></a></div><div class="wt-col-6 wt-col-sm-12 other-tools__card-wrapper wt-offset-top-24"><a data-test="card" href="/teamcity" class="wt-card wt-card_theme_light wt-card_link other-tools__card"><div data-test="cardSection" class="wt-card__section"><svg class="other-tools__logo" data-test="svg-sprite-image" data-test-sprite-id="teamcity"><use href="#teamcity"></use></svg><h3 class="wt-h3 wt-offset-top-12">TeamCity</h3><p class="wt-text-2 wt-text-2_hardness_average wt-offset-top-12">Powerful Continuous Integration out of the box</p></div></a></div><div class="wt-col-6 wt-col-sm-12 other-tools__card-wrapper wt-offset-top-24"><a data-test="card" href="/youtrack" class="wt-card wt-card_theme_light wt-card_link other-tools__card"><div data-test="cardSection" class="wt-card__section"><svg class="other-tools__logo" data-test="svg-sprite-image" data-test-sprite-id="youtrack"><use href="#youtrack"></use></svg><h3 class="wt-h3 wt-offset-top-12">YouTrack</h3><p class="wt-text-2 wt-text-2_hardness_average wt-offset-top-12">Powerful project management for all your teams</p></div></a></div></div></div></div></div></section></div>

< section


class ="wt-section wt-section_bg_gray-light" >

< div
id = "social-footer" > < div


class ="social-footer" > < div class ="wt-container wt-offset-top-96" > < div class ="wt-row wt-row_size_m wt-row_wide wt-row_wrap" > < div class ="wt-col-12" > < p class ="wt-subtitle-2 wt-subtitle-2_theme_light" > Tell me about new product features as they come out < /p > < form > < label class ="wt-input wt-input_theme_light wt-input_size_m wt-input_empty wt-input_icon-position_right wt-offset-top-24" data-test="input" > < div class ="wt-input__wrapper" > < div class ="wt-input__field" > < input placeholder="Email" autocomplete="on" name="Email" class ="wt-input__inner" type="email" aria-invalid="false" value="" > < /div > < /div > < /label > < span class ="wt-privacy-notice wt-privacy-notice_theme_light wt-privacy-notice_size_xs wt-offset-top-12" > < span class ="wt-privacy-notice__message wt-privacy-notice__message_long" > By submitting this form, I agree that JetBrains s.r.o.("JetBrains") may use my name, email address, and location data to send me newsletters, including commercial communications, and to process my personal data for this purpose.I agree that JetBrains may process said data using < a href="https://www.jetbrains.com/legal/privacy/third-parties.html" target="_blank" > third-party services < /a > for this purpose in accordance with the < a href="https://www.jetbrains.com/company/privacy.html" target="_blank" > JetBrains Privacy Policy < /a >.I understand that I can revoke this consent at any time in < a href="https://account.jetbrains.com/profile-details/privacy" target="_blank" > my profile < /a >.In addition, an unsubscribe link is included in each email.< /span > < /span > < div class ="wt-row wt-row_direction_column wt-row_size_m" > < div class ="wt-col-inline wt-offset-top-24" > < button data-test="button" type="submit" class ="wt-button wt-button_mode_primary wt-button_size_m wt-button_theme_light wt-button_align-icon_left wt-offset-top-24" > Submit < /button > < /div > < div class ="wt-col-inline wt-offset-top-24" > < a target="_blank" href="https://info.jetbrains.com/rs/426-QVD-114/images/PyCharm-EN-sample.html" class ="wt-link wt-link_theme_light" > View sample newsletter < /a > < /div > < /div > < div class ="wt-offset-top-24" > < /div > < /form > < /div > < div class ="wt-col-auto-fill" > < h3 class ="wt-h3 wt-h3_theme_light wt-offset-top-sm-48" > Follow us < /h3 > < div class ="wt-row wt-row_size_m wt-row_wide wt-row_wrap" > < div class ="wt-col-12" > < div class ="social-footer__link-wrapper wt-offset-top-24 undefined" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd social-footer__icon" > < path d="M16.444 5H7.556a5.556 5.556 0 0 0 0 11.111v4.445L12 16.11h4.444a5.556 5.556 0 0 0 0-11.111zM6.5 12A1.5 1.5 0 1 1 8 10.5 1.5 1.5 0 0 1 6.5 12zm5.5 0a1.5 1.5 0 1 1 1.5-1.5A1.5 1.5 0 0 1 12 12zm5.5 0a1.5 1.5 0 1 1 1.5-1.5 1.5 1.5 0 0 1-1.5 1.5z" > < /path > < /svg > < a class ="social-footer__link rs-link rs-link_mode_classic rs-link_theme_light" href="//intellij-support.jetbrains.com/hc/en-us/community/topics/200379535-PyCharm" > Community forum < /a > < /div > < div class ="social-footer__link-wrapper wt-offset-top-24 undefined" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd social-footer__icon" > < path d="M8 3H5v2h5a2 2 0 0 0-2-2zm11 0h-3a2 2 0 0 0-2 2h5zM4 17v4h2v-6a2 2 0 0 0-2 2zm14-2v6h2v-4a2 2 0 0 0-2-2z" > < /path > < path d="M16.573 8a4.986 4.986 0 0 0-9.147 0H4v2h3v4a5 5 0 0 0 10 0v-4h3V8z" > < /path > < /svg > < a class ="social-footer__link rs-link rs-link_mode_classic rs-link_theme_light" href="//youtrack.jetbrains.com/issues/PY" > Bug and issue tracker < /a > < /div > < div class ="social-footer__link-wrapper wt-offset-top-24 undefined" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd social-footer__icon" > < circle cx="12.042" cy="4" r="2" > < /circle > < path d="M18.339 7a6.982 6.982 0 0 0-6.3 4 6.982 6.982 0 0 0-6.3-4H3v10h2.739a6.983 6.983 0 0 1 6.3 4 6.582 6.582 0 0 1 6-4.033h2.994L21 7z" > < /path > < /svg > < a class ="social-footer__link rs-link rs-link_mode_classic rs-link_theme_light" href="//blog.jetbrains.com/pycharm/" > PyCharm blog < /a > < /div > < /div > < div class ="wt-col-12" > < div class ="social-footer__link-wrapper wt-offset-top-24 undefined" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd social-footer__icon" > < path d="M21.79993,7.7356a4.80987,4.80987,0,0,0-.79456-2.1189,2.75914,2.75914,0,0,0-2.00378-.9021c-2.799-.217-6.9972-.217-6.9972-.217H11.995s-4.19812,0-6.99659.217a2.75983,2.75983,0,0,0-2.00378.9021,4.81806,4.81806,0,0,0-.79456,2.1189A34.36132,34.36132,0,0,0,2,11.18787v1.618a34.35272,34.35272,0,0,0,.20007,3.45288,4.8,4.8,0,0,0,.79456,2.11694,3.27043,3.27043,0,0,0,2.20508.91211C6.79956,19.45166,12,19.50232,12,19.50232s4.20264-.00745,7.00159-.22192a2.77147,2.77147,0,0,0,2.00378-.90406,4.80739,4.80739,0,0,0,.79456-2.11682A34.37352,34.37352,0,0,0,22,12.8064V11.18848A34.36535,34.36535,0,0,0,21.79993,7.7356ZM9.50232,15.75122V8.24878L15.75427,12Z" > < /path > < /svg > < a class ="social-footer__link rs-link rs-link_mode_classic rs-link_theme_light" href="//www.youtube.com/c/PyCharmIDE" > YouTube < /a > < /div > < div class ="social-footer__link-wrapper wt-offset-top-24 undefined" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd social-footer__icon" > < path d="M8.29 20.25A11.59 11.59 0 0020 8.78v-.73a8.3 8.3 0 002-2.13 8.36 8.36 0 01-2.36.65 4.16 4.16 0 001.81-2.27 8.19 8.19 0 01-2.61 1 4.11 4.11 0 00-7 3.75 11.7 11.7 0 01-8.45-4.3 4.11 4.11 0 001.27 5.48 4.06 4.06 0 01-1.86-.52 4.11 4.11 0 003.29 4 4.13 4.13 0 01-1.85.07 4.12 4.12 0 003.83 2.85A8.25 8.25 0 013 18.47a7.929 7.929 0 01-1-.06 11.69 11.69 0 006.29 1.84" > < /path > < /svg > < a class ="social-footer__link rs-link rs-link_mode_classic rs-link_theme_light" href="//twitter.com/pycharm" > @ PyCharm on Twitter < /a > < /div > < /div > < /div > < /div > < /div > < /div > < /div > < /div >

< / section > < / div >

< div


class ="page__footer" id="footer-container" > < footer class ="wt-footer wt-footer_mode_full wt-footer_theme_dark jb-footer" data-test="footer" data-e2e="footer" > < div class ="wt-container" > < div class ="wt-footer__top wt-footer__top_theme_dark" > < ul class ="jb-footer-catalog wt-row wt-row_size_m" > < li class ="jb-footer-catalog__item wt-offset-top-48 wt-col-2 wt-col-md-4 wt-col-sm-6" > < h2 class ="rs-h5 rs-h5_theme_dark" > Products < /h2 > < ul class ="wt-offset-top-12 jb-footer-catalog-links" > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/products/#type=ide" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > IDEs < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/products/#tech=dotnet" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" >.NET & amp; Visual Studio < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/products/#type=team" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Team Tools < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="https://plugins.jetbrains.com" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Plugins < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/edu-products/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Education < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/products/#type=language" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Languages < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/products/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > All products < /a > < /li > < /ul > < /li > < li class ="jb-footer-catalog__item wt-offset-top-48 wt-col-2 wt-col-md-4 wt-col-sm-6" > < h2 class ="rs-h5 rs-h5_theme_dark" > Solutions < /h2 > < ul class ="wt-offset-top-12 jb-footer-catalog-links" > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/cpp/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > C++ Tools < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/data-tools/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Data Tools < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/devops/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > DevOps < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/education/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Education < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/gamedev/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Game Development < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/space/solutions/software-teams/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Software Development < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/store/business/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Tools For Business < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/quality-assurance-solutions/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Quality Assurance < /a > < /li > < /ul > < /li > < li class ="jb-footer-catalog__item wt-offset-top-48 wt-col-2 wt-col-md-4 wt-col-sm-6" > < h2 class ="rs-h5 rs-h5_theme_dark" > Initiatives < /h2 > < ul class ="wt-offset-top-12 jb-footer-catalog-links" > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/opensource/kotlin/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Kotlin < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/lp/mono/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > JetBrains Mono < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/research/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > JetBrains Research < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/opensource/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Open Source Projects < /a > < /li > < /ul > < /li > < li class ="jb-footer-catalog__item wt-offset-top-48 wt-col-2 wt-col-md-4 wt-col-sm-6" > < h2 class ="rs-h5 rs-h5_theme_dark" > Community < /h2 > < ul class ="wt-offset-top-12 jb-footer-catalog-links" > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/community/education/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Academic Licensing < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/community/opensource/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Open Source Support < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/community/user-groups/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > User Groups < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/community/events-partnership/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Events Partnership < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/community/dev-recognition/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Developer Recognition < /a > < /li > < /ul > < /li > < li class ="jb-footer-catalog__item wt-offset-top-48 wt-col-2 wt-col-md-4 wt-col-sm-6" > < h2 class ="rs-h5 rs-h5_theme_dark" > Resources < /h2 > < ul class ="wt-offset-top-12 jb-footer-catalog-links" > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/support/sales/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Sales Support < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/support/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Product Support < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="https://sales.jetbrains.com/hc/en-gb/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Licensing FAQ < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/help/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Documentation < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/resources/eap/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Early Access < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/company/conferences/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Events and Webinars < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/resources/newsletters/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Newsletters < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/resources/industry-reports/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Industry Reports < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="https://blog.jetbrains.com/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Blog < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/company/brand/desktop-art/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Desktop Art < /a > < /li > < /ul > < /li > < li class ="jb-footer-catalog__item wt-offset-top-48 wt-col-2 wt-col-md-4 wt-col-sm-6" > < h2 class ="rs-h5 rs-h5_theme_dark" > Company < /h2 > < ul class ="wt-offset-top-12 jb-footer-catalog-links" > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/company/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > About < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/company/contacts/#headquarters-international-sales" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Contacts < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/careers/apply/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Careers < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/company/press/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > News < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/company/customers/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Customers & amp; Awards < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/company/commitment/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Our Commitment < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/company/brand/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Brand Assets < /a > < /li > < li class ="jb-footer-catalog-links__item wt-offset-top-8 rs-text-3 rs-text-3_theme_dark" > < a href="/company/partners/" class ="rs-link rs-link_hardness_average rs-link_mode_clear rs-link_theme_dark" > Partners and Resellers < /a > < /li > < /ul > < /li > < /ul > < /div > < div class ="wt-footer__main" > < div class ="wt-footer__social wt-offset-top-24 wt-offset-top-sm-32" > < div class ="wt-social-list wt-social-list_theme_dark wt-row wt-row_size_xs" data-test="social-list" > < a data-test="button" title="JetBrains on Facebook" href="https://www.facebook.com/JetBrains" type="button" class ="_main_1e63mqc_17 _modeClear_1e63mqc_434 _sizeS_1e63mqc_92 _alignIconLeft_1e63mqc_77 _dark_1e63mqc_62 _withIcon_1e63mqc_119 _withoutText_1e63mqc_113 wt-col-inline" > < svg viewBox="0 0 24 24" class ="_icon_jncl6f_3 _sizeM_jncl6f_12 wt-social-list__icon _icon_1e63mqc_525" > < path d="M19.227 4H4.74a1.238 1.238 0 00-1.255 1.228v14.544A1.239 1.239 0 004.74 21h7.852v-5.881h-2.153v-2.47h2.153v-1.901a3.032 3.032 0 01.843-2.41 2.995 2.995 0 012.377-.898c.633.01 1.264.064 1.889.162v2.11h-1.067a1.213 1.213 0 00-1.309.788 1.228 1.228 0 00-.07.542v1.606h2.351l-.377 2.471h-1.974V21h3.972a1.243 1.243 0 001.258-1.227V5.228A1.24 1.24 0 0019.227 4z" > < /path > < /svg > < /a > < a data-test="button" title="JetBrains on Twitter" href="https://twitter.com/jetbrains" type="button" class ="_main_1e63mqc_17 _modeClear_1e63mqc_434 _sizeS_1e63mqc_92 _alignIconLeft_1e63mqc_77 _dark_1e63mqc_62 _withIcon_1e63mqc_119 _withoutText_1e63mqc_113 wt-col-inline" > < svg viewBox="0 0 24 24" class ="_icon_jncl6f_3 _sizeM_jncl6f_12 wt-social-list__icon _icon_1e63mqc_525" > < path d="M8.925 20a11.08 11.08 0 007.848-3.141 10.664 10.664 0 003.222-7.704v-.492a7.868 7.868 0 001.89-1.98 8.032 8.032 0 01-2.23.604 3.862 3.862 0 001.71-2.109 7.802 7.802 0 01-2.467.93 3.93 3.93 0 00-4.67-.754 3.796 3.796 0 00-1.947 4.238 11.142 11.142 0 01-7.988-3.996 3.78 3.78 0 001.201 5.092 3.878 3.878 0 01-1.758-.483 3.841 3.841 0 003.11 3.717 3.97 3.97 0 01-1.749.065 3.887 3.887 0 003.62 2.649 7.917 7.917 0 01-4.792 1.71 8.05 8.05 0 01-.946-.056A11.186 11.186 0 008.925 20z" > < /path > < /svg > < /a > < a data-test="button" title="JetBrains on LinkedIn" href="https://www.linkedin.com/company/jetbrains" type="button" class ="_main_1e63mqc_17 _modeClear_1e63mqc_434 _sizeS_1e63mqc_92 _alignIconLeft_1e63mqc_77 _dark_1e63mqc_62 _withIcon_1e63mqc_119 _withoutText_1e63mqc_113 wt-col-inline" > < svg viewBox="0 0 24 24" class ="_icon_jncl6f_3 _sizeM_jncl6f_12 wt-social-list__icon _icon_1e63mqc_525" > < path d="M4.84 4h14.487a1.241 1.241 0 011.258 1.228v14.544A1.24 1.24 0 0119.327 21H4.84a1.24 1.24 0 01-1.255-1.228V5.228A1.238 1.238 0 014.84 4zm1.264 14.488h2.524v-8.113H6.104v8.113zM7.367 9.26a1.46 1.46 0 10-1.351-.898 1.442 1.442 0 001.351.898zm8.184 9.227h2.521v-4.449c0-2.19-.472-3.862-3.025-3.862a2.644 2.644 0 00-2.385 1.303h-.035v-1.105H10.21v8.113h2.518v-4.014c0-1.058.2-2.087 1.512-2.087 1.294 0 1.311 1.208 1.311 2.153v3.948z" > < /path > < /svg > < /a > < a data-test="button" title="JetBrains on YouTube" href="https://www.youtube.com/user/JetBrainsTV" type="button" class ="_main_1e63mqc_17 _modeClear_1e63mqc_434 _sizeS_1e63mqc_92 _alignIconLeft_1e63mqc_77 _dark_1e63mqc_62 _withIcon_1e63mqc_119 _withoutText_1e63mqc_113 wt-col-inline" > < svg viewBox="0 0 24 24" class ="_icon_jncl6f_3 _sizeM_jncl6f_12 wt-social-list__icon _icon_1e63mqc_525" > < path d="M3.917 17.765a2.94 2.94 0 001.98.82c1.437.146 6.107.191 6.107.191s3.775-.006 6.289-.199a2.486 2.486 0 001.799-.812c.386-.568.63-1.22.714-1.901.112-1.03.172-2.065.18-3.101v-1.454a30.817 30.817 0 00-.18-3.1 4.32 4.32 0 00-.714-1.903 2.473 2.473 0 00-1.8-.81c-2.513-.195-6.284-.195-6.284-.195H12s-3.77 0-6.284.195a2.476 2.476 0 00-1.799.81 4.318 4.318 0 00-.714 1.903 30.782 30.782 0 00-.18 3.1v1.454c.008 1.036.068 2.07.18 3.1a4.31 4.31 0 00.714 1.902zM9.761 8.67l5.615 3.369-5.615 3.369V8.67z" > < /path > < /svg > < /a > < a data-test="button" title="JetBrains on Instagram" href="https://www.instagram.com/jetbrains/" type="button" class ="_main_1e63mqc_17 _modeClear_1e63mqc_434 _sizeS_1e63mqc_92 _alignIconLeft_1e63mqc_77 _dark_1e63mqc_62 _withIcon_1e63mqc_119 _withoutText_1e63mqc_113 wt-col-inline" > < svg viewBox="0 0 24 24" class ="_icon_jncl6f_3 _sizeM_jncl6f_12 wt-social-list__icon _icon_1e63mqc_525" > < path d="M7.857 4h8.257a4.355 4.355 0 014.371 4.373v8.254A4.355 4.355 0 0116.114 21H7.857a4.355 4.355 0 01-4.372-4.373V8.373A4.355 4.355 0 017.857 4zm8.257 15.177a2.561 2.561 0 002.55-2.55V8.373a2.566 2.566 0 00-2.55-2.55H7.857a2.561 2.561 0 00-2.55 2.55v8.254a2.566 2.566 0 002.55 2.55h8.257zm-4.129-9.472a3.036 3.036 0 103.036 3.04 3.011 3.011 0 00-3.036-3.04zm2.793-1.21a1.15 1.15 0 011.215-1.218 1.221 1.221 0 011.214 1.219 1.214 1.214 0 01-2.429 0z" > < /path > < /svg > < /a > < a data-test="button" title="JetBrains on TikTok" href="https://www.tiktok.com/@jetbrains?lang=en" type="button" class ="_main_1e63mqc_17 _modeClear_1e63mqc_434 _sizeS_1e63mqc_92 _alignIconLeft_1e63mqc_77 _dark_1e63mqc_62 _withIcon_1e63mqc_119 _withoutText_1e63mqc_113 wt-col-inline" > < svg viewBox="0 0 24 24" class ="_icon_jncl6f_3 _sizeM_jncl6f_12 wt-social-list__icon _icon_1e63mqc_525" > < path d="M9.712 9.616a5.69 5.69 0 0 0-5.554 5.688 5.68 5.68 0 0 0 1.529 3.878A5.68 5.68 0 0 0 9.85 21a5.7 5.7 0 0 0 5.691-5.696v-6.29a7.355 7.355 0 0 0 4.301 1.383V7.305a4.296 4.296 0 0 1-3.244-1.484A4.275 4.275 0 0 1 15.54 3h-3.094l-.004 12.4a2.6 2.6 0 0 1-2.593 2.503c-.867 0-1.63-.429-2.106-1.079a2.573 2.573 0 0 1-.492-1.515c0-1.433 1.165-2.6 2.598-2.6.267 0 .526.047.768.122V9.67a5.783 5.783 0 0 0-.768-.054" > < /path > < /svg > < /a > < a data-test="button" title="JetBrains blog" href="https://blog.jetbrains.com/" type="button" class ="_main_1e63mqc_17 _modeClear_1e63mqc_434 _sizeS_1e63mqc_92 _alignIconLeft_1e63mqc_77 _dark_1e63mqc_62 _withIcon_1e63mqc_119 _withoutText_1e63mqc_113 wt-col-inline" > < svg viewBox="0 0 24 24" class ="_icon_jncl6f_3 _sizeM_jncl6f_12 wt-social-list__icon _icon_1e63mqc_525" > < path d="M13.999 5a2 2 0 11-4 0 2 2 0 014 0zm4.348 3h2.656l.033 9.967h-2.988A6.624 6.624 0 0012.02 22a6.913 6.913 0 00-6.25-4H3.036V8H5.77a6.912 6.912 0 016.25 4 7.025 7.025 0 016.327-4z" > < /path > < /svg > < /a > < a data-test="button" title="JetBrains RSS Feed" href="https://blog.jetbrains.com/feed/" type="button" class ="_main_1e63mqc_17 _modeClear_1e63mqc_434 _sizeS_1e63mqc_92 _alignIconLeft_1e63mqc_77 _dark_1e63mqc_62 _withIcon_1e63mqc_119 _withoutText_1e63mqc_113 wt-col-inline" > < svg viewBox="0 0 24 24" class ="_icon_jncl6f_3 _sizeM_jncl6f_12 wt-social-list__icon _icon_1e63mqc_525" > < path d="M4.6 3.1v2.2a15.577 15.577 0 0114.2 13.9H21A17.767 17.767 0 004.6 3.1zm0 6v2.2a9.548 9.548 0 018.2 7.9H15A11.688 11.688 0 004.6 9.1zm-.23 7.478A2.2 2.2 0 004 17.8 2.22 2.22 0 006.2 20a2.2 2.2 0 10-1.83-3.422z" > < /path > < /svg > < /a > < /div > < /div > < div class ="wt-footer__region wt-offset-top-24 wt-offset-top-sm-24" > < div class ="wt-row wt-row_size_s" > < button data-test="footer-country-button" type="button" class ="wt-button wt-button_mode_nude wt-button_size_m wt-button_theme_dark wt-button_with-icon wt-button_align-icon_left wt-col-inline" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd wt-button__icon" > < path d="M12 3a9 9 0 1 0 9 9 9.01 9.01 0 0 0-9-9zm1.78 15.762L11 15.764A2.989 2.989 0 0 0 9 15H5.685A6.96 6.96 0 0 1 13 5.08V7a2 2 0 0 1-2 2h-1a2 2 0 0 0 0 4h4a2.476 2.476 0 0 1 2 1 24.497 24.497 0 0 0 1.84 1.85 7.017 7.017 0 0 1-4.06 2.912z" > < /path > < /svg > Kuwait < /button > < span data-test="dropdown-trigger" class ="_triggerWrapper_1t4sa2o_55" > < button data-test="language-picker" type="button" class ="_main_1dh718a_17 _modeClear_1dh718a_478 _sizeM_1dh718a_99 _alignIconLeft_1dh718a_77 _dark_1dh718a_62 _withIcon_1dh718a_144 wt-col-inline" > < svg viewBox="0 0 24 24" class ="_wt-icon_bxtje _m_aq1fd _icon_1dh718a_569" > < path d="m11.62965 16.61452c-1.13922-.692-3.111-2.36313-3.153-2.32718a28.32942 28.32942 0 0 1 -3.30095 2.26177c-.68823.39708-1.38892.49615-1.82064-.09139a.992.992 0 0 1 .26656-1.40406c.00852-.00391 2.44665-1.594 3.25973-2.29678a11.64387 11.64387 0 0 1 -2.23281-3.53521 1.07774 1.07774 0 0 1 .52716-1.36835c.52715-.22205 1.049-.12664 1.48663.61989a10.33341 10.33341 0 0 0 1.8143 2.89517 10.853 10.853 0 0 0 2.1563-4.3469l-7.63293-.02148v-2.00685h4.8124v-.99406a.98574.98574 0 1 1 1.9713 0v.99406h5.1703v2.00685h-2.08646a17.03869 17.03869 0 0 1 -2.64065 5.75689 15.88157 15.88157 0 0 0 2.30149 1.66068l2.3092-5.66617a1.162 1.162 0 0 1 2.1802.01591l3.01041 7.389 1.85638 4.385h-2.47393l-1.08252-2.53924h-4.84082l-.888 2.53924h-2.5993l.287-.69166zm4.31307-5.16715-1.67531 4.55419h3.35059z" > < /path > < /svg > English < /button > < /span > < /div > < /div > < div class ="wt-footer__legal wt-offset-top-24 wt-offset-top-sm-12" > < div class ="wt-row wt-row_size_s rs-text-3 rs-text-3_theme_dark" > < a href="/privacy-security/" class ="rs-link rs-link_mode_clear rs-link_theme_dark wt-col-inline" rel="" > Privacy & amp; Security < /a > < a href="/legal/docs/company/useterms.html" class ="rs-link rs-link_mode_clear rs-link_theme_dark wt-col-inline" rel="" > Terms of Use < /a > < a href="/legal/trademarks/" class ="rs-link rs-link_mode_clear rs-link_theme_dark wt-col-inline" rel="" > Trademarks < /a > < a href="/legal/" class ="rs-link rs-link_mode_clear rs-link_theme_dark wt-col-inline" rel="" > Legal < /a > < a href="/genuine-tools/" class ="rs-link rs-link_mode_clear rs-link_theme_dark wt-col-inline" rel="" > Genuine Tools < /a > < /div > < /div > < div class ="wt-footer__copyright wt-offset-top-24 wt-offset-top-sm-12" > < span class ="rs-text-3 rs-text-3_hardness_pale rs-text-3_theme_dark" > Copyright © 2000-2023 JetBrains s.r.o.< /span > < /div > < div class ="wt-footer__motto wt-offset-top-24 wt-offset-top-sm-0" > < span class ="rs-text-3 rs-text-3_hardness_pale rs-text-3_theme_dark" > Developed with drive and < a href="https://jetbrains.com/idea" class ="rs-link rs-link_mode_clear rs-link_theme_dark" > IntelliJ IDEA < /a > < /span > < /div > < /div > < /div > < /footer > < /div >

< / div >

< script >
(function() {
function getParameterByName(name, url)
{
if (!url)
url = window.location.href;
name = name.replace( / [\[\]] / g, "\\$&");
var
regex = new
RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"), \
    results = regex.exec(url);
if (!results)
return null;
if (!results[2]) return '';
return decodeURIComponent(results[2].replace( /\+ / g, " "));
}

function
updateQueryStringParameter(uri, key, value)
{
var
re = new
RegExp("([?&])" + key + "=.*?(&|$)", "i");
var
separator = uri.indexOf('?') != = -1 ? "&": "?";
if (uri.match(re)) {
return uri.replace(re, '$1' + key + "=" + value + '$2');
}
else {
return uri + separator + key + "=" + value;
}
}

var
downloadLink = document.getElementById("download-link");
if (downloadLink != null)
{
    var
platform = getParameterByName('platform');
platform = platform != null ? platform: "windows";
var
href = downloadLink.getAttribute("href");
var
code = getParameterByName("code");

if (code != null)
{
href = updateQueryStringParameter(href, "code", code)
}
href = updateQueryStringParameter(href, "platform", platform);
downloadLink.setAttribute("href", href);
}
})();
< / script > < script >
    (function() {
    var STORAGE_KEY_NAME = 'firefoxDisappearedSVGWorkaround';
    var STORAGE_KEY_VALUE = '1';

    var isFirefox = /firefox/i.test(navigator.userAgent);
if (!isFirefox | | isFirefox & & sessionStorage.getItem(STORAGE_KEY_NAME) == = STORAGE_KEY_VALUE) {
return;
}

var
arrayFrom = function(arrayLike)
{
return Array.prototype.slice.call(arrayLike, 0);
};

function
workaround()
{
var
uses = document.querySelectorAll('.page svg use');
var
badNodesCount = 0;

arrayFrom(uses).forEach(function(node)
{
    var
rect = node.getBoundingClientRect();
if (rect.width === 0 & & rect.height == = 0)
badNodesCount + +;
});

if (badNodesCount === uses.length) {
sessionStorage.setItem(STORAGE_KEY_NAME, STORAGE_KEY_VALUE);
if (typeof dataLayer != = 'undefined')
dataLayer.push({'firefoxDisappearedSVGWorkaround': STORAGE_KEY_VALUE});

window.location.replace(window.location.href);
}
}

window.addEventListener('DOMContentLoaded', workaround);

})();
< / script > < link
href = "/_assets/banner-rotator.entry.0b418a05856f484a77be.css"
rel = "stylesheet"
type = "text/css" >
       < script
src = "/_assets/banner-rotator.entry.7dd68376a639342b6574.js"
type = "text/javascript" > < / script >

                               < script >
                               (function() {

                               'use strict';

                               function ImagesSrcReplacer ()
{

var
attribute = 'data-src';
var
matches = document.querySelectorAll('img[' + attribute + ']');

for (var i = 0, n = matches.length; i < n; i++) {

    var attrValue = matches[i].getAttribute(attribute);

if (_isHighDensity ()) {

var name = attrValue.substring(0, attrValue.lastIndexOf('.'));
var extention = attrValue.substring(attrValue.lastIndexOf('.'), attrValue.length);

matches[i].setAttribute('src', name + '@2x' + extention);

} else {
matches[i].setAttribute('src', attrValue)
}
}

/ **
*Detect
high
density
* @ returns
{* | boolean}
* /
function
_isHighDensity()
{
return (
        (window.matchMedia & &
         (window.matchMedia(
             'only screen and (min-resolution: 124dpi), only screen and (min-resolution: 1.3dppx), only screen and (min-resolution: 48.8dpcm)').matches | |
          window.matchMedia(
              'only screen and (-webkit-min-device-pixel-ratio: 1.3), only screen and (-o-min-device-pixel-ratio: 2.6/2), only screen and (min--moz-device-pixel-ratio: 1.3), only screen and (min-device-pixel-ratio: 1.3)').matches)) | |
        (window.devicePixelRatio & &
         window.devicePixelRatio > 1.3));
}
}

return new
ImagesSrcReplacer()

}(document, window));
< / script >

    < script
type = "text/javascript"
id = "" > var
separator = "|", firstCookieName = "first_utm_parameters", lastCookieName = "last_utm_parameters", cookieValue = "", undefinedCookieValue = (
                                                                                                                                                        "undefined" + separator).repeat(
    2) + "undefined", undefinedCookieValueExtended = ("undefined" + separator).repeat(5) + "undefined";
function
getCookie(b)
{
return (b
        =document.cookie.match(new RegExp("(?:^|; )"+b.replace( / ([\.$? * | {}\(\)\[\]\\\ / \+ ^]) / g, "\\$1")+"\x3d([^;]*)")))?
b[1]: void
0}
function
setCookie(b, a)
{var
d = 31104E6, c = new
Date, e = c.getTime();
c.setTime(e + d);
c = c.toUTCString();
document.cookie = b + "\x3d" + a + "; SameSite\x3dNone; Secure; expires\x3d" + c + "; path\x3d/; domain\x3d." + stripSubdomain(
    location.hostname)}function
stripSubdomain(b)
{var
a = b.split(".");
return 3 <= a.length?(a.shift(), a.join(".")): b}
function
getReferrerParameters()
{
try{var b=new URL(document.referrer), a=b.hostname;a=a.replace( / ^ www\./i, "");var d=b="referral", c="jetbrains.com jetbrains.ru jetbrains.com.cn pretix.eu kotlinlang.org ktor.io datalore.io talkingkotlin.com jetbrains.dev hyperskill.org teamcity.com kotlinconf.com jetbrains.space youtrack.pro qodana.cloud".split(" ");
return c.some(function(e)
{
return -1 !==a.indexOf(e)})?"undefined|undefined|undefined|undefined|undefined|undefined": (a.includes(
    "baidu") | | a.includes("bing") | |
                                                                                            a.includes(
                                                                                                "google")) & &!a.includes(
    "account") & & (a
                    =a.substring(0, a.indexOf(".")), d = b = "organic", "accounts" == a | | "cn" == a | | "com" == a | | "m" == a)?void
0: a + "|" + b + "|" + d + "|undefined|undefined|undefined"}catch(e)
{
return "undefined|undefined|undefined|undefined|undefined|undefined"}}function
getQueryParam(b)
{var
a = window.location.search.replaceAll("+", "%2b");
a = new
URLSearchParams(a);
return (b=a.get(b))?b.replaceAll("%2b", "+"): void
0}
cookieValue = getQueryParam("utm_source") | | getQueryParam("utm_medium") | | getQueryParam(
    "utm_campaign")?getQueryParam("utm_source") + separator + getQueryParam("utm_medium") + separator + getQueryParam(
    "utm_campaign"): getQueryParam("source") + separator + getQueryParam("medium") + separator + getQueryParam(
    "campaign");
cookieValue = getQueryParam("utm_term")?cookieValue + separator + getQueryParam("utm_term"): getQueryParam(
    "keyword")?cookieValue + separator + getQueryParam("keyword"): cookieValue + separator + getQueryParam("term");
cookieValue = getQueryParam("utm_content")?cookieValue + separator + getQueryParam(
    "utm_content"): cookieValue + separator + getQueryParam("content");
cookieValue = getQueryParam("gclid")?cookieValue + separator + getQueryParam(
    "gclid"): cookieValue + separator + getQueryParam("msclkid");
cookieValue = cookieValue.replace( /\s |, |; / g, "_");cookieValue = cookieValue.substring(0, 2E3);
if (cookieValue !==undefinedCookieValueExtended)
{var
first_cookie_value = getCookie(firstCookieName);
first_cookie_value & & first_cookie_value != = undefinedCookieValue & & first_cookie_value != = undefinedCookieValueExtended | | setCookie(
    firstCookieName, cookieValue);
setCookie(lastCookieName,
          cookieValue)} else cookieValue = getReferrerParameters(), cookieValue != undefinedCookieValueExtended & & (
(first_cookie_value
 =getCookie(firstCookieName)) & & first_cookie_value != = undefinedCookieValue & & first_cookie_value != = undefinedCookieValueExtended | |
setCookie(firstCookieName, cookieValue), setCookie(lastCookieName, cookieValue)); < / script > < script
type = "text/javascript"
id = "" > (function(){function b()
{!1 == = c & & (c=!0, Munchkin.init("426-QVD-114", {clickTime:250}))}var
c =!1, a = document.createElement("script");
a.type = "text/javascript";
a.async=!0;
a.src = "//munchkin.marketo.net/munchkin.js";
a.onreadystatechange = function()
{"complete" != this.readyState & & "loaded" != this.readyState | | b()};
a.onload = b;
document.getElementsByTagName("head")[0].appendChild(a)})(); < / script > < div
style = "display: none; visibility: hidden;" > < script
type = "text/javascript" > dataLayer.push({ecommerce: {detail: {products: [
    {id: "PyCharm", name: "PyCharm", price: "", brand: "JetBrains", category: "PC",
     position: 0}]}}}); < / script > < / div > < div
style = "display: none; visibility: hidden;" > < script > (function(c, d, f, g, e){c[e]=c[e] | |[];var h=function()
{var
b = {ti: "5220035"};
b.q = c[e];
c[e] = new
UET(b);
c[e].push("pageLoad")};var
a = d.createElement(f);
a.src = g;
a.async=1;
a.onload = a.onreadystatechange = function()
{var
b = this.readyState;
b & & "loaded" != = b & & "complete" != = b | | (h(), a.onload=a.onreadystatechange=null)};d = \
d.getElementsByTagName(f)[0];
d.parentNode.insertBefore(a, d)})(
window, document, "script", "//bat.bing.com/bat.js", "uetq"); < / script > < noscript > < / noscript > < / div > < div
style = "display: none; visibility: hidden;" >
        < script >!function(b, e, f, g, a, c, d)
{b.fbq | | (a=b.fbq=function()
{a.callMethod?a.callMethod.apply(a, arguments): a.queue.push(arguments)}, b._fbq | | (b._fbq
                                                                                      =a), a.push = a, a.loaded =!0, a.version = "2.0", a.queue = [], c = e.createElement(
    f), c.async=!0, c.src = g, d = e.getElementsByTagName(f)[0], d.parentNode.insertBefore(c, d))}(
window, document, "script", "https://connect.facebook.net/en_US/fbevents.js");
fbq("dataProcessingOptions", ["LDU"], 0, 0);
fbq("init", "614099138684330");
fbq("track", "PageView"); < / script >
                              < noscript > < / noscript >
                                               < / div > < script
type = "text/javascript"
id = "" > fbq("track", "StartTrial"); < / script > < img
src = "https://t.co/1/i/adsct?bci=4&amp;eci=3&amp;event=%7B%7D&amp;event_id=b4eaac27-588c-4cbc-bcf2-323edb7582f3&amp;integration=gtm&amp;p_id=Twitter&amp;p_user_id=0&amp;pl_id=80f5b32c-fce8-442a-bdf6-473697aa65b6&amp;tw_document_href=https%3A%2F%2Fwww.jetbrains.com%2Fpycharm%2Fdownload%2Fdownload-thanks.html%3Fplatform%3Dwindows%26code%3DPCC&amp;tw_iframe_status=0&amp;txn_id=nv3vm&amp;type=javascript&amp;version=2.3.29"
height = "1"
width = "1"
style = "display: none;" > < img
src = "https://analytics.twitter.com/1/i/adsct?bci=4&amp;eci=3&amp;event=%7B%7D&amp;event_id=b4eaac27-588c-4cbc-bcf2-323edb7582f3&amp;integration=gtm&amp;p_id=Twitter&amp;p_user_id=0&amp;pl_id=80f5b32c-fce8-442a-bdf6-473697aa65b6&amp;tw_document_href=https%3A%2F%2Fwww.jetbrains.com%2Fpycharm%2Fdownload%2Fdownload-thanks.html%3Fplatform%3Dwindows%26code%3DPCC&amp;tw_iframe_status=0&amp;txn_id=nv3vm&amp;type=javascript&amp;version=2.3.29"
height = "1"
width = "1"
style = "display: none;" > < img
src = "https://t.co/1/i/adsct?bci=4&amp;eci=4&amp;event=%7B%7D&amp;event_id=ed449bc0-9db5-4c99-b730-a52257271a58&amp;integration=gtm&amp;p_id=Twitter&amp;p_user_id=0&amp;pl_id=80f5b32c-fce8-442a-bdf6-473697aa65b6&amp;tw_document_href=https%3A%2F%2Fwww.jetbrains.com%2Fpycharm%2Fdownload%2Fdownload-thanks.html%3Fplatform%3Dwindows%26code%3DPCC&amp;tw_iframe_status=0&amp;txn_id=tw-nv3vm-odorw&amp;type=javascript&amp;version=2.3.29"
height = "1"
width = "1"
style = "display: none;" > < img
src = "https://analytics.twitter.com/1/i/adsct?bci=4&amp;eci=4&amp;event=%7B%7D&amp;event_id=ed449bc0-9db5-4c99-b730-a52257271a58&amp;integration=gtm&amp;p_id=Twitter&amp;p_user_id=0&amp;pl_id=80f5b32c-fce8-442a-bdf6-473697aa65b6&amp;tw_document_href=https%3A%2F%2Fwww.jetbrains.com%2Fpycharm%2Fdownload%2Fdownload-thanks.html%3Fplatform%3Dwindows%26code%3DPCC&amp;tw_iframe_status=0&amp;txn_id=tw-nv3vm-odorw&amp;type=javascript&amp;version=2.3.29"
height = "1"
width = "1"
style = "display: none;" > < div
style = "width:0px; height:0px; display:none; visibility:hidden;"
id = "batBeacon686084349506" > < img
style = "width:0px; height:0px; display:none; visibility:hidden;"
id = "batBeacon239237463747"
width = "0"
height = "0"
alt = ""
src = "https://bat.bing.com/action/0?ti=5220035&amp;Ver=2&amp;mid=91e580c8-92c7-44eb-a2d8-68988f9b26e8&amp;sid=4641b650ff6311edbbad5b31af409501&amp;vid=4641dba0ff6311eda7aa79030d243b01&amp;vids=1&amp;msclkid=N&amp;uach=pv%3D10.0.0&amp;pi=918639831&amp;lg=en-US&amp;sw=1920&amp;sh=1080&amp;sc=24&amp;tl=Thank%20you%20for%20downloading%20PyCharm!&amp;p=https%3A%2F%2Fwww.jetbrains.com%2Fpycharm%2Fdownload%2Fdownload-thanks.html%3Fplatform%3Dwindows%26code%3DPCC&amp;r=https%3A%2F%2Fwww.jetbrains.com%2Fpycharm%2Fdownload%2F&amp;lt=336&amp;evt=pageLoad&amp;sv=1&amp;rn=763685" > < / div > < / body > < grammarly - desktop - integration
data - grammarly - shadow - root = "true" > < / grammarly - desktop - integration > < / html >