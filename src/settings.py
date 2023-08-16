from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME = "Cracks and Potholes in Road"
PROJECT_NAME_FULL = "Cracks and Potholes in Road Images"
HIDE_DATASET = False  # set False when 100% sure about repo quality


##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Utilities(), Industry.Safety()]
CATEGORY: Category = Category.EnergyAndUtilities()

CV_TASKS: List[CVTask] = [CVTask.SemanticSegmentation(), CVTask.InstanceSegmentation()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]

RELEASE_DATE: Optional[str] = "2020-07-21"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None
HOMEPAGE_URL: str = "https://data.mendeley.com/datasets/t576ydh9v8/4"

PREVIEW_IMAGE_ID: int = 186409

GITHUB_URL: str = "https://github.com/dataset-ninja/cracks-and-potholes-in-road"

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/t576ydh9v8-4.zip"

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "road": [95, 77, 6],
    "pothole": [21, 59, 86],
    "cracks": [89, 27, 22],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = None
CITATION_URL: Optional[str] = "http://dx.doi.org/10.17632/t576ydh9v8.4"
AUTHORS: Optional[List[str]] = [
    "Bianka T. Passos",
    "Mateus J. Cassaniga",
    "Anita M. R. Fernandes",
    "Kátya B. Medeiros",
    "Eros Comunello",
]


ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "Universidade do Vale do Itajai, Brazil",
    "DNIT, Brazil",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.univali.br/Paginas/default.aspx",
    "https://www.gov.br/dnit/pt-br",
]

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME, PROJECT_NAME_FULL]
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
