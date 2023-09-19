import os
import pathlib
from typing import List

import requests
from stactools.usfs_lcms import constants
from tqdm import tqdm


def download_zips(
    years: List[int], regions: List[str], destination: pathlib.Path
) -> List[pathlib.Path]:
    """Download zipped GeoTiffs from USDA

    Args:
        years: list of years to download
        destination: destination directory for downloaded files

    Returns: list of filepaths for downloaded zip files
    """
    os.makedirs(str(destination), exist_ok=True)
    if not years:
        years = list(
            range(constants.FIRST_AVAILABLE_YEAR, constants.MOST_RECENT_YEAR + 1)
        )
    if not regions:
        regions = [constants.CONUS]
    urls = list()
    for region in regions:
        assert (
            region in constants.REGION_VERSIONS
        ), f"region must be one of {', '.join(constants.REGION_VERSIONS.keys())}"
        version = constants.REGION_VERSIONS.get(region)
        for year in years:
            if (
                year < constants.FIRST_AVAILABLE_YEAR
                or year > constants.MOST_RECENT_YEAR
            ):
                raise Exception(f"Unsupported year: {year}")

            # add annual products
            for product in constants.ANNUAL_PRODUCTS:
                urls.append(
                    constants.ANNUAL_URL_FORMAT.format(
                        region=region, version=version, product=product, year=year
                    )
                )

            # if running most recent year, add change summary products
            if year == constants.MOST_RECENT_YEAR:
                for product in constants.CHANGE_SUMMARY_PRODUCTS:
                    urls.append(
                        constants.CHANGE_SUMMARY_URL_FORMAT.format(
                            region=region,
                            version=version,
                            product=product,
                            first_year=constants.FIRST_AVAILABLE_YEAR,
                            last_year=constants.MOST_RECENT_YEAR,
                        )
                    )

    zips = []
    for url in urls:
        print(url)
        path = pathlib.Path(str(destination)) / os.path.basename(url)
        if path.exists():
            print(f"{path} already exists, skipping...")
            continue
        response = requests.get(url, stream=True)
        with tqdm.wrapattr(
            open(path, "wb"),
            "write",
            miniters=1,
            desc=url.split("/")[-1],
            total=int(response.headers.get("content-length", 0)),
        ) as fout:
            for chunk in response.iter_content(chunk_size=4096):
                fout.write(chunk)

        zips.append(path)

    return zips
