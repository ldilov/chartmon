import os
import sys

from setuptools import setup
from cx_Freeze import setup, Executable

# Define the application name, version, and other metadata
app_name = "ChartMon"
app_version = "0.1"
app_description = "Visualize with nice charts your presentmon telemetry data!"

directory_table = [
    ("ProgramMenuFolder", "TARGETDIR", "."),
    ("MyProgramMenu", "ProgramMenuFolder", "MYPROG~1|My Program"),
]

msi_data = {
    "Directory": directory_table,
    "ProgId": [
        ("Prog.Id", None, None, app_description, "IconId", None),
    ],
    "Icon": [
        ("IconId", "icon.ico"),
    ],
}

bdist_msi_options = {
    "add_to_path": True,
    "data": msi_data,
    "environment_variables": [
        ("E_MYAPP_VAR", "=-*MYAPP_VAR", "1", "TARGETDIR")
    ],
    "upgrade_code": "{aabbf124-7e0b-4e83-b36c-7ca99ce2c100}",
}

build_exe_options = {
    "excludes": [],
    "includes": ["pandas", "numpy", "plotly", "os", "sys", "tkinter"],
    "packages": ["pandas", "numpy", "numpy.core", "plotly", "main.application", "data.data_loader", "plotting.plot_builder", "processing.data_processor"],
    "optimize": 0,
    "include_msvcr": True
}

entry_point = "main.py"

included_packages = ["data", "processing", "plotting", "main"]

additional_files = []

executable = Executable(
    script=entry_point,
    base="Win32GUI",
    copyright="Lazar Dilov"
)

setup(
    name=app_name,
    version=app_version,
    description=app_description,
    options={
        "build_exe": build_exe_options,
        "build_msi": bdist_msi_options
    },
    executables=[executable]
)
