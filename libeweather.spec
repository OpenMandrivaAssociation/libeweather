#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/PROTO/libeweather libeweather; \
#cd libeweather; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#VERSION=$(cat configure.ac | grep "eweather" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
#PKG_VERSION=$VERSION.$SVNREV; \
#cd ..; \
#tar -Jcf libeweather-$PKG_VERSION.tar.xz libeweather/ --exclude .svn --exclude .*ignore

%define svnrev	64528

%define major 0
%define libname %mklibname eweather %{major}
%define develname %mklibname eweather -d

Summary:	Enlightenment weather/forecasts module
Name:		libeweather
Version:	0.2.0
Release:	1.%{svnrev}.1
License:	LGPLv2+
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	%{name}-%{version}.%{svnrev}.tar.xz

BuildRequires:	edje
BuildRequires:	embryo
BuildRequires:	evas
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(edje)

%rename	eweather

%description
Enlightenment weather/forecasts module.

%package -n %{libname}
Summary: Libraries for the %{name} package
Group: System/Libraries

%description -n %{libname}
Libraries for %{name}

%package -n %{develname}
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
%{name} development headers and libraries

%prep
%setup -qn %{name}

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_bindir}/eweather_test
%{_datadir}/*/images/*png
%{_datadir}/eweather/*jpg
%{_datadir}/eweather/*/*edj
%{_libdir}/eweather/plugins/*.so

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*pc

