Name:           ros-indigo-pcl-ros
Version:        1.2.6
Release:        0%{?dist}
Summary:        ROS pcl_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/perception_pcl
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       pcl
Requires:       pcl-devel
Requires:       pcl-tools
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-message-filters
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-nodelet-topic-tools
Requires:       ros-indigo-pcl-conversions
Requires:       ros-indigo-pcl-msgs
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-rosbag
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-tf
Requires:       vtk-java
Requires:       vtk-python
BuildRequires:  eigen3-devel
BuildRequires:  pcl-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-nodelet-topic-tools
BuildRequires:  ros-indigo-pcl-conversions
BuildRequires:  ros-indigo-pcl-msgs
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-rosbag
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  vtk-java
BuildRequires:  vtk-python

%description
PCL (Point Cloud Library) ROS interface stack. PCL-ROS is the preferred bridge
for 3D applications involving n-D Point Clouds and 3D geometry processing in
ROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Feb 04 2015 Paul Bovbel <paul@bovbel.com> - 1.2.6-0
- Autogenerated by Bloom

* Tue Jan 20 2015 Paul Bovbel <paul@bovbel.com> - 1.2.5-0
- Autogenerated by Bloom

* Thu Jan 15 2015 Paul Bovbel <paul@bovbel.com> - 1.2.4-0
- Autogenerated by Bloom

* Sat Jan 10 2015 Paul Bovbel <paul@bovbel.com> - 1.2.3-0
- Autogenerated by Bloom

