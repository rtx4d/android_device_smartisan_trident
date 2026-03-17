#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools

extract_utils.tools.DEFAULT_PATCHELF_VERSION = '0_9'

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/smartisan/trident',
    'hardware/qcom-caf/common/libqti-perfd-client',
    'hardware/qcom-caf/sdm845',
    'hardware/qcom-caf/wlan',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'com.qualcomm.qti.imscmservice@1.0',
        'com.qualcomm.qti.imscmservice@2.0',
        'com.qualcomm.qti.imscmservice@2.1',
        'com.qualcomm.qti.imscmservice@2.2',
        'com.qualcomm.qti.uceservice@2.0',
        'com.qualcomm.qti.uceservice@2.1',
        'libmmosal',
        'vendor.qti.hardware.data.cne.internal.api@1.0',
        'vendor.qti.hardware.data.cne.internal.constants@1.0',
        'vendor.qti.hardware.data.cne.internal.server@1.0',
        'vendor.qti.hardware.data.connection@1.0',
        'vendor.qti.hardware.data.connection@1.1',
        'vendor.qti.hardware.data.dynamicdds@1.0',
        'vendor.qti.hardware.data.iwlan@1.0',
        'vendor.qti.hardware.data.qmi@1.0',
        'vendor.qti.hardware.fm@1.0',
        'vendor.qti.hardware.radio.ims@1.0',
        'vendor.qti.hardware.radio.ims@1.1',
        'vendor.qti.hardware.radio.ims@1.2',
        'vendor.qti.hardware.radio.ims@1.3',
        'vendor.qti.hardware.radio.ims@1.4',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'vendor.qti.ims.callinfo@1.0',
        'vendor.qti.ims.rcsconfig@1.0',
        'vendor.qti.imsrtpservice@2.0.so',
        'vendor.qti.imsrtpservice@2.1.so',
        'libmegvii_scene.so',
        'libmegface.so',
        'libSNPE.so',
        'libsnpe_loader.so',
        'libsymphony-cpu.so',
        'libsymphonypower.so',
        'libgnustl_shared.so',
        'libstdc++.so',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/lib64/lib-imsvideocodec.so': blob_fixup()
        .add_needed('libgui_shim.so'),
    ('vendor/lib64/libwvhidl.so', 'vendor/lib64/mediadrm/libwvdrmengine.so'): blob_fixup()
        .add_needed('libcrypto_shim.so'),
    ('vendor/lib/libmms_gyro_vstab_auth.so', 'vendor/lib/libmms_gyro_vstab.so', 'vendor/lib/libmms_hal_vstab.so', 'vendor/lib/libmms_warper_vstab.so', 'vendor/lib/libmegvii_scene.so', 'vendor/lib/libSNPE.so', 'vendor/lib/libsnpe_loader.so', 'vendor/lib/libSuperSensorCPU.so', 'vendor/lib/libSuperSensor.so', 'vendor/lib/libHalSuperSensorServer.so', 'vendor/lib/libyuvutils_sm.so', 'vendor/lib/libmegface-new.so', 'vendor/lib/libarcsoft_picselfie_algorithm.so', 'vendor/lib/libarcsoft_low_light_shotso', 'vendor/lib/libarcsoft_high_dynamic_range.so', 'vendor/lib/libarcsoft_dualcam_refocus.so', 'vendor/lib/libarcsoft_beautyshot.so', 'vendor/lib/libmmcv_sm.so', 'vendor/lib/libvideoprocess.so', 'vendor/lib/libnative-lib.so', 'vendor/lib/libarcsoft_smart_denoise.so', 'vendor/lib/libarcsoft_mpbase_sm.so', 'vendor/lib/libbeauty_momo_sm.so'): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/lib/libimgcmp_jni.so': blob_fixup()
        .remove_needed('libskia.so'),
    'vendor/lib64/libnotifyaudiohal.so': blob_fixup()
        .remove_needed('libicuuc.so'),
    'vendor/lib/libmmcamera_dbg.so': blob_fixup()
        .add_needed('liblog.so'),
    'vendor/lib64/libgoodixfingerprintd_binder.so': blob_fixup()
        .add_needed('libbinder_shim.so'),
    ('vendor/lib64/vendor.goodix.hardware.fingerprintextension@1.0.so', 'vendor/lib64/com.fingerprints.extension@1.0.so', 'vendor/lib64/com.novatek.fingerprint@1.0_vendor.so', 'vendor/bin/hw/android.hardware.biometrics.fpcfingerprint@2.1-service', 'vendor/bin/hw/android.hardware.biometrics.nvtfingerprint@2.1-service'): blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
    ('vendor/lib/libmms_warper_vstab.so', 'vendor/lib/libmms_hal_vstab.so'): blob_fixup()
        .add_needed('libui_shim.so'),
    ('vendor/lib/libarcsoft_beautyshot.so', 'vendor/lib/libarcsoft_dualcam_refocus.so', 'vendor/lib/libsns_low_lat_stream_stub.so', 'vendor/lib64/libsns_low_lat_stream_stub.so', 'vendor/lib/libssc_default_listener.so', 'vendor/lib64/libssc_default_listener.so'): blob_fixup()
        .clear_symbol_version('remote_handle_close')
        .clear_symbol_version('remote_handle_invoke')
        .clear_symbol_version('remote_handle_open'),
    ('vendor/lib64/libsnsdiaglog.so', 'vendor/lib/libssc.so', 'vendor/lib64/libssc.so', 'vendor/lib64/sensors.ssc.so', 'vendor/bin/sensors.qti', 'vendor/lib/hw/camera.qcom.so'): blob_fixup()
        .replace_needed('libprotobuf-cpp-full.so', 'libprotobuf-cpp-full-v29.so'),
    'vendor/lib/hw/camera.qcom.so': blob_fixup()
        .clear_symbol_version('remote_handle64_close')
        .clear_symbol_version('remote_handle64_invoke')
        .clear_symbol_version('remote_handle64_open'),
    ('vendor/lib64/sensors.elliptic.so', 'vendor/lib/libarcsoft_mpbase_sm.so', 'vendor/lib/libarcsoft_smart_denoise.so', 'vendor/lib/libbeauty_momo_sm.so', 'vendor/lib/libmms_hal_vstab.so', 'vendor/lib/libmms_warper_vstab.so'): blob_fixup()
        .remove_needed('libandroid.so'),
    'vendor/lib64/sensors.ssc.so': blob_fixup()
        .sig_replace('24 76 FF 97', '70 00 00 14'),
    'vendor/lib/libtt_panorama.so': blob_fixup()
        .replace_needed('libsensor.so', 'libsensor_vendor.so'),
    'vendor/lib/hw/audio.primary.sdm845.so': blob_fixup()
        .add_needed('libprocessgroup.so'),
    ('vendor/etc/init/android.hardware.biometrics.fpcfingerprint@2.1-service.rc', 'vendor/etc/init/android.hardware.biometrics.goodixfingerprint@2.1-service.rc', 'vendor/etc/init/android.hardware.biometrics.nvtfingerprint@2.1-service.rc'): blob_fixup()
        .regex_replace('system input', 'system uhid input'),
}  # fmt: skip

module = ExtractUtilsModule(
    'trident',
    'smartisan',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
