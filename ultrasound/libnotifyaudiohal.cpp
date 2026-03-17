#define LOG_TAG "libnotifyaudiohal"

#include <android/hardware/audio/6.0/IDevicesFactory.h>
#include <android/hardware/audio/6.0/IPrimaryDevice.h>
#include <android/hardware/audio/6.0/types.h>

#include <hidl/HidlSupport.h>
#include <log/log.h>

#include <string>

using android::sp;
using android::hardware::hidl_vec;
using android::hardware::audio::V6_0::IDevicesFactory;
using android::hardware::audio::V6_0::IPrimaryDevice;
using android::hardware::audio::V6_0::ParameterValue;
using android::hardware::audio::V6_0::Result;

extern "C" int elliptic_ultrasound_supported(void) {
    return 1;
}

extern "C" int elliptic_notify_audio_hal(char *param)
{
    if (!param) {
        ALOGE("param is null");
        return 1;
    }

    std::string input(param);
    auto pos = input.find('=');

    if (pos == std::string::npos) {
        ALOGE("Invalid input string: %s", param);
        return 1;
    }

    std::string key = input.substr(0, pos);
    std::string value = input.substr(pos + 1);

    ALOGD("setting value: %s", param);

    auto factory = IDevicesFactory::getService();
    if (!factory) {
        ALOGE("devicesFactory is nullptr");
        return 1;
    }

    int status = 1;

   factory->openPrimaryDevice([&](Result retval, const sp<IPrimaryDevice>& device) {
    if (retval != Result::OK || !device) {
        ALOGE("device open failed");
        return;
    }

    auto ret = device->setParameters({}, { { key, value } });

    if (ret == Result::OK) {
        ALOGD("successfully set value: %s", param);
        status = 0;
    } else {
        ALOGE("setParameters failed");
    }
});

    return status;
}
