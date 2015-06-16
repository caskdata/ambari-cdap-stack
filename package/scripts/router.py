import sys
import ambari_helpers as helpers
from resource_management import *

class Router(Script):
  def install(self, env):
    print 'Install the CDAP Router';
    import params
    self.configure(env)
    # Add repository file
    helpers.add_repo(params.files_dir + params.repo_file, params.os_repo_dir)
    # Install any global packages
    self.install_packages(env)
    # Install package
    helpers.package('cdap-gateway')

  def stop(self, env):
    print 'Stop the CDAP Router';

  def start(self, env):
    print 'Start the CDAP Router';

  def status(self, env):
    print 'Status of the CDAP Router';

  def configure(self, env):
    print 'Configure the CDAP Router';

if __name__ == "__main__":
  Router().execute()
