import subprocess

# Get a list of installed packages
result = subprocess.run(['apt-mark', 'showmanual'], stdout=subprocess.PIPE)
installed_packages = result.stdout.decode().split('\n')

# Filter out package names
package_names = [line.split('\t')[0] for line in installed_packages if line]

# Create a script to install the packages
script_content = "#!/bin/bash\n\n"
script_content += "sudo apt-get update\n\n"
script_content += "sudo apt-get install -y " + " ".join(package_names)

# Write the script to a file
with open("script.sh", "w") as file:
    file.write(script_content)

print("Script generated successfully: install_packages.sh")
