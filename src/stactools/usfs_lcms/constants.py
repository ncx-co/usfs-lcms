FIRST_AVAILABLE_YEAR = 1985
MOST_RECENT_YEAR = 2022

# versions
V2022_8 = "v2022-8"
V2020_6 = "v2020-6"

# regions
CONUS = "CONUS"
SEAK = "SEAK"  # southeast Alaska
PRUSVI = "PRUSVI"  # Puerto Rico + US Virgin Islands

# versions by region
REGION_VERSIONS = {
    CONUS: V2022_8,
    SEAK: V2022_8,
    PRUSVI: V2020_6,
}

# change summary product names
CHANGE_FAST_LOSS_SUMMARY = "Fast_Loss_Summary"
CHANGE_GAIN_SUMMARY = "Gain_Summary"
CHANGE_SLOW_LOSS_SUMMARY = "Slow_Loss_Summary"

CHANGE_SUMMARY_PRODUCTS = [CHANGE_FAST_LOSS_SUMMARY, CHANGE_GAIN_SUMMARY, CHANGE_SLOW_LOSS_SUMMARY]

# annual product names
LAND_COVER = "Land_Cover"
LAND_USE = "Land_Use"
CHANGE = "Change"
QA_BITS = "QA_Bits"

ANNUAL_PRODUCTS = [LAND_COVER, LAND_USE, CHANGE, QA_BITS]

# url formats
URL_BASE = "https://data.fs.usda.gov/geodata/LCMS/"
ANNUAL_URL_FORMAT = URL_BASE + "LCMS_{region}_{version}_{product}_Annual_{year}.zip"
CHANGE_SUMMARY_URL_FORMAT = URL_BASE + "LCMS_{region}_{version}_Change_{product}_{first_year}_{last_year}.zip"
