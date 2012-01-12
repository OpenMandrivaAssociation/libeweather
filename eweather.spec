%define svn 20100709
%define release %mkrel 0.%{svn}.3

%define major 0
%define libname %mklibname eweather %major
%define libnamedev %mklibname eweather -d

Summary: Enlightenment weather/forecasts module
Name: eweather
Version: 0.2.0
Release: %release
License: LGPLv2+
Group: Graphical desktop/Enlightenment
URL: http://www.enlightenment.org/
Source:	%{name}-%{version}.tar.bz2
Patch0: eweather-0.2.0-linkage.patch
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ecore-devel >= 0.9.9.063
BuildRequires: edje-devel >= 0.9.93.063
BuildRequires: edje >= 0.9.93.063
BuildRequires: embryo
BuildRequires: gettext-devel
Requires:	ecore >= 0.9.9.063

%description
Enlightenment weather/forecasts module.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries
Requires: %name = %{version}-%{release}

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries

%prep
%setup -q -n %name-%version
%patch0 -p0

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/eweather
%{_datadir}/eweather
%{_datadir}/images/*.png

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.0
%{_libdir}/*.so.0.*

%files -n %libnamedev
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_libdir}/*.la
