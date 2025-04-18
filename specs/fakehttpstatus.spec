Name:       fakehttpstatus
Version:    1.0
Release:    2504
Summary:    fakehttpstatus rpm package
Requires:   python3-requests
License:    MIT

%description
Apr_2025-This is the first release of this program.

%prep


%build


%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 %{_sourcedir}/fakehttpstatus2504.py %{buildroot}/usr/bin/fakehttp
#initialize and assign dir
%files
/usr/bin/fakehttp

%changelog
* Wed Apr 16 2025 ChestNutICE
<sudoavocado@gmail.com> - 1.0-1
- Initial package
