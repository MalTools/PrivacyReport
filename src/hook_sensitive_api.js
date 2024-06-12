//frida -U -f ai.cloudmall.ios  -l hook_sensitive_api.js   --no-pause
//frida -U -F -l hook_script.js

console.log("[*] Started: Modify Return Value");
send("[*] Started: Modify Return Value");
function show_modify_function_return_value(className_arg, funcName_arg) {
    try {
        var className = className_arg;
        var funcName = funcName_arg;
        var hook = eval('ObjC.classes.' + className + '["' + funcName + '"]');
        Interceptor.attach(hook.implementation, {
            onLeave: function (retval) {
                console.log("\n[*] Class Name: " + className);
                console.log("[*] Method Name: " + funcName);
                // console.log("\t[-] Type of return value: " + typeof retval);
                // console.log("\t[-] Return Value: " + ObjC.Object(retval).toString());
                
                //Get current time
                var now = new Date();
                var timestamp = now.toISOString();
                console.log("[*] Timestamp: " + timestamp);
                console.log('\tBacktrace:\n\t' + Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\n\t'));


                // send("\n[*] Class Name: " + className);
                // send("[*] Method Name: " + funcName);
                // send("\t[-] Type of return value: " + typeof retval);
                // send("\t[-] Return Value: " + ObjC.Object(retval).toString());
                // send('\tBacktrace:\n\t' + Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\n\t'));

            }
        });

    }
    catch (error) {
        console.log("funcName_arg " + funcName)
        console.log("[!] funcName_arg Exception: ");
    }
}


function check_if_invoked(className_arg, funcName_arg) {
    //Your class name here
    var className = className_arg;
    //Your function name here
    var funcName = funcName_arg;
    var hook = eval('ObjC.classes.' + className + '["' + funcName + '"]');
    Interceptor.attach(hook.implementation, {
        onEnter: function (args) {
            console.log("\n[*] Class Name: " + className);
            console.log("[*] Method Name: " + funcName);
            console.log('\tBacktrace:\n\t' + Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\n\t'));

            // send("\n[*] Class Name: " + className);
            // send("[*] Method Name: " + funcName);
            // send('\tBacktrace:\n\t' + Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\n\t'));

        }
    });

}


//YOUR_CLASS_NAME_HERE and YOUR_EXACT_FUNC_NAME_HERE
//show_modify_function_return_value("YOUR_CLASS_NAME_HERE", "YOUR_EXACT_FUNC_NAME_HERE")
// show_modify_function_return_value("advertisingIdentifier", "UUIDString")
// show_modify_function_return_value("NSUUID", "init")
// show_modify_function_return_value("ASIdentifierManager", "- advertisingIdentifier")


//location
show_modify_function_return_value("CLLocation", "- coordinate")
// show_modify_function_return_value("CLLocation", "- altitude")
// show_modify_function_return_value("CLLocation", "- floor")
// show_modify_function_return_value("CLLocation", "- horizontalAccuracy")
// show_modify_function_return_value("CLLocation", "- verticalAccuracy")
// show_modify_function_return_value("CLLocation", "- timestamp")
// show_modify_function_return_value("CLLocationManager", "locationServicesEnabled")
// show_modify_function_return_value("CLLocationManager", "authorizationStatus")
// check_if_invoked("CLLocationManager", "- requestWhenInUseAuthorization")
// Add other API as needed...


//contacts
show_modify_function_return_value("CNContact", "namePrefix")
show_modify_function_return_value("CNContact", "givenName")
show_modify_function_return_value("CNContact", "middleName")
show_modify_function_return_value("CNContact", "familyName")
show_modify_function_return_value("CNContact", "previousFamilyName")
show_modify_function_return_value("CNContact", "nickname")
show_modify_function_return_value("CNContact", "phoneticGivenName")
show_modify_function_return_value("CNContact", "phoneticMiddleName")
show_modify_function_return_value("CNContact", "phoneticFamilyName")
show_modify_function_return_value("CNContact", "jobTitle")
show_modify_function_return_value("CNContact", "departmentName")
show_modify_function_return_value("CNContact", "organizationName")
show_modify_function_return_value("CNContact", "phoneticOrganizationName")
show_modify_function_return_value("CNContact", "postalAddresses")
show_modify_function_return_value("CNContact", "urlAddresses")
show_modify_function_return_value("CNContact", "phoneNumbers")
show_modify_function_return_value("CNContact", "socialProfiles")
show_modify_function_return_value("CNContact", "emailAddresses")
show_modify_function_return_value("CNContact", "birthday")
show_modify_function_return_value("CNContact", "dates")
show_modify_function_return_value("CNContact", "nonGregorianBirthday")
show_modify_function_return_value("CNContact", "note")
show_modify_function_return_value("CNContact", "emailAddresses")
show_modify_function_return_value("CNContactStore", "unifiedMeContactWithKeysToFetch:error:")
// Add other API as needed...


// photo
show_modify_function_return_value("ALAssetsLibrary", "authorizationStatus")
show_modify_function_return_value("PHPhotoLibrary", "authorizationStatus")
show_modify_function_return_value("PHPhotoLibrary", "requestAuthorizationForAccessLevel:handler:")
show_modify_function_return_value("PHPhotoLibrary", "requestAuthorization:")
show_modify_function_return_value("", "rfetchAssetsInAssetCollection:options:")
// Add other API as needed...


// screenRecorder
show_modify_function_return_value("RPScreenRecorder", "available")
show_modify_function_return_value("RPScreenRecorder", "recording")
show_modify_function_return_value("RPScreenRecorder", "cameraPreviewView")
show_modify_function_return_value("RPScreenRecorder", "microphoneEnabled")
show_modify_function_return_value("RPScreenRecorder", "cameraEnabled")
show_modify_function_return_value("RPScreenRecorder", "cameraEnabled")
show_modify_function_return_value("RPScreenRecorder", "- startRecordingWithHandler:")
show_modify_function_return_value("RPScreenRecorder", "- stopRecordingWithHandler:")
show_modify_function_return_value("RPScreenRecorder", "- stopCaptureWithHandler:")
show_modify_function_return_value("RPScreenRecorder", "- startClipBufferingWithCompletionHandler:")
show_modify_function_return_value("RPScreenRecorder", "- stopClipBufferingWithCompletionHandler:")
show_modify_function_return_value("RPScreenRecorder", "")
// Add other API as needed...


// Microphone and Camera
show_modify_function_return_value("AVCaptureDevice", "authorizationStatusForMediaType:")
show_modify_function_return_value("AVCaptureDevice", "requestAccessForMediaType:completionHandler:")
// Add other API as needed...


