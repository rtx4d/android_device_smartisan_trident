#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from trident device
$(call inherit-product, device/smartisan/trident/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Device identifier. This must come after all inclusions.
PRODUCT_NAME := lineage_trident
PRODUCT_DEVICE := trident
PRODUCT_BRAND := Smartisan
PRODUCT_MODEL := R1
PRODUCT_MANUFACTURER := Smartisan

PRODUCT_GMS_CLIENTID_BASE := android-smartisan

PRODUCT_SYSTEM_NAME := trident

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="trident-user 8.1.0 OPM1.171019.026 1615464674 release-keys" \
    BuildFingerprint=SMARTISAN/trident/trident:8.1.0/OPM1.171019.026/1615464674:user/dev-keys
