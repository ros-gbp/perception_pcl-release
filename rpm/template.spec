Name:           ros-melodic-pcl-ros
Version:        1.6.1
Release:        0%{?dist}
Summary:        ROS pcl_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/perception_pcl
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       pcl-devel
Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-message-filters
Requires:       ros-melodic-nodelet
Requires:       ros-melodic-nodelet-topic-tools
Requires:       ros-melodic-pcl-conversions
Requires:       ros-melodic-pcl-msgs
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-rosbag
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-tf
Requires:       ros-melodic-tf2-eigen
BuildRequires:  eigen3-devel
BuildRequires:  pcl-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-message-filters
BuildRequires:  ros-melodic-nodelet
BuildRequires:  ros-melodic-nodelet-topic-tools
BuildRequires:  ros-melodic-pcl-conversions
BuildRequires:  ros-melodic-pcl-msgs
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-rosbag
BuildRequires:  ros-melodic-rosconsole
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roslib
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-tf2-eigen

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
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue May 08 2018 Paul Bovbel <paul@bovbel.com> - 1.6.1-0
- Autogenerated by Bloom

* Mon Apr 30 2018 Paul Bovbel <paul@bovbel.com> - 1.6.0-0
- Autogenerated by Bloom

