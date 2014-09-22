Name:           ros-hydro-scitos-dashboard
Version:        0.0.1
Release:        0%{?dist}
Summary:        ROS scitos_dashboard package

Group:          Development/Libraries
License:        GPL
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-roslib
Requires:       ros-hydro-rospy
Requires:       ros-hydro-rqt-gui
Requires:       ros-hydro-rqt-robot-dashboard
Requires:       ros-hydro-scitos-msgs
Requires:       ros-hydro-std-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-roslib
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-rqt-gui
BuildRequires:  ros-hydro-rqt-robot-dashboard
BuildRequires:  ros-hydro-scitos-msgs
BuildRequires:  ros-hydro-std-msgs

%description
The scitos_dashboard package providing and rqt interface for the scitos robot.

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
* Mon Sep 22 2014 chris burbridge <cburbridge@gmail.com> - 0.0.1-0
- Autogenerated by Bloom

