from os import path
from .go_manifester import GoManifester
from .maven_manifester import MavenManifester
from .npm_manifester import NpmManifester
from .nuget_manifester import NugetManifester
from .pip_manifester import PipManifester
from .ruby_manifester import RubyManifester

class ManifesterFactory:
    def get_manifester(filepath):
        """Get the manifester corresponding to the provided file.
        
        Args:
            filepath: The path to the file to scan for dependencies.
        Returns:
            object: class that is able to get a dependency list from the provided file."""
        filename = path.basename(filepath)
        if filename == "Gemfile":
                return RubyManifester()
        elif filename ==  "go.mod":
                return GoManifester()
        elif filename ==  "package.json":
                return NpmManifester()
        elif filename ==  "pom.xml":
                return MavenManifester()
        elif filename ==  "requirements.txt":
                return PipManifester()
        else:
            _, extension = path.splitext(filepath)
            if (extension == '.csproj'):
                return NugetManifester()
            raise ValueError(f"No manifester available for file: {filepath}")