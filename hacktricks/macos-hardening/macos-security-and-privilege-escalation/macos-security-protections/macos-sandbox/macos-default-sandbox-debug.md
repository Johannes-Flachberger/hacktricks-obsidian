# macOS Default Sandbox Debug


In this page you can find how to create an app to launch arbitrary commands from inside the default macOS sandbox:

1. Compile the application:

```objectivec:main.m
#include <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        while (true) {
            char input[512];

            printf("Enter command to run (or 'exit' to quit): ");
            if (fgets(input, sizeof(input), stdin) == NULL) {
                break;
            }

            // Remove newline character
            size_t len = strlen(input);
            if (len > 0 && input[len - 1] == '\n') {
                input[len - 1] = '\0';
            }

            if (strcmp(input, "exit") == 0) {
                break;
            }

            system(input);
        }
    }
    return 0;
}
```
```
Compile it running: `clang -framework Foundation -o SandboxedShellApp main.m`

2. Build the `.app` bundle

```bash
mkdir -p SandboxedShellApp.app/Contents/MacOS
mv SandboxedShellApp SandboxedShellApp.app/Contents/MacOS/

cat << EOF > SandboxedShellApp.app/Contents/Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    CFBundleIdentifier
    com.example.SandboxedShellApp
    CFBundleName
    SandboxedShellApp
    CFBundleVersion
    1\.0
    CFBundleExecutable
    SandboxedShellApp
</dict>
</plist>
EOF
```
```
3. Define the entitlements

**sandbox**

```bash
cat << EOF > entitlements.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    com.apple.security.app\-sandbox
    
</dict>
</plist>
EOF
```
```

**sandbox + downloads**

```bash
cat << EOF > entitlements.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    com.apple.security.app\-sandbox
    
    com.apple.security.files.downloads.read\-write
    
</dict>
</plist>
EOF
```
```


4. Sign the app (you need to create a certificate in the keychain)

```bash
codesign --entitlements entitlements.plist -s "YourIdentity" SandboxedShellApp.app
./SandboxedShellApp.app/Contents/MacOS/SandboxedShellApp

# An d in case you need this in the future
codesign --remove-signature SandboxedShellApp.app
```
```



