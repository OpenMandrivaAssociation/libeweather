#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/PROTO/libeweather libeweather; \
#cd libeweather; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#VERSION=$(cat configure.ac | grep "eweather" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
#PKG_VERSION=$VERSION.$SVNREV; \
#cd ..; \
#tar -Jcf libeweather-$PKG_VERSION.tar.xz libeweather/ --exclude .svn --exclude .*ignore

%define svnrev	84427

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
%rename	eweather

%description
Enlightenment weather/forecasts module.

%package -n %{libname}
Summary:	Libraries for the %{name} package
Group:		System/Libraries

%description -n %{libname}
Libraries for %{name}

%package -n %{develname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

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
%makeinstall_std

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

%changelog
* Thu Jun 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.2.0-1.71876.1
+ Revision: 807368
- version update 0.2.0.71876

* Thu Jan 12 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.2.0-1.64528.1
+ Revision: 760439
- new snapshot 0.2.0.64528
- cleaned up spec
- merged UnityLinux spec
- library was renamed from eweather to libeweather
- to allow a space for the eweather module

* Thu Oct 14 2010 Funda Wang <fwang@mandriva.org> 0.2.0-0.20100709.3mdv2011.0
+ Revision: 585537
- rebuild
- rebuild
- rebuild

* Sat Jul 17 2010 Funda Wang <fwang@mandriva.org> 0.2.0-0.20100709.1mdv2011.0
+ Revision: 554482
- rediff linkage patch
- new snapshot

* Mon Dec 14 2009 Funda Wang <fwang@mandriva.org> 0.2.0-0.20091213.1mdv2010.1
+ Revision: 478423
- add BRs
- fix linkage
- add BR
- import eweather

