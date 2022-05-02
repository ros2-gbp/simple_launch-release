%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-simple-launch
Version:        1.3.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS simple_launch package

License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-ament-index-python
Requires:       ros-humble-launch
Requires:       ros-humble-launch-ros
Requires:       ros-humble-xacro
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-ament-index-python
BuildRequires:  ros-humble-launch
BuildRequires:  ros-humble-launch-ros
BuildRequires:  ros-humble-ros-workspace
BuildRequires:  ros-humble-xacro
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Python helper class for the ROS 2 launch system

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Mon May 02 2022 Olivier Kermorgant <olivier.kermorgant@ec-nantes.fr> - 1.3.1-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Olivier Kermorgant <olivier.kermorgant@ec-nantes.fr> - 1.2.1-3
- Autogenerated by Bloom

* Tue Feb 08 2022 Olivier Kermorgant <olivier.kermorgant@ec-nantes.fr> - 1.2.1-2
- Autogenerated by Bloom

