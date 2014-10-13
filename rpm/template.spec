Name:           ros-hydro-scitos-cmd-vel-mux
Version:        0.0.4
Release:        0%{?dist}
Summary:        ROS scitos_cmd_vel_mux package

Group:          Development/Libraries
License:        MIT
URL:            https://github.com/strands-project/scitos_apps
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-yocs-cmd-vel-mux
BuildRequires:  ros-hydro-catkin

%description
Launch and config files for the yocs_cmd_vel_mux tailored to the scitos A5
robot.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Oct 13 2014 Christian Dondrup <cdondrup@lincoln.ac.uk> - 0.0.4-0
- Autogenerated by Bloom

* Mon Sep 22 2014 Christian Dondrup <cdondrup@lincoln.ac.uk> - 0.0.3-0
- Autogenerated by Bloom

* Mon Sep 22 2014 Christian Dondrup <cdondrup@lincoln.ac.uk> - 0.0.1-0
- Autogenerated by Bloom

* Mon Sep 22 2014 Christian Dondrup <cdondrup@lincoln.ac.uk> - 0.0.2-0
- Autogenerated by Bloom

