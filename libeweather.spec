%define gitdate 20150504

%define major 0
%define libname %mklibname eweather %{major}
%define devname %mklibname eweather -d

Summary:	Enlightenment weather/forecasts module
Name:		libeweather
Version:	0.2.0
Release:	2.%{gitdate}.2
License:	LGPLv2+
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	%{name}-%{version}.%{gitdate}.tar.gz
BuildRequires:	gettext-devel
BuildRequires:	edje
BuildRequires:	embryo
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(ecore-con)
BuildRequires:	pkgconfig(ecore-evas)
BuildRequires:	pkgconfig(ecore-file)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(eio)

%description
Enlightenment weather/forecasts module.

%files
%{_bindir}/eweather_test
%{_datadir}/*/images/*.png
%{_datadir}/eweather/*.jpg
%{_datadir}/eweather/*/*.edj
%{_libdir}/eweather/plugins/*.so

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for the %{name} package
Group:		System/Libraries

%description -n %{libname}
Libraries for %{name}

%files -n %{libname}
%{_libdir}/libeweather.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name} development headers and libraries

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/libeweather.so
%{_libdir}/pkgconfig/eweather.pc

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{gitdate}

%build
autoreconf -fi
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

