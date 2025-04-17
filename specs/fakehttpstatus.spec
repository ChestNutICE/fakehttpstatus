Name:       fakehttpstatus
Version:    1.0
Release:    2504
Summary:    fakehttpstatus rpm package
License:    MIT

%description
Apr_2025-This is the first release of this program.

%prep


%build


%install
mkdir -p %{buildroot}/usr/bin/

#check for python (both pip and pip3 are acceptable)
#not sure whether it is needed to upgrade pip, setuptools and other stuff
#if previous version doesn't support packages like request, 
#We need to handle that manually.
if ! (command -v pip 2>&1 >/dev/null || command -v pip3 2>&1 >/dev/null)
then
    echo "Available Python is not found."
    read -p "Would you like to install one (Python3)? (y/n)"
    #enter a loop, which will illiterate until get valid input (Y/N)
    while [true]
    do
      if [[ "$REPLY" == "y" || "$REPLY == "Y" ]]; then
        sudo apt install python3
        sudo apt install python3-pip
        #not sure whether this one is needed
        sudo apt install python3-dev python3-venv build-essential
        #just break the loop, instead of the whole script
        break
      elif [[ "$REPLY" == "n" || "$REPLY" == "N" ]]; then
        echo "Installation declined. No available Python"
        echo "Failed to install fakehttp."
        #need something to interrupt installation. 
        #Prevent later command from being executed
        #break the whole script
        exit 1
      else
        echo "Invalid input."
        read -p "Would you like to install one (Python3)? (y/n)"
      fi
    done
fi

#import dependencies (Package: requests)
if (command -v pip 2>&1 >/dev/null)
then
  import sudo pip install requests
else
  import sudo pip3 install requests
fi
#install executive sourecode
install -m 755 %{_sourcedir}/fakehttpstatus2504.py %{buildroot}/usr/bin/fakehttp
#initialize and assign dir
%files
/usr/bin/fakehttp

%changelog
* Wed Apr 16 2025 ChestNutICE
<sudoavocado@gmail.com> - 1.0-1
- Initial package
