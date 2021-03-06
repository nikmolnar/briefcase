import os
import distutils.command.install_scripts as orig
from pkg_resources import Distribution, PathMetadata
import shutil
import sys

from .app import app


class linux(app):
    description = "Create a Linux installer to wrap this project"

    def finalize_options(self):
        # Copy over all the options from the base 'app' command
        finalized = self.get_finalized_command('app')
        for attr in ('formal_name', 'organization_name', 'bundle', 'icon', 'guid', 'splash', 'download_dir'):
            if getattr(self, attr) is None:
                setattr(self, attr, getattr(finalized, attr))

        # Set platform-specific options
        self.platform = 'Linux'

        if self.dir is None:
            self.dir = 'linux'

        self.resource_dir = self.dir

    def install_icon(self):
        raise RuntimeError("Linux doesn't support icons screens.")

    def install_splash(self):
        raise RuntimeError("Linux doesn't support splash screens.")

    def install_support_package(self):
        # No support package; we just use the system python
        pass
