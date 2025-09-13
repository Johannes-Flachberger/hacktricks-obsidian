# macOS File Extension & URL scheme app handlers


## LaunchServices Database

This is a database of all the installed applications in the macOS that can be queried to get information about each installed application such as URL schemes it support and MIME types.

It's possible to dump this datase with:

```
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -dump
```
```
Or using the tool [[https://newosxbook.com/tools/lsdtrip.html|**lsdtrip**]].

**`/usr/libexec/lsd`** is the brain of the database. It provides **several XPC services** like `.lsd.installation`, `.lsd.open`, `.lsd.openurl`, and more. But it also **requires some entitlements** to applications to be able to use the exposed XPC functionalities, like `.launchservices.changedefaulthandler` or `.launchservices.changeurlschemehandler` to change default apps for mime types or url schemes and others.

**`/System/Library/CoreServices/launchservicesd`** claims the service `com.apple.coreservices.launchservicesd` and can be queried to get information about running applications. It can be queried with the system tool /**`usr/bin/lsappinfo`** or with [[https://newosxbook.com/tools/lsdtrip.html|**lsdtrip**]].

## File Extension & URL scheme app handlers

The following line can be useful to find the applications that can open files depending on the extension:

```bash
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -dump | grep -E "path:|bindings:|name:"
```
```
Or use something like [[https://github.com/Lord-Kamina/SwiftDefaultApps|**SwiftDefaultApps**]]:

```bash
./swda getSchemes #Get all the available schemes
./swda getApps #Get all the apps declared
./swda getUTIs #Get all the UTIs
./swda getHandler --URL ftp #Get ftp handler
```
```
You can also check the extensions supported by an application doing:

```
cd /Applications/Safari.app/Contents
grep -A3 CFBundleTypeExtensions Info.plist  | grep string
				css
				pdf
				webarchive
				webbookmark
				webhistory
				webloc
				download
				safariextz
				gif
				html
				htm
				js
				jpg
				jpeg
				jp2
				txt
				text
				png
				tiff
				tif
				url
				ico
				xhtml
				xht
				xml
				xbl
				svg
```
```



